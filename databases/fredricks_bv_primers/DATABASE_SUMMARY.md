# Fredricks BV Indicator Primers — Summary

**Compiled:** 2026-03-20
**Purpose:** Targeted qPCR for BV-associated taxa that complement cpn60 community profiling

## Rationale

These 16S rRNA gene-based species-specific primers target BV-associated taxa that are either:
- Not well-resolved by cpn60 amplicon sequencing (BVAB1 is still uncultured, not in cpnDB)
- Require species/type-level discrimination not achievable by community profiling (Megasphaera type 1 vs type 2)
- Serve as validated clinical BV biomarkers with known diagnostic performance

## Primer panel (4 targets)

| Target | Amplicon | BV diagnostic value | Why include |
|--------|----------|-------------------|-------------|
| BVAB1 | 95 bp | High | Still uncultured, not in cpnDB, strongly linked to genital inflammation |
| BVAB2 | 100 bp | **Best single marker** | 98.8% sensitivity combined with Megasphaera type 1 |
| Megasphaera type 1 | 121 bp | High | Distinguishes type 1 from type 2; linked to preterm birth |
| Fannyhessea vaginae | 120 bp | High | Key BV indicator; validates cpn60 Fannyhessea detection |

**Best diagnostic combination:** BVAB2 OR Megasphaera type 1 = 98.8% sensitivity, 93.7% specificity for BV vs Amsel criteria.

## Key file

- `primer_sequences.tsv` — tab-delimited file with all primer sequences, amplicon sizes, references

## Source

Fredricks, D.N., Fiedler, T.L., & Thomas, K.K. (2007). Targeted PCR for detection of vaginal bacteria associated with bacterial vaginosis. JCM, 45, 3270-3276. DOI: 10.1128/JCM.01272-07

Fannyhessea primers from: Fredricks, D.N. et al. (2005). JCM, 43, 4607-4612. DOI: 10.1128/JCM.43.9.4607-4612.2005

## Multiplexing notes

All 4 targets have small amplicons (95-121 bp) suitable for TaqMan or SYBR Green qPCR. Can multiplex as:
- Well 1: BVAB1 (FAM) + BVAB2 (VIC)
- Well 2: Megasphaera type 1 (FAM) + Fannyhessea (VIC)

## Overlap with other markers

| Target | Also detected by cpn60? | Also detected by 16S amplicon? |
|--------|------------------------|-------------------------------|
| BVAB1 | Uncertain — not in cpnDB, uncultured | Yes — by 16S community profiling |
| BVAB2 | Possibly — Acetatifactor in cpnDB (2 seqs) | Yes |
| Megasphaera type 1 | Possibly — 7 Megasphaera in cpnDB (type not specified) | Cannot distinguish type 1 vs 2 |
| Fannyhessea vaginae | Yes — 5 seqs in cpnDB | Yes |

These primers provide **quantitative validation** of taxa that cpn60 may detect qualitatively. The qPCR gives absolute copy numbers; cpn60 gives relative abundance.

## Limitations

- All primers designed and validated on US populations. In silico specificity check against SA-relevant 16S sequences recommended.
- SYBR Green detection requires melt curve confirmation. TaqMan probes (not listed — from Fredricks supplementary) preferred for multiplex.
- BVAB1 taxonomy still uncertain — primer targets the best available 16S sequence.

## Adaptation needed for FRESH

- In silico check primer binding sites against available SA 16S sequences before wet lab use
- Fredricks quantitative cutoffs for BV diagnosis were calibrated on US populations — will need recalibration against FRESH Nugent scores
