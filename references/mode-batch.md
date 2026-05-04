# Mode Batch — 批量论文处理

> 批量处理多篇论文（Paper Alert），并行下载 → 串行 MinerU → 并行归档。

---

## Trigger
用户提供多篇论文列表（通常含 URL/DOI），说 "Paper Alert"、"批量处理"、"并行" 等。

---

## Phase 1: 分类 & 下载

### 1.1 按来源分类

| 来源 | PDF获取策略 | 成功率 |
|------|------------|--------|
| arXiv (`arxiv.org/pdf/ID`) | `curl -L -o` 直接下载 | ✅ 高 |
| Nature/Science 主站 | `curl` → 403 (付费墙) | ❌ |
| Elsevier/ScienceDirect | `curl` → HTML重定向 | ❌ |
| bioRxiv | `curl` → 403/Cloudflare | ❌ |
| GitHub repo | 无需PDF，直接分析 | ✅ |

### 1.2 下载执行

```bash
WORK="/tmp/paper-batch"
mkdir -p "$WORK/pdf" "$WORK/extracted"

# arXiv论文 — 直接下载
curl -sL -o "$WORK/pdf/p02.pdf" "https://arxiv.org/pdf/{ARXIV_ID}"

# 其他论文 — 先尝试，失败则标记为"搜索模式"
# 逐个尝试，记录哪些成功哪些失败
```

### 1.3 付费墙/Cloudflare 绕过策略（按优先级）

1. **web_search 多轮搜索** — 搜索标题+关键词获取摘要、方法、结果
   - 搜索 "标题 abstract"，"标题 method"，"标题 key results"
   - 每篇至少 2-3 轮搜索
2. **web_extract** — 部分环境可用，本环境被屏蔽
3. **browser 工具** — 可绕过部分 Cloudflare，但部分站点仍会拦截
4. **手动下载** — 最终 fallback，告知用户需要浏览器下载 PDF

> ⚠️ **关键教训**: Nature、Elsevier、bioRxiv 等主流出版商均拦截 curl 下载。
> 不要浪费时间尝试各种 curl header/mirror，直接进入搜索模式。
> arXiv 是唯一可靠的自助 PDF 来源。

---

## Phase 2: MinerU 提取（串行！）

**重要**: MinerU 必须严格串行运行，不可并行。

```bash
MINERU="/home/user/.hermes/hermes-agent/venv/bin/mineru"

# 串行提取所有成功下载的 PDF
for pdf in "$WORK/pdf"/*.pdf; do
    name=$(basename "$pdf" .pdf)
    echo "=== $name ==="
    time "$MINERU" -p "$pdf" -o "$WORK/extracted/$name" -b pipeline -l en 2>&1 | tail -3
done
```

### 性能参考
- 43页 → ~1.5 min
- 26页 → ~2 min（因模型初始化开销，短文档不一定更快）

### 优化：后台运行
对 2+ 篇 PDF，用 `terminal(background=true)` 后台运行 MinerU，
同时并行处理搜索模式论文的归档。

---

## Phase 3: 并行归档

将论文分为两组并行处理：

### 3A: MinerU 全文组（深度归档）
- 读取 MinerU 提取的 markdown
- 生成完整归档笔记（方法、结果、图表、局限、启示）
- 复制图片到 `~/obsidian/papers/{domain}/images/`

### 3B: 搜索模式组（基于摘要归档）
- 基于 web_search 收集的信息
- 生成归档笔记，标注"付费论文，未获取全文"
- 仍需填写：基本信息、研究问题、核心内容、启示

### 3.3 归档笔记模板

所有归档笔记必须包含 YAML frontmatter：

```yaml
---
title: "Full English Title"
authors: ["Key Authors"]
year: 2026
journal: "Journal Name"
doi: "10.xxxx/xxxxx"
domain: "ai"  # ai|med|bio|md|prog
sub_domain: "specific topic"
date_read: "YYYY-MM-DD"
tags: [paper/{domain}, tag1, tag2]
paper_type: "research|review|preprint|software"
rating: "3-5"
---
```

### 3.4 目录结构

```
~/obsidian/papers/
├── ai-ml/           # AI/ML 论文
├── medicine/        # 医学/药学
├── bioinformatics/  # 生信
├── molecular-dynamics/  # MD相关
└── images/          # 共享图片目录
```

---

## Phase 4: 汇总报告

生成汇总表格，包含：

| 列 | 内容 |
|----|------|
| # | 序号 |
| 论文 | 短标题 |
| 期刊 | 发表处 |
| 核心价值 | 1句话 |
| 适配度 | ⭐评分（与用户研究方向的相关性） |

最后给出 **Top 3 推荐**（与 MD/AI/药物设计最相关）。

---

## Pitfalls

1. **MinerU 严格串行** — 并行会导致模型加载冲突
2. **curl 下载付费论文必败** — 不浪费时间，直接搜索模式
3. **web_extract 环境依赖** — 部分环境被屏蔽，需要 fallback
4. **delegate_task 超时** — 复杂子任务容易超时(300s)，考虑拆分或直接在主会话执行
5. **bioRxiv PDF URL** — `content/IDv1.full.pdf` 会被 Cloudflare 拦截，不是真正的 PDF 链接
6. **并行数量** — execute_code 算 1 次工具调用（多语句也算），适合批量写文件；但会烧 iteration budget

---

## 实战数据

| 指标 | 值 |
|------|-----|
| 9篇论文总处理时间 | ~8 min |
| PDF成功下载 | 2/7 (arXiv ✅, Nature主页HTML被当PDF ✅) |
| 搜索模式 | 6篇 |
| MinerU提取 | 2篇 (p01: 494行/36图, p02: 646行/75图) |
| 总归档图片 | 111张 |
| 归档笔记 | 9篇 |
