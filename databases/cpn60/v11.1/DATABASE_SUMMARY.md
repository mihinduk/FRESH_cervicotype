# cpn60 Database v11.1 — Summary

**Downloaded:** 2026-03-19
**Source:** https://github.com/HillLabSask/cpn60-Classifier/releases/tag/v11.1

**Version note:** GitHub release tag is v11.1; internal files are named v11.0/v11
(v11.1 is a release-level update to the v11.0 training data). All files in this
directory were downloaded from the v11.1 release.

## Contents

### Reference sequences
- **16,413 curated cpn60 barcode sequences** (refseqs_v11.fasta)
- Taxonomy: 18-rank lineage table (taxonomytable_v11.txt)
- Line endings converted from CRLF to LF (2026-03-19)

### Pre-trained classifiers
- **RDP Naive Bayesian classifier** (v11_training_files/) — ready for standalone RDP classifier
- **QIIME2 q2-feature-classifier artifact** (cpn60_classifier_v11.qza) — ready for QIIME2

### Training data
- Raw FASTA + taxonomy table for retraining if database is expanded

## Key vaginal taxa coverage

| Taxon | # sequences | Species resolved |
|-------|-------------|-----------------|
| Gardnerella | 51 | G. vaginalis (16), G. piotii (7), G. swidsinskii (5), G. leopoldii (4), + 9 genomospecies (19 seqs) |
| Lactobacillus crispatus | 9 | Yes |
| Lactobacillus iners | 15 | Yes |
| Lactobacillus gasseri | 10 | Yes |
| Lactobacillus jensenii | 3 | Yes |
| Prevotella | 124 | 48 unique species including P. bivia (4), P. amnii (3), P. timonensis (2) |
| Megasphaera | 7 | Yes |
| Fannyhessea/Atopobium | 5 | Yes |
| Sneathia | 2 | Yes |
| BVAB (Acetatifactor/Mageeibacillus) | 2 | Yes |

## Gardnerella species breakdown (critical for project)

Species assignments based on updated Gardnerella taxonomy (Vaneechoutte et al. 2019;
cpn60 subgroup assignments from Paramel Jayaprakash et al. 2012):

- G. vaginalis: 16 sequences (sensu stricto)
- G. piotii: 7 sequences (associated with sialidase activity; Schuyler et al. 2016)
- G. swidsinskii: 5 sequences
- G. leopoldii: 4 sequences
- Gardnerella genome sp. 2, 3, 7, 8, 9, 10, 11, 12, 13: 19 sequences across 9 genomospecies

**Genomospecies-to-species name mapping (Vaneechoutte et al. 2019):**
cpnDB v11.1 uses formal species names, not genomospecies numbers. The following
aliases are equivalent — both appear in the literature and cause confusion:

| Genomospecies | Named Species | cpn60 Subgroup | Clade | In cpnDB as |
|---------------|---------------|----------------|-------|-------------|
| GS1 (sensu stricto) | G. vaginalis | Subgroup C | Clade 1 | G. vaginalis (16 seqs) |
| GS2 | (multiple genomospecies) | Subgroup D | Clade 3 | Gardnerella genome sp. 2 (3 seqs) |
| GS3 | (not yet named) | Subgroup D | Clade 3 | Gardnerella genome sp. 3 (6 seqs) |
| **GS4** | **G. piotii** | **Subgroup B** | **Clade 2** | **G. piotii (7 seqs)** |
| **GS5** | **G. leopoldii** | **Subgroup A** | **Clade 4** | **G. leopoldii (4 seqs)** |
| **GS6** | **G. swidsinskii** | **Subgroup A** | **Clade 4** | **G. swidsinskii (5 seqs)** |
| GS7-13 | (not yet named) | Various | Various | Gardnerella genome sp. 7-13 |

**Note:** GS4/5/6 do NOT appear as "genome sp. 4/5/6" in cpnDB because they were
renamed to their formal species names. This is correct and expected — not a gap.

