# pheS Database — Summary

**Built:** 2026-03-19, updated 2026-03-20 (expanded + QA fixes)
**Sources:** Wuyts et al. 2021 File S5 + NCBI GenBank + FRESH SA MAGs

## Final database

- **399 entries, 246 species** (pheS_final_reference.fasta / pheS_final_taxonomy.txt)
- USE THESE FILES for classifier training
- Taxonomy: QIIME2-compatible (k__; p__; c__; o__; f__; g__; s__)
- Output sorted by sequence ID for reproducibility
- 1 multi-species sequence (both identities retained)

### Construction pipeline

1. Wuyts et al. 2021 File S5: 453 seqs extracted from Excel-format FASTA
2. NCBI species lookup: 410/453 mapped to species
3. Deduplication: 336 unique Wuyts sequences
4. NCBI supplement (vaginal Lactobacillus): +47 new sequences
5. Expanded NCBI search (outgroup taxa + vaginal sources): +16 new sequences
6. FRESH SA MAG extraction (L. iners, ectocervical mucosa, South Africa): +1 sequence
7. Outgroup taxa retained with CORRECT higher taxonomy for classifier training
8. Unresolved species flagged with [unresolved] tag

### Vaginal Lactobacillus coverage

| Species | Count | Sources |
|---------|-------|---------|
| L. crispatus | 9 | Type strains + urinary isolates |
| L. iners | 11 | Type strains + urinary + 1 SA ectocervical MAG |
| L. gasseri | 17 | Type strains + urinary isolates |
| L. jensenii | 11 | Type strains + urinary isolates |
| L. vaginalis | 1 | Type strain |

### Outgroup taxa (with correct family taxonomy)

| Taxon | Family | Count | Role |
|-------|--------|-------|------|
| Bifidobacterium spp. | Bifidobacteriaceae | 9 | Vaginal outgroup + classifier training |
| Bacillus subtilis | Bacillaceae | 1 | Non-LAB outgroup |
| Enterococcus faecalis | Enterococcaceae | 1 | Non-LAB outgroup |
| Lactococcus lactis | Streptococcaceae | 1 | Non-LAB outgroup |
| Leuconostoc spp. | Leuconostocaceae | 2 | Non-LAB outgroup |
| Oenococcus oeni | Oenococcaceae | 1 | Non-LAB outgroup |
| Weissella viridescens | Leuconostocaceae | 1 | Non-LAB outgroup |

### Vaginal outgroup taxa identified but pending extraction (WGS genomes, need BLAST)

| Taxon | WGS records | Priority |
|-------|-------------|----------|
| Streptococcus agalactiae | ~100 | High — vaginal colonizer |
| Megasphaera spp. | 28 | High — BV-associated |
| Gardnerella vaginalis | 3 | Medium — primary cpn60 target |
| Prevotella bivia | 4 | Medium — sialidase producer |
| Mobiluncus curtisii | 1 | Medium — BV-associated, vaginal source |
| Sneathia sp. | 1 | Low |

### FRESH SA MAG pheS extraction status

- 50 South African ectocervical Lactobacillus MAGs identified (BioSample SAMN25184*)
- 1 L. iners pheS successfully extracted (JAOBJG contig 74)
- 1 L. crispatus pheS extracted via primer binding (JAOBIJ contig 16)
- Remaining 48 MAGs need full contig download + extraction (batch job pending)

## Primers

- pheS21F: 5-CAYCCNGCHCGYGAYATGC-3
- pheS23R: 5-GGRTGRACCATVCCNGCHCC-3
- Amplicon: ~431 bp

## Known gaps

- No African-origin pheS in direct NCBI deposits (all "not specified" country)
- FRESH SA MAG extraction incomplete (1/50 L. iners done)
- Megasphaera, Gardnerella, Prevotella, Mobiluncus, Sneathia pheS need WGS extraction
- L. vaginalis: only 1 sequence
- Fannyhessea vaginae: 0 pheS found in NCBI

## File paths on HTCF

```
/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/databases/pheS/
├── wuyts2021/
│   ├── pheS_final_reference.fasta     # 399 entries — USE THIS
│   ├── pheS_final_taxonomy.txt        # Final taxonomy — USE THIS
│   ├── pheS_combined_reference.fasta  # Intermediate (383 entries, pre-expansion)
│   ├── pheS_combined_taxonomy.txt     # Intermediate taxonomy
│   ├── wuyts_pheS_db.fasta            # Raw Wuyts 453 sequences
│   ├── wuyts_pheS_reference.fasta     # Wuyts deduplicated (336)
│   ├── wuyts_pheS_taxonomy.txt        # Wuyts taxonomy
│   ├── wuyts_acc_to_species.tsv       # NCBI accession mapping
│   ├── pheS_reference.fasta           # NCBI supplement (59)
│   └── pheS_taxonomy.txt              # NCBI supplement taxonomy
└── DATABASE_SUMMARY.md                # This file
```

## Citations

- Wuyts, S. et al. (2021). Appl Environ Microbiol, 87, e02191-20. DOI: 10.1128/AEM.02191-20
- Naser, S.M. et al. (2007). IJSEM, 57, 2777-2789. DOI: 10.1099/ijs.0.64711-0
