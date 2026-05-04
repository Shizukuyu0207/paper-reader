# Domain: Bioinformatics (生物信息学)

## Domain ID: `bio`
## Archive Dir: `~/obsidian/papers/bioinformatics/`

---

## Extraction Checklist

When analyzing a bioinformatics paper, extract and fill EVERY field below. Use "论文未提及" if the paper does not provide the information.

### Study Design
| # | Field | Extraction Rule |
|---|-------|----------------|
| 1 | 分析类型 | RNA-seq / WGS / WES / GWAS / single-cell / ATAC-seq / ChIP-seq / proteomics / metabolomics / metagenomics / multi-omics |
| 2 | 物种 | Model organism / human / plant / microbial — specific strain if mentioned |
| 3 | 样本量 | Total N + group breakdown (case/control, treated/untreated) + biological replicates |
| 4 | 数据来源 | Public database (SRA/GEO/TCGA/ENA/PRIDE) + accession numbers, or in-house generated |

### Data Processing
| # | Field | Extraction Rule |
|---|-------|----------------|
| 5 | 比对/参考基因组 | Alignment tool + version + reference genome build (e.g. STAR 2.7.11a, GRCh38) |
| 6 | 差异分析工具 | DESeq2 / edgeR / limma-voom / MAST (single-cell) / other + version |
| 7 | 统计阈值 | FDR cutoff / Log2FC cutoff / P-value threshold |

### Functional Analysis
| # | Field | Extraction Rule |
|---|-------|----------------|
| 8 | 功能富集 | GO / KEGG / Reactome / GSEA + tool used + top enriched terms |
| 9 | 验证方法 | qPCR / western blot / immunohistochemistry / independent cohort / functional assay |

### Reproducibility & Key Findings
| # | Field | Extraction Rule |
|---|-------|----------------|
| 10 | Pipeline可复现性 | Code available (GitHub) / containerized (Docker/Singularity) / workflow manager (Snakemake/Nextflow/WDL) |
| 11 | 关键基因/变异 | Gene symbols / rsIDs + effect size + functional annotation |

---

## Special Attention Points for Bioinformatics Papers
- Batch effects: were they addressed? How?
- Multiple testing correction: Bonferroni vs BH vs other?
- Sample size adequacy for the analysis type
- Reference genome version consistency
- Single-cell: doublet detection, cell type annotation method
- GWAS: population stratification, LD structure, fine-mapping
- Multi-omics integration: how are layers connected?
- Code availability and version pinning

## Relevance Assessment
- Does the analysis pipeline match methods the user might apply?
- Are the datasets relevant to user's biological questions?
- Can the tools/workflows be directly adopted?
