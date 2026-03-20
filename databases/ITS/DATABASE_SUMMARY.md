# ITS Database — Summary

**Downloaded:** 2026-03-20
**Source:** UNITE v10.0 (2025-02-19) via colinbrislawn/unite-train pre-trained classifiers

## Contents

### Pre-trained QIIME2 classifiers (ready to use)

| File | Threshold | Scope | Size | Use |
|------|-----------|-------|------|-----|
| unite_v10_dynamic_fungi_Q2-2024.10.qza | Dynamic (97-99%) | Fungi only | 220MB | **PRIMARY — recommended by UNITE experts** |
| unite_v10_99_fungi_Q2-2024.10.qza | 99% | Fungi only | 208MB | Higher species-level resolution |

These are pre-trained Naive Bayesian classifiers for QIIME2 2024.10, trained by
Colin J. Brislawn from the UNITE v10.0 (2025-02-19) release.

### QIIME2 version note

Classifiers are version-specific. These are trained for Q2-2024.10. If we install
a different QIIME2 version, we may need to either:
- Download the matching classifier from colinbrislawn/unite-train/releases
- Retrain from raw UNITE FASTA + taxonomy files

### Raw reference files

Raw FASTA + taxonomy from UNITE are available via:
- UNITE QIIME release DOI: https://doi.org/10.15156/BIO/3301241 (dynamic, fungi)
- Zenodo alternative: https://zenodo.org/records/13336328 (UNITE+INSD 2024)
- QIIME2 rescript plugin: `qiime rescript get-unite-data` (automated download)

Not downloaded yet — the pre-trained classifiers are sufficient for now. If we need
to retrain (e.g., add custom vaginal fungal references), download raw files then.

## Primers

- ITS1F: 5-CTTGGTCATTTAGAGGAAGTAA-3 (forward)
- ITS2: 5-GCTGCGTTCTTCATCGATGC-3 (reverse)
- Region: ITS1
- Amplicon: ~250-400 bp (variable by species — normal for ITS)
- Earth Microbiome Project standard

## Pipeline notes

- **ITSxpress v2** required to trim conserved flanking regions before DADA2
- **DADA2 needs customized parameters** (Rivers et al. 2022) — default filtering
  removes C. glabrata, Aspergillus, S. cerevisiae reads due to variable amplicon length
- Can pool ITS1 + 16S amplicons in single MiSeq run (Virtanen et al. 2024)

## Key vaginal taxa to detect

| Taxon | Expected | Clinical relevance |
|-------|----------|-------------------|
| Candida albicans | Common (65% of VVC) | Primary VVC pathogen |
| Candida glabrata | Second most common | Azole-resistant |
| Candida krusei | Occasional | Fluconazole-resistant |
| Candida tropicalis | Occasional | Severe VVC |
| Malassezia spp. | Increased in BV | BV-mycobiome interaction |

## File paths on HTCF

```
/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/databases/ITS/
├── unite_v10/
│   ├── unite_v10_dynamic_fungi_Q2-2024.10.qza   # Pre-trained classifier (USE THIS)
│   └── unite_v10_99_fungi_Q2-2024.10.qza         # Higher resolution alternative
├── DATABASE_SUMMARY.md                            # This file
└── README.md                                      # Original README
```

## Citations

- Abarenkov, K. et al. (2025). UNITE QIIME release for Fungi. Version 19.02.2025.
  DOI: 10.15156/BIO/3301241
- Nilsson, R.H. et al. (2024). UNITE database for molecular identification and
  taxonomic communication of fungi. Nucleic Acids Research, 52(D1), D791-D797.
  DOI: 10.1093/nar/gkad1039
- Brislawn, C.J. Pre-trained UNITE classifiers for QIIME2.
  https://github.com/colinbrislawn/unite-train
