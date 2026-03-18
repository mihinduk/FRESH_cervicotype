# Alternative and Supplemental Marker Genes for Species-Level Cervicovaginal Microbiome Profiling

**Prepared:** February 25, 2026
**Project:** FRESH 2026 16S Adjuvant

---

## 1. Introduction

Standard 16S rRNA gene amplicon sequencing — typically targeting the V3-V4 hypervariable regions (~460 bp) — has been the workhorse for cervicovaginal microbiome characterization and Community State Type (CST) assignment (Ravel et al., 2011). While adequate for genus-level classification and broad community typing, 16S V3-V4 sequencing fails to achieve species-level resolution for several clinically important vaginal taxa. Most critically, species within *Gardnerella* share 97–100% 16S rRNA identity (Paramel Jayaprakash et al., 2012), and several *Prevotella* species pairs and *Megasphaera* phylotypes are also poorly resolved.

This report evaluates alternative and supplemental molecular markers that could improve species-level resolution for cervicovaginal community profiling. Markers are organized by evidence tier: those proven in vaginal microbiome studies, those validated in other contexts but not yet applied vaginally, genus-specific tools, and non-amplicon technologies.

---

## 2. The 16S rRNA Baseline: Strengths and Limitations

### 2.1 Strengths

The 16S rRNA gene (~1,540 bp) is universally present in bacteria, has extensive reference databases (SILVA: >2 million sequences; Greengenes2; RDP), and benefits from decades of validated primer sets, established bioinformatics pipelines (QIIME2, DADA2, mothur), and a massive body of comparative literature (Quast et al., 2013; Callahan et al., 2016; Schloss et al., 2009).

### 2.2 Species-Level Failures in Vaginal Contexts

| Taxon Group | 16S Identity Between Species | Clinical Consequence |
|-------------|------------------------------|----------------------|
| *Gardnerella* spp. | 97–100% | Cannot distinguish *G. vaginalis*, *G. piotii*, *G. leopoldii*, *G. swidsinskii* — species with different virulence and BV associations |
| *Prevotella* cryptic species | >97% for some pairs | Lumps functionally distinct species |
| *Megasphaera* type 1 vs. type 2 | High similarity | Fails to separate clinically relevant phylotypes |
| Multi-copy bias | 1–15 copies per genome | Distorts relative abundance estimates; *L. iners* (5 copies) overrepresented vs. *L. crispatus* (4 copies) |

---

## 3. cpn60 / GroEL — The Most Validated Alternative

### 3.1 Overview

The cpn60 (chaperonin-60) universal target (UT) is a ~552–558 bp region of the gene encoding the 60 kDa chaperonin protein (also known as GroEL or Hsp60). It is a protein-coding gene with a higher evolutionary rate than ribosomal RNA genes, resulting in greater sequence divergence between species (Links et al., 2012).

**Note on nomenclature:** cpn60, GroEL, Hsp60, and Hsp65 refer to the same protein family. "cpn60" is the standardized term used by the Hill laboratory and cpnDB. "Hsp65" appears primarily in the *Mycobacterium* literature, where Cpn60.2 = Hsp65 = the 65 kDa antigen. "GroEL" is the *E. coli* gene name.

### 3.2 Key Researchers

