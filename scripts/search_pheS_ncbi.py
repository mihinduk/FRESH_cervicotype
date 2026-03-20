#!/usr/bin/env python3
"""
Search NCBI for pheS sequences from vaginal Lactobacillus and vaginal outgroup taxa.
Prioritize: vaginal source, African/non-Western origin, geographic diversity.

Usage:
    python3 search_pheS_ncbi.py output_dir
"""

import sys
import re
import time
import json
import urllib.request
import urllib.parse
from pathlib import Path
from collections import defaultdict

NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

# Search targets: (organism, search terms, description)
TARGETS = [
    # Vaginal Lactobacillus — broad search to catch vaginal/cervical isolates
    ("Lactobacillus crispatus", "pheS[Gene Name] AND 200:800[Sequence Length]", "L. crispatus pheS"),
    ("Lactobacillus iners", "pheS[Gene Name] AND 200:800[Sequence Length]", "L. iners pheS"),
    ("Lactobacillus gasseri", "pheS[Gene Name] AND 200:800[Sequence Length]", "L. gasseri pheS"),
    ("Lactobacillus jensenii", "pheS[Gene Name] AND 200:800[Sequence Length]", "L. jensenii pheS"),
    # Also search with vaginal/cervical in any field
    ("Lactobacillus crispatus", "(pheS OR phenylalanyl) AND (vaginal OR cervical OR genital) AND 200:2000[Sequence Length]", "L. crispatus vaginal"),
    ("Lactobacillus iners", "(pheS OR phenylalanyl) AND (vaginal OR cervical OR genital) AND 200:2000[Sequence Length]", "L. iners vaginal"),
    # Vaginal outgroup taxa — search for pheS where available
    ("Gardnerella vaginalis", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "G. vaginalis pheS"),
    ("Gardnerella piotii", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "G. piotii pheS"),
    ("Fannyhessea vaginae", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "F. vaginae pheS"),
    ("Atopobium vaginae", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "A. vaginae pheS"),
    ("Streptococcus agalactiae", "pheS[Gene Name] AND 200:800[Sequence Length]", "S. agalactiae pheS"),
    ("Bifidobacterium", "pheS[Gene Name] AND 200:800[Sequence Length]", "Bifidobacterium pheS"),
    ("Mobiluncus", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "Mobiluncus pheS"),
    ("Megasphaera", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "Megasphaera pheS"),
    ("Sneathia", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "Sneathia pheS"),
    ("Prevotella bivia", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "P. bivia pheS"),
    ("Prevotella timonensis", "(pheS OR phenylalanyl) AND 200:800[Sequence Length]", "P. timonensis pheS"),
]

# Also search for African-origin Lactobacillus pheS broadly
AFRICAN_SEARCHES = [
    ("Lactobacillus", 'pheS[Gene Name] AND (Africa OR "South Africa" OR Kenya OR Nigeria OR Uganda OR Rwanda OR Ethiopia) AND 200:800[Sequence Length]', "African Lactobacillus pheS"),
    ("Lactobacillus", '(pheS OR phenylalanyl) AND vaginal AND 200:2000[Sequence Length]', "All vaginal Lactobacillus pheS"),
]


def esearch(db, term, retmax=200):
    """Search NCBI and return list of IDs."""
    params = urllib.parse.urlencode({
        "db": db, "term": term, "retmax": retmax, "retmode": "xml"
    })
    url = f"{NCBI_BASE}/esearch.fcgi?{params}"
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            text = resp.read().decode()
        count_m = re.search(r"<Count>(\d+)</Count>", text)
        count = int(count_m.group(1)) if count_m else 0
        ids = re.findall(r"<Id>(\d+)</Id>", text)
        return count, ids
    except Exception as e:
        print(f"  ERROR in esearch: {e}", file=sys.stderr)
        return 0, []


def efetch_gb(db, ids):
    """Fetch GenBank records for a list of IDs."""
    if not ids:
        return ""
    id_str = ",".join(ids[:200])  # Max 200 per request
    data = urllib.parse.urlencode({
        "db": db, "id": id_str, "rettype": "gb", "retmode": "text"
    }).encode()
    try:
        req = urllib.request.Request(f"{NCBI_BASE}/efetch.fcgi", data=data)
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.read().decode()
    except Exception as e:
        print(f"  ERROR in efetch: {e}", file=sys.stderr)
        return ""


