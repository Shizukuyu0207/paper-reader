---
name: paper-reader
description: "Read and analyze academic papers (PDF). Auto-detect domain (MD/medicine/AI/bioinformatics/programming), offer 3 modes: quick scan, deep read with Obsidian archive, Q&A. MinerU-powered extraction."
---

# Paper Reader — 学术论文阅读分析

> MinerU-powered academic paper analysis with domain-aware deep reading and Obsidian archiving.

---

## Trigger Conditions

Activate when user:
- Mentions "读论文", "分析论文", "paper reader", "read this paper", "分析PDF", "帮我看看这篇"
- Provides a PDF file path (ending in .pdf)
- Provides an arXiv ID (e.g. `2402.03300`)
- Provides an arXiv URL (containing `arxiv.org`)
- Provides multiple papers at once ("Paper Alert", "批量处理", paper list with URLs/DOIs) → use batch mode (references/mode-batch.md)

---

## Environment

```
MINERU="/home/user/.hermes/hermes-agent/venv/bin/mineru"
WORK_BASE="/tmp/paper-reader"
ARCHIVE_BASE="$HOME/obsidian/papers"
EXTRACT_SCRIPT="$HOME/.hermes/skills/paper-reader/scripts/extract.sh"
```

---

## Step 1: Input Parse & Fetch

Detect input type and obtain PDF file:

### Local File
```
Input starts with "/" or "~" or "./" or "../" → local file path
1. Verify file exists: ls -la {path}
2. Verify it's PDF: file {path} | grep -i "PDF"
3. Set PDF_PATH={path}
```

### arXiv ID
```
Input matches pattern: \d{4}\.\d{4,5} (e.g. "2402.03300")
1. WORK_DIR="/tmp/paper-reader/$(date +%s)"
2. mkdir -p "$WORK_DIR"
3. curl -L -o "$WORK_DIR/paper.pdf" "https://arxiv.org/pdf/{ARXIV_ID}"
4. Verify: file size > 10KB and file type is PDF
5. Set PDF_PATH="$WORK_DIR/paper.pdf"
```

### arXiv URL
```
Input contains "arxiv.org" → extract arXiv ID from URL
- From "arxiv.org/abs/XXXX.XXXXX" → extract XXXX.XXXXX
- From "arxiv.org/pdf/XXXX.XXXXX" → extract XXXX.XXXXX
Then follow arXiv ID procedure above
```

### Error Handling
- File not found → "❌ 文件不存在: {path}，请检查路径"
- Not PDF → "❌ 不是PDF文件: {actual_type}"
- Download fail → "❌ 下载失败，请手动下载后提供本地路径"

---

## Step 2: Domain Detection

### Quick Scan (3 pages)
```bash
$MINERU -p "$PDF_PATH" -o "$WORK_DIR/scan" -b pipeline -l en -s 0 -e 3
```

### Keyword Matching
Read the extracted scan text and check for domain-specific keywords:

| Domain | ID | Keywords |
|--------|----|----------|
| Molecular Dynamics | `md` | molecular dynamics, force field, simulation, GROMACS, AMBER, NAMD, RMSD, free energy, trajectory, molecular docking |
| Medicine | `med` | clinical trial, randomized, cohort, patients, treatment, placebo, hazard ratio, RCT, prognosis, diagnosis |
| AI/ML | `ai` | neural network, deep learning, transformer, training, benchmark, SOTA, accuracy, generative, LLM |
| Bioinformatics | `bio` | RNA-seq, genome, GWAS, gene expression, variant calling, differential expression, enrichment, sequencing |
| Programming | `prog` | compiler, operating system, database, algorithm, system design, implementation, performance, runtime |

### User Confirmation
Present detection result:
```
检测到论文领域: {domain_name} ({confidence})
标题: {detected_title}

确认领域:
  A. ✅ 正确
  B. 🔄 我选择其他领域 (MD/医学/AI/生信/编程)
```

NEVER auto-proceed without user confirmation.

---

## Step 3: Mode Selection

Present menu:
```
📄 论文已就绪: {title}
🏷️ 领域: {domain} | 📃 页数: {pages}

请选择分析模式:
  A. 🔍 快速筛选 — 3分钟概览，判断是否值得精读
  B. 📖 深度精读 — 全文结构化拆解 + Obsidian归档笔记
  C. 💬 问答阅读 — 进入交互问答模式
  D. ❌ 取消
```

---

