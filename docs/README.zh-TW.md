<div align="center">

# 📄 Paper Reader

**基於 MinerU 的學術論文分析 Hermes Agent Skill**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

[Hermes Agent](https://github.com/henvic/hermes) 的學術論文閱讀分析 Skill。支援 PDF 全文提取、智慧領域偵測、深度結構化分析，並自動歸檔到 Obsidian 知識庫。

無論是單篇 arXiv 預印本的快速篩選，還是 10+ 篇跨出版商論文的批次處理，Paper Reader 都能自動完成提取、分類、分析和歸檔。

## 🎯 核心特性

| 特性 | 說明 |
|------|------|
| 🧠 **自動領域偵測** | 5 大領域：分子動力學、醫學、AI/ML、生物資訊學、程式設計 |
| 📊 **3 種閱讀模式** | 快速篩選（3 分鐘）· 深度精讀（全文分析）· 問答（互動式）|
| ⚡ **批次處理** | 平行下載 + MinerU 提取 + 平行分析，支援 Paper Alert |
| 📝 **Obsidian 歸檔** | YAML frontmatter + 結構化 Markdown 筆記 |
| 🔍 **圖表視覺分析** | AI 驅動的關鍵圖表描述與分析 |
| 🔓 **付費牆處理** | Nature/Elsevier/bioRxiv 付費論文自動回退到 web_search |

## 📖 閱讀模式

### 🔍 快速篩選
3 分鐘概覽，判斷論文是否值得精讀。提取標題、摘要、關鍵發現和意義。不建立歸檔。

### 📖 深度精讀
基於領域專用的分析檢查清單進行全文結構化分析。產生完整的 Obsidian 歸檔筆記，包含方法解析、定量結果、限制性和研究啟示。

### 💬 問答模式
互動式問答。可針對論文內容、圖表或方法論提問。可選儲存問答記錄。

### 📦 批次模式（Paper Alert）
同時處理多篇論文，支援混合來源：
- **arXiv PDF** → 直接下載 + MinerU 全文提取
- **付費論文**（Nature、Elsevier、bioRxiv）→ web_search 元資料回退
- **GitHub 儲存庫** → README 分析

## 🗂️ 領域分析清單

| 領域 | 關鍵分析點 |
|------|-----------|
| 🧬 **分子動力學** | 力場、模擬參數、RMSD/RMSF、自由能方法、軌跡分析 |
| 🏥 **醫學** | 研究設計、佇列資訊、統計方法、臨床結果、風險比 |
| 🤖 **AI / ML** | 架構細節、訓練資料、基準測試、SOTA 對比、計算資源 |
| 🔬 **生物資訊學** | 分析管線、統計檢定、基因體組裝、差異表達、富集分析 |
| 💻 **程式設計** | 演算法複雜度、系統設計、實作細節、效能基準 |

## 🚀 安裝

```bash
# 複製到 Hermes skills 目錄
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

或手動將 `paper-reader/` 資料夾複製到 `~/.hermes/skills/paper-reader/`。

### 前置依賴

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 提取引擎
- [Hermes Agent](https://github.com/henvic/hermes) — Agent 框架
- Obsidian 知識庫（可選，用於歸檔筆記）

## 📋 使用方法

```
# 單篇論文 — 本地檔案
讀論文 /path/to/paper.pdf

# 單篇論文 — arXiv
read this paper https://arxiv.org/abs/2604.18559

# 批次 — Paper Alert
Paper Alert:
1. Allosteric Switches https://www.nature.com/articles/s41587-026-03081-9
2. ConforNets https://arxiv.org/abs/2604.18559
3. trRosettaRNA2 https://doi.org/10.1038/s42256-026-01223-x
```

Skill 將自動：取得/驗證 PDF → 偵測領域 → 選擇模式 → 分析 → 歸檔

## 📝 歸檔輸出範例

筆記儲存到 `~/obsidian/papers/{domain}/`，包含完整 YAML frontmatter：

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

後接結構化章節：基本資訊 · 研究問題 · 方法 · 核心結果 · 限制性 · 研究啟示 · 引用網路

## ⚙️ 設定

| 變數 | 預設值 | 說明 |
|------|--------|------|
| `MINERU` | MinerU 二進位路徑 | MinerU 可執行檔路徑 |
| `WORK_BASE` | `/tmp/paper-reader` | 暫存工作目錄 |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian 歸檔根目錄 |
| `EXTRACT_SCRIPT` | `scripts/extract.sh` | 提取輔助指令碼路徑 |

## 📄 授權

MIT License — 詳見 [LICENSE](../LICENSE)。

## 🙏 致謝

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 提取引擎
- [Hermes Agent](https://github.com/henvic/hermes) — Agent 框架
- 為論文太多讀不完的科研工作者而建

<div align="center">
為論文太多讀不完的科研工作者而建 ❤️
</div>
