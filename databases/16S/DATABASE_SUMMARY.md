# 16S Database — Summary

**Set up:** 2026-03-20
**Sources:** SILVA 138, Greengenes2 2024.09, VIRGO2

## Role in this project

16S is the **baseline comparator**, not the primary profiling marker. It serves to:
1. Link to existing FRESH 16S data from Gosmann et al. 2017 (ENA PRJEB14858)
2. Run VIRGO2 for CST assignment
3. Provide total bacterial load denominator (universal 16S qPCR)
4. Enable cross-study comparisons with the published literature

## Components

### A. Pre-trained QIIME2 classifiers

| File | Path | Description | Size |
|------|------|-------------|------|
| SILVA 138 full-length | `silva/silva-138-99-nb-classifier.qza` | 99% OTUs, sklearn 1.4.2, for Q2-2024.5+ | ~300MB |
| Greengenes2 V4 region | `silva/gg2-2024.09-v4-nb-classifier.qza` | 515F/806R V4 region, sklearn 1.4.2 | ~150MB |

Note: These are for standard 16S taxonomic classification. Use SILVA for broad compatibility; use GG2 V4 if Gosmann et al. data was processed with 515F/806R primers.

### B. VIRGO2 — CST Assignment Pipeline

**Location:** `virgo2/` (cloned from https://github.com/kwondry/virgo2_mapping_and_taxonomy)

**What it is:** VIRGO2 is a curated vaginal non-redundant gene catalog with taxonomic and functional annotations, developed by the Ravel lab. It maps metagenomic/amplicon reads to the VIRGO2 database and assigns community state types.

**Reference:** doi: 10.1101/2025.03.04.641479

**Workflow:** Snakemake-based pipeline that:
1. Maps reads to VIRGO2 database via bowtie2
2. Generates taxonomic annotations
3. Calculates relative abundances
4. Produces summary reports

**Database status: NOT YET DOWNLOADED**

The VIRGO2 database files (VIRGO2.fa.gz + annotation files) are currently distributed via Dropbox. After publication, they will be on Zenodo. Access requires contacting Michael France at the Ravel lab.

**Requirements:**
- conda + Snakemake 8.20.0+
- bowtie2
- VIRGO2 database files (VIRGO2.fa.gz + .txt annotation files)

**To set up once database is obtained:**
```bash
# 1. Place database files in a directory
# 2. Update config/config.yaml with database path
# 3. Run: snakemake --use-conda --configfile config/config.yaml
```

### C. 16S Primer Information

Gosmann et al. 2017 used:
- **515F / 806R** (V4 region) — Earth Microbiome Project standard
- This is the most common primer pair in vaginal microbiome literature

The Ravel lab standard (used in VALENCIA/VIRGO2 development) is:
- **341F / 805R** (V3-V4 region)

**Decision needed:** Which primer pair will be used for new FRESH 16S sequencing? This affects classifier choice. If reprocessing existing Gosmann data only, use 515F/806R-matched classifier.

## Known limitations

- 16S cannot resolve Gardnerella to species level (>99% identity between species)
- 16S cannot reliably resolve Prevotella species (>97% identity)
- Copy number variation (1-15 copies per genome) biases abundance estimates
- VIRGO2 database not yet available — contact Ravel lab/Michael France

## Existing FRESH 16S data

| Dataset | Accession | Samples | Notes |
|---------|-----------|---------|-------|
| Gosmann et al. 2017 | ENA PRJEB14858 | FRESH cohort, 16S V4 | Foundational paper |
| Kwon lab follow-up | NCBI PRJNA738803 / SRP324422 | 30 samples | Transcriptional analysis |
| FRESH LACTIN-V trial | NCBI PRJNA1085249 | 44 women | Clinical trial data (2024) |

## File paths on HTCF

```
/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/databases/16S/
├── silva/
│   ├── silva-138-99-nb-classifier.qza        # SILVA 138 full-length classifier
│   └── gg2-2024.09-v4-nb-classifier.qza      # Greengenes2 V4 region classifier
├── virgo2/                                     # VIRGO2 pipeline (cloned repo)
│   ├── config/config.yaml                      # Configuration
│   ├── workflow/                               # Snakemake workflow
│   │   ├── Snakefile
│   │   ├── scripts/                           # Python scripts
│   │   ├── envs/                              # Conda environments
│   │   └── resources/test_data/               # Test data included
│   └── README.md
├── DATABASE_SUMMARY.md                         # This file
└── README.md                                   # Original README
```

## Citations

- Quast, C. et al. (2013). The SILVA ribosomal RNA gene database project. Nucleic Acids Research, 41(D1), D590-D596.
- McDonald, D. et al. (2024). Greengenes2 unifies microbial data in a single reference tree. Nature Biotechnology.
- France, M.T. et al. (2025). VIRGO2. doi: 10.1101/2025.03.04.641479
- Gosmann, C. et al. (2017). Immunity, 46, 29-37. doi: 10.1016/j.immuni.2016.12.013
