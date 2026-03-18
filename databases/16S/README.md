# 16S Database

## Sources
- **SILVA**: Pre-trained QIIME2 classifier — [SILVA](https://www.arb-silva.de/)
- **Greengenes2**: Alternative classifier — [Greengenes2](https://greengenes2.ucsd.edu/)
- **VALENCIA**: CST centroids + classification script — [GitHub](https://github.com/ravel-lab/VALENCIA)

## Role in this project
16S is the **baseline comparator**, not the primary profiling marker. It serves to:
1. Link to existing FRESH data (Gosmann et al. 2017)
2. Run VALENCIA to quantify how many FRESH samples are unclassifiable by the standard CST framework
3. Provide total bacterial load denominator (universal 16S qPCR)
4. Enable cross-study comparisons with the published literature

## VALENCIA extension plan
- Run VALENCIA on FRESH 16S data; quantify samples with max theta < 0.90
- Cluster unclassified samples to identify novel cervicotypes
- Define new centroids for South African-specific community types
- Publish as extension to VALENCIA framework

## Key references
- France et al. (2020). Microbiome, 8, 166. DOI: 10.1186/s40168-020-00934-6
- Gosmann et al. (2017). Immunity, 46, 29-37. DOI: 10.1016/j.immuni.2016.12.013
