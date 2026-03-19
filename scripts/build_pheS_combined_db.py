#!/usr/bin/env python3
"""
Build combined pheS reference database from Wuyts et al. 2021 + NCBI supplement.

When deduplicating by sequence identity:
- If multiple accessions share the same sequence AND the same species: keep one,
  note alternates in header
- If multiple accessions share the same sequence but DIFFERENT species: retain
  BOTH entries (both identities kept)

Usage:
    python3 build_pheS_combined_db.py <wuyts_dir>

Where <wuyts_dir> contains:
    wuyts_pheS_reference.fasta, wuyts_pheS_taxonomy.txt
    pheS_reference.fasta, pheS_taxonomy.txt (NCBI supplement)
"""

import sys
import re
from collections import defaultdict
from pathlib import Path


def read_fasta(filepath):
    """Read FASTA file, yield (header, sequence) tuples."""
    entries = []
    with open(filepath) as f:
        header = None
        seq_parts = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    entries.append((header[1:], ''.join(seq_parts).upper()))
                header = line
                seq_parts = []
            else:
                seq_parts.append(line)
        if header:
            entries.append((header[1:], ''.join(seq_parts).upper()))
    return entries


def read_taxonomy(filepath):
    """Read taxonomy file, return dict of id -> taxonomy."""
    tax = {}
    with open(filepath) as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                tax[parts[0]] = parts[1]
    return tax


def extract_species(taxonomy_string):
    """Extract species name from QIIME2 taxonomy string."""
    match = re.search(r's__(.+)', taxonomy_string)
    return match.group(1) if match else 'Unknown'


def main():
    wuyts_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')

    # Load Wuyts data
    wuyts_seqs = read_fasta(wuyts_dir / 'wuyts_pheS_reference.fasta')
    wuyts_tax = read_taxonomy(wuyts_dir / 'wuyts_pheS_taxonomy.txt')
    print(f"Wuyts: {len(wuyts_seqs)} sequences, {len(wuyts_tax)} taxonomy entries")

    # Load NCBI supplement
    ncbi_seqs = read_fasta(wuyts_dir / 'pheS_reference.fasta')
    ncbi_tax = read_taxonomy(wuyts_dir / 'pheS_taxonomy.txt')
    print(f"NCBI supplement: {len(ncbi_seqs)} sequences, {len(ncbi_tax)} taxonomy entries")

    # Group ALL entries by sequence content
    # seq -> [(seq_id, species, source), ...]
    seq_to_ids = defaultdict(list)

    for seq_id, seq in wuyts_seqs:
        tax_str = wuyts_tax.get(seq_id, '')
        species = extract_species(tax_str)
        seq_to_ids[seq].append((seq_id, species, 'wuyts'))

    for seq_id_full, seq in ncbi_seqs:
        acc = seq_id_full.split()[0]
        tax_str = ncbi_tax.get(acc, '')
        species = extract_species(tax_str)
        seq_to_ids[seq].append((f"ncbi_{acc}", species, 'ncbi'))

    print(f"\nUnique sequences: {len(seq_to_ids)}")

    # Identify conflicts
    conflicts = []
    for seq, ids in seq_to_ids.items():
        species_set = set(sp for _, sp, _ in ids if sp != 'Unknown')
        if len(species_set) > 1:
            conflicts.append((seq[:30], ids))

    print(f"Sequences with multiple species assignments: {len(conflicts)}")
    if conflicts:
        print("\nConflicts (both identities retained):")
        for seq_start, ids in conflicts:
            print(f"  Seq {seq_start}...")
            for sid, sp, src in ids:
                print(f"    {sid} -> {sp} (from {src})")

    # Build combined output
    out_fasta = wuyts_dir / 'pheS_combined_reference.fasta'
    out_tax = wuyts_dir / 'pheS_combined_taxonomy.txt'

    count = 0
    multi_identity = 0

    with open(out_fasta, 'w') as fasta_out, open(out_tax, 'w') as tax_out:
        for seq, ids in seq_to_ids.items():
            # Filter out Unknown species
            known_ids = [(sid, sp, src) for sid, sp, src in ids if sp != 'Unknown']
            if not known_ids:
                continue

            species_set = set(sp for _, sp, _ in known_ids)

            if len(species_set) == 1:
                # All agree on species — write one entry, note alternates
                primary_id, species, source = known_ids[0]
                alt_ids = [sid for sid, _, _ in known_ids[1:]]

                genus = species.split()[0]
                tax = (f"k__Bacteria; p__Firmicutes; c__Bacilli; "
                       f"o__Lactobacillales; f__Lactobacillaceae; "
                       f"g__{genus}; s__{species}")

                if alt_ids:
                    header = f"{primary_id} alt_ids={';'.join(alt_ids)}"
                else:
                    header = primary_id

                fasta_out.write(f">{header}\n")
                for i in range(0, len(seq), 80):
                    fasta_out.write(seq[i:i + 80] + '\n')
                tax_out.write(f"{primary_id}\t{tax}\n")
                count += 1

            else:
                # DIFFERENT species for same sequence — retain ALL identities
                multi_identity += 1
                for sid, species, source in known_ids:
                    genus = species.split()[0]
                    tax = (f"k__Bacteria; p__Firmicutes; c__Bacilli; "
                           f"o__Lactobacillales; f__Lactobacillaceae; "
                           f"g__{genus}; s__{species}")

                    fasta_out.write(f">{sid} multi_species_seq=true\n")
                    for i in range(0, len(seq), 80):
                        fasta_out.write(seq[i:i + 80] + '\n')
                    tax_out.write(f"{sid}\t{tax}\n")
                    count += 1

    print(f"\n=== Combined database ===")
    print(f"Total entries written: {count}")
    print(f"  Single-identity sequences: {count - sum(len([i for i in ids if i[1] != 'Unknown']) for seq, ids in seq_to_ids.items() if len(set(sp for _, sp, _ in ids if sp != 'Unknown')) > 1)}")
    print(f"  Multi-identity sequences (both retained): {multi_identity}")

    # Vaginal species summary
    sp_counts = defaultdict(int)
    with open(out_tax) as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                sp = extract_species(parts[1])
                sp_counts[sp] += 1

    print(f"\nTotal unique species: {len(sp_counts)}")
    print(f"\nVaginal species coverage:")
    for v in ['crispatus', 'iners', 'gasseri', 'jensenii', 'vaginalis', 'paragasseri']:
        matches = {sp: n for sp, n in sp_counts.items() if v in sp.lower()}
        for sp, n in matches.items():
            print(f"  {n:>3}  {sp}")

    print(f"\nOutput files:")
    print(f"  {out_fasta}")
    print(f"  {out_tax}")


if __name__ == '__main__':
    main()
