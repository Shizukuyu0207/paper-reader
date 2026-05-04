<div align="center">

# 📄 Paper Reader

**學術論文分析 Hermes Agent Skill — MinerU + Jina Reader + Scrapling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

[Hermes Agent](https://github.com/henvic/hermes) 的學術論文閱讀分析 Skill。支援 URL、PDF 路徑或批量 10+ 篇論文的端到端處理——自動內容獲取、領域分類、深度分析與歸檔。

## 🏗️ 架構

5 階段管線 + 3 層內容獲取策略，各階段模組化獨立可配置。

```
獲取(3層) → 領域檢測(5領域) → 模式選擇(4模式) → 領域清單驅動分析 → Obsidian歸檔
```

### 3 層內容獲取

| 優先級 | 工具 | 速度 | 覆蓋 |
|--------|------|------|------|
| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, 大部分 Nature |
| Tier 2 | Scrapling + Camoufox | 5-15s | Tier 1 不完整的 Nature/Elsevier |
| Tier 3 | web_search | 2-5s | 硬付費牆（Cell, NEJM）|
| 本地 | MinerU | ~2min/40p | 本地 PDF 全文+圖片 |

### 領域分析清單

| 領域 | 關鍵分析點 |
|------|-----------|
| 🧬 分子動力學 | 力場、模擬參數、RMSD/RMSF、自由能、軌跡分析 |
| 🏥 醫學 | 研究設計、佇列、統計方法、臨床結局、風險比 |
| 🤖 AI / ML | 架構、訓練資料、基準測試、SOTA、計算資源 |
| 🔬 生物資訊學 | 分析管線、統計檢驗、定序、差異表達、富集分析 |
| 💻 程式設計 | 演算法複雜度、系統設計、效能基準 |

## 📊 案例：9 篇論文批量處理（2026年5月）

### 獲取結果

| # | 論文 | 來源 | 方法 | 耗時 | 品質 |
|---|------|------|------|------|------|
| 1 | Allosteric Switches | Nature NBT | MinerU | 93s | ★★★★★ 全文494行+36圖 |
| 2 | ConforNets | arXiv | MinerU | 118s | ★★★★★ 全文646行+75圖 |
| 3-8 | 6篇付費/預印本 | 混合 | web_search | ~5s各 | ★★☆☆☆ 僅元資料 |
| 9 | lightning-boltz | GitHub | README | ~3s | ★★☆☆☆ 倉庫資訊 |

**總耗時**: ~6分鐘 | **改善**: Jina Reader 整合後，4/7 元資料級論文升級為全文

### 客觀評價

✅ PDF 可用論文深度分析優秀 | ✅ 批量6分鐘處理9篇 | ⚠️ 付費論文缺方法細節 | ⚠️ Elsevier 仍為 Tier 3

## ⚠️ 誠實的侷限性

- **硬付費牆**（Cell, NEJM, JAMA）：需機構登入，不嘗試繞過 → 手動下載 PDF
- **Tier 3 論文**：歸檔筆記缺詳細方法和定量結果
- **arXiv 摘要頁**：內容比 PDF 少，需用 `pdf/` 連結
- **圖表分析**：依賴 AI 視覺能力，純文字模型回退到圖片標題

### 法律與倫理

獲取瀏覽器公開可見內容。需登入才能看到的——應自行登入。

## 🚀 安裝

```bash
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git
```

或直接讓 Hermes Agent 處理：
```
安裝 skill：https://github.com/Shizukuyu0207/paper-reader
```

## 📄 許可證

MIT License — 詳見 [LICENSE](../LICENSE)。

<div align="center">
為論文太多讀不完的科研工作者而建 ❤️
</div>
