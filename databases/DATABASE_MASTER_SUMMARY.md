# Database Master Summary — FRESH Cervicotype Project

**Last updated:** 2026-03-20
**Location:** `/lts/sahlab/data4/DATA_DOWNLOADS_3/fresh_cervicotypes/databases/`

---

## 1. cpn60 — Primary Community Profiler

**Purpose:** Species-level resolution of the full bacterial community, especially Gardnerella, Prevotella, and anaerobes.

**Source:** Hill lab cpn60-Classifier v11.1 + NCBI L. jensenii supplement

### Key files

| File | Path | Contents |
|------|------|----------|
| Reference sequences | `cpn60/v11.1/cpn60-Classifier_v11.0_training/refseqs_v11.fasta` | 16,413 curated cpn60 barcode sequences |
| Taxonomy | `cpn60/v11.1/cpn60-Classifier_v11.0_training/taxonomytable_v11.txt` | 18-rank tab-delimited taxonomy |
| QIIME2 classifier | `cpn60/v11.1/cpn60-q2-feature-classifier-v11/cpn60_classifier_v11.qza` | Pre-trained Naive Bayesian classifier |
| QIIME2 sequences | `cpn60/v11.1/cpn60-q2-feature-classifier-v11/cpn60_v11_seqs.fasta` | QIIME2-formatted reference seqs |
| QIIME2 taxonomy | `cpn60/v11.1/cpn60-q2-feature-classifier-v11/cpn60_v11_taxonomy_table.txt` | QIIME2 k\_\_/p\_\_/.../s\_\_ format |
| RDP trained model | `cpn60/v11.1/v11_training_files/` | 5 files for standalone RDP classifier |
| L. jensenii supplement | `cpn60/v11.1/ljensenii_supplement.fasta` | 8 new UT sequences from NCBI |
| Documentation | `cpn60/v11.1/DATABASE_SUMMARY.md` | Full details incl. Gardnerella GS mapping |

### Key species coverage

| Taxon | Sequences | Notes |
|-------|-----------|-------|
| Gardnerella total | 51 | G. vaginalis 16, G. piotii 7, G. swidsinskii 5, G. leopoldii 4, 9 genomospecies 19 |
| L. crispatus | 9 | |
| L. iners | 15 | |
| L. gasseri | 10 | |
| L. jensenii | 3 + 8 supplement = 11 | Supplement not yet merged into classifier — retraining needed |
| Prevotella | 124 | 48 unique species incl. P. bivia 4, P. amnii 3, P. timonensis 2 |
| Megasphaera | 7 | |
| Fannyhessea/Atopobium | 5 | |
| Sneathia | 2 | |
| BVAB Acetatifactor/Mageeibacillus | 2 | |

### Limitations

- L. jensenii supplement 8 seqs requires classifier retraining before it is active. The pre-trained QZA does NOT include them.
- Mollicutes: 82 entries exist in cpnDB since some Mollicute lineages retain cpn60. However, M. hominis and all Ureaplasma LACK cpn60 entirely. M. genitalium present at 5 seqs but unlikely to amplify with universal primers in vaginal samples — flag hits for comparison with MgPa qPCR.
- No South African-specific sequences in cpnDB. Novel taxa in FRESH samples may classify only to genus level.
- cpnDB website under construction — cpnDB\_nr\_vag and VOGUE Reference Assembly may need direct Hill lab contact.

### Classifier note

Use the QIIME2 classifier or RDP trained model. Do NOT use 16S-trained classifiers for cpn60 data.

---

## 2. pheS — Lactobacillus Zoom Lens

**Purpose:** Species- and strain-level resolution within Lactobacillus. Supplements cpn60 for the dominant vaginal genus.

**Source:** Wuyts et al. 2021 + NCBI GenBank supplement + expanded NCBI search + 1 FRESH SA MAG extract

### Key files

| File | Path | Contents |
|------|------|----------|
| **Final reference** | `pheS/wuyts2021/pheS_final_reference.fasta` | **399 entries — USE THIS** |
| **Final taxonomy** | `pheS/wuyts2021/pheS_final_taxonomy.txt` | **399 entries — USE THIS** |
| Intermediate pre-expansion | `pheS/wuyts2021/pheS_combined_reference.fasta` | 383 entries, Wuyts + first NCBI supplement |
| Accession mapping | `pheS/wuyts2021/wuyts_acc_to_species.tsv` | NCBI accession-to-species lookup |
| Documentation | `pheS/DATABASE_SUMMARY.md` | Full build details |

### Key species coverage

