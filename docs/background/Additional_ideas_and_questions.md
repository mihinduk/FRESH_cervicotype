# Additional Ideas and Questions — FRESH Cervicotype Multiplex PCR Project

**Prepared:** March 18, 2026
**Project:** FRESH 2026 16S Adjuvant

---

## Unanswered Scientific Questions

### 1. Is *L. iners* dominance truly "less protective" in South African women, or is that a Western-calibrated assumption?

The entire CST literature treats *L. iners* (CST-III) as a transitional, less-protective state compared to *L. crispatus* (CST-I). But **75% of Lactobacillus-positive South African women are *L. iners*-dominant** and most are healthy. This raises a fundamental question:

- Does *L. iners* dominance carry the same HIV risk in a population where it's the norm vs. in Western populations where it's less common?
- Are there **strain-level differences** in *L. iners* across populations? South African *L. iners* strains may have different functional properties (lactic acid production, bacteriocins) than North American strains.
- **pheS would let you test this** — it resolves Lactobacillus at species/strain level. If South African *L. iners* strains cluster differently from Western reference strains, that's a publication on its own.

### 2. What's happening in the transition zone between cervicotypes?

Gosmann et al. (2017) defined CT1-CT4, but those are snapshots. The Masha et al. (2021) Markov model showed transitions happen. The critical unknowns:

- **How fast do transitions occur?** Days? Weeks? Menstrual cycle phases?
- **Are there "gateway" species** — organisms whose arrival predicts a community shift? For example, does *G. piotii* colonization precede the shift from *L. iners*-dominant to diverse?
- **Is there a point of no return** — once biofilm establishes, does the community become locked into CST-IV?
- A multiplex qPCR panel could detect these transitions in near-real-time with weekly sampling, which sequencing can't do at that turnaround time or cost.

### 3. Does the *Gardnerella* species composition differ between South African and Western women?

