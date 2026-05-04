# Domain: Medicine (医学)

## Domain ID: `med`
## Archive Dir: `~/obsidian/papers/medicine/`

---

## Extraction Checklist

When analyzing a medical research paper, extract and fill EVERY field below. Use "论文未提及" if the paper does not provide the information.

### Study Design
| # | Field | Extraction Rule |
|---|-------|----------------|
| 1 | 研究类型 | RCT / cohort (prospective/retrospective) / case-control / cross-sectional / case report / review / meta-analysis / systematic review |
| 2 | 样本量 | Total N + per-group breakdown + power analysis if reported |
| 3 | 人群 | Inclusion/exclusion criteria, age range, sex ratio, ethnicity, disease stage |

### Intervention & Comparison
| # | Field | Extraction Rule |
|---|-------|----------------|
| 4 | 干预措施 | Drug name + dose + route + frequency + duration, or surgical procedure details |
| 5 | 对照 | Placebo / active control (name) / historical control / usual care / dose-comparison |

### Outcomes & Statistics
| # | Field | Extraction Rule |
|---|-------|----------------|
| 6 | 主要终点 | Primary endpoint + measurement time point + assessment method |
| 7 | 统计方法 | Specific tests (t-test, chi-square, Cox regression, Kaplan-Meier, logistic regression, mixed model, etc.) + software |
| 8 | 效应量 | HR / OR / RR / MD / SMD + 95% CI + exact P-value |

### Safety & Quality
| # | Field | Extraction Rule |
|---|-------|----------------|
| 9 | 不良事件 | Specific AEs + incidence rate per group + severity grading + discontinuation rate |
| 10 | 报告规范 | CONSORT / STROBE / PRISMA / CARE / STARD compliance — check against checklist |
| 11 | 证据等级 | GRADE assessment: High / Moderate / Low / Very Low + reasoning |

### Clinical Relevance
| # | Field | Extraction Rule |
|---|-------|----------------|
| 12 | 临床意义 | NNT (Number Needed to Treat) / MCID (Minimum Clinically Important Difference) achieved? Absolute risk reduction? |

---

## Special Attention Points for Medical Papers
- Randomization method: truly random or quasi-random?
- Blinding: double-blind / single-blind / open-label
- Allocation concealment: adequate or not?
- ITT (intention-to-treat) vs per-protocol analysis
- Follow-up rate: >80%? Loss to follow-up reasons?
- Conflict of interest and funding source
- External validity: can results be generalized to user's population of interest?
- Subgroup analyses: pre-specified or post-hoc?
- For meta-analyses: heterogeneity (I²), publication bias assessment

## Relevance Assessment
Consider user's medical background when evaluating:
- Does this study address a condition relevant to user's clinical/research interests?
- Is the intervention feasible in user's setting?
- Are the results practice-changing or confirmatory?
