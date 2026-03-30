#!/usr/bin/env python3
"""
Fetch SRA run accessions for a list of BioProject accessions.
Writes one file per BioProject with run accessions (one per line).

Usage:
    python3 get_sra_runs.py <output_dir> <PRJNA1> [PRJNA2] ...
"""

import sys
import re
import json
import time
import xml.etree.ElementTree as ET
import urllib.request
from pathlib import Path


def esearch(db, term, retmax=500):
    """Search NCBI and return list of internal IDs."""
    url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
           f"?db={db}&term={term}&retmax={retmax}&retmode=xml")
    try:
        with urllib.request.urlopen(url, timeout=30) as resp:
            text = resp.read().decode()
        tree = ET.fromstring(text)
        count = tree.find("Count").text
        ids = [i.text for i in tree.findall(".//Id")]
        return int(count), ids
    except Exception as e:
        print(f"  ERROR in esearch: {e}", file=sys.stderr)
        return 0, []


def get_run_accessions(sra_ids):
    """Fetch SRA summaries and extract SRR/ERR run accessions."""
    runs = []
    # Process in batches of 200
    for i in range(0, len(sra_ids), 200):
        batch = sra_ids[i:i+200]
        id_str = ",".join(batch)
        url = (f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
               f"?db=sra&id={id_str}&retmode=json")
        try:
            with urllib.request.urlopen(url, timeout=60) as resp:
                data = json.loads(resp.read())
            for uid in data.get("result", {}).get("uids", []):
                entry = data["result"][uid]
                runs_xml = entry.get("runs", "")
                srrs = re.findall(r'acc="(SRR\d+|ERR\d+)"', runs_xml)
                runs.extend(srrs)
        except Exception as e:
            print(f"  ERROR fetching batch: {e}", file=sys.stderr)
        time.sleep(0.5)
    return runs


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 get_sra_runs.py <output_dir> <PRJNA1> [PRJNA2] ...")
        sys.exit(1)

    outdir = Path(sys.argv[1])
    outdir.mkdir(parents=True, exist_ok=True)
    bioprojects = sys.argv[2:]

    for proj in bioprojects:
        print(f"\n=== {proj} ===")
        count, ids = esearch("sra", f"{proj}[BioProject]")
        print(f"  Total SRA entries: {count}")
        print(f"  Retrieved IDs: {len(ids)}")

        if not ids:
            print(f"  No data found for {proj}")
            continue

        runs = get_run_accessions(ids)
        print(f"  Run accessions: {len(runs)}")
        if runs:
            print(f"  First 5: {runs[:5]}")
            outfile = outdir / f"{proj}_runs.txt"
            with open(outfile, "w") as f:
                f.write("\n".join(runs) + "\n")
            print(f"  Written to: {outfile}")


if __name__ == "__main__":
    main()
