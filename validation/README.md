# Validation with Public Datasets

## Datasets to download and test

| Priority | Dataset | Population | Marker | SRA accession | Purpose |
|----------|---------|-----------|--------|---------------|---------|
| 1 | Kyongo et al. 2023 | Kenyan women (n=41, 362 samples) | cpn60 | TBD — check Front Immunol paper | cpn60 pipeline on African vaginal samples |
| 2 | Gosmann et al. 2017 | FRESH SA (n=~236) | 16S V4 | TBD — check Immunity paper | VALENCIA gap quantification; baseline |
| 3 | Albert et al. 2015 | Canadian women | cpn60 | TBD — check PLoS ONE paper | cpn60 pipeline validation (Western reference) |
| 4 | Wuyts et al. 2021 | Fermented food | pheS | TBD — check AEM paper | pheS classifier validation |
| 5 | VALENCIA training data | US women (n=1,975) | 16S profiles | GitHub ravel-lab/VALENCIA | Test VALENCIA on non-US data |
| 6 | Rowley et al. 2024 | Fiji (n=258) | Metagenomics | TBD — check mBio paper | Generalizability of SA cervicotypes |

## Validation strategy

1. Download raw reads from SRA
2. Process through our pipelines (cpn60, pheS, ITS, 16S)
3. Compare our taxonomy assignments to published results
4. Quantify classification success rates
5. Identify gaps in reference databases
