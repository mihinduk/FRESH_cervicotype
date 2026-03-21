# Mollicute-Specific Primers — Summary

**Compiled:** 2026-03-20
**Purpose:** Targeted qPCR detection of vaginal Mollicutes invisible to cpn60

## Rationale

Mycoplasma and Ureaplasma (class Mollicutes) are underdetected by both cpn60 (M. hominis and Ureaplasma lack the gene entirely) and 16S universal primers (primer bias). Species-specific qPCR is the standard detection method.

## Primer panel (4 targets)

| Target | Gene | Amplicon | Method | SA prevalence |
|--------|------|----------|--------|---------------|
| M. genitalium | MgPa adhesin | 78 bp | TaqMan qPCR | ~10% in women; independent HIV risk factor |
| M. hominis | 16S rRNA | ~270 bp | SYBR or TaqMan | 81% in HIV+ SA pregnant women |
| U. parvum | ureC urease | ~100 bp | TaqMan qPCR | 77% in SA HIV+ women |
| U. urealyticum | ureC urease | ~100 bp | TaqMan qPCR | Less common, more pathogenic |

## Key file

- `primer_sequences.tsv` — tab-delimited file with all primer/probe sequences, references, and notes

## Design notes

- M. genitalium: MgPa target preferred over 16S for higher sensitivity (<5 copies/reaction vs ~23 for 16S). Small risk of strain variation in MgPa adhesin variable regions.
- Ureaplasma: U. parvum and U. urealyticum share the same forward/reverse ureC primers. Species discrimination is by TaqMan probe sequence, not primers. Both run in the same well with different fluorophores.
- M. hominis: 16S species-specific primers. Multiple validated sets exist. The ones listed are from Baczynska et al. 2004.
- All primers validated on vaginal/cervical swab specimens in published literature.
- FRESH already has M. genitalium presence/absence data (6.7% positive, variable sti_result_genitalium). This panel adds M. hominis, Ureaplasma, and quantification.

## Multiplexing notes

These 4 targets fit in 2 duplex or 1 quadruplex qPCR reaction:
- Well 1: M. genitalium (FAM) + M. hominis (VIC/HEX)
- Well 2: U. parvum (FAM) + U. urealyticum (VIC/HEX)
- Or combine all 4 with FAM/VIC/ROX/Cy5 in a single quadruplex

## Limitations

- These are qPCR assays, not amplicon sequencing — results are presence/absence + copy number, not community composition.
- Primer sequences are from published literature, not independently validated by us. In silico specificity check against NCBI recommended before wet lab use.
- No South African-specific Mollicute primer validation published, though SA prevalence data exists for all 4 targets.

## References

- Jensen, J.S. et al. (2004). JCM, 42, 683-692. (MgPa qPCR)
- Baczynska, A. et al. (2004). JCM, 42, 3260-3263. (M. hominis 16S)
- Kong, F. et al. (2000). JCM, 38, 1175-1179. (Ureaplasma ureC species-specific PCR)
- Yi, J. et al. (2005). JCM, 43, 5765-5768. (Ureaplasma real-time PCR)
