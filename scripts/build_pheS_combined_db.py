#!/usr/bin/env python3
"""
Build combined pheS reference database from Wuyts et al. 2021 + NCBI supplement.

When deduplicating by sequence identity:
- If multiple accessions share the same sequence AND the same species: keep one,
  note alternates in header (alt_ids=)
- If multiple accessions share the same sequence but DIFFERENT species: retain
  BOTH entries (both identities kept, flagged multi_species_seq=true)

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

# Minimum sequence length to include
MIN_SEQ_LEN = 200

# Outgroup genera — NOT Lactobacillaceae but retained with correct taxonomy
# to aid Bayesian classifier training (helps classifier learn what is NOT Lactobacillaceae)
OUTGROUP_GENERA = {
    'Bacillus', 'Enterococcus', 'Lactococcus', 'Leuconostoc',
    'Oenococcus', 'Weissella', 'Streptococcus',
}

# Species names that indicate unresolved taxonomy — flag but don't exclude
UNRESOLVED_SPECIES_PATTERNS = [
    r'^Lactobacillus sp\.$',
    r'^partial ',
    r' sp\.$',
]

# Family and higher taxonomy by genus
# Outgroups get their CORRECT taxonomy (not Lactobacillaceae)
# This is essential for training a Bayesian classifier that can distinguish
# Lactobacillaceae from non-Lactobacillaceae
GENUS_TAXONOMY = {
    # Lactobacillaceae sensu lato
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
    'Schleiferilactobacillus': ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Secundilactobacillus':    ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Dellaglioa':              ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Lapidilactobacillus':     ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Liquorilactobacillus':    ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Amylolactobacillus':      ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Bombilactobacillus':      ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Acetilactobacillus':      ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Apilactobacillus':        ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Agrilactobacillus':       ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Holzapfelia':             ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    'Pediococcus':             ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae'),
    # Outgroups with CORRECT taxonomy
    'Bacillus':                ('Firmicutes', 'Bacilli', 'Bacillales', 'Bacillaceae'),
    'Enterococcus':            ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Enterococcaceae'),
    'Lactococcus':             ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Streptococcaceae'),
    'Leuconostoc':             ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Leuconostocaceae'),
    'Oenococcus':              ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Oenococcaceae'),
    'Weissella':               ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Leuconostocaceae'),
    'Streptococcus':           ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Streptococcaceae'),
}


def read_fasta(filepath):
    """Read FASTA file, return list of (header, sequence) tuples."""
    entries = []
    with open(filepath) as f:
        header = None
        seq_parts = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header:
                    seq = ''.join(seq_parts).upper()
                    entries.append((header[1:], seq))
                header = line
                seq_parts = []
            else:
                seq_parts.append(line)
        if header:
            seq = ''.join(seq_parts).upper()
            entries.append((header[1:], seq))
    return entries


def read_taxonomy(filepath):
    """Read taxonomy file, return dict of id -> taxonomy string."""
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
    return match.group(1).strip() if match else 'Unknown'


def is_outgroup(species):
    """Check if a species belongs to an outgroup genus."""
    genus = species.split()[0] if species else ''
    if genus in OUTGROUP_GENERA:
        return True
    # Also catch malformed entries like "partial Streptococcus"
    # Use word-boundary matching to avoid "Bacillus" matching inside "Lactobacillus"
    for og in OUTGROUP_GENERA:
        if re.search(r'\b' + og + r'\b', species):
            return True
    return False


def is_unresolved(species):
    """Check if a species name indicates unresolved taxonomy."""
    for pattern in UNRESOLVED_SPECIES_PATTERNS:
        if re.match(pattern, species):
            return True
    return False


def build_taxonomy(species):
    """Build QIIME2-format taxonomy string with correct higher taxonomy per genus."""
    genus = species.split()[0]
    phylum, cls, order, family = GENUS_TAXONOMY.get(
        genus,
        ('Firmicutes', 'Bacilli', 'Lactobacillales', 'Lactobacillaceae')  # default
    )
    return (f"k__Bacteria; p__{phylum}; c__{cls}; "
            f"o__{order}; f__{family}; "
            f"g__{genus}; s__{species}")


def validate_sequence(seq, seq_id):
    """Validate a sequence. Return (is_valid, warnings)."""
    warnings = []
    if len(seq) < MIN_SEQ_LEN:
        warnings.append(f"Sequence too short ({len(seq)}bp < {MIN_SEQ_LEN}bp)")
        return False, warnings
    if len(seq) == 0:
        warnings.append("Empty sequence")
        return False, warnings
    non_atcg = set(seq) - set('ACGT')
    if non_atcg:
        warnings.append(f"Non-ATCG characters: {non_atcg}")
        # Don't exclude — ambiguous bases are acceptable
    n_count = seq.count('N')
    if n_count > len(seq) * 0.1:
        warnings.append(f">{10}% N's ({n_count}/{len(seq)})")
        return False, warnings
    return True, warnings


def main():
    wuyts_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('.')

    # Validate input files exist
    required_files = [
        'wuyts_pheS_reference.fasta', 'wuyts_pheS_taxonomy.txt',
        'pheS_reference.fasta', 'pheS_taxonomy.txt'
    ]
    for fname in required_files:
        fpath = wuyts_dir / fname
        if not fpath.exists():
            print(f"ERROR: Required file not found: {fpath}", file=sys.stderr)
            sys.exit(1)

    # Load Wuyts data
    wuyts_seqs = read_fasta(wuyts_dir / 'wuyts_pheS_reference.fasta')
    wuyts_tax = read_taxonomy(wuyts_dir / 'wuyts_pheS_taxonomy.txt')
    print(f"Wuyts: {len(wuyts_seqs)} sequences, {len(wuyts_tax)} taxonomy entries")
    assert len(wuyts_seqs) == len(wuyts_tax), \
        f"Wuyts FASTA ({len(wuyts_seqs)}) != taxonomy ({len(wuyts_tax)}) count mismatch"

    # Load NCBI supplement
    ncbi_seqs = read_fasta(wuyts_dir / 'pheS_reference.fasta')
    ncbi_tax = read_taxonomy(wuyts_dir / 'pheS_taxonomy.txt')
    print(f"NCBI supplement: {len(ncbi_seqs)} sequences, {len(ncbi_tax)} taxonomy entries")
    assert len(ncbi_seqs) == len(ncbi_tax), \
        f"NCBI FASTA ({len(ncbi_seqs)}) != taxonomy ({len(ncbi_tax)}) count mismatch"

    # Group ALL entries by sequence content, with filtering
    # seq -> [(seq_id, species, source), ...]
    seq_to_ids = defaultdict(list)
    stats = {
        'outgroup_retained': 0, 'unresolved_flagged': 0,
        'bad_seq_filtered': 0,
    }

    for seq_id, seq in wuyts_seqs:
        tax_str = wuyts_tax.get(seq_id, '')
        species = extract_species(tax_str)

        # Validate sequence
        is_valid, warnings = validate_sequence(seq, seq_id)
        if not is_valid:
            stats['bad_seq_filtered'] += 1
            for w in warnings:
                print(f"  WARNING: {seq_id}: {w}", file=sys.stderr)
            continue

        # Track outgroups (retained with correct taxonomy for classifier training)
        if is_outgroup(species):
            stats['outgroup_retained'] += 1

        if is_unresolved(species):
            stats['unresolved_flagged'] += 1
            species = species + " [unresolved]"

        seq_to_ids[seq].append((seq_id, species, 'wuyts'))

    for seq_id_full, seq in ncbi_seqs:
        acc = seq_id_full.split()[0]
        tax_str = ncbi_tax.get(acc, '')
        species = extract_species(tax_str)

        is_valid, warnings = validate_sequence(seq, acc)
        if not is_valid:
            stats['bad_seq_filtered'] += 1
            for w in warnings:
                print(f"  WARNING: {acc}: {w}", file=sys.stderr)
            continue

        if is_outgroup(species):
            stats['outgroup_retained'] += 1

        if is_unresolved(species):
            stats['unresolved_flagged'] += 1
            species = species + " [unresolved]"

        seq_to_ids[seq].append((f"ncbi_{acc}", species, 'ncbi'))

    print(f"\nFiltering stats:")
    print(f"  Outgroup taxa retained (with correct taxonomy): {stats['outgroup_retained']}")
    print(f"  Unresolved species flagged: {stats['unresolved_flagged']}")
    print(f"  Bad sequences removed: {stats['bad_seq_filtered']}")
    print(f"  Unique sequences after filtering: {len(seq_to_ids)}")

    # Identify conflicts (same sequence, different species)
    conflicts = []
    for seq, ids in seq_to_ids.items():
        species_set = set(sp for _, sp, _ in ids if sp != 'Unknown')
        if len(species_set) > 1:
            conflicts.append((seq[:30], ids))

    print(f"\nSequences with multiple species assignments: {len(conflicts)}")
    if conflicts:
        print("Conflicts (both identities retained):")
        for seq_start, ids in conflicts:
            print(f"  Seq {seq_start}...")
            for sid, sp, src in ids:
                print(f"    {sid} -> {sp} (from {src})")

    # Build combined output — sorted by sequence ID for reproducibility
    out_fasta = wuyts_dir / 'pheS_combined_reference.fasta'
    out_tax = wuyts_dir / 'pheS_combined_taxonomy.txt'

    count = 0
    multi_identity = 0
    single_identity = 0

    # Sort by first ID in each group for deterministic output
    sorted_items = sorted(seq_to_ids.items(), key=lambda x: x[1][0][0])

    with open(out_fasta, 'w') as fasta_out, open(out_tax, 'w') as tax_out:
        for seq, ids in sorted_items:
            known_ids = [(sid, sp, src) for sid, sp, src in ids if sp != 'Unknown']
            if not known_ids:
                continue

            species_set = set(sp for _, sp, _ in known_ids)

            if len(species_set) == 1:
                # All agree on species — write one entry, note alternates
                primary_id, species, source = known_ids[0]
                alt_ids = [sid for sid, _, _ in known_ids[1:]]

                tax = build_taxonomy(species)

                if alt_ids:
                    header = f"{primary_id} alt_ids={';'.join(alt_ids)}"
                else:
                    header = primary_id

                fasta_out.write(f">{header}\n")
                for i in range(0, len(seq), 80):
                    fasta_out.write(seq[i:i + 80] + '\n')
                tax_out.write(f"{primary_id}\t{tax}\n")
                count += 1
                single_identity += 1

            else:
                # DIFFERENT species for same sequence — retain ALL identities
                multi_identity += 1
                for sid, species, source in known_ids:
                    tax = build_taxonomy(species)

                    fasta_out.write(f">{sid} multi_species_seq=true\n")
                    for i in range(0, len(seq), 80):
                        fasta_out.write(seq[i:i + 80] + '\n')
                    tax_out.write(f"{sid}\t{tax}\n")
                    count += 1

    # Verify output consistency
    out_fasta_count = sum(1 for line in open(out_fasta) if line.startswith('>'))
    out_tax_count = sum(1 for _ in open(out_tax))
    assert out_fasta_count == out_tax_count, \
        f"Output mismatch: FASTA has {out_fasta_count} seqs, taxonomy has {out_tax_count} entries"
    assert out_fasta_count == count, \
        f"Count mismatch: wrote {count} but FASTA has {out_fasta_count}"

    print(f"\n=== Combined database ===")
    print(f"Total entries written: {count}")
    print(f"  Single-identity sequences: {single_identity}")
    print(f"  Multi-identity sequences (both retained): {multi_identity}")
    print(f"  FASTA entries: {out_fasta_count}")
    print(f"  Taxonomy entries: {out_tax_count}")
    print(f"  Consistency check: PASS")

    # Species summary
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

    # Flag unresolved entries
    unresolved = {sp: n for sp, n in sp_counts.items() if '[unresolved]' in sp}
    if unresolved:
        print(f"\nUnresolved species (flagged, not excluded):")
        for sp, n in unresolved.items():
            print(f"  {n:>3}  {sp}")

    print(f"\nOutput files:")
    print(f"  {out_fasta}")
    print(f"  {out_tax}")


if __name__ == '__main__':
    main()
