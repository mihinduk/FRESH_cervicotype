# FRESH Cervicotype Project

**Multi-marker molecular profiling for species-level cervicovaginal community typing in South African women**

## Overview

Standard 16S-based cervicovaginal community typing cannot resolve the species-level variation within diverse (non-*Lactobacillus*) communities that dominate in sub-Saharan African women, and this resolution gap obscures the biological mechanisms linking specific bacterial species, fungi, and Mollicutes to HIV acquisition risk.

This project develops an integrated multi-marker approach (cpn60 + pheS + ITS + 16S + Mollicute-specific PCR) for species-level cervicotyping, applied to the FRESH cohort (Females Rising through Education, Support and Health) in Durban, South Africa.

## Project structure

```
FRESH_cervicotype/
├── databases/                  # Reference databases and classifiers
│   ├── cpn60/                  # cpnDB references, cpn60-Classifier training sets
│   ├── pheS/                   # Wuyts et al. framework + NCBI supplements
│   ├── ITS/                    # UNITE v10.0 classifier
│   ├── 16S/                    # SILVA/GG2 classifier + VALENCIA centroids
│   ├── mollicute_primers/      # MgPa, M. hominis 16S, ureC primer sequences
│   └── fredricks_bv_primers/   # BVAB1, BVAB2, Megasphaera, Fannyhessea primers
├── pipelines/                  # Analysis pipelines
│   ├── cpn60/                  # DADA2 → cpn60-Classifier
│   ├── pheS/                   # DADA2 → custom pheS classifier
│   ├── ITS/                    # ITSxpress → DADA2 → UNITE
│   ├── 16S/                    # DADA2 → SILVA → VALENCIA
│   └── integration/            # Multi-marker merge and cervicotype assignment
├── validation/                 # Testing with public datasets
│   ├── public_data/            # Downloaded SRA data (gitignored)
│   └── results/                # Validation outputs
├── docs/                       # Documentation
│   ├── study_plan/             # Study plans and rationale
│   └── background/             # Background documents and notes
├── scripts/                    # Utility scripts
└── README.md
```

## Markers and their roles

| Marker | Role | Database | Classifier |
|--------|------|----------|------------|
| **16S** | Baseline comparator; VALENCIA classification; total bacterial load | SILVA / Greengenes2 | QIIME2 pre-trained |
| **cpn60** | Primary community profiler — resolves *Gardnerella*, *Prevotella* species | cpnDB (v11.1, 16,413 seqs) | RDP Naive Bayesian / QIIME2 |
| **pheS** | *Lactobacillus* zoom lens — strain-level resolution | Wuyts et al. (445 seqs) + NCBI | Custom RDP classifier |
| **ITS** | Fungal profiling — *Candida*, *Malassezia* | UNITE v10.0 | QIIME2 pre-trained |
| **Mollicute PCR** | *M. genitalium*, *M. hominis*, *U. parvum*, *U. urealyticum* | Species-specific primers | qPCR (not amplicon seq) |

## Key references

- Gosmann et al. (2017) *Immunity* 46:29-37. DOI: 10.1016/j.immuni.2016.12.013
- Ren & Hill (2023) *ISME Communications* 3:77. DOI: 10.1038/s43705-023-00283-z
- Wuyts et al. (2021) *Appl Environ Microbiol* 87:e02191-20. DOI: 10.1128/AEM.02191-20
- France et al. (2020) *Microbiome* 8:166. DOI: 10.1186/s40168-020-00934-6
- Kyongo et al. (2023) *Front Immunol* 13:974195. DOI: 10.3389/fimmu.2022.974195

## Validation datasets

| Dataset | Population | Marker | SRA accession | Purpose |
|---------|-----------|--------|---------------|---------|
| Kyongo et al. 2023 | Kenyan women | cpn60 | TBD | cpn60 pipeline on African samples |
| Gosmann et al. 2017 | FRESH (SA) | 16S V4 | TBD | VALENCIA gap quantification |
| Albert et al. 2015 | Canadian women | cpn60 | TBD | cpn60 pipeline validation |
| Wuyts et al. 2021 | Fermented food | pheS | TBD | pheS classifier validation |
