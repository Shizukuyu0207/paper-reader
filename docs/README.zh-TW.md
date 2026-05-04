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

### 方式一：Git Clone（推薦）

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### 方式二：「懶人科研」法

不想碰終端機？直接把這個倉庫連結甩給你的 Hermes Agent，然後複製貼上：

```
安裝這個 skill：https://github.com/Shizukuyu0207/paper-reader

把它 clone 到 ~/.hermes/skills/paper-reader/，
確保 MinerU 已安裝（which mineru），如果沒有就跳過這一步提醒我。
clone 完成後告訴我安裝好了，順便介紹一下它能幹什麼。
```

你的 Agent 會搞定剩下的事。喝茶去吧。🍵

### 方式三：手動安裝

下載 ZIP 包，解壓到 `~/.hermes/skills/paper-reader/`。

### 前置依賴

| 依賴 | 必要 | 安裝方式 |
|------|------|---------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ 必要 | 參見 Hermes 文件 |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ 必要 | `pip install mineru` 或參見其 README |
| Obsidian | 可選 | 用於歸檔筆記 |

## 📋 快速開始

```bash
# 1. 安裝
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git

# 2. 驗證
ls paper-reader/SKILL.md  # 應該存在

# 3. 使用（在 Hermes 對話中）
```

然後在 Hermes 對話中：

```
read this paper https://arxiv.org/abs/2604.18559
```

就這樣。Skill 會自動偵測領域、詢問模式、完成剩餘工作。

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

## 🤝 貢獻

發現 Bug？想新增新的領域檢查清單？歡迎 PR。

1. Fork 本倉庫
2. 建立分支 (`git checkout -b feature/my-feature`)
3. 提交 (`git commit -m 'Add my feature'`)
4. 推送 (`git push origin feature/my-feature`)
5. 發起 Pull Request

## 📄 授權

MIT License — 詳見 [LICENSE](../LICENSE)。

## 🙏 致謝

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 提取引擎
- [Hermes Agent](https://github.com/henvic/hermes) — Agent 框架
- 致敬每一位瀏覽器裡開著 50 個未讀論文分頁的科研工作者

<div align="center">
為論文太多讀不完的科研工作者而建 ❤️
</div>