def parse_gb_records(text):
    """Parse GenBank text into list of record dicts."""
    records = []
    for rec in text.split("//\n"):
        if not rec.strip():
            continue
        acc_m = re.search(r'ACCESSION\s+(\S+)', rec)
        org_m = re.search(r'/organism="([^"]+)"', rec)
        strain_m = re.search(r'/strain="([^"]+)"', rec)
        country_m = re.search(r'/country="([^"]+)"', rec)
        iso_m = re.search(r'/isolation_source="([^"]+)"', rec)
        len_m = re.search(r'LOCUS\s+\S+\s+(\d+)\s+bp', rec)

        # Extract sequence
        origin_m = re.search(r'ORIGIN\s*\n(.*)', rec, re.DOTALL)
        seq = ""
        if origin_m:
            seq = re.sub(r'[^acgtACGT]', '', origin_m.group(1)).upper()

        records.append({
            "acc": acc_m.group(1) if acc_m else "?",
            "organism": org_m.group(1) if org_m else "?",
            "strain": strain_m.group(1) if strain_m else "not specified",
            "country": country_m.group(1) if country_m else "not specified",
            "isolation_source": iso_m.group(1) if iso_m else "not specified",
            "length": int(len_m.group(1)) if len_m else len(seq),
            "sequence": seq,
        })
    return records


def main():
    outdir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    outdir.mkdir(parents=True, exist_ok=True)

    all_records = []

    # Run all searches
    for searches in [TARGETS, AFRICAN_SEARCHES]:
        for organism, extra_terms, desc in searches:
            term = f'"{organism}"[Organism] AND {extra_terms}'
            print(f"\n--- {desc} ---")
            print(f"  Query: {term}")

            count, ids = esearch("nucleotide", term)
            print(f"  Results: {count} (fetching {len(ids)})")

            if ids:
                gb_text = efetch_gb("nucleotide", ids[:100])  # Limit to 100 per target
                records = parse_gb_records(gb_text)
                print(f"  Parsed: {len(records)} records")
                for r in records:
                    r["search_desc"] = desc
                all_records.extend(records)

            time.sleep(0.5)  # Be nice to NCBI

    # Deduplicate by accession
    seen_acc = set()
    unique_records = []
    for r in all_records:
        if r["acc"] not in seen_acc and r["acc"] != "?":
            seen_acc.add(r["acc"])
            unique_records.append(r)

    print(f"\n{'='*80}")
    print(f"TOTAL UNIQUE RECORDS: {len(unique_records)}")
    print(f"{'='*80}")

    # Summary tables
    print(f"\n{'Accession':<15} {'Organism':<30} {'Country':<20} {'Source':<25} {'Len':>5}")
    print("-" * 100)
    for r in sorted(unique_records, key=lambda x: x["organism"]):
        print(f"{r['acc']:<15} {r['organism'][:30]:<30} {r['country'][:20]:<20} {r['isolation_source'][:25]:<25} {r['length']:>5}")

    # Geographic summary
    print(f"\n{'='*80}")
    print("GEOGRAPHIC SUMMARY")
    print(f"{'='*80}")
    countries = defaultdict(int)
    for r in unique_records:
        countries[r["country"].split(":")[0]] += 1
    for c, n in sorted(countries.items(), key=lambda x: -x[1]):
        african = " *** AFRICAN ***" if any(a in c.lower() for a in
            ["south africa", "kenya", "nigeria", "uganda", "rwanda",
             "ethiopia", "tanzania", "mozambique", "zimbabwe", "burkina",
             "senegal", "ghana", "cameroon", "mali", "congo"]) else ""
        vaginal = ""
        print(f"  {n:>3}  {c}{african}")

    # Source summary
    print(f"\n{'='*80}")
    print("ISOLATION SOURCE SUMMARY")
    print(f"{'='*80}")
    sources = defaultdict(int)
    for r in unique_records:
        sources[r["isolation_source"].lower()[:40]] += 1
    for s, n in sorted(sources.items(), key=lambda x: -x[1]):
        vaginal = " *** VAGINAL ***" if any(v in s for v in ["vagin", "cervic", "genital"]) else ""
        print(f"  {n:>3}  {s}{vaginal}")

    # Write FASTA
    fasta_path = outdir / "pheS_ncbi_expanded.fasta"
    with open(fasta_path, "w") as f:
        for r in unique_records:
            if r["sequence"] and len(r["sequence"]) >= 200:
                f.write(f">{r['acc']} {r['organism']} strain={r['strain']} "
                        f"country={r['country']} source={r['isolation_source']}\n")
                seq = r["sequence"]
                for i in range(0, len(seq), 80):
                    f.write(seq[i:i + 80] + "\n")

    seq_count = sum(1 for line in open(fasta_path) if line.startswith(">"))
    print(f"\nWrote {seq_count} sequences to {fasta_path}")

    # Write metadata TSV
    tsv_path = outdir / "pheS_ncbi_expanded_metadata.tsv"
    with open(tsv_path, "w") as f:
        f.write("accession\torganism\tstrain\tcountry\tisolation_source\tlength\tsearch\n")
        for r in unique_records:
            f.write(f"{r['acc']}\t{r['organism']}\t{r['strain']}\t{r['country']}\t"
                    f"{r['isolation_source']}\t{r['length']}\t{r['search_desc']}\n")

    print(f"Wrote metadata to {tsv_path}")


if __name__ == "__main__":
    main()