## Mollicute coverage — NUANCED

The database contains **82 Mollicute entries**, including:
- 27 Mycoplasma (M. gallisepticum: 12, M. genitalium: 5, M. pneumoniae: 4, others)
- 39 Candidatus Phytoplasma
- 5 Acholeplasma
- 5 Spiroplasma
- 6 other Mollicutes

Some Mollicute lineages (Acholeplasma, Phytoplasma, certain Mycoplasma spp.) retain
the cpn60 gene. However, the clinically relevant vaginal Mollicutes for this project
— specifically **M. hominis and all Ureaplasma species** — LACK cpn60 entirely
(0 Ureaplasma entries in the database). M. genitalium IS present (5 entries) but is
not expected to be detected by the universal cpn60 primers in a vaginal community
context due to its intracellular lifestyle and low abundance.

**Practical implication:** Supplementary Mollicute-specific PCR (MgPa, 16S, ureC
targets) remains essential for detecting M. hominis and Ureaplasma in FRESH samples.

## File paths on HTCF

```
/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/databases/cpn60/v11.1/
├── cpn60-Classifier_v11.0_training/
│   ├── refseqs_v11.fasta          # 16,413 reference sequences
│   └── taxonomytable_v11.txt      # Full taxonomy table (LF line endings)
├── cpn60-q2-feature-classifier-v11/
│   ├── cpn60_classifier_v11.qza   # Pre-trained QIIME2 classifier
│   ├── cpn60_v11_seqs.fasta       # QIIME2-formatted sequences
│   └── cpn60_v11_taxonomy_table.txt  # QIIME2-formatted taxonomy (LF)
├── v11_training_files/            # RDP trained classifier files
│   ├── bergeyTrainingTree.xml
│   ├── genus_wordConditionalProbList.txt
│   ├── logWordPrior.txt
│   ├── rRNAClassifier.properties
│   └── wordConditionalProbIndexArr.txt
├── addFullLineage-jh.py           # Utility: add full lineage
├── lineage2taxTrain.py            # Utility: convert lineage to training format
└── DATABASE_SUMMARY.md            # This file
```

## Citations

- Ren, Q. & Hill, J.E. (2023). Rapid and accurate taxonomic classification of cpn60 amplicon sequence variants. ISME Communications, 3, 77. DOI: 10.1038/s43705-023-00283-z
- Vaneechoutte, M. et al. (2019). Emended description of Gardnerella vaginalis and description of G. leopoldii, G. piotii, G. swidsinskii. IJSEM, 69(3), 679-687.
- Paramel Jayaprakash, T. et al. (2012). Resolution and characterization of distinct cpn60-based subgroups of Gardnerella vaginalis. PLoS ONE, 7(8), e43009.
- Schuyler, J.A. et al. (2016). Identification of Gardnerella vaginalis subgroup distribution by cpn60. PLoS ONE, 11(1), e0146510.

## L. jensenii Supplementation (2026-03-19)

cpnDB v11.1 contained only 3 L. jensenii cpn60 sequences. To improve CST-V
classification confidence, 8 additional L. jensenii cpn60 UT sequences were
extracted from NCBI:

- 5 from direct NCBI nucleotide deposits (552bp UT fragments)
- 3 extracted from complete genomes via reference-anchored in silico PCR
  (using AY608421.1 as reference, 25bp anchors at each end, 3 mismatch tolerance)

Source accessions: FJ577623.1, FJ577617.1, FJ577600.1, FJ577568.1, FR775916.1,
CP160086.1, CP046310.1, VYVV01000033.1

Stored in: ljensenii_supplement.fasta (8 sequences)

**Updated L. jensenii count: 3 (cpnDB) + 8 (supplement) = 11 total**
This is comparable to L. crispatus (9) and L. gasseri (10) representation.

Note: These supplemental sequences need to be merged into the classifier
training set and the classifier retrained before use. The pre-trained
cpn60_classifier_v11.qza does NOT include these supplements.
