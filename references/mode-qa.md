# Mode C: Q&A Reading (问答阅读)

## Purpose
Interactive — user asks questions, agent answers from paper content.

## Setup
- MinerU-extracted content is cached at `/tmp/paper-reader/{session}/`
- Full markdown + content_list.json + images are available

## Q&A Loop

Enter interactive loop. For each user question:

1. **Search**: Find relevant sections in extracted markdown
2. **Answer**: Provide grounded answer with citation
3. **Cite**: Always include location reference

### Citation Format
- Text: "根据 [Section Name] 第N段..."
- Figure: "Figure N 显示..." + embed image path
- Table: "Table N 的数据显示..." + render table
- Formula: show LaTeX from extraction

### Answer Rules
- ✅ MUST be grounded in paper text — no fabrication
- ✅ MUST cite specific section/page/figure
- ✅ Use `vision_analyze` for figure-related questions
- ❌ If answer not in paper: state "论文中未提及此内容"
- ❌ Never speculate beyond what the paper states

### Special Question Types
- **"这个方法具体怎么做的?"** → Extract detailed methodology from Methods section
- **"Figure X 说了什么?"** → vision_analyze on corresponding image + caption
- **"和其他方法对比?"** → Extract comparison data from Results/Tables
- **"创新点在哪?"** → Synthesize from Abstract + Introduction + Conclusion
- **"局限性?"** → Extract from Discussion + own assessment

## Exit Conditions
User says: "结束" / "save" / "done" / "exit" / "退出"

## Optional: Save Q&A Log
On exit, offer to save the Q&A transcript as an Obsidian note.
Format: timestamped Q&A pairs in markdown.
