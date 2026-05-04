<div align="center">

# 📄 Paper Reader

**學術論文分析 Hermes Agent Skill — MinerU + Jina Reader + Scrapling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概述

[Hermes Agent](https://github.com/henvic/hermes) 的學術論文閱讀分析 Skill。支援 3 層智慧獲取、自動領域偵測、深度結構化分析，並自動歸檔到 Obsidian 知識庫。

## 🎯 核心特性

| 特性 | 說明 |
|------|------|
| 🧠 **自動領域偵測** | 5 大領域：分子動力學、醫學、AI/ML、生物資訊學、程式設計 |
| 📊 **3 種閱讀模式** | 快速篩選（3 分鐘）· 深度精讀（全文分析）· 問答（互動式）|
| ⚡ **3 層內容獲取** | Jina Reader → Scrapling 隱身瀏覽器 → web_search 回退 |
| 📝 **Obsidian 歸檔** | YAML frontmatter + 結構化 Markdown 筆記 |
| 🔍 **圖表視覺分析** | AI 驅動的關鍵圖表描述與分析 |
| 📦 **批次處理** | 平行獲取 + 平行分析，支援 Paper Alert |

## 🔗 內容獲取 — 3 層策略

沒有魔法——只有分層的降級策略和誠實的取捨。

| 層級 | 工具 | 速度 | 輸出 | 適用於 |
|------|------|------|------|--------|
| **第1層** | [Jina Reader](https://github.com/jina-ai/reader) | 1-2s | Markdown | arXiv, bioRxiv, 開放取用, 多數 Nature 文章 |
| **第2層** | [Scrapling](https://github.com/D4Vinci/Scrapling) + Camoufox | 5-15s | HTML 文字 | 第1層失敗, Nature/Elsevier 部分內容 |
| **第3層** | web_search | 2-5s | 僅元資料 | 硬付費牆（Cell, NEJM, Lancet） |

### 實測效能（2026年5月真實資料）

| 來源 | 層級 | 結果 | 耗時 | 內容量 |
|------|------|------|------|--------|
| arXiv PDF | 第1層 | ✅ 全文 | 0.8s | 所有章節 |
| bioRxiv PDF | 第1層 | ✅ 全文 | 0.8s | 所有章節 |
| Nature Biotechnology | 第1層 | ✅ 全文 | 1.0s | 117K字元 |
| Nature Machine Intelligence | 第1→2層 | ✅ 全文 | 6.3s | Jina部分→Scrapling補全 |
| Elsevier/ScienceDirect | 第3層 | ⚠️ 元資料 | 3s | 僅摘要+引用 |

## ⚠️ 誠實的限制

這個工具有用但**並非萬能**。

### 無法突破的

| 場景 | 現實 | 解決方案 |
|------|------|---------|
| **硬付費牆**（Cell, NEJM, JAMA） | 需要機構登入或個人訂閱 | 使用學校/研究所VPN，手動下載PDF後作為本地檔案提供 |
| **機構認證**（SSO, Shibboleth） | 登入大學門戶超出 Skill 範圍 | 手動下載PDF，再提供給 Paper Reader |
| **剛發表的文章** | 部分需數天/數週才被收錄 | 等待預印本發布或透過機構取得 |
| **補充材料** | 通常單獨託管 | 單獨提供補充材料檔案 |

### 法律與倫理聲明

- 我們獲取的是**瀏覽器裡公開可見的內容**。如果你需要登入才能看到——你應該自己登入。
- 開放取用論文：出版商明確允許獲取。
- 付費內容：不嘗試繞過認證或突破付費牆，回退到公開元資料。
- 速率限制：Jina Reader 免費層 20 RPM，不會轟炸出版商伺服器。

## 🚀 安裝

### 方式一：Git Clone（推薦）

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### 方式二：「懶人科研」法

```
安裝這個 skill：https://github.com/Shizukuyu0207/paper-reader

把它 clone 到 ~/.hermes/skills/paper-reader/，
確保 MinerU 已安裝（which mineru），如果沒有就跳過這一步提醒我。
clone 完成後告訴我安裝好了，順便介紹一下它能幹什麼。
```

喝茶去吧。🍵

### 前置依賴

| 依賴 | 必要 | 安裝方式 |
|------|------|---------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ 必要 | 參見 Hermes 文件 |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ 必要 | `pip install mineru` |
| [Jina Reader](https://github.com/jina-ai/reader) | 內建 | 使用 `r.jina.ai` API |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | 推薦 | `pip install scrapling camoufox && python -m camoufox fetch` |
| Obsidian | 可選 | 用於歸檔筆記 |

## ⚙️ 設定

| 變數 | 預設值 | 說明 |
|------|--------|------|
| `MINERU` | MinerU 二進位路徑 | MinerU 可執行檔路徑 |
| `WORK_BASE` | `/tmp/paper-reader` | 暫存工作目錄 |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian 歸檔根目錄 |
| `JINA_READER` | `https://r.jina.ai` | Jina Reader API 端點 |

## 🤝 貢獻

發現 Bug？想新增新的領域檢查清單？歡迎 PR。

## 📄 授權

MIT License — 詳見 [LICENSE](../LICENSE)。

## 🙏 致謝

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 提取引擎
- [Jina Reader](https://github.com/jina-ai/reader) — URL 轉 Markdown
- [Scrapling](https://github.com/D4Vinci/Scrapling) — 隱身瀏覽器抓取
- [Hermes Agent](https://github.com/henvic/hermes) — Agent 框架
- 致敬每一位瀏覽器裡開著 50 個未讀論文分頁的科研工作者

<div align="center">
為論文太多讀不完的科研工作者而建 ❤️
</div>