| Taxon | Sequences | Source |
|-------|-----------|-------|
| L. crispatus | 9 | Type strains + urinary isolates |
| L. iners | 11 | Type strains + urinary + 1 SA ectocervical MAG |
| L. gasseri | 17 | Type strains + urinary isolates |
| L. jensenii | 11 | Type strains + urinary isolates |
| L. vaginalis | 1 | Type strain only |
| Bifidobacterium spp. | 9 | Outgroup for classifier training |
| Other LAB genera | ~200+ | Broad Lactobacillaceae from Wuyts framework |
| Non-LAB outgroups | 8 | Bacillus, Enterococcus, Lactococcus, Leuconostoc, Oenococcus, Weissella with correct family taxonomy |

### Limitations

- No pre-trained classifier exists. Must be trained from the FASTA + taxonomy files in Phase 2.
- No African-origin pheS in direct NCBI deposits — all have "not specified" country. The 1 SA L. iners MAG extract is the only confirmed African sequence.
- L. vaginalis severely underrepresented at 1 sequence.
- FRESH SA MAG extraction incomplete: 50 SA ectocervical Lactobacillus MAGs identified at BioSample SAMN25184*, only 1 extracted. Remaining 49 need full contig download + pheS extraction requiring BLAST.
- 472 WGS genome assemblies identified with pheS annotation but gene not yet extracted. Includes vaginal outgroup taxa: Megasphaera 28, S. agalactiae ~100, Gardnerella 3, Prevotella 4, Mobiluncus 1, Sneathia 1.
- 43 Wuyts accessions unmapped to species via NCBI, excluded from combined DB.
- 1 multi-species sequence retained with both identities.
- 11 unresolved entries flagged with [unresolved] tag.

### Primers

- pheS21F: 5'-CAYCCNGCHCGYGAYATGC-3'
- pheS23R: 5'-GGRTGRACCATVCCNGCHCC-3'
- Amplicon: ~431 bp
- Lactobacillaceae-specific — will NOT amplify Gardnerella, Prevotella, Sneathia, etc.

---

## 3. ITS — Fungal Profiler

**Purpose:** Detect and classify fungal community members: Candida spp., Malassezia, others.

**Source:** UNITE v10.0 2025-02-19 pre-trained classifiers from colinbrislawn/unite-train

### Key files

| File | Path | Contents |
|------|------|----------|
| **Primary classifier** | `ITS/unite_v10/unite_v10_dynamic_fungi_Q2-2024.10.qza` | **220MB — USE THIS** dynamic threshold fungi only |
| Alternative classifier | `ITS/unite_v10/unite_v10_99_fungi_Q2-2024.10.qza` | 208MB, 99% threshold higher species resolution |
| Documentation | `ITS/DATABASE_SUMMARY.md` | Full details |

### What it covers

- 239,180 fungal species hypotheses from UNITE v10.0
- All Candida species: albicans, glabrata, krusei, tropicalis, parapsilosis
- Malassezia species
- Pre-trained — no further database work needed

### Limitations

- Pre-trained classifier is QIIME2 version-specific at Q2-2024.10. Different QIIME2 versions need matching classifier.
- Raw FASTA + taxonomy not downloaded — available via DOI 10.15156/BIO/3301241 if retraining needed.
- ITS amplicon length varies dramatically at 250-800+ bp requiring ITSxpress trimming and customized DADA2 parameters per Rivers et al. 2022.
- Low fungal biomass expected in most vaginal samples.

### Primers

- ITS1F: 5'-CTTGGTCATTTAGAGGAAGTAA-3'
- ITS2: 5'-GCTGCGTTCTTCATCGATGC-3'
- Region: ITS1, ~250-400 bp variable
- Earth Microbiome Project standard

---

## 4. 16S — Baseline Comparator

**Purpose:** Standard marker for comparison with existing literature, VIRGO2 CST assignment, total bacterial load.

**Status:** COMPLETE (classifiers downloaded, VIRGO2 cloned, database pending)

### Key files

| File | Path | Contents |
|------|------|----------|
| **SILVA 138 classifier** | `16S/silva/silva-138-99-nb-classifier.qza` | Full-length 99% OTUs, sklearn 1.4.2, 209MB |
| **Greengenes2 V4 classifier** | `16S/silva/gg2-2024.09-v4-nb-classifier.qza` | 515F/806R V4 region, sklearn 1.4.2, 47MB |
| **VIRGO2 pipeline** | `16S/virgo2/` | Snakemake workflow for CST assignment (cloned repo) |
| Documentation | `16S/DATABASE_SUMMARY.md` | Full details incl. VIRGO2 setup instructions |

### Limitations

- VIRGO2 database files NOT yet downloaded — requires Dropbox link from Michael France at Ravel lab. After publication will be on Zenodo.
- Primer choice for new FRESH 16S: 515F/806R (Gosmann) vs 341F/805R (Ravel lab) — decision needed.
- 16S copy number variation biases abundance — cpn60 is more accurate for quantification.
- 16S cannot resolve Gardnerella or Prevotella to species level.

### Existing FRESH 16S data

