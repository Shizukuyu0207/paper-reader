<div align="center">

# 📄 Paper Reader

**学术论文分析 Hermes Agent Skill — MinerU + Jina Reader + Scrapling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

[Hermes Agent](https://github.com/henvic/hermes) 的学术论文阅读分析 Skill。支持 3 层智能获取、自动领域检测、深度结构化分析，并自动归档到 Obsidian 知识库。

## 🎯 核心特性

| 特性 | 说明 |
|------|------|
| 🧠 **自动领域检测** | 5 大领域：分子动力学、医学、AI/ML、生物信息学、编程 |
| 📊 **3 种阅读模式** | 快速筛选（3分钟）· 深度精读（全文分析）· 问答（交互式）|
| ⚡ **3 层内容获取** | Jina Reader → Scrapling 隐身浏览器 → web_search 回退 |
| 📝 **Obsidian 归档** | YAML frontmatter + 结构化 Markdown 笔记 |
| 🔍 **图表视觉分析** | AI 驱动的关键图表描述与分析 |
| 📦 **批量处理** | 并行获取 + 并行分析，支持 Paper Alert |

## 🔗 内容获取 — 3 层策略

这是真正获取论文内容的核心管线。没有魔法——只有分层的降级策略和诚实的取舍。

```
URL 输入 → 第1层: Jina Reader (r.jina.ai) → 全文 Markdown? → 完成 ✅
                                             → 不完整/超时? → 第2层 ↓
          → 第2层: Scrapling 隐身浏览器 → 完整 HTML? → 完成 ✅
                                           → 失败? → 第3层 ↓
          → 第3层: web_search → 元数据 + 摘要 → 标记为部分获取 ⚠️
```

### 实测性能（2026年5月真实数据）

| 来源 | 使用层级 | 结果 | 耗时 | 内容量 |
|------|---------|------|------|--------|
| arXiv PDF | 第1层 | ✅ 全文 | 0.8s | 所有章节 |
| bioRxiv PDF | 第1层 | ✅ 全文 | 0.8s | 所有章节 |
| Nature Biotechnology | 第1层 | ✅ 全文 | 1.0s | 117K字符，全部章节 |
| Nature Machine Intelligence | 第1层→2层 | ✅ 全文 | 6.3s | Jina部分→Scrapling补全 |
| Nature Reviews Drug Discovery | 第1层→2层 | ✅ 全文 | 6.8s | 合计149K字符 |
| Elsevier/ScienceDirect | 第3层 | ⚠️ 元数据 | 3s | 仅摘要+引用 |
| Cell / NEJM / Lancet | 第3层 | ⚠️ 元数据 | 3s | 仅摘要+引用 |

## ⚠️ 诚实的局限性

这个工具有用但**并非万能**。以下是它能做和不能做的事。

### 内容获取 — 无法突破的

| 场景 | 现实 | 解决方案 |
|------|------|---------|
| **硬付费墙**（Cell, NEJM, Lancet, JAMA） | 需要机构登录或个人订阅。任何爬虫工具都无法绕过认证访问——也不应该。 | 使用学校/研究所VPN或图书馆。手动下载PDF后作为本地文件提供给Paper Reader。 |
| **机构认证**（SSO, Shibboleth） | 登录大学门户超出了 Skill 的范围。我们不能也不应该自动化凭证访问。 | 手动通过机构下载PDF，然后作为本地文件喂给Paper Reader。 |
| **刚发表的文章** | 部分论文需要数天/数周才能被搜索引擎收录或出现在预印本服务器上。 | 等待预印本发布，或通过机构获取。 |
| **补充材料** | 补充PDF、数据集和代码通常单独托管，可能无法一并获取。 | 单独提供补充材料文件。 |
| **非英语论文** | MinerU 支持中文（`-l ch`）等多种语言，但 Jina Reader 和 web_search 对英语内容效果最好。 | 使用本地PDF + MinerU并指定对应语言参数。 |

### 分析质量 — 你应该知道的

| 方面 | 现实 |
|------|------|
| **第3层（仅元数据）论文** | 归档笔记将缺少详细方法、定量结果和图表描述。会明确标注。 |
| **图表分析** | 取决于AI模型的视觉能力。部分模型（如纯文本LLM）无法分析图表，Skill会回退到提取的图片说明。 |
| **领域检测** | 基于关键词。交叉学科论文（如AI+医学）可能被分入任一领域。你可以覆盖检测结果。 |
| **归档质量 ≠ 亲自读论文** | Skill 生成结构化摘要，不能替代你亲自阅读。重要论文仍需全文精读。 |

### 法律与伦理声明

- **开放获取论文**（arXiv, bioRxiv, PLOS等）：出版商明确允许获取。
- **Nature/Springer Nature**：HTML内容公开可访问（无需登录）。Jina Reader 和 Scrapling 获取的是任何浏览器都能看到的内容。
- **付费内容**：当第1/2层无法获取全文时，我们**不会**尝试绕过认证或突破付费墙。回退到公开可用的元数据（标题、摘要、作者、DOI）。
- **速率限制**：Jina Reader 免费层 20 RPM。Scrapling 请求有节流。我们不会轰炸出版商服务器。
- **一句话总结**：我们获取的是浏览器里公开可见的内容。如果你需要登录才能看到——你应该自己登录。

## 🚀 安装

### 方式一：Git Clone（推荐）

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### 方式二：「懒人科研」法

```
安装这个 skill：https://github.com/Shizukuyu0207/paper-reader

把它 clone 到 ~/.hermes/skills/paper-reader/，
确保 MinerU 已安装（which mineru），如果没有就跳过这一步提醒我。
clone 完成后告诉我安装好了，顺便介绍一下它能干什么。
```

你的 Agent 会搞定剩下的事。喝茶去吧。🍵

### 方式三：手动安装

下载 ZIP 包，解压到 `~/.hermes/skills/paper-reader/`。

### 前置依赖

| 依赖 | 必须 | 安装方式 |
|------|------|---------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ 必须 | 参见 Hermes 文档 |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ 必须 | `pip install mineru` |
| [Jina Reader](https://github.com/jina-ai/reader) | 内置 | 使用 `r.jina.ai` API，无需安装 |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | 推荐 | `pip install scrapling && pip install camoufox && python -m camoufox fetch` |
| Obsidian | 可选 | 用于归档笔记 |

## 📋 快速开始

```bash
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git
ls paper-reader/SKILL.md  # 应该存在
```

在 Hermes 对话中：

```
read this paper https://arxiv.org/abs/2604.18559
```

Skill 会自动检测领域、询问模式、完成剩余工作。

## 📝 归档输出示例

```yaml
---
title: "Artificial allosteric protein switches with ML-designed receptors"
authors: ["Zhong Guo", "David Baker"]
year: 2026
journal: "Nature Biotechnology"
doi: "10.1038/s41587-026-03081-9"
domain: "ai"
tags: [paper/ai, allosteric-switch, biosensor, protein-design]
rating: "5"
---
```

## ⚙️ 配置

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `MINERU` | MinerU 二进制路径 | MinerU 可执行文件路径 |
| `WORK_BASE` | `/tmp/paper-reader` | 临时工作目录 |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian 归档根目录 |
| `JINA_READER` | `https://r.jina.ai` | Jina Reader API 端点 |

## 🤝 贡献

发现 Bug？想添加新的领域检查清单？欢迎 PR。

## 📄 许可证

MIT License — 详见 [LICENSE](../LICENSE)。

## 🙏 致谢

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 提取引擎
- [Jina Reader](https://github.com/jina-ai/reader) — URL 转 Markdown
- [Scrapling](https://github.com/D4Vinci/Scrapling) — 隐身浏览器抓取 + Camoufox
- [Hermes Agent](https://github.com/henvic/hermes) — Agent 框架
- 致敬每一位浏览器里开着 50 个未读论文标签的科研工作者

<div align="center">
为论文太多读不完的科研工作者而建 ❤️
</div>
