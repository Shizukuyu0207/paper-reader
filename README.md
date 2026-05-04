<div align="center">

# 📄 Paper Reader

**Academic Paper Analysis for Hermes Agent — MinerU + Jina Reader + Scrapling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](README.md) · [简体中文](docs/README.zh-CN.md) · [繁體中文](docs/README.zh-TW.md) · [日本語](docs/README.ja.md) · [Español](docs/README.es.md) · [Русский](docs/README.ru.md)

</div>

---

## ✨ Overview

An [Hermes Agent](https://github.com/henvic/hermes) skill that reads, analyzes, and archives academic papers (PDF) with intelligent domain detection and structured Obsidian vault integration.

Whether you're scanning a single arXiv preprint or processing a batch of 10+ papers from different publishers, Paper Reader handles content acquisition, domain classification, deep analysis, and archiving — all automatically.

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| 🧠 **Auto Domain Detection** | Classifies papers into 5 domains: Molecular Dynamics, Medicine, AI/ML, Bioinformatics, Programming |
| 📊 **3 Reading Modes** | Quick Scan (3 min) · Deep Read (full analysis) · Q&A (interactive) |
| ⚡ **3-Tier Content Acquisition** | Jina Reader → Scrapling stealth browser → web_search fallback |
| 📝 **Obsidian Archive** | YAML frontmatter + structured markdown notes in your vault |
| 🔍 **Vision Analysis** | AI-powered figure descriptions and analysis |
| 📦 **Batch Processing** | Parallel fetching + parallel analysis for Paper Alerts |

## 🔗 Content Acquisition — 3-Tier Strategy

This is the core pipeline that actually gets paper content. No magic — just layered fallbacks with honest trade-offs.

```
URL Input → Tier 1: Jina Reader (r.jina.ai) → Full Markdown text? → Done ✅
                                              → Partial/Timeout? → Tier 2 ↓
           → Tier 2: Scrapling StealthyFetcher → Full HTML? → Done ✅
                                                → Failed? → Tier 3 ↓
           → Tier 3: web_search → Metadata + abstract → Mark as partial ⚠️
```

### What Each Tier Does

| Tier | Tool | Speed | Output | Best For |
|------|------|-------|--------|----------|
| **1** | [Jina Reader](https://github.com/jina-ai/reader) | 1-2s | Clean Markdown | arXiv, bioRxiv, open-access, most Nature articles |
| **2** | [Scrapling](https://github.com/D4Vinci/Scrapling) + Camoufox | 5-15s | Raw HTML text | Tier 1 fails, Nature/Elsevier partial content |
| **3** | web_search | 2-5s | Metadata only | Hard paywalls (Cell, NEJM, Lancet) |

### Benchmarked Performance (real data, May 2026)

| Source | Tier Used | Result | Time | Content |
|--------|-----------|--------|------|---------|
| arXiv PDF | Tier 1 | ✅ Full text | 0.8s | All sections |
| bioRxiv PDF | Tier 1 | ✅ Full text | 0.8s | All sections |
| Nature Biotechnology | Tier 1 | ✅ Full text | 1.0s | 117K chars, all sections |
| Nature Machine Intelligence | Tier 1 → 2 | ✅ Full text | 6.3s | Jina partial → Scrapling complete |
| Nature Reviews Drug Discovery | Tier 1 → 2 | ✅ Full text | 6.8s | 149K chars combined |
| Elsevier/ScienceDirect | Tier 3 | ⚠️ Metadata | 3s | Abstract + citation only |
| Cell / NEJM / Lancet | Tier 3 | ⚠️ Metadata | 3s | Abstract + citation only |

## 📖 Reading Modes

### 🔍 Quick Scan
3-minute overview to decide if a paper is worth deep reading. Extracts title, abstract, key findings, and significance. No archive created.

### 📖 Deep Read
Full structured analysis with domain-specific checklists. Generates a comprehensive Obsidian archive note with YAML frontmatter, methods breakdown, quantitative results, limitations, and research implications.

### 💬 Q&A Mode
Interactive question-answering session. Ask anything about the paper's content, figures, or methodology. Optionally saves a Q&A log.

### 📦 Batch Mode (Paper Alert)
Process multiple papers simultaneously. The 3-tier acquisition runs in parallel, then analysis runs in parallel:
- **Open-access papers** → Tier 1 Jina Reader (full text, <2s each)
- **Nature/Springer** → Tier 1+2 combined (full text, ~7s each)
- **Hard paywalls** → Tier 3 web_search (metadata, ~3s each)
- **GitHub repos** → README analysis
- **Local PDF files** → MinerU extraction

## 🗂️ Domain Checklists

| Domain | Key Analysis Points |
|--------|-------------------|
| 🧬 **Molecular Dynamics** | Force fields, simulation parameters, RMSD/RMSF, free energy methods, trajectory analysis |
| 🏥 **Medicine** | Study design, cohort info, statistical methods, clinical outcomes, hazard ratios |
| 🤖 **AI / ML** | Architecture details, training data, benchmarks, SOTA comparisons, compute requirements |
| 🔬 **Bioinformatics** | Pipeline tools, statistical tests, genome assembly, differential expression, enrichment analysis |
| 💻 **Programming** | Algorithm complexity, system design, implementation details, performance benchmarks |

## ⚠️ Honest Limitations

This tool is useful but **not omnipotent**. Here's what it can and cannot do:

### Content Acquisition — What We Cannot Break

| Scenario | Reality | Workaround |
|----------|---------|------------|
| **Hard paywalls** (Cell, NEJM, Lancet, JAMA) | These require institutional login or personal subscription. No scraping tool bypasses authenticated access — and none should. | Use your university/institute VPN or library access. Provide the downloaded PDF as a local file. |
| **Authenticated access** (institutional SSO, Shibboleth) | Logging into your university portal is outside the scope of a skill. We cannot and should not automate credential-based access. | Download the PDF manually through your institution, then feed it to Paper Reader as a local file. |
| **Freshly published papers** | Some papers take days/weeks before being indexed by search engines or mirrored on preprint servers. | Wait for preprint availability, or access through your institution. |
| **Supplementary materials** | Supplementary PDFs, datasets, and code are often hosted separately and may not be captured. | Provide supplementary files separately. |
| **Non-English papers** | MinerU supports Chinese (`-l ch`) and several other languages, but Jina Reader and web_search work best with English content. | Use local PDF + MinerU with appropriate language flag. |

### Analysis Quality — What You Should Know

| Aspect | Reality |
|--------|---------|
| **Tier 3 (metadata-only) papers** | Archive notes will lack detailed methods, quantitative results, and figure descriptions. They are marked clearly. |
| **Figure analysis** | Depends on your AI model's vision capability. Some models (e.g., text-only LLMs) cannot analyze figures. The skill falls back to image captions from extraction. |
| **Domain detection** | Keyword-based. Interdisciplinary papers (e.g., AI + medicine) may be classified into either domain. You can override the detection. |
| **Archive quality ≠ reading the paper yourself** | The skill produces structured summaries, not replacements for reading. Critical papers should still be read in full. |

### Legal & Ethical Considerations

- **Open-access papers** (arXiv, bioRxiv, PLOS, etc.): Fetching is explicitly permitted by publishers.
- **Nature/Springer Nature**: HTML content is publicly accessible (no login required). Jina Reader and Scrapling fetch what any browser can see.
- **Paywalled content**: When Tier 1/2 cannot access full text, we do **not** attempt to bypass authentication or circumvent paywalls. We fall back to publicly available metadata (title, abstract, authors, DOI).
- **Rate limiting**: Jina Reader free tier is 20 RPM. Scrapling requests are throttled. We do not hammer publisher servers.
- **TL;DR**: We fetch what's publicly visible in a browser. If you need to log in to see it, you should log in yourself.

## 🚀 Installation

### Option 1: Git Clone (Recommended)

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### Option 2: The "Lazy Researcher" Method

Don't want to touch the terminal? Just throw this repo URL at your Hermes Agent and paste this:

```
安装这个 skill：https://github.com/Shizukuyu0207/paper-reader

把它 clone 到 ~/.hermes/skills/paper-reader/，
确保 MinerU 已安装（which mineru），如果没有就跳过这一步提醒我。
clone 完成后告诉我安装好了，顺便介绍一下它能干什么。
```

Your agent will handle the rest. You're welcome. 🍵

### Option 3: Manual

Download this repo as ZIP, extract to `~/.hermes/skills/paper-reader/`.

### Prerequisites

| Dependency | Required | Install |
|-----------|----------|---------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ Yes | See Hermes docs |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ Yes | `pip install mineru` or see their README |
| [Jina Reader](https://github.com/jina-ai/reader) | Built-in | Uses `r.jina.ai` API, no install needed |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | Recommended | `pip install scrapling` + `pip install camoufox && python -m camoufox fetch` |
| Obsidian | Optional | For archive notes |

## 📋 Quick Start

```bash
# 1. Install
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git

# 2. Verify
ls paper-reader/SKILL.md  # should exist

# 3. Use (in Hermes chat)
```

Then in your Hermes conversation:

```
read this paper https://arxiv.org/abs/2604.18559
```

That's it. The skill will auto-detect domain, ask for mode, and do the rest.

## 📁 Directory Structure

```
paper-reader/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file (English)
├── LICENSE                           # MIT License
├── scripts/
│   ├── extract.sh                    # MinerU extraction helper
│   └── fetch_paper.py                # Unified 3-tier content acquisition
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
| `JINA_READER` | `https://r.jina.ai` | Jina Reader API endpoint |
| `EXTRACT_SCRIPT` | `scripts/extract.sh` | Extraction helper script |

## 🤝 Contributing

Found a bug? Have a domain checklist to add? PRs welcome.

1. Fork this repo
2. Create your branch (`git checkout -b feature/my-feature`)
3. Commit (`git commit -m 'Add my feature'`)
4. Push (`git push origin feature/my-feature`)
5. Open a Pull Request

## 📄 License

MIT License — see [LICENSE](LICENSE).

## 🙏 Acknowledgments

- [MinerU](https://github.com/opendatalab/MinerU) — PDF extraction engine
- [Jina Reader](https://github.com/jina-ai/reader) — URL-to-Markdown conversion
- [Scrapling](https://github.com/D4Vinci/Scrapling) — Stealth web fetching with Camoufox
- [Hermes Agent](https://github.com/henvic/hermes) — Agent framework
- Every researcher who has 50 tabs of unread papers open right now

<div align="center">
Made with ❤️ for researchers who read too many papers
</div>
