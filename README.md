<div align="center">

# 📄 Paper Reader

**Academic Paper Analysis — Agent-Agnostic Pipeline**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](README.md) · [简体中文](docs/README.zh-CN.md) · [繁體中文](docs/README.zh-TW.md) · [日本語](docs/README.ja.md) · [Español](docs/README.es.md) · [Русский](docs/README.ru.md)

</div>

---

## ✨ Overview

Paper Reader reads, analyzes, and archives academic papers with intelligent domain detection and structured Obsidian vault integration.

Give it a URL, a PDF path, or a batch of 10+ papers — it handles content acquisition, domain classification, deep analysis, and archiving automatically.

Designed as a pipeline that works with **any AI agent** (Hermes, Claude Code, Codex, OpenCode, etc.). Adapter files included in `adapters/`.

---

## 🏗️ Architecture

5-stage pipeline with 3-tier content acquisition. Each stage is modular and independently configurable.

```
┌──────────────────────────────────────────────────────────────────┐
│                        Paper Reader Pipeline                      │
│                                                                    │
│  ┌─────────┐   ┌──────────┐   ┌──────────┐   ┌────────┐   ┌──────┐  │
│  │ Stage 1 │──▶│ Stage 2  │──▶│ Stage 3  │──▶│ Stage 4│──▶│Stage5│  │
│  │  Fetch  │   │  Detect  │   │  Select  │   │Execute │   │Output│  │
│  └─────────┘   └──────────┘   └──────────┘   └────────┘   └──────┘  │
│       │                                              │              │
│  ┌────┴──────────────────────────┐          ┌───────┴───────┐      │
│  │ 3-Tier Content Acquisition   │          │  Domain       │      │
│  │ ① Jina Reader  (1-2s)       │          │  Checklists   │      │
│  │ ② Scrapling     (5-15s)     │          │  · MD / Med   │      │
│  │ ③ web_search    (2-5s)      │          │  · AI / Bio   │      │
│  └──────────────────────────────┘          │  · Programming│      │
│                                             └───────────────┘      │
└──────────────────────────────────────────────────────────────────┘
```

### Stage 1: Input Parse & Fetch

