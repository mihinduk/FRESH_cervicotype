#!/usr/bin/env python3
"""
Extract cpn60 universal target (UT) region from genome sequences using
in silico PCR with H279/H280 primer binding sites.

The cpn60 UT corresponds to nt 274-828 of the E. coli groEL gene (~555 bp).
Rather than filtering by size, we locate the primer binding sites and extract
the region between them.

Usage:
    python3 extract_cpn60_ut.py input.fasta output_ut.fasta [--min-len 500] [--max-len 600]

Input: FASTA file (genomes, contigs, or gene sequences)
Output: FASTA file with extracted UT regions

Primer sequences (degenerate, from Hill lab):
  H279 (forward): GAIIIIGCIGGIGAYGGIACIACIAC
  H280 (reverse): YKIYKITCICCRAAICCIGGIGCYTT

Where I = inosine (matches any base), Y = C/T, K = G/T, R = A/G, S = G/C, D = A/G/T
"""

import re
import sys
import argparse
from pathlib import Path


# IUPAC degenerate base to regex mapping
IUPAC = {
    'A': 'A', 'C': 'C', 'G': 'G', 'T': 'T',
    'R': '[AG]', 'Y': '[CT]', 'K': '[GT]', 'M': '[AC]',
    'S': '[GC]', 'W': '[AT]', 'B': '[CGT]', 'D': '[AGT]',
    'H': '[ACT]', 'V': '[ACG]', 'N': '[ACGT]',
    'I': '[ACGT]',  # Inosine pairs with all bases
}


def degenerate_to_regex(primer_seq):
    """Convert a degenerate primer sequence to a regex pattern."""
    pattern = ''.join(IUPAC.get(base.upper(), base) for base in primer_seq)
    return pattern


def reverse_complement(seq):
    """Return reverse complement of a DNA sequence."""
    complement = str.maketrans('ACGTRYKMSWBDHVNacgtrykmswbdhvn',
                                'TGCAYRMKSWVHDBNtgcayrkmswvhdbn')
    return seq.translate(complement)[::-1]


def read_fasta(filepath):
    """Read FASTA file, yield (header, sequence) tuples."""
    header = None
    seq_parts = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if header is not None:
                    yield header, ''.join(seq_parts)
                header = line[1:]
                seq_parts = []
            else:
                seq_parts.append(line.upper())
    if header is not None:
        yield header, ''.join(seq_parts)


def find_ut_region(sequence, fwd_regex, rev_regex, min_len=500, max_len=600):
    """
    Find cpn60 UT region by locating forward and reverse primer binding sites.

    Returns list of (start, end, ut_sequence) tuples for all hits.
    Searches both strands.
    """
    hits = []

    # Search forward strand
    for fwd_match in re.finditer(fwd_regex, sequence, re.IGNORECASE):
        fwd_start = fwd_match.start()
        # Look for reverse primer downstream (within reasonable distance)
        search_region = sequence[fwd_start:fwd_start + max_len + 100]
        rev_match = re.search(rev_regex, search_region, re.IGNORECASE)
        if rev_match:
            ut_end = fwd_start + rev_match.end()
            ut_seq = sequence[fwd_start:ut_end]
            if min_len <= len(ut_seq) <= max_len:
                hits.append((fwd_start, ut_end, ut_seq))

    # Search reverse strand
    rc_sequence = reverse_complement(sequence)
    for fwd_match in re.finditer(fwd_regex, rc_sequence, re.IGNORECASE):
        fwd_start = fwd_match.start()
        search_region = rc_sequence[fwd_start:fwd_start + max_len + 100]
        rev_match = re.search(rev_regex, search_region, re.IGNORECASE)
        if rev_match:
            ut_end = fwd_start + rev_match.end()
            ut_seq = rc_sequence[fwd_start:ut_end]
            if min_len <= len(ut_seq) <= max_len:
                # Convert coordinates back to forward strand
                orig_start = len(sequence) - ut_end
                orig_end = len(sequence) - fwd_start
                hits.append((orig_start, orig_end, ut_seq))

    return hits


def main():
    parser = argparse.ArgumentParser(
        description='Extract cpn60 UT region using in silico PCR with H279/H280 primers')
    parser.add_argument('input_fasta', help='Input FASTA file (genomes, contigs, or genes)')
    parser.add_argument('output_fasta', help='Output FASTA with extracted UT regions')
    parser.add_argument('--min-len', type=int, default=500,
                        help='Minimum UT length (default: 500)')
    parser.add_argument('--max-len', type=int, default=600,
                        help='Maximum UT length (default: 600)')
    parser.add_argument('--allow-mismatches', type=int, default=0,
                        help='Not yet implemented — future: allow N mismatches in primers')
    args = parser.parse_args()

    # H279 forward primer
    H279 = 'GAIIIIGCIGGIGAYGGIACIACIAC'
    # H280 reverse primer — we need its reverse complement to find binding site on template
    H280 = 'YKIYKITCICCRAAICCIGGIGCYTT'
    H280_rc = reverse_complement(H280)

    fwd_regex = degenerate_to_regex(H279)
    # The reverse primer binds the opposite strand, so on the template strand
    # we look for the reverse complement of H280
    rev_regex = degenerate_to_regex(H280_rc)

    print(f"Forward primer (H279): {H279}")
    print(f"Forward regex: {fwd_regex}")
    print(f"Reverse primer RC (H280_rc): {H280_rc}")
    print(f"Reverse regex: {rev_regex}")
    print(f"Expected UT size: {args.min_len}-{args.max_len} bp")
    print()

    total_seqs = 0
    total_hits = 0

    with open(args.output_fasta, 'w') as out:
        for header, sequence in read_fasta(args.input_fasta):
            total_seqs += 1
            hits = find_ut_region(sequence, fwd_regex, rev_regex,
                                  args.min_len, args.max_len)

            for i, (start, end, ut_seq) in enumerate(hits):
                total_hits += 1
                # Parse accession from header
                acc = header.split()[0]
                hit_header = f"{acc}_UT{i+1} len={len(ut_seq)} pos={start}-{end} {header}"
                out.write(f">{hit_header}\n")
                # Write sequence in 80-char lines
                for j in range(0, len(ut_seq), 80):
                    out.write(ut_seq[j:j+80] + '\n')

            if total_seqs % 100 == 0:
                print(f"  Processed {total_seqs} sequences, {total_hits} UT regions found...",
                      file=sys.stderr)

    print(f"\nResults:")
    print(f"  Input sequences: {total_seqs}")
    print(f"  UT regions extracted: {total_hits}")
    print(f"  Output: {args.output_fasta}")


if __name__ == '__main__':
    main()