- Gosmann et al. 2017: ENA PRJEB14858
- Kwon lab follow-up: NCBI PRJNA738803
- FRESH LACTIN-V trial: NCBI PRJNA1085249

---

## 5. Mollicute-Specific Primers

**Purpose:** Targeted qPCR for M. genitalium, M. hominis, U. parvum, U. urealyticum — invisible to cpn60 and underdetected by 16S.

**Status:** COMPLETE

### Key files

| File | Path | Contents |
|------|------|----------|
| Primer sequences | `mollicute_primers/primer_sequences.tsv` | 4 targets with primer/probe seqs, references |
| Documentation | `mollicute_primers/DATABASE_SUMMARY.md` | Full details |

### Targets

| Target | Gene | Amplicon | SA prevalence |
|--------|------|----------|---------------|
| M. genitalium | MgPa adhesin | 78 bp TaqMan | ~10% in women |
| M. hominis | 16S rRNA species-specific | ~270 bp | 81% in HIV+ SA women |
| U. parvum | ureC | ~100 bp TaqMan | 77% in SA HIV+ women |
| U. urealyticum | ureC | ~100 bp TaqMan | Less common |

### Limitations

- Primers from published literature, not independently validated by us
- No SA-specific Mollicute primer validation published
- In silico specificity check recommended before wet lab use

---

## 6. Fredricks BV Indicator Primers

**Purpose:** Targeted qPCR for BV-associated taxa: BVAB1, BVAB2, Megasphaera type 1, Fannyhessea vaginae.

**Status:** COMPLETE

### Key files

| File | Path | Contents |
|------|------|----------|
| Primer sequences | `fredricks_bv_primers/primer_sequences.tsv` | 4 targets with primer seqs, references |
| Documentation | `fredricks_bv_primers/DATABASE_SUMMARY.md` | Full details incl. diagnostic performance |

### Targets

| Target | Amplicon | Diagnostic value |
|--------|----------|-----------------|
| BVAB1 | 95 bp | Strongly associated with BV and inflammation |
| BVAB2 | 100 bp | Best single BV marker |
| Megasphaera type 1 | 121 bp | Distinguishes type 1 from type 2 |
| Fannyhessea vaginae | 120 bp | Key BV indicator |

Best combination: BVAB2 OR Megasphaera type 1 = 98.8% sensitivity, 93.7% specificity.

### Limitations

- Designed/validated on US populations — SA recalibration needed
- In silico specificity check against SA 16S sequences recommended

---

## Cross-Database Reference

### What each marker can and cannot see

| Taxon | cpn60 | pheS | ITS | 16S | Mollicute PCR | Fredricks PCR |
|-------|-------|------|-----|-----|---------------|---------------|
| Gardnerella species | **Yes species** | No | No | Genus only | No | No |
| Prevotella species | **Yes species** | No | No | Poor | No | No |
| L. crispatus/iners/gasseri/jensenii | Yes species | **Yes strain** | No | Species | No | No |
| Candida spp. | No | No | **Yes** | No | No | No |
| M. genitalium | Unlikely | No | No | Poor | **Yes** | No |
| M. hominis | **No** | No | No | Poor | **Yes** | No |
| Ureaplasma spp. | **No** | No | No | Poor | **Yes** | No |
| BVAB1 | Uncertain | No | No | Yes | No | **Yes** |
| Megasphaera type 1 vs 2 | Uncertain | No | No | No | No | **Yes** |
| Fannyhessea vaginae | Yes | No | No | Yes | No | **Yes** |

**No single marker sees everything — that is the rationale for the multi-marker approach.**

---

## Pending Tasks

| Task | Priority | Blocked by |
|------|----------|------------|
| Retrain cpn60 classifier with L. jensenii supplement | High | QIIME2 installation Phase 2 |
| Train pheS classifier from final reference | High | QIIME2 installation Phase 2 |
| Extract pheS from 49 remaining SA FRESH MAGs | Medium | BLAST installation or disk quota |
| Extract pheS from 472 WGS genomes for outgroup enrichment | Medium | BLAST installation |
| Download raw UNITE FASTA + taxonomy | Low | Only if retraining needed |
| Contact Hill lab for cpnDB\_nr\_vag + VOGUE reference | Medium | Scott approval |
| Set up 16S SILVA + VIRGO2 | ~~Next~~ **DONE** | Classifiers downloaded, VIRGO2 cloned, DB pending Ravel lab |
| Obtain VIRGO2 database files | High | Contact Michael France / Ravel lab for Dropbox link |
| Compile Mollicute primer sequences | ~~Next~~ **DONE** | 4 targets compiled with sequences and references |
| Compile Fredricks BV primer sequences | ~~Next~~ **DONE** | 4 targets compiled with sequences and references |
| Download validation datasets from SRA | **Next** | Step 1g |