| Priority | Tool | Speed | Output | Covers |
|----------|------|-------|--------|--------|
| **Tier 1** | [Jina Reader](https://github.com/jina-ai/reader) (`r.jina.ai`) | 1-2s | Clean Markdown | arXiv, bioRxiv, open-access, most Nature articles |
| **Tier 2** | [Scrapling](https://github.com/D4Vinci/Scrapling) + Camoufox | 5-15s | Raw HTML text | Nature/Elsevier when Tier 1 is partial |
| **Tier 3** | web_search | 2-5s | Metadata only | Hard paywalls (Cell, NEJM, Lancet) |
| **Local** | [MinerU](https://github.com/opendatalab/MinerU) | ~2min/40p | Markdown + images | Local PDF files, full extraction |

### Stage 2: Domain Detection

| Domain | ID | Example Keywords |
|--------|----|------------------|
| Molecular Dynamics | `md` | force field, AMBER, GROMACS, RMSD, free energy, simulation |
| Medicine | `med` | clinical trial, RCT, cohort, hazard ratio, prognosis |
| AI / ML | `ai` | transformer, deep learning, benchmark, SOTA, training |
| Bioinformatics | `bio` | RNA-seq, GWAS, genome, differential expression, enrichment |
| Programming | `prog` | compiler, algorithm, system design, database, runtime |

### Stage 3: Mode Selection

| Mode | Purpose | Output |
|------|---------|--------|
| 🔍 **Quick Scan** | 3-min screening: worth reading? | Conversation only |
| 📖 **Deep Read** | Full structured analysis | Obsidian archive note |
| 💬 **Q&A** | Interactive paper Q&A | Conversation + optional log |
| 📦 **Batch** | Process N papers in parallel | Archive notes + summary table |

### Stage 5: Output & Archive

Archives to `~/obsidian/papers/{domain}/` with structured YAML frontmatter and sections: 基本信息 · 研究问题 · 方法 · 核心结果 · 局限性 · 研究启示 · 引用网络

---

## 📊 Case Study: 9-Paper Batch (May 2026)

A real Paper Alert processed end-to-end. Honest breakdown.

### Acquisition Results

| # | Paper | Source | Method | Time | Content Quality |
|---|-------|--------|--------|------|----------------|
| 1 | Allosteric Switches (Baker) | Nature NBT | MinerU (PDF) | 93s | ★★★★★ Full text, 494 lines, 36 figures |
| 2 | ConforNets (AlQuraishi) | arXiv PDF | MinerU (PDF) | 118s | ★★★★★ Full text, 646 lines, 75 figures |
| 3 | Closing the Loop | ScienceDirect | web_search | ~5s | ★★☆☆☆ Metadata + abstract only |
| 4 | trRosettaRNA2 | Nature NMI | web_search | ~5s | ★★☆☆☆ Metadata + abstract only |
| 5 | Target ID in AI Era | Nature NRDD | web_search | ~5s | ★★★☆☆ Rich metadata (review article) |
| 6 | ERAST | Nature NBT | web_search | ~5s | ★★☆☆☆ Metadata only |
| 7 | AlphaFast | bioRxiv | web_search | ~5s | ★★☆☆☆ Metadata only |
| 8 | Flow Matching | Nature NMI | web_search | ~5s | ★★☆☆☆ Metadata only |
| 9 | lightning-boltz | GitHub | README scan | ~3s | ★★☆☆☆ Repo info only |

**Total time**: ~6 minutes

### Post-Hoc: Jina Reader + Scrapling Integration

| Paper | Previous | With Jina Reader | Improvement |
|-------|----------|-----------------|------------|
| Allosteric Switches | MinerU 93s | **1.0s, 117K chars** | 93× faster |
| Target ID (NRDD) | web_search metadata | **1.3s, 149K chars** | Metadata → **full text** |
| ERAST (NBT) | web_search metadata | **1.0s, full text** | Metadata → **full text** |

### Objective Assessment

✅ **Worked well**: Full-text papers → 100+ line archive notes with quantitative results. 9 papers in 6 min. All domains correctly classified.

⚠️ **Suboptimal**: Paywalled papers (pre-Jina) → 34-53 line metadata-only notes. MinerU serial bottleneck.

❌ **Remaining gap**: ScienceDirect/Elsevier still Tier 3. arXiv abstract URLs need `pdf/` for full text.

---

## ⚠️ Honest Limitations

### What We Cannot Break

| Scenario | Reality | Workaround |
|----------|---------|------------|
| **Hard paywalls** (Cell, NEJM, Lancet, JAMA) | Require institutional login. | Use VPN, download PDF manually. |
| **Authenticated access** (SSO, Shibboleth) | Outside scope. | Download PDF through your institution. |
| **Freshly published** | Days/weeks before indexed. | Wait for preprint. |
| **Non-English** | MinerU supports Chinese (`-l ch`) etc. | Use local PDF + MinerU. |

### What You Should Know

- **Tier 3 papers** — Archive notes lack methods detail and quantitative results.
- **Figure analysis** — Depends on model vision capability. Falls back to captions.
- **Archive ≠ reading the paper** — Structured summaries, not replacements.

### Legal & Ethical Stance

We fetch what's publicly visible in a browser. If you need to log in to see it — you should log in yourself. No bypassing authentication.

---

## 🚀 Installation

### Option 1: npx (Recommended)

```bash
npx skills add nowa277/paper-reader -g -y
```

One command. Works with Claude Code, Hermes, Cursor, and any agent that supports the [skills convention](https://github.com/anthropics/skills).

### Option 2: npm

```bash
npm install paper-reader
```

### Option 3: Git Clone

```bash
git clone https://github.com/nowa277/paper-reader.git
cp -r paper-reader ~/.hermes/skills/
```

### Prerequisites

| Dependency | Required | Install |
|-----------|----------|---------|
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ | `pip install mineru` |
| [Jina Reader](https://github.com/jina-ai/reader) | Built-in | `r.jina.ai` API, no install needed |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | Recommended | `pip install scrapling camoufox && python -m camoufox fetch` |
| Obsidian | Optional | For archive notes |

---

## 📋 Quick Start

```
# Single paper
read this paper https://arxiv.org/abs/2604.18559

# Batch
Paper Alert:
1. ConforNets https://arxiv.org/abs/2604.18559
2. Allosteric Switches https://www.nature.com/articles/s41587-026-03081-9
3. Target ID https://doi.org/10.1038/s41573-026-01412-8
```

---

## 📁 Project Structure

```
paper-reader/
├── SKILL.md                          # Main skill definition (5-stage pipeline)
├── README.md                         # This file
├── LICENSE                           # MIT
├── adapters/                         # Agent-specific config files
├── scripts/
│   ├── extract.sh                    # MinerU extraction wrapper
│   └── fetch_paper.py                # Unified 3-tier content acquisition
├── references/
│   ├── archive-template.md           # Obsidian note YAML + section template
│   ├── domain-{ai,md,med,bio,prog}.md  # Domain analysis checklists
│   ├── mode-{scan,deep,qa,batch}.md  # Mode execution instructions
│   └── mineru-quirks.md              # MinerU known issues
└── docs/                             # 6-language READMEs
```

---

## 📝 Archive Output Example

```yaml
---
title: "Artificial allosteric protein switches with ML-designed receptors"
authors: ["Zhong Guo", "David Baker"]
year: 2026
journal: "Nature Biotechnology"
doi: "10.1038/s41587-026-03081-9"
domain: "ai"
tags: [paper/ai, allosteric-switch, biosensor, protein-design]
date_read: "2026-05-04"
rating: "5"
---

# Artificial allosteric protein switches with ML-designed receptors

## 基本信息
## 研究问题与动机
## 方法                    # Core architecture, ML design, experimental validation
## 核心结果                # Kd = 0.9 μM, 400-fold dynamic range, etc.
## 关键创新
## 局限性                  # Author-stated + independent assessment
## 研究启示
## 引用网络
```

---

## ⚙️ Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `MINERU` | MinerU binary path | MinerU executable |
| `WORK_BASE` | `/tmp/paper-reader` | Temporary working directory |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian vault archive root |
| `JINA_READER` | `https://r.jina.ai` | Jina Reader API endpoint |

---

## 🤝 Contributing

PRs welcome — especially new agent adapters (Cursor, Aider, Continue, etc.).

## 📄 License

MIT License — see [LICENSE](LICENSE).

## 🙏 Acknowledgments

- [MinerU](https://github.com/opendatalab/MinerU) — PDF extraction
- [Jina Reader](https://github.com/jina-ai/reader) — URL-to-Markdown
- [Scrapling](https://github.com/D4Vinci/Scrapling) — Stealth web fetching
- Every researcher who has 50 tabs of unread papers open right now

<div align="center">
Made with ❤️ for researchers who read too many papers
</div>
