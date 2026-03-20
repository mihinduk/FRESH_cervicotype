#!/usr/bin/env python3
"""
Merge expanded NCBI pheS sequences + FRESH SA MAG extract into the
existing combined pheS database.

Reads:
  - pheS_combined_reference.fasta + pheS_combined_taxonomy.txt (existing DB)
  - pheS_ncbi_expanded.fasta + pheS_ncbi_expanded_metadata.tsv (new expanded search)
  - fresh_sa_pheS.fasta (FRESH SA MAG extract, if available)

Writes:
  - pheS_final_reference.fasta + pheS_final_taxonomy.txt

Deduplication: by exact sequence. Different species for same sequence both retained.
"""

import sys
import re
from collections import defaultdict
from pathlib import Path

# Genus to taxonomy mapping (same as build_pheS_combined_db.py)
GENUS_TAXONOMY = {
    'Lactobacillus':           ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Lacticaseibacillus':      ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Limosilactobacillus':     ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Ligilactobacillus':       ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Latilactobacillus':       ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Lentilactobacillus':      ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Levilactobacillus':       ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Companilactobacillus':    ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Furfurilactobacillus':    ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Lactiplantibacillus':     ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Loigolactobacillus':      ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Pediococcus':             ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    # Outgroups with correct taxonomy
    'Bacillus':                ('Firmicutes', 'Bacilli', 'Bacillales', 'Bacillaceae'),
    'Enterococcus':            ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Enterococcaceae'),
    'Lactococcus':             ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Streptococcaceae'),
    'Leuconostoc':             ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Leuconostocaceae'),
    'Oenococcus':              ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Oenococcaceae'),
    'Weissella':               ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Leuconostocaceae'),
    'Streptococcus':           ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Streptococcaceae'),
    # New outgroups from expanded search
    'Bifidobacterium':         ('Actinobacteria', 'Actinobacteria', 'Bifidobacteriales', 'Bifidobacteriaceae'),
    'Gardnerella':             ('Actinobacteria', 'Actinomycetia', 'Bifidobacteriales', 'Bifidobacteriaceae'),
    'Fannyhessea':             ('Actinobacteria', 'Coriobacteriia', 'Coriobacteriales', 'Atopobiaceae'),
    'Atopobium':               ('Actinobacteria', 'Coriobacteriia', 'Coriobacteriales', 'Atopobiaceae'),
    'Mobiluncus':              ('Actinobacteria', 'Actinomycetia', 'Actinomycetales', 'Actinomycetaceae'),
    'Megasphaera':             ('Firmicutes', 'Negativicutes', 'Veillonellales', 'Veillonellaceae'),
    'Sneathia':                ('Fusobacteria', 'Fusobacteriia', 'Fusobacteriales', 'Leptotrichiaceae'),
    'Prevotella':              ('Bacteroidetes', 'Bacteroidia', 'Bacteroidales', 'Prevotellaceae'),
}


def read_fasta(filepath):
    entries = []
    with open(filepath) as f:
        header = None
        parts = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    entries.append((header[1:], ''.join(parts).upper()))
                header = line
                parts = []
            else:
                parts.append(line)
        if header:
            entries.append((header[1:], ''.join(parts).upper()))
    return entries


