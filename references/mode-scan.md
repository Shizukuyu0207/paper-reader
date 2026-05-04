# Mode A: Quick Scan (快速筛选)

## Purpose
3-minute assessment: is this paper worth reading in depth?

## Process
1. Read MinerU-extracted markdown — focus on **title, abstract, conclusion, figure/table captions**
2. If `content_list.json` available, extract section headers for structure overview
3. Produce screening report (conversation output only, NO archive)

## Output Format

Produce exactly this structure:

```markdown
## 🔍 Screening Report: [Title]

- **Core Question**: [one sentence — what problem does this paper solve?]
- **Method Type**: [experimental / simulation / theoretical / review / meta-analysis]
- **Key Findings** (≤3):
  1. [finding with key metric]
  2. [finding with key metric]
  3. [finding with key metric]
- **Relevance**: [High / Medium / Low] — [one sentence why]
- **Recommendation**: [Deep Read / Browse / Skip]
- **Recommended Sections**: [which sections to read if relevant]
```

## Decision Rules
- **Deep Read**: Directly relevant to user's research, novel method, or high-impact finding
- **Browse**: Tangentially relevant, useful background but not critical
- **Skip**: Low relevance, incremental work, or poor methodology

## Constraints
- Do NOT fabricate findings — only report what's in the paper
- If abstract is insufficient, scan introduction and conclusion
- Keep total output under 200 words
