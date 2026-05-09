     1|<div align="center">
     2|
     3|# 📄 Paper Reader
     4|
     5|**学术论文分析 — Agent 无关管线**
     6|
     7|[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
     8|[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)
     9|
    10|[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)
    11|
    12|</div>
    13|
    14|---
    15|
    16|## ✨ 概述
    17|
    18|自动阅读、分析和归档学术论文——智能领域检测 + Obsidian 笔记集成。
    19|
    20|给它一个 URL、PDF 路径、或一批论文，自动完成获取、分类、深度分析和归档。
    21|
    22|设计为 Agent 无关的管线，兼容 Hermes、Claude Code、Codex、OpenCode 等任意 Agent。适配文件见 `adapters/`。
    23|
    24|---
    25|
    26|## 🏗️ 架构
    27|
    28|5 阶段管线 + 3 层内容获取策略。
    29|
    30|```
    31|获取(3层) → 领域检测(5领域) → 模式选择(4模式) → 领域清单驱动分析 → Obsidian归档
    32|```
    33|
    34|### 3 层内容获取
    35|
    36|| 优先级 | 工具 | 速度 | 覆盖 |
    37||--------|------|------|------|
    38|| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, 大部分 Nature |
    39|| Tier 2 | Scrapling + Camoufox | 5-15s | Nature/Elsevier 补位 |
    40|| Tier 3 | web_search | 2-5s | 硬付费墙（Cell, NEJM）|
    41|| 本地 | MinerU | ~2min/40p | 本地 PDF 全文+图片 |
    42|
    43|### 领域检测
    44|
    45|| 领域 | 关键词示例 |
    46||------|-----------|
    47|| 🧬 分子动力学 | AMBER, GROMACS, RMSD, 自由能, 模拟 |
    48|| 🏥 医学 | 临床试验, RCT, 队列, 风险比, 预后 |
    49|| 🤖 AI / ML | transformer, 深度学习, benchmark, SOTA |
    50|| 🔬 生物信息学 | RNA-seq, GWAS, 基因组, 差异表达 |
    51|| 💻 编程 | 编译器, 算法, 系统设计, 数据库 |
    52|
    53|### 4 种分析模式
    54|
    55|🔍 **快速筛选** — 3分钟判断是否值得精读
    56|📖 **深度精读** — 全文结构化分析 + Obsidian 归档
    57|💬 **问答模式** — 交互式论文问答
    58|📦 **批量处理** — 多篇并行 + 汇总表
    59|
    60|---
    61|
    62|## 📊 案例：9篇论文批量处理（2026年5月）
    63|
    64|### 获取结果
    65|
    66|| # | 论文 | 来源 | 方法 | 质量 |
    67||---|------|------|------|------|
    68|| 1 | Allosteric Switches (Baker) | Nature NBT | MinerU 93s | ★★★★★ 全文494行+36图 |
    69|| 2 | ConforNets | arXiv | MinerU 118s | ★★★★★ 全文646行+75图 |
    70|| 3-8 | 6篇付费/预印本 | 混合 | web_search | ★★☆☆☆ 仅元数据 |
    71|| 9 | lightning-boltz | GitHub | README | ★★☆☆☆ 仓库信息 |
    72|
    73|**总耗时**: ~6分钟
    74|
    75|### Jina Reader + Scrapling 整合后
    76|
    77|| 论文 | 之前 | 之后 | 改善 |
    78||------|------|------|------|
    79|| Allosteric Switches | MinerU 93s | **Jina 1.0s, 117K字符** | 快93倍 |
    80|| Target ID (NRDD) | web_search 元数据 | **Jina 1.3s, 149K字符** | 元数据→**全文** |
    81|| ERAST (NBT) | web_search 元数据 | **Jina 1.0s, 全文** | 元数据→**全文** |
    82|
    83|### 客观评价
    84|
    85|✅ 全文论文 → 100+行深度归档，含定量结果。9篇6分钟。领域全部正确分类。
    86|⚠️ 付费论文（整合前）→ 34-53行元数据级笔记。MinerU 串行瓶颈。
    87|❌ ScienceDirect/Elsevier 仍为 Tier 3。arXiv 摘要页需用 `pdf/` 链接获取全文。
    88|
    89|---
    90|
    91|## ⚠️ 诚实的局限性
    92|
    93|### 无法突破的
    94|
    95|| 场景 | 现实 | 解决方案 |
    96||------|------|---------|
    97|| **硬付费墙**（Cell, NEJM, JAMA） | 需机构登录 | 用 VPN，手动下载 PDF |
    98|| **机构认证**（SSO） | 超出范围 | 通过机构下载 PDF |
    99|| **非英文论文** | MinerU 支持中文 `-l ch` | 本地 PDF + MinerU |
   100|
   101|### 应该知道的
   102|
   103|- **Tier 3 论文**：归档笔记缺方法细节和定量结果
   104|- **图片分析**：依赖模型视觉能力，回退到图注
   105|- **归档 ≠ 读论文**：结构化摘要，非替代阅读
   106|
   107|### 法律立场
   108|
   109|获取浏览器公开可见内容。需登录才能看到的——请自行登录。
   110|
   111|---
   112|
   113|## 🚀 安装
   114|
   115|```bash
   116|git clone https://github.com/nowa277/paper-reader.git
   117|
   118|# Hermes: 放入 skill 目录
   119|cp -r paper-reader ~/.hermes/skills/
   120|
   121|# 其他 Agent: 见 adapters/ 目录的适配文件
   122|```
   123|
   124|### 依赖
   125|
   126|| 依赖 | 必须 | 安装 |
   127||------|------|------|
   128|| MinerU | ✅ | `pip install mineru` |
   129|| Jina Reader | 内置 | `r.jina.ai` API |
   130|| Scrapling | 推荐 | `pip install scrapling camoufox` |
   131|| Obsidian | 可选 | 归档笔记 |
   132|
   133|---
   134|
   135|## 📋 快速开始
   136|
   137|```
   138|# 单篇
   139|read this paper https://arxiv.org/abs/2604.18559
   140|
   141|# 批量
   142|Paper Alert:
   143|1. ConforNets https://arxiv.org/abs/2604.18559
   144|2. Allosteric Switches https://www.nature.com/articles/s41587-026-03081-9
   145|3. Target ID https://doi.org/10.1038/s41573-026-01412-8
   146|```
   147|
   148|---
   149|
   150|## 📁 项目结构
   151|
   152|```
   153|paper-reader/
   154|├── SKILL.md                 # 主 skill 定义（5阶段管线）
   155|├── adapters/                # Agent 适配文件
   156|├── scripts/                 # MinerU + fetch 脚本
   157|├── references/              # 领域清单 + 模板
   158|│   ├── domain-{ai,md,med,bio,prog}.md
   159|│   ├── mode-{scan,deep,qa,batch}.md
   160|│   └── archive-template.md
   161|└── docs/                    # 6语言 README
   162|```
   163|
   164|---
   165|
   166|## 📝 归档输出示例
   167|
   168|```yaml
   169|---
   170|title: "Artificial allosteric protein switches with ML-designed receptors"
   171|authors: ["Zhong Guo", "David Baker"]
   172|year: 2026
   173|journal: "Nature Biotechnology"
   174|domain: "ai"
   175|tags: [paper/ai, allosteric-switch, protein-design]
   176|rating: "5"
   177|---
   178|```
   179|
   180|---
   181|
   182|## ⚙️ 配置
   183|
   184|| 变量 | 默认值 | 说明 |
   185||------|--------|------|
   186|| `MINERU` | MinerU 路径 | 可执行文件路径 |
   187|| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian 归档根目录 |
   188|| `JINA_READER` | `https://r.jina.ai` | Jina Reader API |
   189|
   190|---
   191|
   192|## 🤝 贡献
   193|
   194|欢迎 PR。
   195|
   196|## 📄 许可证
   197|
   198|MIT License — 详见 [LICENSE](../LICENSE)。
   199|
   200|## 🙏 致谢
   201|
   202|MinerU · Jina Reader · Scrapling
   203|致敬每一位浏览器里开着 50 个未读论文标签的科研工作者
   204|
   205|<div align="center">
   206|为论文太多读不完的科研工作者而建 ❤️
   207|</div>
   208|