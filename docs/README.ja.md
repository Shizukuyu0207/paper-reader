<div align="center">

# 📄 Paper Reader

**学術論文分析 — エージェント非依存パイプライン**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概要

学術論文の自動読解・分析・アーカイブ。インテリジェントな領域検出 + Obsidian 統合。

エージェント非依存のパイプライン設計。任意のエージェントに対応。適合ファイルは `adapters/` を参照。

## 🏗️ アーキテクチャ

5段階パイプライン + 3層コンテンツ取得。

| 優先度 | ツール | 速度 | カバー |
|--------|--------|------|--------|
| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, 大部分のNature |
| Tier 2 | Scrapling | 5-15s | Nature/Elsevier補完 |
| Tier 3 | web_search | 2-5s | ペイウォール |
| ローカル | MinerU | ~2分/40p | ローカルPDF |

### 領域：🧬 分子動力学 | 🏥 医学 | 🤖 AI/ML | 🔬 バイオインフォ | 💻 プログラミング

### モード：🔍 クイックスキャン | 📖 ディープリード+アーカイブ | 💬 Q&A | 📦 バッチ

## 📊 ケース：9論文バッチ処理

✅ フルテキスト論文 → 100行以上の深いアーカイブ。9編6分。
⚠️ ペイウォール論文 → メタデータのみ。Elsevier は Tier 3。
改善：Jina Reader 導入後 4/7編がメタデータからフルテキストに改善。

## ⚠️ 正直な限界

- **ハードペイウォール** (Cell, NEJM, JAMA): 機関ログイン必要 → PDF手動ダウンロード
- **Tier 3論文**: 詳細な方法・定量的結果なし
- ブラウザで公開閲覧可能なコンテンツのみ取得

## 🚀 インストール

```bash
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

## 📄 ライセンス

MIT License — [LICENSE](../LICENSE) 参照。

<div align="center">
論文を読みきれない研究者のために ❤️
</div>
