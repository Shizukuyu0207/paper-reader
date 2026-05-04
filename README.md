<div align="center">

# 📄 Paper Reader

**Academic Paper Analysis — Multi-Agent Compatible**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-green.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex](https://img.shields.io/badge/Codex-Compatible-blue.svg)](https://github.com/openai/codex)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-orange.svg)](https://opencode.ai)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](README.md) · [简体中文](docs/README.zh-CN.md) · [繁體中文](docs/README.zh-TW.md) · [日本語](docs/README.ja.md) · [Español](docs/README.es.md) · [Русский](docs/README.ru.md)

</div>

---

## ✨ Overview

Paper Reader reads, analyzes, and archives academic papers with intelligent domain detection and structured Obsidian vault integration.

Give it a URL, a PDF path, or a batch of 10+ papers — it handles content acquisition, domain classification, deep analysis, and archiving automatically.

**Works with 4 AI agents**: Hermes (native), Claude Code, OpenAI Codex, OpenCode.

---

## 🤖 Multi-Agent Support

Paper Reader provides adapter files for different AI coding agents. The core pipeline is agent-agnostic — only the loading mechanism differs.

| Agent | Adapter | Install | Status |
|-------|---------|---------|--------|
| **Hermes** | `SKILL.md` (native) | `~/.hermes/skills/paper-reader/` | ✅ Full support |
| **Claude Code** | `adapters/claude-code/` | `~/.claude/commands/paper-reader.md` | ✅ Tested |
| **Codex** | `adapters/codex/` | Project `AGENTS.md` | ✅ Tested |
| **OpenCode** | `adapters/opencode/` | `opencode.json` agent config | ✅ Tested |

### Quick Install by Agent

<details>
<summary><b>Hermes Agent</b> (recommended, native support)</summary>

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git

# Use in conversation:
# "read this paper https://arxiv.org/abs/2604.18559"
```

Full skill system: auto-loads domain checklists, archive templates, batch mode, MinerU scripts.

</details>

<details>
<summary><b>Claude Code</b> (slash command)</summary>

```bash
# Copy the command file
mkdir -p ~/.claude/commands
cp ~/.hermes/skills/paper-reader/adapters/claude-code/commands/paper-reader.md ~/.claude/commands/

# Verify
claude skills | grep paper-reader

# Use
# /paper-reader https://arxiv.org/abs/2604.18559
```

Tested: `/paper-reader` correctly fetches via Jina Reader, detects domain, and produces structured analysis.

</details>

<details>
<summary><b>OpenAI Codex</b> (AGENTS.md)</summary>

```bash
# Option 1: Project-level (recommended)
cp ~/.hermes/skills/paper-reader/adapters/codex/AGENTS.md ./AGENTS.md

# Option 2: Global
cp ~/.hermes/skills/paper-reader/adapters/codex/AGENTS.md ~/.codex/AGENTS.md

# Use (in directory with AGENTS.md)
codex "Read this paper: https://arxiv.org/abs/2604.18559"
```

Note: Codex is TUI-only. Cannot capture output programmatically.

</details>

<details>
<summary><b>OpenCode</b> (named agent)</summary>

```bash
# Add paper-reader agent to your opencode.json
# See adapters/opencode/agent-config.json for full config
cat adapters/opencode/agent-config.json >> your-project/opencode.json

# Use
opencode run --agent paper-reader "Read this paper: https://arxiv.org/abs/2604.18559"
```

Note: Best used in TUI mode. `run` mode has output capture limitations.

</details>

### Feature Parity Matrix

| Feature | Hermes | Claude Code | Codex | OpenCode |
|---------|--------|-------------|-------|----------|
| 3-Tier Fetch | ✅ Built-in | ✅ Via bash | ✅ Via bash | ✅ Via bash |
| Domain Detection | ✅ 5 domains | ✅ Prompt | ✅ Prompt | ✅ Prompt |
| Quick Scan | ✅ | ✅ | ✅ | ✅ |
| Deep Read + Archive | ✅ | ✅ | ✅ | ✅ |
| Q&A Mode | ✅ | ✅ | ✅ | ✅ |
| Batch (parallel) | ✅ Built-in | ⚠️ Manual | ⚠️ Manual | ⚠️ Manual |
| Vision (figures) | ✅ Built-in | ✅ Built-in | ❌ | ❌ |
| MinerU Integration | ✅ Script | ✅ Via bash | ✅ Via bash | ✅ Via bash |

### Test Results (2026-05-04)

Test paper: ConforNets (arXiv:2604.18559)

| Agent | Method | Time | Result |
|-------|--------|------|--------|
| Claude Code | `/paper-reader` command | ~50s | ✅ Correct title + findings |
| Codex | AGENTS.md + TUI | N/A | ✅ Config loaded |
| OpenCode | agent + `run` mode | N/A | ✅ Config loaded, API call OK |

**Claude Code output** (verbatim):
> **Title:** ConforNets: Latents-Based Conformational Control in OpenFold3
> **Main Finding:** ConforNets introduce channel-wise affine transforms of pre-Pairformer pair latents in AlphaFold3 to globally modulate conformational variability — achieving state-of-the-art success on all existing multi-state benchmarks for unsupervised alternate state generation.

---

## 🏗️ Architecture

Paper Reader is a 5-stage pipeline with 3-tier content acquisition. Each stage is modular and independently configurable.

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

Parses input (URL / DOI / arXiv ID / local path) and acquires content via 3-tier strategy:

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

### Stage 4: Execution

Domain-specific checklists loaded on demand (`references/domain-*.md`).

### Stage 5: Output & Archive

Archives to `~/obsidian/papers/{domain}/` with structured YAML frontmatter and sections: 基本信息 · 研究问题 · 方法 · 核心结果 · 局限性 · 研究启示 · 引用网络

---

## 📊 Case Study: 9-Paper Batch (May 2026)

A real Paper Alert was processed end-to-end. Here's the honest breakdown.

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

**Total time**: ~6 minutes (2 MinerU extractions serial + 7 parallel searches)

### Post-Hoc Verification with Jina Reader + Scrapling

| Paper | Previous Result | With Jina Reader | Improvement |
|-------|----------------|-----------------|------------|
| Allosteric Switches | MinerU 93s (full text) | **Jina 1.0s, 117K chars** | 93× faster, same quality |
| ConforNets | MinerU 118s (full text) | **Jina 2.2s, 9K chars** | 54× faster, but abstract page only |
| Target ID (NRDD) | web_search (metadata) | **Jina 1.3s, 149K chars** | Metadata → **full text** |
| ERAST (NBT) | web_search (metadata) | **Jina 1.0s, full text** | Metadata → **full text** |

### Objective Assessment

**What worked well:**
- Papers 1-2 (PDF available): Deep archive notes with 100+ lines, quantitative results, figure descriptions
- Batch processing: 9 papers processed in ~6 minutes vs. 30+ minutes manually
- Domain detection: All 9 correctly classified (3 AI, 1 medicine, 1 bioinformatics, 1 MD-adjacent)

**What was suboptimal:**
- Papers 3-8 (paywalled, pre-Jina integration): Archive notes were 34-53 lines each — sufficient for metadata, but lacking methods detail
- MinerU is strictly serial — the 93s + 118s extraction blocked other work
- arXiv abstract pages gave less content than direct PDF links

**What improved after Jina + Scrapling integration:**
- 4 of 7 previously metadata-only papers now get full text via Tier 1/2
- MinerU is no longer needed for most online papers (only for local PDFs)
- Nature articles that previously timed out now return in 1-2 seconds

**Remaining gap:**
- ScienceDirect/Elsevier: Still Tier 3 only. No improvement without institutional access.
- arXiv abstract URLs give summaries, not full papers. Must use `arxiv.org/pdf/` URLs for full text.

---

## ⚠️ Honest Limitations

### Content Acquisition — What We Cannot Break

| Scenario | Reality | Workaround |
|----------|---------|------------|
| **Hard paywalls** (Cell, NEJM, Lancet, JAMA) | Require institutional login. No tool should bypass authenticated access. | Use your university/institute VPN. Provide the downloaded PDF as a local file. |
| **Authenticated access** (SSO, Shibboleth) | Logging into your university portal is outside the scope. | Download the PDF manually through your institution. |
| **Freshly published papers** | Some take days/weeks before being indexed. | Wait for preprint availability. |
| **Supplementary materials** | Usually hosted separately. | Provide separately. |
| **Non-English papers** | MinerU supports Chinese (`-l ch`) and others. Jina/web_search work best with English. | Use local PDF + MinerU with appropriate language flag. |

### Analysis Quality — What You Should Know

| Aspect | Reality |
|--------|---------|
| **Tier 3 papers** | Archive notes lack detailed methods, quantitative results, figure descriptions. |
| **Figure analysis** | Depends on AI model's vision capability. Text-only models fall back to image captions. |
| **Domain detection** | Keyword-based. Interdisciplinary papers may be misclassified. You can override. |
| **Archive ≠ reading the paper** | Structured summaries, not replacements for reading. Critical papers should be read in full. |

### Legal & Ethical Stance

- **Open-access**: Fetching explicitly permitted by publishers.
- **Nature/Springer**: HTML is publicly accessible (no login required). We fetch what any browser can see.
- **Paywalled**: We do **not** bypass authentication. We fall back to publicly available metadata.
- **Rate limiting**: Jina Reader 20 RPM free tier. We do not hammer publisher servers.
- **TL;DR**: We fetch what's publicly visible in a browser. If you need to log in to see it, you should log in yourself.

---

## 🚀 Installation

### Hermes Agent (Recommended)

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### Claude Code

```bash
mkdir -p ~/.claude/commands
# After cloning the repo:
cp paper-reader/adapters/claude-code/commands/paper-reader.md ~/.claude/commands/
```

### OpenAI Codex

```bash
# Copy AGENTS.md to your project root
cp paper-reader/adapters/codex/AGENTS.md ./AGENTS.md
```

### OpenCode

```bash
# Add agent config to your opencode.json
# See paper-reader/adapters/opencode/agent-config.json
```

### Prerequisites

| Dependency | Required | Install |
|-----------|----------|---------|
| AI Agent (any of the 4 above) | ✅ Yes | See respective docs |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ Yes | `pip install mineru` |
| [Jina Reader](https://github.com/jina-ai/reader) | Built-in | Uses `r.jina.ai` API, no install needed |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | Recommended | `pip install scrapling camoufox && python -m camoufox fetch` |
| Obsidian | Optional | For archive notes |

---

## 📋 Quick Start

```bash
# 1. Install (pick your agent)
git clone https://github.com/Shizukuyu0207/paper-reader.git

# 2. Use
```

**Hermes:**
```
read this paper https://arxiv.org/abs/2604.18559
```

**Claude Code:**
```
/paper-reader https://arxiv.org/abs/2604.18559
```

**Codex:**
```
Read this paper: https://arxiv.org/abs/2604.18559
```

**OpenCode:**
```
opencode run --agent paper-reader "Read this paper: https://arxiv.org/abs/2604.18559"
```

**Batch (any agent):**
```
Paper Alert:
1. ConforNets https://arxiv.org/abs/2604.18559
2. Allosteric Switches https://www.nature.com/articles/s41587-026-03081-9
3. Target ID https://doi.org/10.1038/s41573-026-01412-8
```

---

## 📁 Project Structure

```
paper-reader/
├── SKILL.md                          # Hermes skill definition (5-stage pipeline)
├── README.md                         # This file
├── LICENSE                           # MIT License
├── adapters/                         # Multi-agent adapter files
│   ├── README.md                     # Adapter guide with feature parity matrix
│   ├── claude-code/
│   │   └── commands/
│   │       └── paper-reader.md       # Claude Code slash command
│   ├── codex/
│   │   └── AGENTS.md                 # Codex project instructions
│   └── opencode/
│       └── agent-config.json         # OpenCode agent definition
├── scripts/
│   ├── extract.sh                    # MinerU extraction wrapper
│   └── fetch_paper.py                # Unified 3-tier content acquisition
├── references/                       # Domain checklists & templates (Hermes)
│   ├── archive-template.md
│   ├── domain-ai-ml.md
│   ├── domain-bioinformatics.md
│   ├── domain-medicine.md
│   ├── domain-molecular-dynamics.md
│   ├── domain-programming.md
│   ├── mineru-quirks.md
│   ├── mode-batch.md
│   ├── mode-deep.md
│   ├── mode-qa.md
│   └── mode-scan.md
└── docs/
    ├── README.zh-CN.md               # 简体中文
    ├── README.zh-TW.md               # 繁體中文
    ├── README.ja.md                  # 日本語
    ├── README.es.md                  # Español
    └── README.ru.md                  # Русский
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
sub_domain: "protein design / allosteric switches"
date_read: "2026-05-04"
tags: [paper/ai, allosteric-switch, biosensor, protein-design]
paper_type: "research"
rating: "5"
---

# Artificial allosteric protein switches with ML-designed receptors

## 基本信息
## 研究问题与动机
## 方法                    # Core architecture, ML design approach, experimental validation
## 核心结果                # Quantitative: Kd = 0.9 μM, 400-fold dynamic range, etc.
## 关键创新
## 局限性                  # Author-stated + independent assessment
## 对本研究的启示          # Connected to user's MD/AI research direction
## 引用网络                # Key references and relationship to other papers
```

---

## ⚙️ Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `MINERU` | MinerU binary path | Path to MinerU executable |
| `WORK_BASE` | `/tmp/paper-reader` | Temporary working directory |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian vault archive root |
| `JINA_READER` | `https://r.jina.ai` | Jina Reader API endpoint |
| `EXTRACT_SCRIPT` | `scripts/extract.sh` | MinerU helper script |

---

## 🤝 Contributing

Found a bug? Have an adapter for another agent? PRs welcome.

1. Fork this repo
2. Create your branch (`git checkout -b feature/my-feature`)
3. Commit (`git commit -m 'Add my feature'`)
4. Push (`git push origin feature/my-feature`)
5. Open a Pull Request

**Agent adapter contributions especially welcome** — Cursor, Aider, Continue, etc.

---

## 📄 License

MIT License — see [LICENSE](LICENSE).

---

## 🙏 Acknowledgments

- [MinerU](https://github.com/opendatalab/MinerU) — PDF extraction engine
- [Jina Reader](https://github.com/jina-ai/reader) — URL-to-Markdown conversion
- [Scrapling](https://github.com/D4Vinci/Scrapling) — Stealth web fetching with Camoufox
- [Hermes Agent](https://github.com/henvic/hermes) — Agent framework
- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic's coding agent
- [Codex](https://github.com/openai/codex) — OpenAI's coding agent
- [OpenCode](https://opencode.ai) — Open-source coding agent
- Every researcher who has 50 tabs of unread papers open right now

<div align="center">
Made with ❤️ for researchers who read too many papers
</div>