def build_taxonomy(species):
    genus = species.split()[0]
    phylum, cls, order, family = GENUS_TAXONOMY.get(
        genus, ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'))
    return (f"k__Bacteria; p__{phylum}; c__{cls}; "
            f"o__{order}; f__{family}; "
            f"g__{genus}; s__{species}")


def main():
    db_dir = Path(sys.argv[1])
    expanded_dir = Path(sys.argv[2])
    fresh_pheS = Path(sys.argv[3]) if len(sys.argv) > 3 else None

    # Load existing combined DB
    existing_seqs = read_fasta(db_dir / 'pheS_combined_reference.fasta')
    existing_tax = {}
    with open(db_dir / 'pheS_combined_taxonomy.txt') as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                existing_tax[parts[0]] = parts[1]
    print(f"Existing DB: {len(existing_seqs)} sequences, {len(existing_tax)} taxonomy entries")

    # Load expanded NCBI sequences + metadata
    expanded_seqs = read_fasta(expanded_dir / 'pheS_ncbi_expanded.fasta')
    expanded_meta = {}
    with open(expanded_dir / 'pheS_ncbi_expanded_metadata.tsv') as f:
        next(f)  # skip header
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) >= 6:
                expanded_meta[parts[0]] = {
                    'organism': parts[1], 'strain': parts[2],
                    'country': parts[3], 'source': parts[4], 'length': int(parts[5])
                }
    print(f"Expanded NCBI: {len(expanded_seqs)} sequences, {len(expanded_meta)} metadata entries")

    # Load FRESH SA MAG extract if available
    fresh_seqs = []
    if fresh_pheS and fresh_pheS.exists():
        fresh_seqs = read_fasta(fresh_pheS)
        print(f"FRESH SA MAGs: {len(fresh_seqs)} sequences")

    # Build unified sequence -> identities map
    seq_to_ids = defaultdict(list)

    # Add existing DB
    for seq_id, seq in existing_seqs:
        primary_id = seq_id.split()[0]
        tax = existing_tax.get(primary_id, '')
        sp_match = re.search(r's__(.+)', tax)
        species = sp_match.group(1).strip() if sp_match else 'Unknown'
        seq_to_ids[seq].append((primary_id, species, 'existing_db'))

    # Add expanded NCBI (only sequences > 200bp)
    added_expanded = 0
    skipped_short = 0
    for seq_id, seq in expanded_seqs:
        if len(seq) < 200:
            skipped_short += 1
            continue
        acc = seq_id.split()[0]
        meta = expanded_meta.get(acc, {})
        species = meta.get('organism', 'Unknown')
        source = meta.get('source', '')
        country = meta.get('country', '')
        new_id = f"expanded_{acc}"
        if source:
            new_id += f"_src={source.replace(' ', '_')[:20]}"
        if country and country != 'not specified':
            new_id += f"_country={country.replace(' ', '_')[:15]}"
        seq_to_ids[seq].append((new_id, species, 'expanded_ncbi'))
        added_expanded += 1

    print(f"Expanded sequences added: {added_expanded}, skipped (short): {skipped_short}")

    # Add FRESH SA MAGs
    for seq_id, seq in fresh_seqs:
        if len(seq) < 200:
            continue
        species_match = re.search(r'Lactobacillus[_ ](\w+)', seq_id)
        species = f"Lactobacillus {species_match.group(1)}" if species_match else 'Unknown'
        seq_to_ids[seq].append((seq_id.split()[0], species, 'fresh_sa_mag'))

    print(f"\nTotal unique sequences: {len(seq_to_ids)}")

    # Write final output
    out_fasta = db_dir / 'pheS_final_reference.fasta'
    out_tax = db_dir / 'pheS_final_taxonomy.txt'

    count = 0
    multi_species = 0
    sorted_items = sorted(seq_to_ids.items(), key=lambda x: x[1][0][0])

    with open(out_fasta, 'w') as ff, open(out_tax, 'w') as tf:
        for seq, ids in sorted_items:
            known = [(sid, sp, src) for sid, sp, src in ids if sp != 'Unknown']
            if not known:
                continue

            species_set = set(sp for _, sp, _ in known)

            if len(species_set) == 1:
                primary_id, species, source = known[0]
                alt_ids = [sid for sid, _, _ in known[1:]]
                tax = build_taxonomy(species)

                header = primary_id
                if alt_ids:
                    header += f" alt_ids={';'.join(alt_ids)}"

                ff.write(f">{header}\n")
                for i in range(0, len(seq), 80):
                    ff.write(seq[i:i + 80] + '\n')
                tf.write(f"{primary_id}\t{tax}\n")
                count += 1
            else:
                multi_species += 1
                for sid, species, source in known:
                    tax = build_taxonomy(species)
                    ff.write(f">{sid} multi_species_seq=true\n")
                    for i in range(0, len(seq), 80):
                        ff.write(seq[i:i + 80] + '\n')
                    tf.write(f"{sid}\t{tax}\n")
                    count += 1

    # Verify
    fasta_count = sum(1 for line in open(out_fasta) if line.startswith('>'))
    tax_count = sum(1 for _ in open(out_tax))
    assert fasta_count == tax_count, f"Mismatch: FASTA={fasta_count}, taxonomy={tax_count}"

    print(f"\n=== Final pheS database ===")
    print(f"Total entries: {count}")
    print(f"Multi-species sequences: {multi_species}")
    print(f"FASTA entries: {fasta_count}")
    print(f"Taxonomy entries: {tax_count}")

    # Species summary
    sp_counts = defaultdict(int)
    with open(out_tax) as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                sp = re.search(r's__(.+)', parts[1])
                if sp:
                    sp_counts[sp.group(1)] += 1

    print(f"\nUnique species: {len(sp_counts)}")
    print(f"\nVaginal Lactobacillus:")
    for v in ['crispatus', 'iners', 'gasseri', 'jensenii', 'vaginalis']:
        for sp, n in sp_counts.items():
            if v in sp.lower():
                print(f"  {n:>3}  {sp}")

    print(f"\nOutgroup/vaginal non-Lactobacillus taxa:")
    non_lacto = {sp: n for sp, n in sp_counts.items()
                 if not any(g in sp for g in ['Lactobacillus', 'Lacticaseibacillus',
                     'Limosilactobacillus', 'Lactiplantibacillus', 'Levilactobacillus',
                     'Pediococcus', 'Loigolactobacillus', 'Companilactobacillus'])}
    for sp, n in sorted(non_lacto.items(), key=lambda x: -x[1]):
        print(f"  {n:>3}  {sp}")

    print(f"\nOutput files:")
    print(f"  {out_fasta}")
    print(f"  {out_tax}")


if __name__ == '__main__':
    main()