## Step 4: Execution

### Pre-execution: Full Extraction (all modes)

For Mode A, if scan was already done, check if full extraction is needed.
For Modes B and C, always do full extraction:

```bash
$MINERU -p "$PDF_PATH" -o "$WORK_DIR/full" -b pipeline -l en
```

**Large PDF protection**: If page count > 200, auto-split:
```bash
$MINERU -p "$PDF_PATH" -o "$WORK_DIR/part1" -b pipeline -l en -s 0 -e 200
$MINERU -p "$PDF_PATH" -o "$WORK_DIR/part2" -b pipeline -l en -s 200 -e 400
# Merge: cat part1/*/auto/*.md part2/*/auto/*.md > $WORK_DIR/merged.md
```

### Mode A: Quick Scan
1. Load `skill_view("paper-reader", "references/mode-scan.md")`
2. Read extracted markdown (title, abstract, conclusion, captions)
3. Produce screening report per template
4. Output to conversation only — NO archive

### Mode B: Deep Read
1. Load `skill_view("paper-reader", "references/mode-deep.md")`
2. Load `skill_view("paper-reader", "references/domain-{domain}.md")`
3. Load `skill_view("paper-reader", "references/archive-template.md")`
4. Execute deep analysis per mode-deep.md instructions
5. Fill ALL domain checklist fields
6. For key figures: use `vision_analyze` on image files
7. Present conversation summary
8. Generate archive note → save to `~/obsidian/papers/{domain}/`
9. Copy images to `~/obsidian/papers/{domain}/images/`
10. Report archive path

### Mode C: Q&A Mode
1. Load `skill_view("paper-reader", "references/mode-qa.md")`
2. Enter interactive Q&A loop
3. Answer from paper content with citations
4. Use `vision_analyze` for figure questions
5. Exit on user command, optionally save Q&A log

---

## Step 5: Output & Archive

| Mode | Conversation Output | Archive Note |
|------|-------------------|--------------|
| A (Scan) | Screening report | ❌ No |
| B (Deep) | Summary + key findings | ✅ Obsidian note |
| C (Q&A) | Interactive answers | Optional Q&A log |

### Archive Directory Structure
```
~/obsidian/papers/
├── molecular-dynamics/
│   ├── 2026-AlphaFold3-MD-Simulations.md
│   └── images/
│       ├── fig1_rmsd_plot.jpg
│       └── ...
├── medicine/
├── ai-ml/
├── bioinformatics/
└── programming/
```

File naming: `{year}-{ShortTitleKeyword}.md`

---

## Error Recovery

| Error | Response |
|-------|----------|
| arXiv download fail | "❌ 下载失败。请手动下载后提供本地路径。" |
| File not found | "❌ 文件不存在: {path}" |
| Not PDF | "❌ 不是PDF: {actual_type}" |
| MinerU extraction fail | "❌ PDF提取失败。尝试: 1) 检查文件完整性 2) 用-s/-e分段处理" |
| Large PDF (>200 pages) | "📄 大文件检测({N}页)，自动分段处理..." |

---

## Batch Mode

When user provides multiple papers (Paper Alert), use batch mode:

```
skill_view("paper-reader", "references/mode-batch.md")
```

Key workflow: classify by source → parallel download (arXiv only) → serial MinerU (background) → parallel search-mode for paywalled papers → parallel archive → summary table.

**Critical**: MinerU is strictly serial. Paywalled papers (Nature/Elsevier/bioRxiv) cannot be downloaded via curl — use web_search fallback immediately.

---

## Important Notes
- MinerU runs **strictly serial** — never run multiple MinerU processes simultaneously
- Default language flag: `-l en` for English/arXiv papers, `-l ch` for Chinese. MinerU does NOT support `-l auto`
- Always verify PDF before extraction
- Domain checklist: fill EVERY field, use "论文未提及" for missing info
- Archive notes: proper YAML frontmatter for Obsidian searchability
- For Mode B: always use `vision_analyze` on key figures for richer description
- **Vision fallback**: If current model lacks vision (e.g. GLM-5.1), rely on content_list.json image_caption + md figure captions instead
- **Review papers**: Have no tables/equations typically — domain checklist may have many "论文未提及" fields, this is expected
- **Page range quirk**: `-s 0 -e 3` may process 4 pages. For strict 3-page scan, consider `-s 0 -e 2`
- See `references/mineru-quirks.md` for full validation notes and content_list.json type reference
