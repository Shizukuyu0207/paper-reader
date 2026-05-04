# Mode B: Deep Read (深度精读)

## Purpose
Full structured analysis + Obsidian archive note.

## Process

### Phase 1: Extraction
1. Confirm MinerU full extraction is complete (markdown + content_list.json + images)
2. Read the full markdown content
3. Parse content_list.json for structured elements (sections, tables, figures, equations)

### Phase 2: Domain Analysis
1. Load domain checklist from `references/domain-{domain}.md`
2. Fill each field from paper content — leave no field blank, use "论文未提及" for missing
3. For key figures: use `vision_analyze` on extracted image files to describe content
4. For tables: render from content_list.json data

### Phase 3: Structured Analysis
Analyze section by section:
- **Basic Info**: title, authors, journal, year, DOI/arXiv
- **Research Question**: what gap does this paper address?
- **Methods**: fill domain checklist fields
- **Results**: extract key data, metrics, figures with specific values
- **Discussion**: limitations, implications, future directions
- **Citation Network**: key references (foundational works this builds on)

### Phase 4: Dual Output

#### Conversation Summary
Condensed version for the chat:
```
## 📖 Deep Read: [Title]

**One-line summary**: [核心贡献一句话]

**Methods**: [方法概述，2-3句]

**Key Results**:
- [结果1 + 具体数值]
- [结果2 + 具体数值]

**Key Figures**: [列出关键图表]

**Limitations**: [主要局限]

**Relevance**: [与用户研究方向的关联]
```

#### Archive Note Generation
1. Load `references/archive-template.md`
2. Fill all template fields from analysis
3. Copy extracted images to `~/obsidian/papers/{domain}/images/`
4. Save note to `~/obsidian/papers/{domain}/{year}-{keyword}.md`
5. Report: "📎 Archive saved to: {path}"

## Quality Standards
- Every field in domain checklist MUST be filled (no blanks)
- Key figures MUST be described (not just referenced)
- Specific values with units where available
- Relevance section MUST connect to user's known research interests
