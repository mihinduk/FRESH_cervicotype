# QA Human Review Items — FRESH Cervicotype Project

Items flagged by the QA subagent that require human domain expertise. Check at your convenience.

---

## 2026-03-19 — Phase 1 Step 1a: cpn60 Database v11.1 Setup

- [ ] **Mollicute entries in cpnDB**: The database contains 82 Mollicute entries including 5 M. genitalium sequences. QA flagged that M. genitalium is present in cpnDB but unlikely to be detected by universal cpn60 primers in vaginal samples due to its intracellular lifestyle. **Decision needed**: Should M. genitalium cpn60 hits be treated as valid or filtered in downstream analysis? — `databases/cpn60/v11.1/DATABASE_SUMMARY.md` — QA reasoning: M. genitalium detection will rely on MgPa-specific qPCR, not cpn60 amplicon sequencing, so cpn60 hits for M. genitalium would likely be spurious.

- [ ] **Gardnerella genomospecies representation**: 9 genomospecies (sp. 2, 3, 7, 8, 9, 10, 11, 12, 13) are in cpnDB but sp. 4, 5, 6 are absent. **Decision needed**: Is this a gap that needs filling (contact Hill lab), or are sp. 4-6 not relevant for vaginal samples? — `databases/cpn60/v11.1/DATABASE_SUMMARY.md` — QA reasoning: Missing genomospecies could cause misclassification of novel South African Gardnerella variants.

- [ ] **L. jensenii underrepresented**: Only 3 reference sequences vs 9-15 for other vaginal Lactobacillus species. **Decision needed**: Is this sufficient for reliable classification, or should additional L. jensenii cpn60 sequences be sourced from NCBI? — `databases/cpn60/v11.1/DATABASE_SUMMARY.md` — QA reasoning: Low reference count may reduce classifier confidence for L. jensenii-dominant samples (CST-V).

- [x] **L. jensenii underrepresented**: Supplemented with 8 new sequences from NCBI (5 direct deposits + 3 genome extracts). Total now 11, comparable to other vaginal Lactobacillus species. — `databases/cpn60/v11.1/ljensenii_supplement.fasta` — Classifier retraining needed before these are active.

- [ ] **M. genitalium cpn60 hits**: Flag for comparison with Mollicute-specific qPCR results. Do not filter from cpn60 output but annotate as "requires confirmation by MgPa qPCR". — Implementation note for pipeline step 2a.

- [x] **Gardnerella genomospecies 4/5/6**: Not a gap — GS4=G. piotii (7 seqs), GS5=G. leopoldii (4 seqs), GS6=G. swidsinskii (5 seqs) are present under their formal species names per Vaneechoutte et al. 2019 nomenclature update.
