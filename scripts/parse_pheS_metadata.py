#!/usr/bin/env python3
"""Parse GenBank records to extract geographic origin and strain info for pheS sequences."""

import re
import sys
from collections import defaultdict

infile = sys.argv[1] if len(sys.argv) > 1 else "vaginal_lacto_pheS_gb.txt"

with open(infile) as f:
    text = f.read()

records = text.split("//\n")

header = f"{'Accession':<15} {'Species':<28} {'Strain':<25} {'Country':<25} {'Isolation source':<30}"
print(header)
print("-" * len(header))

country_counts = defaultdict(int)
source_counts = defaultdict(int)
species_data = defaultdict(lambda: {"total": 0, "countries": defaultdict(int), "sources": defaultdict(int)})

for rec in records:
    if not rec.strip():
        continue

    acc_m = re.search(r'ACCESSION\s+(\S+)', rec)
    acc = acc_m.group(1) if acc_m else "?"

    org_m = re.search(r'/organism="([^"]+)"', rec)
    org = org_m.group(1) if org_m else "?"

    strain_m = re.search(r'/strain="([^"]+)"', rec)
    strain = strain_m.group(1) if strain_m else "not specified"

    country_m = re.search(r'/country="([^"]+)"', rec)
    country = country_m.group(1) if country_m else "not specified"

    iso_m = re.search(r'/isolation_source="([^"]+)"', rec)
    iso = iso_m.group(1) if iso_m else "not specified"

    print(f"{acc:<15} {org[:28]:<28} {strain[:25]:<25} {country[:25]:<25} {iso[:30]:<30}")

    country_counts[country.split(":")[0]] += 1
    source_counts[iso.lower()[:40]] += 1

    # Map to vaginal species
    for sp in ["crispatus", "iners", "gasseri", "jensenii"]:
        if sp in org.lower():
            species_data[sp]["total"] += 1
            species_data[sp]["countries"][country.split(":")[0]] += 1
            species_data[sp]["sources"][iso.lower()[:40]] += 1

print("\n" + "=" * 80)
print("GEOGRAPHIC SUMMARY")
print("=" * 80)
for country, n in sorted(country_counts.items(), key=lambda x: -x[1]):
    print(f"  {n:>3}  {country}")

print("\n" + "=" * 80)
print("ISOLATION SOURCE SUMMARY")
print("=" * 80)
for source, n in sorted(source_counts.items(), key=lambda x: -x[1]):
    print(f"  {n:>3}  {source}")

print("\n" + "=" * 80)
print("PER-SPECIES GEOGRAPHIC BREAKDOWN")
print("=" * 80)
for sp in ["crispatus", "iners", "gasseri", "jensenii"]:
    data = species_data[sp]
    print(f"\nL. {sp} ({data['total']} sequences):")
    print(f"  Countries:")
    for c, n in sorted(data["countries"].items(), key=lambda x: -x[1]):
        african = " *** AFRICAN ***" if any(a in c.lower() for a in
            ["south africa", "kenya", "nigeria", "uganda", "rwanda", "ethiopia",
             "tanzania", "mozambique", "zimbabwe", "burkina", "senegal", "ghana"]) else ""
        print(f"    {n:>3}  {c}{african}")
    print(f"  Sources:")
    for s, n in sorted(data["sources"].items(), key=lambda x: -x[1]):
        vaginal = " *** VAGINAL ***" if any(v in s for v in ["vagin", "cervic", "genital"]) else ""
        print(f"    {n:>3}  {s}{vaginal}")

# Check for African origin
print("\n" + "=" * 80)
print("AFRICAN ISOLATES CHECK")
print("=" * 80)
african_countries = ["south africa", "kenya", "nigeria", "uganda", "rwanda",
                     "ethiopia", "tanzania", "mozambique", "zimbabwe", "burkina",
                     "senegal", "ghana", "cameroon", "mali", "congo"]
african_found = False
for country, n in country_counts.items():
    if any(ac in country.lower() for ac in african_countries):
        print(f"  FOUND: {n} sequences from {country}")
        african_found = True
if not african_found:
    print("  *** NO AFRICAN ISOLATES FOUND IN DATABASE ***")