- **Dr. Janet E. Hill** (Department of Veterinary Microbiology, University of Saskatchewan, Canada) — principal architect of cpn60-based microbiome profiling; developed the cpn60 UT approach, cpnDB reference database, and primer cocktails.
- **Sean Hemmingsen** (National Research Council Canada) — co-developer of cpnDB and primer systems.
- **John Schellenberg** — early cpn60 vaginal profiling; Gardnerella subgroup characterization.
- **Tim Paramel Jayaprakash** — resolved *Gardnerella vaginalis* subgroups by cpn60.
- **Tim Dumonceaux** (Agriculture and Agri-Food Canada) — developed CaptureSeq, an amplification-free cpn60 enrichment method.
- **VOGUE Research Group** (Vaginal Microbiome Group Initiative) — multi-institutional Canadian collaboration led by **Dr. Deborah Money** (Women's Health Research Institute, UBC), in partnership with Hill, Hemmingsen, and **Dr. Gregor Reid** (University of Western Ontario). Funded by CIHR and Genome British Columbia. Five sub-studies: healthy non-pregnant women, women with HIV, recurrent vulvovaginitis, low-risk and high-risk pregnancies.

### 3.3 Species Resolution

cpn60 has been formally demonstrated to be a **preferred barcode for bacteria** over 16S rRNA, using criteria from the International Barcode of Life project. In an analysis of complete bacterial genomes representing 983 species from 21 phyla, cpn60 showed the largest barcode gap (difference between median pairwise inter-specific and intra-specific distances) of any marker tested (Links et al., 2012).

Key comparative data:

| Metric | cpn60 | 16S rRNA |
|--------|-------|----------|
| Barcode gap | Largest of any tested marker | Smaller |
| Copy number | Single-copy in most bacteria | 1–15 copies (varies by species) |
| Species-level classification of vaginal reads | ~86% | ~50–70% (V3-V4) |
| Gardnerella inter-species identity | 87–93% (easily distinguishable) | 97–100% (virtually indistinguishable) |

### 3.4 The Gardnerella Case Study

This is the most striking demonstration of cpn60's superiority. cpn60 sequencing revealed four subgroups within what was previously considered a single species (*G. vaginalis*), later validated as distinct species:

| cpn60 Subgroup | Current Species Name | Sialidase Activity | BV Association |
|----------------|----------------------|-------------------|----------------|
| Subgroup A / Clade 4 | *G. leopoldii* and *G. swidsinskii* | Variable (9% positive) | Variable |
| Subgroup B / Clade 2 | *G. piotii* | **100% positive** | **Strongly associated with BV** |
| Subgroup C / Clade 1 | *G. vaginalis* (sensu stricto) | Variable | Common, variable virulence |
| Subgroup D / Clade 3 | Multiple genomospecies | 0% positive | Low virulence |

Vaneechoutte et al. (2019) formally described *G. leopoldii*, *G. piotii*, and *G. swidsinskii* as new species, delineating 13 genomic species within the genus — a taxonomic revision that was **preceded and predicted by cpn60 subgroup analysis** (Paramel Jayaprakash et al., 2012; Schuyler et al., 2016; Janssen et al., 2019).

### 3.5 Other Species Better Resolved by cpn60

- **Prevotella**: cpn60 profiling detected 14 different *Prevotella* spp. plus 15 additional Prevotella-like OTUs with 80–95% similarity to references, suggesting novel taxa that 16S lumps together (Albert et al., 2015).
- **Megasphaera type 1 vs. type 2**: Distinguished by cpn60 but not reliably by 16S.
- **Lactobacillus species**: *L. crispatus*, *L. iners*, *L. gasseri*, *L. jensenii* all readily resolved without specialized reference curation.
- **BV-associated bacteria**: BVAB1, BVAB2 (now *Acetatifactor indicium*), and BVAB3 (now *Mageeibacillus indolicus*) resolved.

### 3.6 Diseases and Conditions Studied

| Condition | Key Findings | Reference |
|-----------|-------------|-----------|
| **Bacterial vaginosis** | Gardnerella subgroup B (*G. piotii*) significantly more abundant in BV; sialidase activity detected in all subgroup B isolates | Paramel Jayaprakash et al., 2012; Schuyler et al., 2016 |
| **Spontaneous preterm birth** | Higher vaginal diversity and Mollicutes prevalence in preterm cases; swabs at 11–16 weeks could distinguish risk groups | Freitas et al., 2018 |
| **PPROM** | Highly diverse communities; *Megasphaera* type 1 and *Prevotella* spp. in all samples; *Mycoplasma/Ureaplasma* in 81% of women | Paramel Jayaprakash et al., 2016 |
| **HIV susceptibility** | Divergent Gardnerella subgroup associations with pro-inflammatory cytokines and chemokine IP-10 in Kenyan women | Kyongo et al., 2022 |
| **Menstrual cycle dynamics** | Baseline community dynamics with species-level resolution in healthy Canadian women | Chaban et al., 2014 |
| **Pregnancy** | Lower richness and diversity; lower Mollicutes prevalence vs. non-pregnant | Freitas et al., 2017 |

### 3.7 Primers and Databases

**Primer cocktail** (1:3 molar ratio):

| Primer | Direction | Role |
|--------|-----------|------|
| H279 | Forward | Original universal primer |
| H280 | Reverse | Original universal primer |
| H1612 | Forward | Enhanced for high G+C templates (Actinobacteria) |
| H1613 | Reverse | Enhanced for high G+C templates |

Product size: 552–558 bp. Illumina MiSeq protocol: 500-cycle kit, 400 cycles Read 1 (5' end), 100 cycles Read 2; only Read 1 used in downstream analysis.

**cpnDB** (www.cpndb.ca): Established 2004 (Hill et al., 2004). Over 25,000 sequence records covering 1,802 genera; >4,000 records from bacterial type strains. Manually curated. Includes cpnDB_nr (non-redundant) and cpnDB_nr_vag (vaginal-specific reference set).

**CpnClassiPhyR**: Taxonomic classification tool for cpn60 ASVs, achieving 86% species-level classification for vaginal datasets (Hay et al., 2023).

**CaptureSeq**: Amplification-free, hybridization-based enrichment using cpn60 probes. Avoids PCR bias entirely; profiles all three domains of life (Dumonceaux et al., 2021).

### 3.8 Limitations

1. **Mollicute blind spot**: Certain *Mycoplasma* and *Ureaplasma* species lack the cpn60 gene entirely — requires supplementary PCR assays.
2. **Smaller reference database**: ~25,000 records vs. millions for 16S.
3. **Paralog complications**: Some taxa have multiple divergent cpn60 copies (Chlamydia, some Rhizobia, some Actinobacteria).
4. **Limited adoption**: Most microbiome studies use 16S, complicating cross-study comparisons.
5. **No equivalent of QIIME2/DADA2/mothur ecosystem**: CpnClassiPhyR exists but the pipeline infrastructure is less mature.
6. **Read length constraints**: Full UT (~555 bp) exceeds typical Illumina paired-end merge lengths; current protocols use primarily Read 1 (~400 bp).

---

## 4. 5S rRNA — Assessed and Rejected

### 4.1 Rationale for Investigation

At ~120 bp, the 5S rRNA gene is universally present in bacteria and could theoretically be recovered from highly degraded samples. Its short length is compatible with single Illumina reads without paired-end merging.

### 4.2 Evidence Against Use

Won, Cho & Kim (2024) directly compared classification accuracy across rRNA components:

| Marker | Species-Level Accuracy | Std. Deviation |
|--------|----------------------|----------------|
| Full rRNA operon (16S-ITS-23S) | 0.999 | 0.005 |
| 23S rRNA | 0.985 | 0.048 |
| 16S rRNA | 0.937 | 0.109 |
| 16S V3-V4 only | 0.702 | 0.301 |
| **5S rRNA** | **0.500** | **0.341** |

de Oliveira Martins et al. (2020) confirmed that "the 5S gene showed an overall poor congruence with the established taxonomic information."

Carl Woese himself initially considered 5S rRNA for molecular phylogenetics but concluded the information content was insufficient, leading to the adoption of 16S rRNA as the standard.

### 4.3 Assessment

| Criterion | 5S rRNA Status |
|-----------|---------------|
| Species-level accuracy | ~50% (coin-flip) |
| Universal primers | None validated |
| Reference database | 5SRNAdb: ~7,300 bacterial sequences (Szymanski et al., 2016) |
| Bioinformatics tools | None purpose-built |
| Vaginal microbiome use | None published |
| **Recommendation** | **Not viable as standalone marker** |

The only scenario where 5S has value is as part of the complete rRNA operon (~5 kb) sequenced on long-read platforms, where it contributes marginally to overall resolution.

---

## 5. rpoB (RNA Polymerase Beta Subunit) — Strong Untapped Candidate

### 5.1 Overview

rpoB is a single-copy, protein-coding gene (~4,026 nt) encoding the beta subunit of RNA polymerase. Its evolutionary rate provides greater interspecies divergence than 16S rRNA.

### 5.2 Key Researchers and Studies

- **Ogier et al. (2019)** — the landmark paper for rpoB amplicon-based community profiling. Designed universal primers for Illumina sequencing and built a curated reference database of ~45,000 rpoB sequences. Validated on a 19-strain mock community and entomopathogenic nematode-associated communities.
- **Tarrand et al. (2024)** (Mayo Clinic) — broad-range rpoB amplification and Sanger sequencing for clinical bacterial identification: unambiguous species-level ID for 84% of 115 isolates vs. only 50% with 16S.
- **Adekambi, Drancourt & Raoult (2009)** — comprehensive review of rpoB as a clinical microbiological tool.
- **Vos et al. (2012)** — compared rpoB and 16S in pyrosequencing, finding rpoB classifies OTUs more effectively to species level.

### 5.3 Species Resolution

- Split *Prevotella melaninogenica* into two distinct clusters (ANI 87.9%) — directly relevant to vaginal microbiome where multiple *Prevotella* species co-occur.
- Distinguished *Bacteroides fragilis* divisions I and II.
- Higher sensitivity (all species detected in mock communities) and higher specificity (fewer spurious OTUs) than V3-V4.
- Amplicon products <300 bp, compatible with standard Illumina chemistry.

### 5.4 Vaginal Application Status

No published study has applied rpoB amplicon sequencing to vaginal microbiome samples. However, the universal primer availability, 45,000-sequence database, *Prevotella* resolution capability, and Illumina compatibility make it an immediately feasible candidate.

### 5.5 Limitations

No single primer pair amplifies all bacteria; broad-spectrum primers covering multiple phyla have been designed but gaps remain. The database, while substantial, is smaller than 16S references.

---

## 6. pheS (Phenylalanyl-tRNA Synthase) — Best-in-Class for Lactobacillus

### 6.1 Overview

pheS encodes the alpha subunit of phenylalanyl-tRNA synthase, a single-copy housekeeping gene with high discriminatory power among lactic acid bacteria (LAB).

### 6.2 Key Researchers and Studies

- **Naser et al. (2005, 2007)** — pioneered pheS for Lactobacillus identification. Evaluated 201 strains representing 98 species and 17 subspecies.
- **Wuyts, Wittouck, Salvetti et al. (2021)** — the landmark paper for pheS-based amplicon sequencing. Built a framework of 445 pheS sequences covering 277 of 283 validly described Lactobacillus species/subspecies (98% coverage). Designed universal Lactobacillus primers (pheS21F/pheS23R) for high-throughput Illumina sequencing. Validated on fermented food and environmental samples.

### 6.3 Species Resolution

| Metric | Value |
|--------|-------|
| Interspecies gap | >10% sequence dissimilarity |
| Intraspecies variation | <3% |
| Species coverage | 277/283 described species (98%) |
| Copy number | Single-copy |
| Amplicon size | ~450 bp (Illumina-compatible) |

This is the best available marker for discriminating vaginal Lactobacillus species — would cleanly separate *L. crispatus*, *L. iners*, *L. gasseri*, and *L. jensenii*.

### 6.4 Limitations

Primers are designed specifically for Lactobacillaceae and related LAB. They do **not** amplify *Gardnerella*, *Prevotella*, *Sneathia*, *Atopobium/Fannyhessea*, or other non-LAB vaginal taxa. Must be paired with another marker for complete community profiling.

---

## 7. Full rRNA Operon Sequencing (16S-ITS-23S)

### 7.1 Overview

The complete bacterial rRNA operon (~4,500 bp) contains the 16S rRNA gene, the internal transcribed spacer (ITS), the 23S rRNA gene, and the 5S rRNA gene. Long-read sequencing of this entire region captures all phylogenetic information from every component.

### 7.2 Key Studies

- **Won, Cho & Kim (2024)** — direct comparison showing species-level accuracy of 0.999 for full operon vs. 0.937 for 16S alone.
- **Petrone et al. (2023)** — developed the RESCUE pipeline for Oxford Nanopore sequencing of 16S-ITS-23S, validated on mock communities and saliva.
- **Szoboszlay et al. (2024)** — evaluated 16S-ITS-23S operon sequencing efficiency for species-level resolution.
- **Budding et al. (2021)** — IS-pro technology (ITS length polymorphism with phylum-specific fluorescent 16S primers), applied to 297 vaginal swab samples from reproductive-age women; median Pearson R² = 0.97 vs. 16S amplicon sequencing.
- **Curry et al. (2022)** — developed Emu, a species-level classifier for full-length 16S Nanopore data (*Nature Methods*).

### 7.3 Platforms and Resolution

| Platform | Read Length | Current Accuracy | Species Classification | Cost/Sample |
|---------|------------|-----------------|----------------------|-------------|
| PacBio HiFi | Full operon (~4.5 kb) | >99.9% (HiFi) | ~99.9% | $50–150 |
| Nanopore R10.4.1 | Full operon | >99% (duplex) | ~99%+ | $20–80 |
| IS-pro (ITS only) | Fragment analysis | N/A (length polymorphism) | Species-level | $30–60 |

### 7.4 Vaginal Application

IS-pro has been directly validated on vaginal samples (Budding et al., 2021). Full rrn operon sequencing on Nanopore or PacBio has not yet been published for vaginal communities specifically but is immediately applicable.

### 7.5 Limitations

Requires long-read sequencing infrastructure. Nanopore error rates, while greatly improved, still require careful bioinformatic quality control. The ITS region can vary in length and copy number, complicating quantification. Reference databases for the full operon are smaller than 16S-only databases, though growing rapidly (MIrROR database: 97,781 operon sequences covering 9,485 species; Seol & Kim, 2022).

---

## 8. Other Genus-Specific Markers

### 8.1 tuf (Elongation Factor Tu)

- **Researchers**: Ventura et al. (2003) — analyzed tuf across 17 *Lactobacillus* and 8 *Bifidobacterium* species. Xu et al. (2023) — tuf-targeted amplicon sequencing for *Bacillus* metataxonomics.
- **Resolution**: Species-specific identification for closely related Lactobacillus species; consistent with 16S phylogeny but with better resolution. Single-copy gene.
- **Limitation**: Genus-specific primers only (Lactobacillus, Bifidobacterium, Bacillus). Not suitable for pan-bacterial community profiling.

### 8.2 recA

- **Researchers**: Torriani et al. (2001) — differentiated *L. plantarum*, *L. pentosus*, and *L. paraplantarum* (impossible with 16S; >99% identity). Felis et al. (2001) — *L. casei* group taxonomy.
- **Resolution**: Excellent for close Lactobacillus species pairs. recA-RFLP can identify strains representing 17 Lactobacillus species.
- **Limitation**: Species-specific or multiplex PCR primers only; no universal community profiling primers. Used for isolate-level work, not community sequencing.

### 8.3 gyrB (DNA Gyrase Subunit B)

- **Researchers**: Poirier et al. (2018) — gyrB amplicon sequencing of meat/seafood spoilage microbiota, comparing to 16S V3-V4 and demonstrating species- and subspecies-level resolution.
- **Resolution**: ~94–95% sequence identity among strains of same species, matching ANI threshold. Mutation rate surpasses 16S. Single-copy gene.
- **Limitation**: Universal primer design across all bacteria is challenging due to sequence divergence in primer-binding regions. Better suited for targeted genera (Pseudomonas, Vibrio) than pan-bacterial surveys. No vaginal application published.

### 8.4 atpD (ATP Synthase Beta Subunit)

- **Researchers**: Naser et al. (2005, 2007) — included in MLSA schemes for Enterococcus and Pediococcus. Christensen et al. (2004) — Pasteurellaceae phylogenies.
- **Resolution**: Can differentiate *L. gasseri* from *L. johnsonii* — directly relevant to vaginal microbiome.
- **Limitation**: No universal pan-bacterial primers; genus-level primers only. Not practical for whole-community profiling.

### 8.5 Summary Table

| Marker | Universal Primers? | Species Resolution | Vaginal Use? | Best For |
|--------|-------------------|-------------------|-------------|----------|
| **tuf** | Genus-specific only | Good (LAB) | No | Lactobacillus, Bifidobacterium |
| **recA** | Species-specific only | Excellent (Lactobacillus pairs) | No (isolates) | *L. plantarum* group |
| **gyrB** | Genus-specific only | Excellent (subspecies) | No | Pseudomonas, Vibrio |
| **atpD** | Genus-specific only | Good (LAB pairs) | No | *L. gasseri*/*L. johnsonii* |

---

## 9. Non-Amplicon Approaches

### 9.1 Shotgun Metagenomics

**Key researchers**: Jacques Ravel (University of Maryland) — VALENCIA framework, CST standardization; Nicola Segata (University of Trento) — MetaPhlAn/StrainPhlAn pipelines; David Fredricks (Fred Hutchinson Cancer Center).

**Landmark study**: Fettweis et al. (2019) applied shotgun metagenomics to >1,500 vaginal samples from ~600 pregnant women (MOMS-PI/NIH Human Microbiome Project). Demonstrated that *L. crispatus* dominance was protective against preterm birth while *Sneathia amnii*, *Prevotella* cluster 2, and BVAB1-enriched communities were associated with preterm birth (*Nature Medicine*).

**Resolution**: Strain-level identification; functional pathway, antibiotic resistance, and virulence factor detection; simultaneous detection of bacteria, fungi, viruses, and parasites.

**Limitations**: $150–400/sample; vaginal samples typically contain 90–99% human DNA requiring deep sequencing or host depletion; bioinformatically complex.

### 9.2 Full-Length 16S on Long-Read Platforms

**PacBio HiFi**: Callahan et al. (2019) demonstrated single-nucleotide resolution of full-length 16S via circular consensus sequencing. Matsuo et al. (2021) applied this to vaginal samples from Japanese women, achieving species discrimination of *L. crispatus*, *L. iners*, *L. jensenii*, and *L. gasseri*.

**Nanopore**: Curry et al. (2022) developed the Emu classifier for long-read 16S (*Nature Methods*). Nanopore R10.4.1 with duplex basecalling achieves >99% accuracy.

**Remaining limitation**: Even full-length 16S struggles with Gardnerella species (98.5–99.5% identity across the full gene). Strain-level resolution is not achievable.

**Cost**: $50–150 (PacBio); $20–80 (Nanopore).

### 9.3 MALDI-TOF Mass Spectrometry

**Key researchers**: Mario Vaneechoutte (University of Ghent) — Gardnerella speciation; Janulaitiene et al. — Gardnerella clade separation.

**Resolution**: Excellent species-level ID for cultured isolates (>95% concordance with molecular methods). MALDI-TOF protein spectra clearly separated Gardnerella clades that 16S cannot resolve.

**Limitation**: Requires culture — cannot profile unculturable organisms (BVAB1-3, TM7 candidates). Not suitable for high-throughput community profiling. Database-dependent.

### 9.4 Metabolomics

**Key researchers**: Sujatha Srinivasan and David Fredricks (Fred Hutchinson Cancer Center) — BV metabolite signatures; Ceccarani et al. — integrated metabolomics/metagenomics.

**Capability**: Reliably distinguishes *Lactobacillus*-dominant vs. depleted communities. D-lactic acid/L-lactic acid ratios can differentiate *L. crispatus* dominance (high D-lactate) from *L. iners* dominance. Elevated biogenic amines (cadaverine, putrescine, tyramine) and short-chain fatty acids (succinate, butyrate) mark BV (Srinivasan et al., 2015).

**Limitation**: Community-level, not species-level resolution for complex anaerobic communities. Influenced by host physiology. Requires specialized instrumentation (LC-MS/MS, GC-MS, NMR). $200–500/sample.

### 9.5 FISH (Fluorescence In Situ Hybridization)

**Key researchers**: Alexander Swidsinski (Charite Hospital, Berlin) — vaginal biofilm architecture in BV; Nuno Cerca (University of Minho, Portugal) — FISH probes for *G. vaginalis*, *Atopobium vaginae*, Lactobacillus species.

**Unique value**: Provides spatial and structural information (biofilm architecture, epithelial association, species co-localization) that no sequencing method can deliver. Swidsinski demonstrated that *G. vaginalis* forms dense, adherent biofilms on vaginal epithelium in BV that persist after antibiotics and can be sexually transmitted (Swidsinski et al., 2005, 2010, 2014).

**Probes available**: *G. vaginalis* (Gard162), *Fannyhessea vaginae* (Ato291), *L. crispatus*, *L. iners*, *L. jensenii*, *L. gasseri*, *Prevotella bivia*, *Mobiluncus* spp., *Sneathia* spp., universal eubacterial (EUB338).

**Limitation**: Very low throughput; semi-quantitative; requires microscopy expertise; cannot detect organisms without pre-designed probes.

### 9.6 Species-Specific qPCR Panels

**Key researchers**: David Fredricks (Fred Hutchinson Cancer Center) — developed most vaginal-specific assays; Jean-Pierre Menard — BV diagnostic qPCR.

**Commercial panels**:
- **BD MAX Vaginal Panel** (FDA-cleared): *G. vaginalis*, *A. vaginae*, *Megasphaera* type 1, BVAB2, *L. crispatus*, *L. jensenii*, *L. gasseri*
- **Aptima BV Assay** (Hologic): RNA-based detection of *G. vaginalis*, *A. vaginae*, Lactobacillus spp.
- **NuSwab VG** / **SureSwab BV**: Combined BV/candidiasis/trichomoniasis panels

**Resolution**: Definitive species-level with absolute quantification. Sensitivity: 10–100 copies per reaction. Results in 1–3 hours.

**Limitation**: Targeted only (10–30 targets practical maximum); cannot discover novel organisms; requires validated primer/probe design for each target.

### 9.7 CRISPR-Based Diagnostics

**Researchers**: Feng Zhang (Broad Institute) — SHERLOCK platform; Jennifer Doudna (UC Berkeley) — DETECTR platform. HPV genotyping in cervical samples demonstrated feasibility (Chen et al., 2018). Proof-of-concept for BV-associated bacteria (Deng et al., 2024).

**Status**: No validated vaginal community typing panel exists as of early 2026. Multiplexing beyond 4–5 targets remains technically challenging. Promising for future point-of-care applications.

### 9.8 Microarrays

**PhyloChip** (Lawrence Berkeley National Laboratory): High-density 16S microarray with probes for >50,000 OTUs. Applied to vaginal samples by Dols et al. (2011), detecting organisms missed by 16S amplicon sequencing due to primer bias.

**Status**: Largely superseded by next-generation sequencing. PhyloChip no longer commercially available as of ~2016. Custom arrays are expensive and cannot detect organisms not represented on the array.

### 9.9 Summary Comparison

| Approach | Species Resolution | Strain Resolution | Discovery? | Cost/Sample | Key Advantage |
|---------|-------------------|-------------------|-----------|-------------|---------------|
| Shotgun metagenomics | Excellent | Yes | Yes | $150–400 | Comprehensive, functional |
| Full-length 16S (PacBio) | Very good | No | Limited | $50–150 | Species ID, familiar workflow |
| Full-length 16S (Nanopore) | Good–Very good | No | Limited | $20–80 | Rapid, portable, affordable |
| MALDI-TOF | Excellent (cultured) | Limited | No | $2–5/isolate | Rapid clinical ID |
| Metabolomics | Community-level | No | Functional | $200–500 | Functional readout |
| FISH | Excellent (targeted) | No | No | $50–100 | Spatial/biofilm information |
| qPCR panels | Excellent (targeted) | No | No | $20–100 | Quantitative, rapid, clinical |
| CRISPR diagnostics | Excellent (targeted) | No | No | $10–30 (projected) | Point-of-care potential |
| Microarrays | Good | No | Limited | $100–300 | Historical; superseded |

---

## 10. Comprehensive Marker Comparison

| Marker | Universal Primers? | Species Resolution | Vaginal Studies? | Amplicon Feasible? | Best For | Key Limitation |
|--------|-------------------|-------------------|-----------------|-------------------|----------|----------------|
| **16S V3-V4** | Yes | Genus-level | Standard | Yes (Illumina) | Broad profiling | Poor species resolution |
| **cpn60** | Yes (degenerate) | **Best barcode gap** | **Yes (multiple)** | Yes (Illumina) | Gardnerella, Prevotella, pan-bacterial | Misses Mollicutes |
| **rpoB** | Yes (broad) | Excellent | Not yet | Yes (Illumina) | Prevotella resolution | No vaginal validation |
| **pheS** | Lactobacillus only | **Best for Lactobacillus** | Not yet | Yes (Illumina) | Lactobacillus speciation | LAB-only |
| **Full rrn operon** | Yes (universal) | Near-perfect (0.999) | IS-pro: Yes | Long-read only | Comprehensive species ID | Requires Nanopore/PacBio |
| **tuf** | Genus-specific | Good (LAB) | No | Genus-targeted | Lactobacillus typing | Narrow scope |
| **recA** | Species-specific | Excellent (LAB pairs) | No | Limited | Isolate-level ID | Not for community profiling |
| **gyrB** | Genus-specific | Excellent (sub-spp.) | No | Genus-targeted | Pseudomonas, Vibrio | Narrow scope |
| **5S rRNA** | None validated | **~50% (not viable)** | No | No | Nothing standalone | Insufficient information |

---

## 11. Recommended Strategies

### 11.1 Dual-Marker Amplicon Approach

The strongest amplicon-based strategy for comprehensive species-level vaginal community profiling:

1. **cpn60** as the primary community marker — proven in vaginal studies, resolves Gardnerella species complex (the most critical gap), resolves Prevotella cryptic species, universal degenerate primers exist, curated database and classification tools available.
2. **pheS** as a supplementary Lactobacillus-specific marker — provides the highest available resolution for discriminating *L. crispatus*, *L. iners*, *L. gasseri*, *L. jensenii*, and other vaginal Lactobacillus species.
3. **Supplementary Mycoplasma/Ureaplasma-specific PCR** — fills the cpn60 Mollicute blind spot.

### 11.2 Single-Marker Long-Read Approach

If long-read sequencing infrastructure is available:

- **Full rrn operon on Nanopore or PacBio** — near-perfect species-level accuracy (0.999), universal primers, captures information from 16S + ITS + 23S + 5S in a single amplicon. Rapidly maturing bioinformatics tools (Emu, RESCUE, MIrROR).

### 11.3 Multi-Modal Approach

For maximum resolution and clinical relevance:

- **cpn60 amplicon sequencing** (community composition at species level)
- **Metabolomics** (D/L-lactate ratios for functional community state confirmation)
- **Species-specific qPCR** (quantitative validation of key taxa: *G. piotii*, *L. crispatus*, *L. iners*, Mollicutes)

---

## References

Adekambi, T., Drancourt, M., & Raoult, D. (2009). The rpoB gene as a tool for clinical microbiologists. *Trends in Microbiology*, 17(1), 37–45. https://doi.org/10.1016/j.tim.2008.09.006

Albert, A.Y., Chaban, B., Wagner, E.C., et al. (2015). A study of the vaginal microbiome in healthy Canadian women utilizing cpn60-based molecular profiling reveals distinct Gardnerella subgroup community state types. *PLoS ONE*, 10(8), e0135620. https://doi.org/10.1371/journal.pone.0135620

Budding, A.E., Hoogewerf, M., Bik, E.M., et al. (2021). IS-pro: comparison of the vaginal microbiota with 16S rRNA gene sequencing. *BMC Microbiology*, 21, 118. https://doi.org/10.1186/s12866-021-02149-7

Callahan, B.J., McMurdie, P.J., Rosen, M.J., et al. (2016). DADA2: High-resolution sample inference from Illumina amplicon data. *Nature Methods*, 13(7), 581–583. https://doi.org/10.1038/nmeth.3869

Callahan, B.J., Wong, J., Heiner, C., et al. (2019). High-throughput amplicon sequencing of the full-length 16S rRNA gene with single-nucleotide resolution. *Nucleic Acids Research*, 47(18), e103. https://doi.org/10.1093/nar/gkz569

Chaban, B., Links, M.G., Jayaprakash, T.P., et al. (2014). Characterization of the vaginal microbiota of healthy Canadian women through the menstrual cycle. *Microbiome*, 2, 23. https://doi.org/10.1186/2049-2618-2-23

Christensen, H., Kuhnert, P., Olsen, J.E., & Bisgaard, M. (2004). Comparative phylogenies of the housekeeping genes atpD, infB and rpoB and the 16S rRNA gene within the Pasteurellaceae. *International Journal of Systematic and Evolutionary Microbiology*, 54(5), 1601–1609. https://doi.org/10.1099/ijs.0.03018-0

Curry, K.D., Wang, Q., Nute, M.G., et al. (2022). Emu: species-level microbial community profiling of full-length 16S rRNA Oxford Nanopore sequencing data. *Nature Methods*, 19(7), 845–853. https://doi.org/10.1038/s41592-022-01520-4

de Oliveira Martins, L., Page, A.J., Mather, A.E., & Charles, I.G. (2020). Taxonomic resolution of the ribosomal RNA operon in bacteria: implications for its use with long-read sequencing. *NAR Genomics and Bioinformatics*, 2(4), lqaa073. https://doi.org/10.1093/nargab/lqaa073

Dumonceaux, T.J., Schellenberg, J., Golber, T., et al. (2021). Multiplex detection of bacteria in complex clinical and environmental samples using oligonucleotide-coupled fluorescent microspheres. *Microorganisms*, 9(4), 816. https://doi.org/10.3390/microorganisms9040816

Felis, G.E., Dellaglio, F., Mizzi, L., & Torriani, S. (2001). Comparative sequence analysis of a recA gene fragment brings new evidence for a change in the taxonomy of the Lactobacillus casei group. *International Journal of Systematic and Evolutionary Microbiology*, 51(6), 2113–2117. https://doi.org/10.1099/00207713-51-6-2113

Fettweis, J.M., Serrano, M.G., Brooks, J.P., et al. (2019). The vaginal microbiome and preterm birth. *Nature Medicine*, 25(6), 1012–1021. https://doi.org/10.1038/s41591-019-0450-2

France, M.T., Ma, B., Gajer, P., et al. (2020). VALENCIA: a nearest centroid classification method for vaginal microbial communities based on composition. *Microbiome*, 8(1), 166. https://doi.org/10.1186/s40168-020-00934-6

Freitas, A.C., Chaban, B., Bocking, A., et al. (2017). The vaginal microbiome of pregnant women is less rich and diverse, with lower prevalence of Mollicutes, compared to non-pregnant women. *Scientific Reports*, 7, 9212. https://doi.org/10.1038/s41598-017-07790-9

Freitas, A.C., Bocking, A., Hill, J.E., & Money, D.M. (2018). Increased richness and diversity of the vaginal microbiota and spontaneous preterm birth. *Microbiome*, 6, 117. https://doi.org/10.1186/s40168-018-0502-8

Hay, R.T., Albert, A.Y.K., & Hill, J.E. (2023). CpnClassiPhyR: a phylogeny-based classifier for cpn60 amplicon sequence variant taxonomic assignment. *ISME Communications*, 3, 71. https://doi.org/10.1038/s43705-023-00283-z

Hill, J.E., Penny, S.L., Crowell, K.G., Goh, S.H., & Hemmingsen, S.M. (2004). cpnDB: a chaperonin sequence database. *Genome Research*, 14(8), 1669–1675. https://doi.org/10.1101/gr.2649204

Janssen, K.N., Schellenberg, J.J., & Hill, J.E. (2019). Gardnerella vaginalis subgroup distribution in Nugent score categories. *Infection and Immunity*, 87(12), e00540-19. https://doi.org/10.1128/IAI.00540-19

Kyongo, J.K., Crucitti, T., Menten, J., et al. (2022). Cervicovaginal microbiota-cytokine profiles and their association with HIV acquisition in South African women. *Frontiers in Immunology*, 13, 974195. https://doi.org/10.3389/fimmu.2022.974195

Links, M.G., Dumonceaux, T.J., Hemmingsen, S.M., & Hill, J.E. (2012). The chaperonin-60 universal target is a barcode for bacteria that enables de novo assembly of metagenomic sequence data. *PLoS ONE*, 7(11), e49755. https://doi.org/10.1371/journal.pone.0049755

Naser, S.M., Thompson, F.L., Hoste, B., et al. (2005). Application of multilocus sequence analysis (MLSA) for rapid identification of Enterococcus species based on rpoA and pheS genes. *Microbiology*, 151(7), 2141–2150. https://doi.org/10.1099/mic.0.27840-0

Naser, S.M., Dawyndt, P., Hoste, B., et al. (2007). Identification of lactobacilli by pheS and rpoA gene sequence analyses. *International Journal of Systematic and Evolutionary Microbiology*, 57(12), 2777–2789. https://doi.org/10.1099/ijs.0.64711-0

Ogier, J.C., Pagès, S., Galan, M., Barret, M., & Gaudriault, S. (2019). rpoB, a promising marker for analyzing the diversity of bacterial communities by amplicon sequencing. *BMC Microbiology*, 19, 171. https://doi.org/10.1186/s12866-019-1546-z

Paramel Jayaprakash, T., Schellenberg, J.J., & Hill, J.E. (2012). Resolution and characterization of distinct cpn60-based subgroups of Gardnerella vaginalis in the vaginal microbiota. *PLoS ONE*, 7(8), e43009. https://doi.org/10.1371/journal.pone.0043009

Paramel Jayaprakash, T., Wagner, E.C., van Schalkwyk, J., et al. (2016). High diversity and variability in the vaginal microbiome in women following preterm premature rupture of membranes (PPROM): a prospective cohort study. *PLoS ONE*, 11(11), e0166794. https://doi.org/10.1371/journal.pone.0166794

Petrone, B.L., Lejars, M., Neville, B.A., & Garrett, W.S. (2023). RESCUE: Ribosomal operon Evaluation, Sequencing, Curation, and Usability Enhancement for metataxonomic profiling. *Frontiers in Microbiology*, 14, 1201064. https://doi.org/10.3389/fmicb.2023.1201064

Poirier, S., Rué, O., Peguilhan, R., et al. (2018). Deciphering intra-species bacterial diversity of meat and seafood spoilage microbiota using gyrB amplicon sequencing: a comparative analysis with 16S rDNA V3-V4 amplicon sequencing. *PLoS ONE*, 13(9), e0204629. https://doi.org/10.1371/journal.pone.0204629

Quast, C., Pruesse, E., Yilmaz, P., et al. (2013). The SILVA ribosomal RNA gene database project: improved data processing and web-based tools. *Nucleic Acids Research*, 41(D1), D590–D596. https://doi.org/10.1093/nar/gks1219

Ravel, J., Gajer, P., Abdo, Z., et al. (2011). Vaginal microbiome of reproductive-age women. *Proceedings of the National Academy of Sciences*, 108(Suppl 1), 4680–4687. https://doi.org/10.1073/pnas.1002611107

Schloss, P.D., Westcott, S.L., Ryabin, T., et al. (2009). Introducing mothur: open-source, platform-independent, community-supported software for describing and comparing microbial communities. *Applied and Environmental Microbiology*, 75(23), 7537–7541. https://doi.org/10.1128/AEM.01541-09

Schuyler, J.A., Mordechai, E., Gal-Mor, O., et al. (2016). Identification of Gardnerella vaginalis subgroup distribution in vaginal swabs by Gardnerella vaginalis cpn60 combined community profiling. *PLoS ONE*, 11(1), e0146510. https://doi.org/10.1371/journal.pone.0146510

Seol, D., & Kim, H. (2022). MIrROR: Microbial Identification using rRNA Operon Region. Database and tool for metataxonomics with long-read sequence. *Microbiology Spectrum*, 10(2), e02017-21. https://doi.org/10.1128/spectrum.02017-21

Srinivasan, S., Morgan, M.T., Fiedler, T.L., et al. (2015). Metabolic signatures of bacterial vaginosis. *mBio*, 6(2), e00204-15. https://doi.org/10.1128/mBio.00204-15

Swidsinski, A., Mendling, W., Loening-Baucke, V., et al. (2005). Adherent biofilms in bacterial vaginosis. *Obstetrics & Gynecology*, 106(5), 1013–1023. https://doi.org/10.1097/01.AOG.0000183594.45524.d2

Swidsinski, A., Doerffel, Y., Loening-Baucke, V., et al. (2010). Gardnerella biofilm involves females and males and is transmitted sexually. *Gynecologic and Obstetric Investigation*, 70(4), 256–263. https://doi.org/10.1159/000314015

Szoboszlay, M., Zis, L., & Hedtke, S.M. (2024). Evaluating the efficiency of 16S-ITS-23S rRNA operon sequencing for species-level resolution. *Scientific Reports*, 14, 85211. https://doi.org/10.1038/s41598-024-83410-7

Szymanski, M., Zielezinski, A., Barciszewski, J., Erdmann, V.A., & Karlowski, W.M. (2016). 5SRNAdb: an information resource for 5S ribosomal RNAs. *Nucleic Acids Research*, 44(D1), D199–D203. https://doi.org/10.1093/nar/gkv1081

Tarrand, J.J., Liu, B., Glass, N.R., et al. (2024). Broad-range rpoB amplification and Sanger sequencing for clinical bacterial identification. *Journal of Clinical Microbiology*, 62(7), e00266-24. https://doi.org/10.1128/jcm.00266-24

Torriani, S., Felis, G.E., & Dellaglio, F. (2001). Differentiation of Lactobacillus plantarum, L. pentosus, and L. paraplantarum by recA gene sequence analysis and multiplex PCR assay with recA gene-derived primers. *Applied and Environmental Microbiology*, 67(8), 3450–3454. https://doi.org/10.1128/AEM.67.8.3450-3454.2001

Vaneechoutte, M., Guschin, A., Van Simaey, L., et al. (2019). Emended description of Gardnerella vaginalis and description of Gardnerella leopoldii sp. nov., Gardnerella piotii sp. nov. and Gardnerella swidsinskii sp. nov., with delineation of 13 genomic species within the genus Gardnerella. *International Journal of Systematic and Evolutionary Microbiology*, 69(3), 679–687. https://doi.org/10.1099/ijsem.0.003200

Ventura, M., Canchaya, C., Meylan, V., Klaenhammer, T.R., & Zink, R. (2003). Analysis, characterization, and loci of the tuf genes in Lactobacillus and Bifidobacterium species and their direct application for species identification. *Applied and Environmental Microbiology*, 69(11), 6908–6922. https://doi.org/10.1128/AEM.69.11.6908-6922.2003

Vos, M., Quince, C., Pijl, A.S., de Hollander, M., & Kowalchuk, G.A. (2012). A comparison of rpoB and 16S rRNA as markers in pyrosequencing studies of bacterial diversity. *PLoS ONE*, 7(2), e30600. https://doi.org/10.1371/journal.pone.0030600

Won, S., Cho, S., & Kim, H. (2024). rRNA operon improves species-level classification of bacteria and microbial community analysis compared to 16S rRNA. *Microbiology Spectrum*, 12(11), e00931-24. https://doi.org/10.1128/spectrum.00931-24

Wuyts, S., Wittouck, S., De Boeck, I., et al. (2021). pheS amplicon sequencing to unravel Lactobacillus community composition. *Applied and Environmental Microbiology*, 87(8), e02191-20. https://doi.org/10.1128/AEM.02191-20

Xu, Z., Xie, J., Liu, L., et al. (2023). tuf-targeted amplicon sequencing reveals high Bacillus diversity misidentified by 16S rRNA V3-V4 amplicon sequencing. *ISME Communications*, 3, 114. https://doi.org/10.1038/s43705-023-00330-9
