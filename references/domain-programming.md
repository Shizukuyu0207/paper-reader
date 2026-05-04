# Domain: Programming & Systems (编程与系统)

## Domain ID: `prog`
## Archive Dir: `~/obsidian/papers/programming/`

---

## Extraction Checklist

When analyzing a programming/systems paper, extract and fill EVERY field below. Use "论文未提及" if the paper does not provide the information.

### System Overview
| # | Field | Extraction Rule |
|---|-------|----------------|
| 1 | 系统类型 | Compiler / OS / database / network / storage / distributed system / tool / library / framework |
| 2 | 核心算法 | Specific algorithm + time complexity + space complexity |
| 3 | 编程语言 | Primary language + version + supplementary languages |

### Scale & Performance
| # | Field | Extraction Rule |
|---|-------|----------------|
| 4 | 系统规模 | Lines of code / module count / supported scale / concurrent users |
| 5 | 性能指标 | Throughput (QPS/RPS) / latency (P50/P99) / memory usage + specific values |
| 6 | 对比基准 | Compared against which systems/tools + percentage improvement |

### Evaluation
| # | Field | Extraction Rule |
|---|-------|----------------|
| 7 | 实验环境 | Hardware specs + OS + software versions |
| 8 | Benchmark设计 | Fair comparison? Realistic workload? Reproducible setup? |
| 9 | 代码开源 | Repository link + license + activity level |

### Practical Value
| # | Field | Extraction Rule |
|---|-------|----------------|
| 10 | 实用价值 | Can it be used directly? Migration cost? Dependency requirements? |

---

## Special Attention Points for Programming Papers
- Is the benchmark realistic or synthetic only?
- Does the improvement hold at scale?
- Backward compatibility and migration path
- Dependency on specific hardware or platform
- Security implications if relevant
- Community adoption and maintenance status
- For ML systems papers: inference optimization, serving architecture

## Relevance Assessment
- Could this tool/system be useful for user's workflows (MD simulation, bioinformatics pipelines)?
- Does it solve a bottleneck the user currently faces?
- Is the technology mature enough for adoption?
