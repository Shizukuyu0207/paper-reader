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

[Hermes Agent](https://github.com/henvic/hermes) 的学术论文阅读分析 Skill。给它一个 URL、一个 PDF 路径、或一批 10+ 篇论文——自动完成内容获取、领域分类、深度分析和归档。

---

## 🏗️ 架构

Paper Reader 是一个 5 阶段管线，配备 3 层内容获取策略。每个阶段模块化、独立可配置。

```
┌─────────────────────────────────────────────────────────────┐
│                    Paper Reader 管线                          │
│                                                               │
│  ┌─────────┐   ┌──────────┐   ┌──────────┐   ┌──────┐   ┌──────┐ │
│  │ 阶段 1  │──▶│ 阶段 2   │──▶│ 阶段 3   │──▶│阶段 4│──▶│阶段 5│ │
│  │  获取   │   │  检测    │   │  选择    │   │ 执行 │   │ 输出 │ │
│  └─────────┘   └──────────┘   └──────────┘   └──────┘   └──────┘ │
│       │                              │                        │
│  ┌────┴───────────────────┐   ┌─────┴──────┐                │
│  │ 3层内容获取策略        │   │ 领域清单   │                │
│  │ ① Jina Reader (1-2s)  │   │ · MD / 医学│                │
│  │ ② Scrapling   (5-15s) │   │ · AI / 生信│                │
│  │ ③ web_search  (2-5s)  │   │ · 编程     │                │
│  └────────────────────────┘   └────────────┘                │
└─────────────────────────────────────────────────────────────┘
```

### 阶段说明

| 阶段 | 功能 | 细节 |
|------|------|------|
| **1. 获取** | 解析输入 + 3层策略获取内容 | URL/DOI/arXiv ID/本地路径 → Markdown/HTML/元数据 |
| **2. 检测** | 关键词匹配 + 用户确认 | 5领域：MD、医学、AI/ML、生信、编程 |
| **3. 选择** | 交互式模式选择 | 快速筛选 / 深度精读 / 问答 / 批量 |
| **4. 执行** | 领域清单驱动的结构化分析 | 加载领域专用检查清单 + 归档模板 |
| **5. 输出** | Obsidian 归档 + 对话摘要 | YAML frontmatter + 结构化 Markdown |

### 领域专用分析清单

| 领域 | 关键分析点 |
|------|-----------|
| 🧬 **分子动力学** | 力场、模拟参数、RMSD/RMSF、自由能方法、轨迹分析 |
| 🏥 **医学** | 研究设计、队列信息、统计方法、临床结局、风险比 |
| 🤖 **AI / ML** | 架构细节、训练数据、基准测试、SOTA 对比、计算资源 |
| 🔬 **生物信息学** | 分析管线、统计检验、基因组组装、差异表达、富集分析 |
| 💻 **编程** | 算法复杂度、系统设计、实现细节、性能基准 |

---

## 📊 案例：9篇论文批量处理（2026年5月）

一个真实的 Paper Alert 被端到端处理。以下是客观分析。

### 获取结果

| # | 论文 | 来源 | 方法 | 耗时 | 内容质量 |
|---|------|------|------|------|---------|
| 1 | Allosteric Switches (Baker) | Nature NBT | MinerU(PDF) | 93s | ★★★★★ 全文, 494行, 36图 |
| 2 | ConforNets (AlQuraishi) | arXiv PDF | MinerU(PDF) | 118s | ★★★★★ 全文, 646行, 75图 |
| 3 | Closing the Loop | ScienceDirect | web_search | ~5s | ★★☆☆☆ 仅元数据+摘要 |
| 4 | trRosettaRNA2 | Nature NMI | web_search | ~5s | ★★☆☆☆ 仅元数据+摘要 |
| 5 | Target ID (英矽智能) | Nature NRDD | web_search | ~5s | ★★★☆☆ 丰富元数据（综述文） |
| 6 | ERAST | Nature NBT | web_search | ~5s | ★★☆☆☆ 仅元数据 |
| 7 | AlphaFast | bioRxiv | web_search | ~5s | ★★☆☆☆ 仅元数据 |
| 8 | Flow Matching | Nature NMI | web_search | ~5s | ★★☆☆☆ 仅元数据 |
| 9 | lightning-boltz | GitHub | README扫描 | ~3s | ★★☆☆☆ 仓库信息 |

**总耗时**: ~6分钟（MinerU串行 + 7篇并行搜索）

### 集成 Jina Reader + Scrapling 后的复测

| 论文 | 之前结果 | Jina Reader 后 | 改善 |
|------|---------|---------------|------|
| Allosteric Switches | MinerU 93s（全文） | **Jina 1.0s, 117K字符** | 快93倍，质量相同 |
| ConforNets | MinerU 118s（全文） | **Jina 2.2s, 9K字符** | 快54倍，但仅摘要页 |
| Target ID (NRDD) | web_search（元数据） | **Jina 1.3s, 149K字符** | 元数据→**全文** |
| ERAST (NBT) | web_search（元数据） | **Jina 1.0s, 全文** | 元数据→**全文** |

### 客观评价

**做得好的：**
- PDF可用论文（#1-2）：深度归档笔记 100+ 行，含定量结果和图表描述
- 批量处理：9篇6分钟 vs. 手动30+分钟
- 领域检测：9篇全部正确分类

**不够理想的：**
- 付费论文（#3-8，集成前）：归档笔记仅34-53行——元数据够用，但缺方法细节
- MinerU 严格串行——93s + 118s 阻塞了其他工作
- arXiv 摘要页 URL 比直接 PDF 链接内容少

**集成 Jina + Scrapling 后的改善：**
- 7篇元数据级论文中 4 篇现在可获取全文
- MinerU 对在线论文不再必需（仅用于本地PDF）
- 之前超时的 Nature 文章现在1-2秒返回

**仍存在的差距：**
- ScienceDirect/Elsevier：仍为第3层（404或付费墙）
- arXiv 摘要页给的是概要，不是全文。必须用 `arxiv.org/pdf/` 链接

---

## ⚠️ 诚实的局限性

这个工具有用但**并非万能**。

### 无法突破的

| 场景 | 现实 | 解决方案 |
|------|------|---------|
| **硬付费墙**（Cell, NEJM, JAMA） | 需机构登录或个人订阅 | 用学校/研究所VPN，手动下载PDF |
| **机构认证**（SSO, Shibboleth） | 超出 Skill 范围 | 手动下载PDF，再提供给Paper Reader |
| **刚发表的文章** | 可能数天/数周才被收录 | 等待预印本或通过机构获取 |
| **补充材料** | 通常单独托管 | 单独提供 |

### 法律与伦理

- 我们获取的是**浏览器里公开可见的内容**。如果你需要登录才能看到——你应该自己登录。
- 开放获取：出版商明确允许。
- 付费内容：不尝试绕过认证，回退到公开元数据。
- 速率限制：Jina Reader 免费20RPM，不轰炸出版商服务器。

---

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

喝茶去吧。🍵

### 前置依赖

| 依赖 | 必须 | 安装方式 |
|------|------|---------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ | 参见文档 |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ | `pip install mineru` |
| [Jina Reader](https://github.com/jina-ai/reader) | 内置 | `r.jina.ai` API |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | 推荐 | `pip install scrapling camoufox && python -m camoufox fetch` |
| Obsidian | 可选 | 归档笔记 |

---

## ⚙️ 配置

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `MINERU` | MinerU 路径 | MinerU 可执行文件路径 |
| `WORK_BASE` | `/tmp/paper-reader` | 临时工作目录 |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian 归档根目录 |
| `JINA_READER` | `https://r.jina.ai` | Jina Reader API 端点 |

---

## 🤝 贡献

欢迎 PR。

## 📄 许可证

MIT License — 详见 [LICENSE](../LICENSE)。

## 🙏 致谢

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 提取引擎
- [Jina Reader](https://github.com/jina-ai/reader) — URL 转 Markdown
- [Scrapling](https://github.com/D4Vinci/Scrapling) — 隐身浏览器抓取
- [Hermes Agent](https://github.com/henvic/hermes) — Agent 框架
- 致敬每一位浏览器里开着 50 个未读论文标签的科研工作者

<div align="center">
为论文太多读不完的科研工作者而建 ❤️
</div>
