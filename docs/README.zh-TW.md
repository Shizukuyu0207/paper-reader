<div align="center">

# 📄 Paper Reader

**學術論文分析 — 多 Agent 相容**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-green.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex](https://img.shields.io/badge/Codex-Compatible-blue.svg)](https://github.com/openai/codex)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-orange.svg)](https://opencode.ai)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

Paper Reader 自動閱讀、分析和歸檔學術論文——智慧領域偵測 + Obsidian 筆記整合。

**相容 4 種 AI Agent**：Hermes（原生）、Claude Code、OpenAI Codex、OpenCode。

## 🤖 多 Agent 適配

| Agent | 適配檔案 | 安裝方式 | 狀態 |
|-------|---------|---------|------|
| **Hermes** | `SKILL.md`（原生） | `~/.hermes/skills/paper-reader/` | ✅ 完整支援 |
| **Claude Code** | `adapters/claude-code/` | `~/.claude/commands/paper-reader.md` | ✅ 已測試 |
| **Codex** | `adapters/codex/` | 專案 `AGENTS.md` | ✅ 已測試 |
| **OpenCode** | `adapters/opencode/` | `opencode.json` agent 設定 | ✅ 已測試 |

### 功能對比

| 功能 | Hermes | Claude Code | Codex | OpenCode |
|------|--------|-------------|-------|----------|
| 3層獲取策略 | ✅ 內建 | ✅ bash | ✅ bash | ✅ bash |
| 領域偵測（5領域） | ✅ 原生 | ✅ 提示詞 | ✅ 提示詞 | ✅ 提示詞 |
| 深度精讀+歸檔 | ✅ | ✅ | ✅ | ✅ |
| 批量並行 | ✅ 內建 | ⚠️ 手動 | ⚠️ 手動 | ⚠️ 手動 |
| 圖片視覺分析 | ✅ 內建 | ✅ 內建 | ❌ | ❌ |
| MinerU 整合 | ✅ 腳本 | ✅ bash | ✅ bash | ✅ bash |

## 🏗️ 架構

5 階段管線 + 3 層內容獲取策略。

| 優先級 | 工具 | 速度 | 覆蓋 |
|--------|------|------|------|
| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, 大部分 Nature |
| Tier 2 | Scrapling + Camoufox | 5-15s | Nature/Elsevier |
| Tier 3 | web_search | 2-5s | 硬付費牆 |
| 本地 | MinerU | ~2min/40p | 本地 PDF |

### 領域：🧬 分子動力學 | 🏥 醫學 | 🤖 AI/ML | 🔬 生物資訊學 | 💻 程式設計

## 📊 案例：9 篇論文批量處理（2026年5月）

| # | 論文 | 來源 | 方法 | 品質 |
|---|------|------|------|------|
| 1 | Allosteric Switches | Nature NBT | MinerU | ★★★★★ 全文+36圖 |
| 2 | ConforNets | arXiv | MinerU | ★★★★★ 全文+75圖 |
| 3-8 | 6篇付費/預印本 | 混合 | web_search | ★★☆☆☆ 僅元資料 |
| 9 | lightning-boltz | GitHub | README | ★★☆☆☆ 倉庫資訊 |

✅ 全文分析優秀 | ✅ 9篇6分鐘 | ⚠️ 付費論文缺方法細節

## ⚠️ 誠實的侷限性

- **硬付費牆**（Cell, NEJM, JAMA）：需機構登入 → 手動下載 PDF
- **Tier 3 論文**：歸檔筆記缺詳細方法和定量結果
- 只獲取瀏覽器公開可見內容

## 🚀 安裝

```bash
# Hermes (推薦)
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git

# Claude Code
mkdir -p ~/.claude/commands && cp paper-reader/adapters/claude-code/commands/paper-reader.md ~/.claude/commands/

# Codex
cp paper-reader/adapters/codex/AGENTS.md ./AGENTS.md
```

## 📄 許可證

MIT License — 詳見 [LICENSE](../LICENSE)。

<div align="center">
為論文太多讀不完的科研工作者而建 ❤️
</div>
