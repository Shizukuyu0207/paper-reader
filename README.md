# 📄 Paper Reader — Hermes Skill

> MinerU-powered academic paper analysis with domain-aware deep reading and Obsidian archiving.

## What It Does

An [Hermes Agent](https://github.com/henvic/hermes) skill that reads, analyzes, and archives academic papers (PDF). Auto-detects domain (Molecular Dynamics / Medicine / AI-ML / Bioinformatics / Programming) and offers three reading modes.

### Three Modes

| Mode | Purpose | Output |
|------|---------|--------|
| 🔍 **Quick Scan** | 3-min overview, decide if worth deep reading | Conversation only |
| 📖 **Deep Read** | Full structured analysis + Obsidian archive note | Markdown archive |
| 💬 **Q&A** | Interactive question-answering on paper content | Conversation + optional log |

### Batch Mode

Process multiple papers in parallel (Paper Alert). Handles mixed sources:
- **arXiv PDFs**: Direct download + MinerU extraction
- **Paywalled papers** (Nature, Elsevier, bioRxiv): web_search fallback for abstracts/metadata
- **GitHub repos**: README analysis

## Features

- **MinerU Extraction**: High-quality PDF→Markdown with figure extraction
- **Domain Detection**: Auto-classify into 5 domains with keyword matching
- **Domain Checklists**: Specialized analysis criteria per domain (MD force fields, AI architectures, clinical trial design, etc.)
- **Obsidian Archive**: Structured YAML frontmatter + markdown notes in your vault
- **Vision Analysis**: Key figure descriptions via AI vision
- **Batch Processing**: Parallel download + serial MinerU + parallel analysis

## Prerequisites

- [MinerU](https://github.com/opendatalab/MinerU) (PDF extraction engine)
- [Hermes Agent](https://github.com/henvic/hermes) (host agent framework)
- Obsidian vault (optional, for archive notes)

## Installation

```bash
# Clone into your Hermes skills directory
cd ~/.hermes/skills/
git clone https://github.com/YOUR_USERNAME/paper-reader.git
```

Or manually copy the `paper-reader/` directory to `~/.hermes/skills/paper-reader/`.

## Directory Structure

```
paper-reader/
├── SKILL.md                          # Main skill definition
├── README.md                         # This file
├── LICENSE                           # MIT License
├── scripts/
│   └── extract.sh                    # MinerU extraction helper script
└── references/
    ├── archive-template.md           # Obsidian note template
    ├── domain-ai-ml.md               # AI/ML domain checklist
    ├── domain-bioinformatics.md      # Bioinformatics domain checklist
    ├── domain-medicine.md            # Medicine domain checklist
    ├── domain-molecular-dynamics.md  # MD simulation domain checklist
    ├── domain-programming.md         # Programming domain checklist
    ├── mineru-quirks.md              # MinerU known issues & workarounds
    ├── mode-batch.md                 # Batch processing instructions
    ├── mode-deep.md                  # Deep read mode instructions
    ├── mode-qa.md                    # Q&A mode instructions
    └── mode-scan.md                  # Quick scan mode instructions
```

## Usage

In Hermes, simply mention papers:

```
# Single paper
读论文 /path/to/paper.pdf
read this paper https://arxiv.org/abs/2604.18559

# Batch (Paper Alert)
Paper Alert:
1. Title1 https://arxiv.org/abs/XXXX.XXXXX
2. Title2 https://doi.org/10.1038/...
```

The skill will:
1. Fetch/verify the PDF
2. Detect domain automatically
3. Ask which mode you want
4. Execute analysis and (optionally) archive

## Archive Output Example

Notes are saved to `~/obsidian/papers/{domain}/` with YAML frontmatter:

```markdown
---
title: "Paper Title"
authors: ["Author1", "Author2"]
year: 2026
journal: "Nature Biotechnology"
doi: "10.1038/s41587-026-03081-9"
domain: "ai"
tags: [paper/ai, protein-design, biosensor]
rating: "5"
---
# Paper Title
## 基本信息
## 方法
## 核心结果
## 局限性
## 对本研究的启示
```

## Configuration

Set in SKILL.md environment section:

| Variable | Default | Description |
|----------|---------|-------------|
| `MINERU` | MinerU binary path | Path to MinerU executable |
| `WORK_BASE` | `/tmp/paper-reader` | Temporary working directory |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian archive root |
| `EXTRACT_SCRIPT` | `scripts/extract.sh` | Extraction helper script |

## License

MIT License — see [LICENSE](LICENSE).

## Acknowledgments

- [MinerU](https://github.com/opendatalab/MinerU) — PDF extraction engine
- [Hermes Agent](https://github.com/henvic/hermes) — Agent framework
- Built for researchers in molecular dynamics, medicine, AI, and bioinformatics
