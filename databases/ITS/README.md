# ITS Database

## Sources
- **UNITE v10.0** (updated 2025-12-10): 3.85 million ITS sequences; 239,180 species hypotheses — [UNITE](https://unite.ut.ee/repository.php)
- Pre-trained QIIME2 classifiers available for download from UNITE

## Primers
- ITS1F / ITS2 — Earth Microbiome Project standard; ITS1 region; ~250-400 bp (variable)
- Fungal-specific (ITS1F excludes most plants)

## Pipeline notes
- Variable amplicon length requires ITSxpress trimming before DADA2
- DADA2 needs customized parameters (Rivers et al. 2022) — default settings remove C. glabrata, Aspergillus reads
- Can pool ITS1 + 16S amplicons in single MiSeq run (Virtanen et al. 2024)

## Key references
- Rivers et al. (2022). JCI Insight, 7, e151663 — customized DADA2 for ITS1
- Virtanen et al. (2024). Microbiome, 12, 273. DOI: 10.1186/s40168-024-01993-9
- Gangiah et al. (2025). Microbiome. DOI: 10.1186/s40168-025-02066-1 — SA FGT mycobiome
