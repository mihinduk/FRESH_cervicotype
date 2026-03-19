# cpn60 Database v11.1 — Summary

**Downloaded:** 2026-03-19
**Source:** https://github.com/HillLabSask/cpn60-Classifier/releases/tag/v11.1

## Contents

### Reference sequences
- **16,413 curated cpn60 barcode sequences** (refseqs_v11.fasta)
- Taxonomy: 18-rank lineage table (taxonomytable_v11.txt)

### Pre-trained classifiers
- **RDP Naive Bayesian classifier** (v11_training_files/) — ready for standalone RDP classifier
- **QIIME2 q2-feature-classifier artifact** (cpn60_classifier_v11.qza) — ready for QIIME2

### Training data
- Raw FASTA + taxonomy table for retraining if database is expanded

## Key vaginal taxa coverage

| Taxon | # sequences | Species resolved |
|-------|-------------|-----------------|
| Gardnerella | 51 | G. vaginalis (15), G. piotii (7), G. swidsinskii (5), G. leopoldii (4), + 8 genomospecies |
| Lactobacillus crispatus | 9 | Yes |
| Lactobacillus iners | 15 | Yes |
| Lactobacillus gasseri | 10 | Yes |
| Lactobacillus jensenii | 3 | Yes |
| Prevotella | 124 | Multiple species |
| Megasphaera | 7 | Yes |
| Fannyhessea/Atopobium | 5 | Yes |
| Sneathia | 2 | Yes |
| BVAB (Acetatifactor/Mageeibacillus) | 2 | Yes |

## Gardnerella species breakdown (critical for project)

- G. vaginalis: 15 sequences (sensu stricto, subgroup C / clade 1)
- G. piotii: 7 sequences (subgroup B / clade 2, 100% sialidase+)
- G. swidsinskii: 5 sequences (subgroup A / clade 4)
- G. leopoldii: 4 sequences (subgroup A / clade 4)
- Gardnerella genome sp. 2-13: 20 sequences across 8 genomospecies

## Mollicute coverage
- **None** — Mollicutes lack cpn60. If any Mollicute sequences appear in results, this indicates a database or analysis error.

## File paths on HTCF

```
/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/databases/cpn60/v11.1/
├── cpn60-Classifier_v11.0_training/
│   ├── refseqs_v11.fasta          # 16,413 reference sequences
│   └── taxonomytable_v11.txt      # Full taxonomy table
├── cpn60-q2-feature-classifier-v11/
│   ├── cpn60_classifier_v11.qza   # Pre-trained QIIME2 classifier
│   ├── cpn60_v11_seqs.fasta       # QIIME2-formatted sequences
│   └── cpn60_v11_taxonomy_table.txt  # QIIME2-formatted taxonomy
├── v11_training_files/            # RDP trained classifier files
│   ├── bergeyTrainingTree.xml
│   ├── genus_wordConditionalProbList.txt
│   ├── logWordPrior.txt
│   ├── rRNAClassifier.properties
│   └── wordConditionalProbIndexArr.txt
├── addFullLineage-jh.py           # Utility: add full lineage
└── lineage2taxTrain.py            # Utility: convert lineage to training format
```

## Citation
Ren, Q. & Hill, J.E. (2023). Rapid and accurate taxonomic classification of cpn60 amplicon sequence variants. ISME Communications, 3, 77. DOI: 10.1038/s43705-023-00283-z
