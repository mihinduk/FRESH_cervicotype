# pheS Database — Summary

**Built:** 2026-03-19
**Sources:** Wuyts et al. 2021 File S5 (Excel-formatted FASTA) + NCBI GenBank supplement

## Construction

1. Extracted 453 pheS sequences from Wuyts et al. 2021 File S5 (aem.02191-20-sd005.xlsx)
   — yes, the FASTA was stored in a single-column Excel file
2. Retrieved species names for 410/453 accessions via NCBI ESummary
3. Supplemented with 59 additional pheS sequences from NCBI GenBank, focused on
   vaginal Lactobacillus species (L. crispatus, L. iners, L. gasseri, L. jensenii)
4. Deduplicated by exact sequence identity. When multiple accessions shared the
   same sequence, species assignments were compared:
   - Same species: one entry retained, alternates noted in FASTA header (alt_ids=)
   - Different species: BOTH entries retained with multi_species_seq=true flag
   - Result: 0 conflicts found — all shared sequences had concordant species
5. 47 NCBI sequences were novel (not in Wuyts); 12 were duplicates

## Combined database

- **383 unique pheS sequences** (pheS_combined_reference.fasta)
- **240 unique species** (pheS_combined_taxonomy.txt)
- Taxonomy format: QIIME2-compatible (k__; p__; c__; o__; f__; g__; s__)

### Vaginal species coverage (critical for this project)

| Species | Wuyts only | + NCBI supplement | Total |
|---------|-----------|-------------------|-------|
| L. crispatus | 1 | +8 | **9** |
| L. iners | 2 | +6 | **8** |
| L. gasseri | 6 | +11 | **17** |
| L. jensenii | 1 | +10 | **11** |
| L. vaginalis | 1 | +0 | **1** |

The NCBI supplement was essential — Wuyts had only 1-2 sequences per vaginal
species because the database was built from food/environment isolates.

### Comparison to original Wuyts framework

| Feature | Wuyts 2021 | Combined database |
|---------|-----------|-------------------|
| Total sequences | 445 (453 in Excel) | 383 (after dedup + unmapped removal) |
| Species covered | 277 | 240 |
| Vaginal Lactobacillus depth | 11 total | 46 total |
| African isolates | 0 | 0 (gap remains) |

Note: Combined database has fewer total sequences than Wuyts because 43 accessions
could not be mapped to species via NCBI (excluded), and duplicates were removed.

## Primers

- pheS21F: 5-CAYCCNGCHCGYGAYATGC-3
- pheS23R: 5-GGRTGRACCATVCCNGCHCC-3
- Amplicon: ~431 bp (Illumina-compatible)
- Specificity: Lactobacillaceae and related LAB only

## Classifier status

**Not yet built.** Next steps:
1. Train RDP Naive Bayesian classifier on the combined reference
2. Prepare QIIME2 q2-feature-classifier artifact
3. Validate with leave-one-out cross-validation

## Known gaps

- No African pheS isolates in any public database
- L. vaginalis underrepresented (1 sequence)
- 43 Wuyts accessions unmapped — may be retrievable with manual curation
- L. iners strain-level diversity may not be fully captured (8 sequences)

## File paths on HTCF

```
/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/databases/pheS/
├── wuyts2021/
│   ├── pheS_combined_reference.fasta   # 383 combined unique sequences (USE THIS)
│   ├── pheS_combined_taxonomy.txt      # Combined taxonomy (USE THIS)
│   ├── wuyts_pheS_db.fasta             # Original 453 Wuyts sequences (raw extract)
│   ├── wuyts_pheS_reference.fasta      # Wuyts only, deduplicated (336 seqs)
│   ├── wuyts_pheS_taxonomy.txt         # Wuyts taxonomy
│   ├── wuyts_acc_to_species.tsv        # Accession-to-species mapping from NCBI
│   ├── pheS_reference.fasta            # NCBI supplement only (59 seqs)
│   ├── pheS_taxonomy.txt               # NCBI supplement taxonomy
│   └── pheS_vaginal_species.fasta      # Raw NCBI vaginal species downloads
├── DATABASE_SUMMARY.md                 # This file
└── README.md                           # Original README
```

## Citations

- Wuyts, S. et al. (2021). Appl Environ Microbiol, 87, e02191-20. DOI: 10.1128/AEM.02191-20
- Naser, S.M. et al. (2007). IJSEM, 57, 2777-2789. DOI: 10.1099/ijs.0.64711-0
