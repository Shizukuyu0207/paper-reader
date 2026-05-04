<div align="center">

# 📄 Paper Reader

**学术论文分析 — 多 Agent 兼容**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-green.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex](https://img.shields.io/badge/Codex-Compatible-blue.svg)](https://github.com/openai/codex)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-orange.svg)](https://opencode.ai)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

Paper Reader 自动阅读、分析和归档学术论文——智能领域检测 + Obsidian 笔记集成。

给它一个 URL、PDF 路径、或一批 10+ 篇论文，自动完成获取、分类、分析和归档。

**兼容 4 种 AI Agent**：Hermes（原生）、Claude Code、OpenAI Codex、OpenCode。

---

## 🤖 多 Agent 适配

核心管线与 Agent 无关——仅加载机制不同。

| Agent | 适配文件 | 安装方式 | 状态 |
|-------|---------|---------|------|
| **Hermes** | `SKILL.md`（原生） | `~/.hermes/skills/paper-reader/` | ✅ 完整支持 |
| **Claude Code** | `adapters/claude-code/` | `~/.claude/commands/paper-reader.md` | ✅ 已测试 |
| **Codex** | `adapters/codex/` | 项目 `AGENTS.md` | ✅ 已测试 |
| **OpenCode** | `adapters/opencode/` | `opencode.json` agent 配置 | ✅ 已测试 |

### 功能对比

| 功能 | Hermes | Claude Code | Codex | OpenCode |
|------|--------|-------------|-------|----------|
| 3层获取策略 | ✅ 内置 | ✅ bash | ✅ bash | ✅ bash |
| 领域检测（5领域） | ✅ 原生 | ✅ 提示词 | ✅ 提示词 | ✅ 提示词 |
| 深度精读+归档 | ✅ | ✅ | ✅ | ✅ |
| 批量并行 | ✅ 内置 | ⚠️ 手动 | ⚠️ 手动 | ⚠️ 手动 |
| 图片视觉分析 | ✅ 内置 | ✅ 内置 | ❌ | ❌ |
| MinerU 集成 | ✅ 脚本 | ✅ bash | ✅ bash | ✅ bash |

### 测试结果（2026-05-04）

测试论文：ConforNets (arXiv:2604.18559)

| Agent | 方式 | 耗时 | 结果 |
|-------|------|------|------|
| Claude Code | `/paper-reader` 命令 | ~50s | ✅ 正确标题+发现 |
| Codex | AGENTS.md + TUI | N/A | ✅ 配置已加载 |
| OpenCode | agent + run 模式 | N/A | ✅ 配置已加载，API调用成功 |

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
| Tier 2 | Scrapling + Camoufox | 5-15s | Tier 1 不完整的 Nature/Elsevier |
| Tier 3 | web_search | 2-5s | 硬付费墙（Cell, NEJM）|
| 本地 | MinerU | ~2min/40p | 本地 PDF 全文+图片 |

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

### 获取结果

| # | 论文 | 来源 | 方法 | 耗时 | 质量 |
|---|------|------|------|------|------|
| 1 | Allosteric Switches (Baker) | Nature NBT | MinerU | 93s | ★★★★★ 全文494行+36图 |
| 2 | ConforNets | arXiv | MinerU | 118s | ★★★★★ 全文646行+75图 |
| 3-8 | 6篇付费/预印本 | 混合 | web_search | ~5s各 | ★★☆☆☆ 仅元数据 |
| 9 | lightning-boltz | GitHub | README | ~3s | ★★☆☆☆ 仓库信息 |

**总耗时**: ~6分钟 | **改善**: Jina Reader 整合后，4/7 元数据级论文升级为全文

### 客观评价

✅ PDF 可用论文深度分析优秀 | ✅ 批量6分钟处理9篇 | ⚠️ 付费论文缺方法细节 | ⚠️ Elsevier 仍为 Tier 3

---

## ⚠️ 诚实的局限性

- **硬付费墙**（Cell, NEJM, JAMA）：需机构登录，不尝试绕过 → 手动下载 PDF
- **Tier 3 论文**：归档笔记缺详细方法和定量结果
- **arXiv 摘要页**：内容比 PDF 少，需用 `pdf/` 链接
- **图片分析**：依赖 AI 视觉能力，纯文字模型回退到图片标题

### 法律与伦理

获取浏览器公开可见内容。需登录才能看到的——应自行登录。

---

## 🚀 安装

### Hermes Agent（推荐）

```bash
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### Claude Code

```bash
mkdir -p ~/.claude/commands
cp paper-reader/adapters/claude-code/commands/paper-reader.md ~/.claude/commands/
# 使用: /paper-reader https://arxiv.org/abs/2604.18559
```

### Codex

```bash
cp paper-reader/adapters/codex/AGENTS.md ./AGENTS.md
# 在含 AGENTS.md 的目录中: codex "Read this paper: ..."
```

### OpenCode

```bash
# 将 agent-config.json 内容添加到你的 opencode.json
# 使用: opencode run --agent paper-reader "..."
```

---

## 📁 项目结构

```
paper-reader/
├── SKILL.md              # Hermes skill 定义
├── adapters/             # 多 Agent 适配文件
│   ├── claude-code/      # Claude Code slash 命令
│   ├── codex/            # Codex AGENTS.md
│   └── opencode/         # OpenCode agent 配置
├── scripts/              # MinerU + fetch 脚本
├── references/           # 领域清单 + 模板
└── docs/                 # 6语言 README
```

---

## 🤝 贡献

欢迎 PR，特别是新的 Agent 适配器（Cursor、Aider、Continue 等）。

## 📄 许可证

MIT License — 详见 [LICENSE](../LICENSE)。

## 🙏 致谢

MinerU · Jina Reader · Scrapling · Hermes · Claude Code · Codex · OpenCode
致敬每一位浏览器里开着 50 个未读论文标签的科研工作者

<div align="center">
为论文太多读不完的科研工作者而建 ❤️
</div>
