# pheS Database

## Sources
- **Wuyts et al. framework**: 445 pheS sequences covering 277/283 Lactobacillus species (98%) — [AEM supplementary](https://journals.asm.org/doi/10.1128/aem.02191-20)
- **NCBI GenBank supplement**: Additional L. iners, L. crispatus, L. gasseri, L. jensenii pheS sequences, especially any from African isolates

## Primers
- pheS21F / pheS23R — amplicon ~431 bp, Illumina-compatible
- Designed for Lactobacillaceae only (will not amplify Gardnerella, Prevotella, etc.)

## Classifier build
- No pre-trained classifier exists for pheS
- Build custom RDP Naive Bayesian classifier from Wuyts framework (same method as Ren & Hill 2023 for cpn60)
- Alternative: BLAST against reference FASTA

## Key reference
Wuyts, S. et al. (2021). Appl Environ Microbiol, 87, e02191-20. DOI: 10.1128/AEM.02191-20

## Notes
- No pheS study has been applied to vaginal samples from any population
- No African pheS data exists — novel findings expected
- Gap in L. iners strain-level representation likely