The Gardnerella species distribution has been characterized primarily in Canadian (Hill's cpn60 work) and European populations. Nobody has done species-level Gardnerella profiling in a large South African cohort. You might find:

- Different relative prevalence of *G. piotii* vs. *G. vaginalis* s.s.
- Novel Gardnerella genomospecies not yet in cpnDB (13 have been delineated, but likely more exist)
- Different co-occurrence patterns — which Gardnerella species appear together, and with which Prevotella species?

### 4. The Mollicute question — how much are we missing?

cpn60 is blind to *Mycoplasma* and *Ureaplasma* (they lack the gene). In the FRESH context:

- *M. genitalium* is a **known independent risk factor for HIV acquisition** in sub-Saharan Africa
- *Ureaplasma* was found in **81% of women with PPROM** in cpn60 studies (Paramel Jayaprakash et al., 2016)
- If the multiplex doesn't include Mollicute targets, we're missing organisms that may be as important as Gardnerella for HIV risk
- **Question**: Should Mollicute targets be in Tier 1 (core panel), not Tier 2? For the FRESH HIV question, they may be essential.

### 5. Sialidase — bacterial or host-derived?

Sialidase is a key virulence readout for biofilm-forming communities, but there's a complication: **human cells also produce sialidases** (NEU1-4). A positive sialidase activity assay from a vaginal swab doesn't tell you whether the enzyme is bacterial or host-derived. This matters because:

- Genital inflammation itself upregulates host sialidases
- **Bacterial-specific sialidase gene detection** (nanH2/nanH3 qPCR) rather than just enzyme activity would be needed to attribute it correctly
- Alternatively, combine both: total sialidase activity (colorimetric) + bacterial nanH gene presence (qPCR) = distinguish bacterial vs. host contribution

---

## Design and Implementation Questions

### 6. What's the denominator for quantitative PCR?

If we want quantitative cervicotyping (not just presence/absence), we need a denominator to express results as proportions. Options:

| Denominator | Pros | Cons |
|---|---|---|
| **Universal 16S qPCR** (total bacterial load) | Well-established, proven primers | Copy number variation (1-15x) distorts proportions |
| **Universal cpn60 qPCR** | Single-copy in most bacteria, matches primary marker | Misses Mollicutes; less established as total load marker |
| **Human gene qPCR** (e.g., RNase P, beta-globin) | Normalizes for swab quality and cellularity | Doesn't give total bacterial load |
| **Spiked-in synthetic standard** | Absolute quantification, controls for extraction efficiency | Requires careful calibration |

**Recommendation**: Use **both** a human gene (swab quality control) and universal 16S (total bacterial load). Express results as copies of target per copy of human gene (bacterial burden) and as proportion of total 16S (community composition).

### 7. What sample type — vaginal vs. cervical vs. both?

Rowley et al. (2024, Fiji) found that **41% of endocervical samples were unclassifiable** vs. 36% of vaginal samples — the cervical and vaginal microbiomes are related but not identical. For HIV susceptibility:

- HIV infection occurs at the **cervical transformation zone**, not the vaginal wall
- The endocervical microbiome may be more directly relevant to HIV risk than the vaginal microbiome
- But cervical sampling is more invasive and less feasible in community settings
- **Question**: Is FRESH collecting both sample types? If so, profiling both with the multiplex could reveal whether cervical community composition is a better predictor of HIV risk than vaginal.

### 8. What about fungi?

The VMRC4Africa study (ongoing) includes **ITS sequencing for fungi** alongside 16S. *Candida* species are common in the cervicovaginal environment and may interact with bacterial communities:

- *Candida albicans* can co-exist with *Lactobacillus* but competes with *Gardnerella* for epithelial adhesion sites
- Vulvovaginal candidiasis causes inflammation that could independently affect HIV susceptibility
- **Question**: Should a *Candida* target be included in the panel? It's a single additional primer pair.

### 9. Antibiotic resistance as a co-variable

If BV is treated with metronidazole in FRESH participants, biofilm resistance to metronidazole could explain:

- Treatment failure → persistent CST-IV → prolonged HIV susceptibility window
- The Gardnerella biofilm literature shows established biofilms survive metronidazole by reducing metabolic activity
- **Question**: Should a metronidazole resistance marker (e.g., *nim* genes) be included to track whether treatment-resistant biofilms explain persistent high-risk community states?

### 10. Controls for LMIC deployment

For a field-deployable panel, internal controls should be built in from the start:

- **Extraction control**: Spiked-in non-vaginal organism (e.g., *Thermus aquaticus* DNA) to verify extraction worked
- **PCR inhibition control**: Internal amplification control in every reaction
- **Positive control**: Synthetic DNA mix at defined ratios mimicking each cervicotype (CT1-CT4)
- **Negative control**: Water + extraction reagents
- **Swab adequacy control**: Human gene target (minimum threshold to confirm adequate sampling)
- **Question**: Can these all be multiplexed into a single control well, or do they need dedicated wells?

---

## Strategic and Collaboration Questions

### 11. Landscape — who else is doing this, and where are the gaps?

| Group | What they're doing | Gap this project fills |
|---|---|---|
| **Hill lab** (Saskatchewan) | cpn60 profiling, cpnDB, CpnClassiPhyR | All work on Canadian/Western populations |
| **Ravel lab** (Maryland) | VALENCIA, CST framework, metagenomics | Framework doesn't fit African populations |
| **VMRC4Africa** | Longitudinal 16S + ITS in SA/Kenya | Using 16S (not cpn60), no multiplex qPCR |
| **Fredricks lab** | Species-specific qPCR, BV biomarkers | Focused on US populations |
| **FRESH** (our cohort) | HIV acquisition, longitudinal follow-up | Has the cohort but lacks species-level molecular tools |

This project sits at the intersection nobody else occupies: **cpn60/multiplex molecular resolution + African population + HIV outcome data + longitudinal design**.

### 12. Publication strategy

This project has at least 3-4 papers:

1. **Methods paper**: "A multiplex PCR panel for species-resolved cervicotyping in sub-Saharan African women" — the assay itself
2. **Descriptive paper**: "Species-level cervicovaginal community structure in young South African women" — applying cpn60 to FRESH samples, defining SA-specific cervicotypes
3. **Clinical paper**: "*Gardnerella piotii* and sialidase-producing Prevotella species predict HIV acquisition in the FRESH cohort" — linking species-resolved cervicotypes to HIV outcomes
4. **Framework paper**: "Extending VALENCIA for sub-Saharan African cervicovaginal communities" — the classification contribution

### 13. What existing FRESH samples are available?

Before designing new sample collection:

- Are there **archived swabs** from Gosmann et al. (2017) and subsequent FRESH collections?
- Is DNA already extracted, or are swabs in storage media?
- What metadata exists — Nugent scores, pH, cytokine data, HIV status, longitudinal timepoints?
- Could cpn60 be run on existing DNA extractions as a pilot (50-100 samples) before committing to a full panel design?

---

## Brainstormed ideas from earlier discussion

### Tiered multiplex qPCR panel design

**Tier 1 — Core cervicotype assignment (8-10 targets):**
- *L. crispatus*, *L. iners*, *L. gasseri*, *L. jensenii* (cpn60 or pheS primers)
- *G. vaginalis*, *G. piotii*, *G. swidsinskii* (cpn60 primers)
- *Fannyhessea vaginae* (formerly *Atopobium*)
- *Mycoplasma genitalium*, *Ureaplasma* spp.
- Total bacterial load (universal 16S qPCR as denominator)

**Tier 2 — HIV-risk refinement (additional 5-6 targets):**
- *Sneathia amnii*, *Prevotella bivia*, BVAB1, *Megasphaera* type 1
- Sialidase gene (nanH) as a functional marker

### CST-IV functional stratification by biofilm/virulence potential

| Proposed subtype | Composition | Virulence profile | Predicted HIV risk |
|---|---|---|---|
| **IV-high** | *G. piotii* + sialidase+ Prevotella (P. timonensis, P. bivia) | Active sialidase, vaginolysin, MMP activation, biofilm-forming | **Highest** |
| **IV-moderate** | *G. vaginalis* s.s. + mixed Prevotella | Some sialidase, moderate biofilm | Moderate |
| **IV-low** | Clade 3 Gardnerella + Sneathia/Dialister (current IV-A-like) | No/low sialidase, weak biofilm | Lower (may be asymptomatic) |
| **IV-commensal** | Diverse but non-biofilm-forming anaerobes | Minimal virulence factors | Possibly similar to Lactobacillus-dominant |

### Additional approaches considered

- **De novo FRESH cervicotype classification** rather than retrofitting CSTs
- **Host cytokine integration** (IL-1a, IL-8, MIP-3a, secretory IgA from same swab) for functional risk scoring
- **Nanopore full rrn operon sequencing** as discovery/validation platform alongside qPCR
- **Longitudinal transition analysis** — tracking cervicotype trajectories preceding HIV seroconversion
- **South African reference database expansion** — culturing + sequencing vaginal isolates from FRESH to expand cpnDB

---

## Prioritized next steps for planning

1. **Audit existing FRESH samples and metadata** — determines what's feasible now vs. requires new collection
2. **Pilot cpn60 sequencing** on a subset — validates species-level resolution in this population before investing in multiplex panel design
3. **Define SA-specific cervicotypes** from the pilot data
4. **Design the multiplex qPCR panel** targeting the species/genes that best discriminate cervicotypes and predict HIV risk
5. **Validate the panel** against the cpn60 sequencing gold standard

---

## Key references discussed

- Gosmann, C., et al. (2017). Lactobacillus-deficient cervicovaginal bacterial communities are associated with increased HIV acquisition in young South African women. *Immunity*, 46(1), 29–37. DOI: 10.1016/j.immuni.2016.12.013
- Masha, S.C., et al. (2021). Modeling the temporal dynamics of cervicovaginal microbiota identifies targets that may promote reproductive health. *Microbiome*, 9, 163. DOI: 10.1186/s40168-021-01096-9
- France, M.T., et al. (2020). VALENCIA: a nearest centroid classification method for vaginal microbial communities based on composition. *Microbiome*, 8(1), 166. DOI: 10.1186/s40168-020-00934-6
- Rowley, N., et al. (2024). Unique microbial diversity among Pacific Islander microbiomes in Fiji. *mBio*, 15(1), e03063-23. DOI: 10.1128/mbio.03063-23
- Paramel Jayaprakash, T., et al. (2012). Resolution and characterization of distinct cpn60-based subgroups of Gardnerella vaginalis. *PLoS ONE*, 7(8), e43009. DOI: 10.1371/journal.pone.0043009
- Fredricks, D.N., Fiedler, T.L., & Marrazzo, J.M. (2005). Molecular identification of bacteria associated with bacterial vaginosis. *NEJM*, 353, 1899–1911. DOI: 10.1056/NEJMoa043802
- Gajer, P., et al. (2012). Temporal dynamics of the human vaginal microbiota. *Science Translational Medicine*, 4(132), 132ra52. DOI: 10.1126/scitranslmed.3003605
- Lennard, K., et al. (2018). A longitudinal analysis of the vaginal microbiota and vaginal immune mediators in women from sub-Saharan Africa. *Scientific Reports*, 7, 11974. DOI: 10.1038/s41598-017-12198-6
- Mtshali, A., et al. (2023). Changes in the vaginal microbiome during pregnancy and the postpartum period in South African women. *Reproductive Sciences*, 30, 2825–2837. DOI: 10.1007/s43032-023-01351-4
