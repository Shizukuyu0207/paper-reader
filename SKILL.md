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
JINA_READER="https://r.jina.ai"
FETCH_SCRIPT="$HOME/.hermes/skills/paper-reader/scripts/fetch_paper.py"
```

### PDF Fetch Strategy (3-Tier)

**Unified tool**: `python3 $FETCH_SCRIPT <url> --output-dir <dir>` handles all tiers automatically. Use it for both single and batch mode.

| Priority | Method | Works For | Quality |
|----------|--------|-----------|---------|
| **Tier 1** | Jina Reader (`r.jina.ai`) | arXiv, bioRxiv, open-access PDFs, most DOIs | Full text → Markdown |
| **Tier 2** | `curl -L` direct download | arXiv PDF only | Raw PDF → MinerU |
| **Tier 3** | web_search fallback | Nature, Elsevier, all paywalled | Metadata + abstract only |

**Why Jina Reader first**: It converts PDF URLs directly to Markdown text, bypassing Cloudflare/bot detection. For open-access papers, this eliminates the need to download PDF + run MinerU entirely.

**Jina Reader Usage**:
```bash
# Convert any paper URL to Markdown
curl -sL --max-time 30 "https://r.jina.ai/{PAPER_URL}" -H "Accept: text/plain"

# Examples (all verified working):
# arXiv:      https://r.jina.ai/https://arxiv.org/pdf/2604.18559         ✅ Full text
# bioRxiv:    https://r.jina.ai/https://www.biorxiv.org/content/...v1.full.pdf  ✅ Full text
# DOI:        https://r.jina.ai/https://doi.org/10.1038/s42256-026-01223-x      ⚠️ Partial (paywall)
# Nature:     https://r.jina.ai/https://www.nature.com/articles/...              ⚠️ Timeout likely
```

**Rate limits**: Free tier 20 RPM. For batch processing, add delays or use API key.

---

## Step 1: Input Parse & Fetch

Detect input type and obtain paper content. **Always try Jina Reader first** for URLs.

### Decision Flow

```
Input → Is it a local file? → Yes → Use local file
                             → No  → Try Jina Reader (Tier 1)
                                    → Got full text? → Use it directly (skip MinerU!)
                                    → Timeout/partial? → Try curl download (Tier 2)
                                                         → Got PDF? → MinerU extraction
                                                         → Failed? → web_search fallback (Tier 3)
```

### Local File
```
Input starts with "/" or "~" or "./" or "../" → local file path
1. Verify file exists: ls -la {path}
2. Verify it's PDF: file {path} | grep -i "PDF"
3. Set PDF_PATH={path}
```

### URL — Jina Reader (Tier 1, ALWAYS TRY FIRST)

For ANY URL (arXiv, bioRxiv, DOI, publisher page):
```bash
# Try Jina Reader
RESPONSE=$(curl -sL --max-time 30 "https://r.jina.ai/{URL}" -H "Accept: text/plain")
# Check if we got meaningful content (>1000 chars = likely full text)
if [ $(echo "$RESPONSE" | wc -c) -gt 1000 ]; then
    # Save the markdown directly — NO need for MinerU!
    echo "$RESPONSE" > "$WORK_DIR/paper_jina.md"
    FULLTEXT_PATH="$WORK_DIR/paper_jina.md"
    SKIP_MINERU=true  # Skip MinerU step, go directly to analysis
fi
```

### URL — Direct PDF Download (Tier 2, for arXiv only)

Only if Jina Reader fails or returns <1000 chars:
```bash
# arXiv PDF download
curl -L -o "$WORK_DIR/paper.pdf" "https://arxiv.org/pdf/{ARXIV_ID}"
# Verify: file size > 10KB and file type is PDF
```

### URL — web_search Fallback (Tier 3)

For paywalled papers where both Jina Reader and curl fail:
- Use `web_search()` with paper title/DOI to gather metadata
- Accept that archive will be metadata-level only
- Mark archive note: `注: 付费论文，基于搜索信息整理`

### Error Handling
- File not found → "❌ 文件不存在: {path}，请检查路径"
- Not PDF → "❌ 不是PDF文件: {actual_type}"
- Jina Reader timeout → Fall to Tier 2/3 automatically
- All methods fail → "❌ 无法获取论文内容。请手动下载PDF后提供本地路径"

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

Key workflow: classify by source → **parallel Jina Reader for ALL URLs** (Tier 1) → serial MinerU for local/failed PDFs (Tier 2) → parallel web_search for remaining paywalled (Tier 3) → parallel archive → summary table.

**Critical**: MinerU is strictly serial. **Always try Jina Reader first** — it converts PDF URLs to Markdown directly, bypassing Cloudflare/bot detection. For arXiv/bioRxiv/open-access, this skips MinerU entirely.

### Batch Mode — Operational Notes (validated 2026-05-04)

**Jina Reader (`r.jina.ai`) — THE Game Changer**:
- arXiv PDFs: `r.jina.ai/https://arxiv.org/pdf/XXXX.XXXXX` → Full Markdown text ✅
- bioRxiv PDFs: `r.jina.ai/https://www.biorxiv.org/content/...v1.full.pdf` → Full text ✅
- DOI redirects: `r.jina.ai/https://doi.org/10....` → Partial/full depending on paywall ⚠️
- Nature articles: Likely timeout (>30s) → Fall to web_search ❌
- Free tier: 20 RPM. For 9-paper batches, use ~3s delay between requests.
- **Key benefit**: Jina Reader bypasses Cloudflare entirely — no 403/403 errors!

**PDF Download Reality Check (without Jina Reader)**:
- arXiv PDFs: `curl -L` works reliably → get actual PDF
- Nature (`nature.com/*.pdf`): Returns HTML redirect, NOT PDF. Use web_search for metadata.
- Elsevier/ScienceDirect: 403 Forbidden. Use web_search.
- bioRxiv: Cloudflare bot detection (403). Use Jina Reader or web_search.
- `web_extract` may be blocked by the runtime environment entirely — always have web_search as primary fallback.

**MinerU Timing** (reference, your hardware):
- 43-page paper: ~1m33s
- 26-page paper: ~1m58s
- Always run MinerU in background (`terminal(background=true)`) so other tasks proceed in parallel.

**Deep Analysis of Extracted Papers**:
- `delegate_task` subagents may timeout (300s) when reading large extracted Markdown files (500+ lines). Prefer direct `read_file` + `execute_code` in the main session for reliability.
- For 9+ paper batches: write archive notes via `execute_code` batch script (1 tool call for all notes) rather than individual writes.

**Paywalled Paper Archive Quality**:
- web_search returns enough for: title, authors, journal, DOI, abstract, key methods, main results.
- NOT sufficient for: detailed figures, supplementary data, specific quantitative results.
- Mark these notes clearly with `注: 付费论文，基于搜索信息整理` in the archive.

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
