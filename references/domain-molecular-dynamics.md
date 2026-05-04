# Domain: Molecular Dynamics (分子动力学)

## Domain ID: `md`
## Archive Dir: `~/obsidian/papers/molecular-dynamics/`

---

## Extraction Checklist

When analyzing an MD paper, extract and fill EVERY field below. Use "论文未提及" if the paper does not provide the information. Do NOT leave any field blank.

### System Setup
| # | Field | Extraction Rule |
|---|-------|----------------|
| 1 | 模拟体系 | Protein/nucleic acid/complex name, PDB ID if available |
| 2 | 力场 | Specific force field + version (e.g. AMBER ff19SB, CHARMM36m, OPLS-AA/M, GROMOS 54A7) |
| 3 | 溶剂模型 | Water model: TIP3P/TIP4P-Ew/SPC/E/OPC/etc. |
| 4 | 盒类型+尺寸 | Box shape (dodecahedron/cubic/orthorhombic) + buffer distance or explicit dimensions |
| 5 | 离子 | Ion type + concentration (e.g. 0.15 M NaCl, neutralizing counterions) |

### Simulation Protocol
| # | Field | Extraction Rule |
|---|-------|----------------|
| 6 | 平衡协议 | Minimization steps/method, NVT duration+temp, NPT duration+temp+pressure, restraints used |
| 7 | 生产模拟时长 | Total simulation time in ns or μs, number of replicas |
| 8 | 时间步长 | Integration timestep (1 fs, 2 fs, 4 fs with H-mass repartitioning) |
| 9 | 软件 | Specific software + version (AMBER20, GROMACS 2024.1, NAMD 3.0, OpenMM 8.0, etc.) |
| 10 | 硬件 | GPU model + count, or CPU info, total wall time if reported |

### Enhanced Sampling & Free Energy
| # | Field | Extraction Rule |
|---|-------|----------------|
| 11 | 自由能方法 | FEP/TI/MM-PBSA/MM-GBSA/thermodynamic integration/Wham/none |
| 12 | 增强采样 | REMD (T-RED/pH-REMD), metadynamics (CVs), aMD, GaMD, umbrella sampling, none |

### Analysis & Results
| # | Field | Extraction Rule |
|---|-------|----------------|
| 13 | 分析指标 | RMSD/RMSF/Rg/SASA/hydrogen bonds/secondary structure/PCA/cluster/contacts/interaction energy — list all used |
| 14 | 关键参数值 | Extract specific quantitative results with units (e.g. "RMSD stabilized at 2.1 ± 0.3 Å", "ΔG = -8.2 ± 1.1 kcal/mol") |

### Assessment
| # | Field | Extraction Rule |
|---|-------|----------------|
| 15 | 局限性 | Author-stated limitations + your own assessment of methodological gaps |
| 16 | 可复现性评分 | Parameter completeness score 1-5: 1=insufficient info, 5=all parameters specified and reproducible |

---

## Special Attention Points for MD Papers
- Force field version matters — ff14SB and ff19SB are very different
- Water model choice affects results significantly
- Check if equilibration was sufficient (convergence criteria?)
- Production simulation length: is it adequate for the system size?
- Replica count: single trajectory or multiple independent runs?
- Free energy: convergence? Sampling adequacy?
- Enhanced sampling: are CVs justified? Is the bias properly removed?

## Cross-reference with User's AMBER Setup
The user primarily works with AMBER (sander, CPU mode). When assessing relevance:
- Note if the paper uses AMBER-compatible methods
- Flag if GPU-accelerated methods are discussed (user currently CPU-only)
- Identify if force fields/software versions match user's setup
