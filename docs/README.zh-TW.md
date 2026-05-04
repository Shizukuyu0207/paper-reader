<div align="center">

# 📄 Paper Reader

**學術論文分析 — Agent 無關管線**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

自動閱讀、分析和歸檔學術論文——智慧領域偵測 + Obsidian 筆記整合。

設計為 Agent 無關的管線，相容任意 Agent。適配檔案見 `adapters/`。

## 🏗️ 架構

5 階段管線 + 3 層內容獲取策略。

| 優先級 | 工具 | 速度 | 覆蓋 |
|--------|------|------|------|
| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, 大部分 Nature |
| Tier 2 | Scrapling + Camoufox | 5-15s | Nature/Elsevier 補位 |
| Tier 3 | web_search | 2-5s | 硬付費牆 |
| 本地 | MinerU | ~2min/40p | 本地 PDF |

### 領域：🧬 分子動力學 | 🏥 醫學 | 🤖 AI/ML | 🔬 生物資訊學 | 💻 程式設計

### 模式：🔍 快速篩選 | 📖 深度精讀+歸檔 | 💬 互動問答 | 📦 批量處理

## 📊 案例：9 篇論文批量處理

✅ 全文論文 → 100+行深度歸檔。9篇6分鐘。領域全部正確分類。
⚠️ 付費論文 → 元資料級筆記。ScienceDirect 仍為 Tier 3。
改善：Jina Reader 整合後 4/7 篇元資料級升級為全文。

## ⚠️ 誠實的侷限性

- **硬付費牆**（Cell, NEJM, JAMA）：需機構登入 → 手動下載 PDF
- **Tier 3 論文**：歸檔筆記缺方法和定量結果
- 歸檔 ≠ 讀論文。只獲取瀏覽器公開可見內容。

## 🚀 安裝

```bash
git clone https://github.com/Shizukuyu0207/paper-reader.git
# Hermes: cp -r paper-reader ~/.hermes/skills/
# 其他 Agent: 見 adapters/
```

## 📄 許可證

MIT License — 詳見 [LICENSE](../LICENSE)。

<div align="center">
為論文太多讀不完的科研工作者而建 ❤️
</div>
