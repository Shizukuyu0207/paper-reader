<div align="center">

# 📄 Paper Reader

**基于 MinerU 的学术论文分析 Hermes Agent Skill**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

[Hermes Agent](https://github.com/henvic/hermes) 的学术论文阅读分析 Skill。支持 PDF 全文提取、智能领域检测、深度结构化分析，并自动归档到 Obsidian 知识库。

无论是单篇 arXiv 预印本的快速筛选，还是 10+ 篇跨出版商论文的批量处理，Paper Reader 都能自动完成提取、分类、分析和归档。

## 🎯 核心特性

| 特性 | 说明 |
|------|------|
| 🧠 **自动领域检测** | 5 大领域：分子动力学、医学、AI/ML、生物信息学、编程 |
| 📊 **3 种阅读模式** | 快速筛选（3分钟）· 深度精读（全文分析）· 问答（交互式）|
| ⚡ **批量处理** | 并行下载 + MinerU 提取 + 并行分析，支持 Paper Alert |
| 📝 **Obsidian 归档** | YAML frontmatter + 结构化 Markdown 笔记 |
| 🔍 **图表视觉分析** | AI 驱动的关键图表描述与分析 |
| 🔓 **付费墙处理** | Nature/Elsevier/bioRxiv 付费论文自动回退到 web_search |

## 📖 阅读模式

### 🔍 快速筛选
3 分钟概览，判断论文是否值得精读。提取标题、摘要、关键发现和意义。不创建归档。

### 📖 深度精读
基于领域专用的分析检查清单进行全文结构化分析。生成完整的 Obsidian 归档笔记，包含方法解析、定量结果、局限性和研究启示。

### 💬 问答模式
交互式问答。可针对论文内容、图表或方法论提问。可选保存问答记录。

### 📦 批量模式（Paper Alert）
同时处理多篇论文，支持混合来源：
- **arXiv PDF** → 直接下载 + MinerU 全文提取
- **付费论文**（Nature、Elsevier、bioRxiv）→ web_search 元数据回退
- **GitHub 仓库** → README 分析

## 🗂️ 领域分析清单

| 领域 | 关键分析点 |
|------|-----------|
| 🧬 **分子动力学** | 力场、模拟参数、RMSD/RMSF、自由能方法、轨迹分析 |
| 🏥 **医学** | 研究设计、队列信息、统计方法、临床结局、风险比 |
| 🤖 **AI / ML** | 架构细节、训练数据、基准测试、SOTA 对比、计算资源 |
| 🔬 **生物信息学** | 分析管线、统计检验、基因组组装、差异表达、富集分析 |
| 💻 **编程** | 算法复杂度、系统设计、实现细节、性能基准 |

## 🚀 安装

```bash
# 克隆到 Hermes skills 目录
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

或手动将 `paper-reader/` 文件夹复制到 `~/.hermes/skills/paper-reader/`。

### 前置依赖

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 提取引擎
- [Hermes Agent](https://github.com/henvic/hermes) — Agent 框架
- Obsidian 知识库（可选，用于归档笔记）

## 📋 使用方法

```
# 单篇论文 — 本地文件
读论文 /path/to/paper.pdf

# 单篇论文 — arXiv
read this paper https://arxiv.org/abs/2604.18559

# 批量 — Paper Alert
Paper Alert:
1. Allosteric Switches https://www.nature.com/articles/s41587-026-03081-9
2. ConforNets https://arxiv.org/abs/2604.18559
3. trRosettaRNA2 https://doi.org/10.1038/s42256-026-01223-x
```

Skill 将自动：获取/验证 PDF → 检测领域 → 选择模式 → 分析 → 归档

## 📝 归档输出示例

笔记保存到 `~/obsidian/papers/{domain}/`，包含完整 YAML frontmatter：

```yaml
---
title: "Artificial allosteric protein switches with ML-designed receptors"
authors: ["Zhong Guo", "David Baker"]
year: 2026
journal: "Nature Biotechnology"
doi: "10.1038/s41587-026-03081-9"
domain: "ai"
sub_domain: "protein design / allosteric switches"
date_read: "2026-05-04"
tags: [paper/ai, allosteric-switch, biosensor, protein-design]
paper_type: "research"
rating: "5"
---
```

后接结构化章节：基本信息 · 研究问题 · 方法 · 核心结果 · 局限性 · 研究启示 · 引用网络

## ⚙️ 配置

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `MINERU` | MinerU 二进制路径 | MinerU 可执行文件路径 |
| `WORK_BASE` | `/tmp/paper-reader` | 临时工作目录 |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian 归档根目录 |
| `EXTRACT_SCRIPT` | `scripts/extract.sh` | 提取辅助脚本路径 |

## 📄 许可证

MIT License — 详见 [LICENSE](../LICENSE)。

## 🙏 致谢

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 提取引擎
- [Hermes Agent](https://github.com/henvic/hermes) — Agent 框架
- 为论文太多读不完的科研工作者而建

<div align="center">
为论文太多读不完的科研工作者而建 ❤️
</div>
