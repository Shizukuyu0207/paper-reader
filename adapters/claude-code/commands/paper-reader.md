# Paper Reader — Academic Paper Analysis

Read and analyze the academic paper provided as $ARGUMENTS.

## Pipeline

### Step 1: Input Parse
Detect if input is:
- A URL (arXiv, DOI, publisher page, bioRxiv)
- A local PDF file path
- Multiple papers (batch mode)

For URLs, use Jina Reader first:
```bash
curl -sL --max-time 30 "https://r.jina.ai/{URL}" -H "Accept: text/plain"
```
If response >1000 chars → use it directly. Otherwise try curl PDF download, then web_search fallback.

For local PDFs, verify file exists and is PDF format.

### Step 2: Domain Detection
Check content for domain keywords:
- **MD**: molecular dynamics, force field, simulation, AMBER, GROMACS, RMSD, free energy
- **Medicine**: clinical trial, RCT, cohort, hazard ratio, prognosis
- **AI/ML**: neural network, transformer, deep learning, benchmark, SOTA
- **Bioinformatics**: RNA-seq, genome, GWAS, differential expression, enrichment
- **Programming**: compiler, algorithm, system design, database, runtime

Present detected domain and ask user to confirm or override.

### Step 3: Mode Selection
Ask user to choose:
- **A. Quick Scan** — 3-min screening: worth reading?
- **B. Deep Read** — Full structured analysis + archive to ~/obsidian/papers/{domain}/
- **C. Q&A** — Interactive paper Q&A
- **D. Batch** — Multiple papers parallel processing

### Step 4: Execute Analysis
For Deep Read, produce structured output covering:
- Basic info (title, authors, year, journal, DOI)
- Research questions and motivation
- Methods (architecture, experimental design, parameters)
- Core results (quantitative data, key figures)
- Key innovations
- Limitations (author-stated + independent assessment)
- Implications for research
- Citation network (key references)

### Step 5: Archive (Mode B only)
Save to ~/obsidian/papers/{domain}/YYYY-{ShortTitle}.md with YAML frontmatter:
```yaml
---
title: "Paper Title"
authors: ["Author1", "Author2"]
year: YYYY
journal: "Journal Name"
doi: "10.xxxx/xxxxx"
domain: "ai"
tags: [paper/ai, keyword1, keyword2]
date_read: "YYYY-MM-DD"
rating: "1-5"
---
```

### Important Notes
- Jina Reader free tier: 20 RPM
- For paywalled papers (Cell, NEJM, JAMA): metadata only, clearly mark in archive
- arXiv: use pdf/ URL for full text, abs/ URL gives only abstract
- MinerU for local PDFs: `mineru -p file.pdf -o output/ -b pipeline -l en`
- Never bypass authenticated access

## 3-Tier Content Acquisition

| Priority | Tool | Speed | Works For |
|----------|------|-------|-----------|
| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, open-access, most DOIs |
| Tier 2 | Scrapling + Camoufox | 5-15s | Nature/Elsevier when Tier 1 partial |
| Tier 3 | web_search | 2-5s | Hard paywalls (Cell, NEJM) |
| Local | MinerU | ~2min/40p | Local PDF files |
