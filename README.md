\
<div align="center">

# 📄 Paper Reader

**MinerU-Powered Academic Paper Analysis for Hermes Agent**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](README.md) · [简体中文](docs/README.zh-CN.md) · [繁體中文](docs/README.zh-TW.md) · [日本語](docs/README.ja.md) · [Español](docs/README.es.md) · [Русский](docs/README.ru.md)

</div>

---

## ✨ Overview

An [Hermes Agent](https://github.com/henvic/hermes) skill that reads, analyzes, and archives academic papers (PDF) with intelligent domain detection and structured Obsidian vault integration.

Whether you're scanning a single arXiv preprint or processing a batch of 10+ papers from different publishers, Paper Reader handles PDF extraction, domain classification, deep analysis, and archiving — all automatically.

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| 🧠 **Auto Domain Detection** | Classifies papers into 5 domains: Molecular Dynamics, Medicine, AI/ML, Bioinformatics, Programming |
| 📊 **3 Reading Modes** | Quick Scan (3 min) · Deep Read (full analysis) · Q&A (interactive) |
| ⚡ **Batch Processing** | Parallel download + MinerU extraction + parallel analysis for Paper Alerts |
| 📝 **Obsidian Archive** | YAML frontmatter + structured markdown notes in your vault |
| 🔍 **Vision Analysis** | AI-powered figure descriptions and analysis |
| 🔓 **Paywall Handling** | Graceful fallback to web search for Nature/Elsevier/bioRxiv papers |

## 📖 Reading Modes

### 🔍 Quick Scan
3-minute overview to decide if a paper is worth deep reading. Extracts title, abstract, key findings, and significance. No archive created.

### 📖 Deep Read
Full structured analysis with domain-specific checklists. Generates a comprehensive Obsidian archive note with YAML frontmatter, methods breakdown, quantitative results, limitations, and research implications.

### 💬 Q&A Mode
Interactive question-answering session. Ask anything about the paper's content, figures, or methodology. Optionally saves a Q&A log.

### 📦 Batch Mode (Paper Alert)
Process multiple papers simultaneously. Handles mixed sources:
- **arXiv PDFs** → Direct download + MinerU full extraction
- **Paywalled papers** (Nature, Elsevier, bioRxiv) → web_search metadata fallback
- **GitHub repos** → README analysis

## 🗂️ Domain Checklists

Each domain has specialized analysis criteria:

| Domain | Key Analysis Points |
|--------|-------------------|
| 🧬 **Molecular Dynamics** | Force fields, simulation parameters, RMSD/RMSF, free energy methods, trajectory analysis |
| 🏥 **Medicine** | Study design, cohort info, statistical methods, clinical outcomes, hazard ratios |
| 🤖 **AI / ML** | Architecture details, training data, benchmarks, SOTA comparisons, compute requirements |
| 🔬 **Bioinformatics** | Pipeline tools, statistical tests, genome assembly, differential expression, enrichment analysis |
| 💻 **Programming** | Algorithm complexity, system design, implementation details, performance benchmarks |

## 🚀 Installation

```bash
# Clone into your Hermes skills directory
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

Or manually copy the `paper-reader/` folder to `~/.hermes/skills/paper-reader/`.

### Prerequisites

- [MinerU](https://github.com/opendatalab/MinerU) — PDF extraction engine
- [Hermes Agent](https://github.com/henvic/hermes) — Agent framework
- Obsidian vault (optional, for archive notes)

## 📋 Usage

```
# Single paper — local file
读论文 /path/to/paper.pdf

# Single paper — arXiv
read this paper https://arxiv.org/abs/2604.18559

# Batch — Paper Alert
Paper Alert:
1. Allosteric Switches https://www.nature.com/articles/s41587-026-03081-9
2. ConforNets https://arxiv.org/abs/2604.18559
3. trRosettaRNA2 https://doi.org/10.1038/s42256-026-01223-x
```

The skill will: fetch/verify PDF → detect domain → select mode → analyze → archive

## 📁 Directory Structure

```
paper-reader/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file (English)
├── LICENSE                           # MIT License
├── scripts/
│   └── extract.sh                    # MinerU extraction helper
├── references/
│   ├── archive-template.md           # Obsidian note template
│   ├── domain-ai-ml.md               # AI/ML analysis checklist
│   ├── domain-bioinformatics.md      # Bioinformatics checklist
│   ├── domain-medicine.md            # Medicine checklist
│   ├── domain-molecular-dynamics.md  # MD simulation checklist
│   ├── domain-programming.md         # Programming checklist
│   ├── mineru-quirks.md              # MinerU known issues
│   ├── mode-batch.md                 # Batch mode instructions
│   ├── mode-deep.md                  # Deep read instructions
│   ├── mode-qa.md                    # Q&A mode instructions
│   └── mode-scan.md                  # Quick scan instructions
└── docs/
    ├── README.zh-CN.md               # 简体中文
    ├── README.zh-TW.md               # 繁體中文
    ├── README.ja.md                  # 日本語
    ├── README.es.md                  # Español
    └── README.ru.md                  # Русский
```

## 📝 Archive Output Example

Notes saved to `~/obsidian/papers/{domain}/` with full YAML frontmatter:

```yaml
---
title: "Artificial allosteric protein switches with ML-designed receptors"
authors: ["Zhong Guo", "David Baker"]
year: 2026
journal: "Nature Biotechnology"
doi: "10.1038/s41587-026-03081-9"
domain: "ai"
sub_domain: "protein design / allosteric switches"
date_read: "2026-05-04"
tags: [paper/ai, allosteric-switch, biosensor, protein-design]
paper_type: "research"
rating: "5"
---
```

Followed by structured sections: 基本信息 · 研究问题 · 方法 · 核心结果 · 局限性 · 研究启示 · 引用网络

## ⚙️ Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `MINERU` | MinerU binary path | Path to MinerU executable |
| `WORK_BASE` | `/tmp/paper-reader` | Temporary working directory |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian vault archive root |
| `EXTRACT_SCRIPT` | `scripts/extract.sh` | Extraction helper script |

## 📄 License

MIT License — see [LICENSE](LICENSE).

## 🙏 Acknowledgments

- [MinerU](https://github.com/opendatalab/MinerU) — PDF extraction engine
- [Hermes Agent](https://github.com/henvic/hermes) — Agent framework
- Built for researchers in molecular dynamics, medicine, AI, and bioinformatics

<div align="center">
Made with ❤️ for researchers who read too many papers
</div>
