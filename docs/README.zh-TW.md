     1|<div align="center">
     2|
     3|# 📄 Paper Reader
     4|
     5|**學術論文分析 — Agent 無關管線**
     6|
     7|[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
     8|[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)
     9|
    10|[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)
    11|
    12|</div>
    13|
    14|---
    15|
    16|## ✨ 概述
    17|
    18|自動閱讀、分析和歸檔學術論文——智慧領域偵測 + Obsidian 筆記整合。
    19|
    20|設計為 Agent 無關的管線，相容任意 Agent。適配檔案見 `adapters/`。
    21|
    22|## 🏗️ 架構
    23|
    24|5 階段管線 + 3 層內容獲取策略。
    25|
    26|| 優先級 | 工具 | 速度 | 覆蓋 |
    27||--------|------|------|------|
    28|| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, 大部分 Nature |
    29|| Tier 2 | Scrapling + Camoufox | 5-15s | Nature/Elsevier 補位 |
    30|| Tier 3 | web_search | 2-5s | 硬付費牆 |
    31|| 本地 | MinerU | ~2min/40p | 本地 PDF |
    32|
    33|### 領域：🧬 分子動力學 | 🏥 醫學 | 🤖 AI/ML | 🔬 生物資訊學 | 💻 程式設計
    34|
    35|### 模式：🔍 快速篩選 | 📖 深度精讀+歸檔 | 💬 互動問答 | 📦 批量處理
    36|
    37|## 📊 案例：9 篇論文批量處理
    38|
    39|✅ 全文論文 → 100+行深度歸檔。9篇6分鐘。領域全部正確分類。
    40|⚠️ 付費論文 → 元資料級筆記。ScienceDirect 仍為 Tier 3。
    41|改善：Jina Reader 整合後 4/7 篇元資料級升級為全文。
    42|
    43|## ⚠️ 誠實的侷限性
    44|
    45|- **硬付費牆**（Cell, NEJM, JAMA）：需機構登入 → 手動下載 PDF
    46|- **Tier 3 論文**：歸檔筆記缺方法和定量結果
    47|- 歸檔 ≠ 讀論文。只獲取瀏覽器公開可見內容。
    48|
    49|## 🚀 安裝
    50|
    51|```bash
    52|git clone https://github.com/Shizukuyu0207/paper-reader.git
    53|# Hermes: cp -r paper-reader ~/.hermes/skills/
    54|# 其他 Agent: 見 adapters/
    55|```
    56|
    57|## 📄 許可證
    58|
    59|MIT License — 詳見 [LICENSE](../LICENSE)。
    60|
    61|<div align="center">
    62|為論文太多讀不完的科研工作者而建 ❤️
    63|</div>
    64|