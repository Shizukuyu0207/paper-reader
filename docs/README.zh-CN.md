<div align="center">

# 📄 Paper Reader

**学术论文分析 — Agent 无关管线**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

自动阅读、分析和归档学术论文——智能领域检测 + Obsidian 笔记集成。

给它一个 URL、PDF 路径、或一批论文，自动完成获取、分类、深度分析和归档。

设计为 Agent 无关的管线，兼容 Hermes、Claude Code、Codex、OpenCode 等任意 Agent。适配文件见 `adapters/`。

---

## 🏗️ 架构

5 阶段管线 + 3 层内容获取策略。

```
获取(3层) → 领域检测(5领域) → 模式选择(4模式) → 领域清单驱动分析 → Obsidian归档
```

### 3 层内容获取

| 优先级 | 工具 | 速度 | 覆盖 |
|--------|------|------|------|
| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, 大部分 Nature |
| Tier 2 | Scrapling + Camoufox | 5-15s | Nature/Elsevier 补位 |
| Tier 3 | web_search | 2-5s | 硬付费墙（Cell, NEJM）|
| 本地 | MinerU | ~2min/40p | 本地 PDF 全文+图片 |

### 领域检测

| 领域 | 关键词示例 |
|------|-----------|
| 🧬 分子动力学 | AMBER, GROMACS, RMSD, 自由能, 模拟 |
| 🏥 医学 | 临床试验, RCT, 队列, 风险比, 预后 |
| 🤖 AI / ML | transformer, 深度学习, benchmark, SOTA |
| 🔬 生物信息学 | RNA-seq, GWAS, 基因组, 差异表达 |
| 💻 编程 | 编译器, 算法, 系统设计, 数据库 |

### 4 种分析模式

🔍 **快速筛选** — 3分钟判断是否值得精读
📖 **深度精读** — 全文结构化分析 + Obsidian 归档
💬 **问答模式** — 交互式论文问答
📦 **批量处理** — 多篇并行 + 汇总表

---

## 📊 案例：9篇论文批量处理（2026年5月）

### 获取结果

| # | 论文 | 来源 | 方法 | 质量 |
|---|------|------|------|------|
| 1 | Allosteric Switches (Baker) | Nature NBT | MinerU 93s | ★★★★★ 全文494行+36图 |
| 2 | ConforNets | arXiv | MinerU 118s | ★★★★★ 全文646行+75图 |
| 3-8 | 6篇付费/预印本 | 混合 | web_search | ★★☆☆☆ 仅元数据 |
| 9 | lightning-boltz | GitHub | README | ★★☆☆☆ 仓库信息 |

**总耗时**: ~6分钟

### Jina Reader + Scrapling 整合后

| 论文 | 之前 | 之后 | 改善 |
|------|------|------|------|
| Allosteric Switches | MinerU 93s | **Jina 1.0s, 117K字符** | 快93倍 |
| Target ID (NRDD) | web_search 元数据 | **Jina 1.3s, 149K字符** | 元数据→**全文** |
| ERAST (NBT) | web_search 元数据 | **Jina 1.0s, 全文** | 元数据→**全文** |

### 客观评价

✅ 全文论文 → 100+行深度归档，含定量结果。9篇6分钟。领域全部正确分类。
⚠️ 付费论文（整合前）→ 34-53行元数据级笔记。MinerU 串行瓶颈。
❌ ScienceDirect/Elsevier 仍为 Tier 3。arXiv 摘要页需用 `pdf/` 链接获取全文。

---

## ⚠️ 诚实的局限性

### 无法突破的

| 场景 | 现实 | 解决方案 |
|------|------|---------|
| **硬付费墙**（Cell, NEJM, JAMA） | 需机构登录 | 用 VPN，手动下载 PDF |
| **机构认证**（SSO） | 超出范围 | 通过机构下载 PDF |
| **非英文论文** | MinerU 支持中文 `-l ch` | 本地 PDF + MinerU |

### 应该知道的

- **Tier 3 论文**：归档笔记缺方法细节和定量结果
- **图片分析**：依赖模型视觉能力，回退到图注
- **归档 ≠ 读论文**：结构化摘要，非替代阅读

### 法律立场

获取浏览器公开可见内容。需登录才能看到的——请自行登录。

---

## 🚀 安装

```bash
git clone https://github.com/Shizukuyu0207/paper-reader.git

# Hermes: 放入 skill 目录
cp -r paper-reader ~/.hermes/skills/

# 其他 Agent: 见 adapters/ 目录的适配文件
```

### 依赖

| 依赖 | 必须 | 安装 |
|------|------|------|
| MinerU | ✅ | `pip install mineru` |
| Jina Reader | 内置 | `r.jina.ai` API |
| Scrapling | 推荐 | `pip install scrapling camoufox` |
| Obsidian | 可选 | 归档笔记 |

---

## 📋 快速开始

```
# 单篇
read this paper https://arxiv.org/abs/2604.18559

# 批量
Paper Alert:
1. ConforNets https://arxiv.org/abs/2604.18559
2. Allosteric Switches https://www.nature.com/articles/s41587-026-03081-9
3. Target ID https://doi.org/10.1038/s41573-026-01412-8
```

---

## 📁 项目结构

```
paper-reader/
├── SKILL.md                 # 主 skill 定义（5阶段管线）
├── adapters/                # Agent 适配文件
├── scripts/                 # MinerU + fetch 脚本
├── references/              # 领域清单 + 模板
│   ├── domain-{ai,md,med,bio,prog}.md
│   ├── mode-{scan,deep,qa,batch}.md
│   └── archive-template.md
└── docs/                    # 6语言 README
```

---

## 📝 归档输出示例

```yaml
---
title: "Artificial allosteric protein switches with ML-designed receptors"
authors: ["Zhong Guo", "David Baker"]
year: 2026
journal: "Nature Biotechnology"
domain: "ai"
tags: [paper/ai, allosteric-switch, protein-design]
rating: "5"
---
```

---

## ⚙️ 配置

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `MINERU` | MinerU 路径 | 可执行文件路径 |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian 归档根目录 |
| `JINA_READER` | `https://r.jina.ai` | Jina Reader API |

---

## 🤝 贡献

欢迎 PR。

## 📄 许可证

MIT License — 详见 [LICENSE](../LICENSE)。

## 🙏 致谢

MinerU · Jina Reader · Scrapling
致敬每一位浏览器里开着 50 个未读论文标签的科研工作者

<div align="center">
为论文太多读不完的科研工作者而建 ❤️
</div>
