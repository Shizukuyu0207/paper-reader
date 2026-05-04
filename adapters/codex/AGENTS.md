# Paper Reader Instructions

When asked to read or analyze an academic paper:

## Pipeline

### Step 1: Fetch Content
For URLs, use Jina Reader:
```bash
curl -sL --max-time 30 "https://r.jina.ai/{URL}" -H "Accept: text/plain"
```
If response >1000 chars → use it. Otherwise fallback to web search.

For local PDFs: `mineru -p file.pdf -o output/ -b pipeline -l en`

### Step 2: Domain Detection
Classify by keywords:
- **MD**: molecular dynamics, force field, simulation, AMBER, GROMACS, RMSD, free energy
- **Medicine**: clinical trial, RCT, cohort, hazard ratio, prognosis
- **AI/ML**: neural network, transformer, deep learning, benchmark, SOTA
- **Bioinformatics**: RNA-seq, genome, GWAS, differential expression, enrichment
- **Programming**: compiler, algorithm, system design, database, runtime

### Step 3: Analyze
- Basic info (title, authors, year, journal, DOI)
- Research questions and motivation
- Methods (architecture, experimental design, parameters)
- Core results (quantitative data, key figures)
- Key innovations
- Limitations
- Implications

### Step 4: Archive (Deep Read)
Save to ~/obsidian/papers/{domain}/YYYY-{ShortTitle}.md with YAML frontmatter.

## Tools
- Jina Reader (Tier 1, 1-2s): arXiv, bioRxiv, open-access
- MinerU (local PDFs): `mineru -p file.pdf -o output/ -b pipeline -l en`
- web_search (Tier 3): paywalled papers

## Limitations
- Cannot bypass hard paywalls (Cell, NEJM, JAMA)
- arXiv: use pdf/ URL for full text
- Jina Reader free tier: 20 RPM
- Never bypass authenticated access
