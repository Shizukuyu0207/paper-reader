# Domain: AI/ML (人工智能与机器学习)

## Domain ID: `ai`
## Archive Dir: `~/obsidian/papers/ai-ml/`

---

## Extraction Checklist

When analyzing an AI/ML paper, extract and fill EVERY field below. Use "论文未提及" if the paper does not provide the information.

### Task & Architecture
| # | Field | Extraction Rule |
|---|-------|----------------|
| 1 | 任务类型 | Classification / Detection / Segmentation / Generation / RL / NLP / Representation Learning / Multi-modal / Other |
| 2 | 模型架构 | Specific network architecture + key innovation (e.g. "Transformer with rotary position encoding", "U-Net with attention gates") |

### Data & Training
| # | Field | Extraction Rule |
|---|-------|----------------|
| 3 | 预训练数据 | Pre-training dataset name + scale + source (if applicable) |
| 4 | 训练数据 | Training/finetuning dataset name + scale + split ratio + data augmentation |
| 5 | 超参数 | Learning rate + schedule / batch size / epochs / optimizer / key regularization (dropout, weight decay) |

### Evaluation
| # | Field | Extraction Rule |
|---|-------|----------------|
| 6 | Benchmark | Evaluation dataset + metrics + compared methods (list all baselines) |
| 7 | SOTA对比 | Whether SOTA surpassed, specific metric values before and after |
| 8 | 评估指标 | Specific metrics + values (Accuracy, F1, AUC, BLEU, etc.) |
| 9 | 消融实验 | Which ablations performed, key findings (what component matters most) |

### Resources & Reproducibility
| # | Field | Extraction Rule |
|---|-------|----------------|
| 10 | 计算资源 | GPU type + count + training time + memory usage + inference speed |
| 11 | 可复现性 | Code open-source (link) / model weights available / data available / container provided |

### Assessment
| # | Field | Extraction Rule |
|---|-------|----------------|
| 12 | 局限性 | Author-stated + own assessment: fairness issues, data bias, scalability, generalizability |

---

## Special Attention Points for AI/ML Papers
- Is the improvement over baselines statistically significant?
- Are comparisons fair (same data, same compute budget)?
- Data contamination: train/test overlap?
- Compute cost vs performance gain — is it worth it?
- Ablation completeness: do they ablate ALL key components?
- Evaluation on diverse benchmarks or cherry-picked?
- Scaling behavior: does it work at different scales?
- For LLM papers: prompt engineering impact, evaluation methodology
- Check if the paper's contribution is primarily engineering or scientific

## Relevance Assessment
- Is the method/applicable to user's research areas (molecular simulation, bioinformatics)?
- Can the approach be adapted for the user's specific use cases?
- Is the compute requirement feasible for user's setup (RTX 5060 Laptop 8GB)?
