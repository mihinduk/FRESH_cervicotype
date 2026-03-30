# Validation with Public Datasets

## Datasets

| Priority | Dataset | Population | Marker | BioProject | Runs | Status |
|----------|---------|-----------|--------|------------|------|--------|
| 1 | Kyongo et al. 2023 | Kenyan women, n=41, 362 samples | cpn60 | PRJNA898823 | 384 | Downloading (SLURM 38341581) |
| 2 | Kwon lab FRESH 16S | SA women, n=30 | 16S V4 | PRJNA738803 | 29 | Downloading |
| 3 | Albert et al. 2015 | Canadian women, n=310 | cpn60 | PRJNA278895 | 310 | Downloading |
| 4 | Wuyts et al. 2021 | Fermented food | pheS | PRJNA629775 | 52 | Downloading |
| 5 | VIRGO2/VALENCIA | US women, n=1,975 | 16S profiles | GitHub | N/A | Pending VIRGO2 DB |
| 6 | Rowley et al. 2024 | Fiji, n=258 | Metagenomics | TBD | TBD | Future |

**Total runs downloading: 775**

### Note on Gosmann et al. 2017 (PRJEB14858)

The original Gosmann 2017 FRESH 16S data exists on ENA as study PRJEB14858 but has **no downloadable read files**. The data may be restricted or deposited as processed files only. PRJNA738803 (Kwon lab, 29 SA vaginal 16S samples related to FRESH) is the accessible alternative.

## Download details

- Run accession files: `public_data/PRJNA*_runs.txt`
- Download script: `../scripts/download_sra_validation.sh` (SLURM)
- SRA toolkit: `/ref/sahlab/software/sra-tools-env` (fasterq-dump 3.2.1)
- Downloads go to: `public_data/{dataset_name}/`

## File paths on HTCF

```
/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/validation/
├── public_data/
│   ├── PRJNA898823_runs.txt           # Kyongo cpn60 run accessions (384)
│   ├── PRJNA738803_runs.txt           # Kwon FRESH 16S run accessions (29)
│   ├── PRJNA278895_runs.txt           # Albert cpn60 run accessions (310)
│   ├── PRJNA629775_runs.txt           # Wuyts pheS run accessions (52)
│   ├── kyongo_2023_cpn60/             # FASTQ files (downloading)
│   ├── gosmann_kwon_16S/              # FASTQ files (downloading)
│   ├── albert_2015_cpn60/             # FASTQ files (downloading)
│   └── wuyts_2021_pheS/               # FASTQ files (downloading)
└── results/                           # Pipeline output (Phase 3)
```

## Validation strategy

1. Download raw reads from SRA (Step 1g — in progress)
2. Process through our pipelines: cpn60, pheS, ITS, 16S (Phase 2 required first)
3. Compare our taxonomy assignments to published results
4. Quantify classification success rates
5. Identify gaps in reference databases
6. For Kyongo cpn60: verify Gardnerella subgroup resolution matches published findings

## Key validation questions

| Dataset | Question to answer |
|---------|-------------------|
| Kyongo cpn60 | Does our cpn60 pipeline reproduce their Gardnerella subgroup assignments? |
| Kwon FRESH 16S | How many SA samples are unclassifiable by VIRGO2/VALENCIA? |
| Albert cpn60 | Does our classifier match published Canadian community profiles? |
| Wuyts pheS | Can our pheS classifier correctly identify Lactobacillus species? |
