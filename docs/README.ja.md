     1|<div align="center">
     2|
     3|# 📄 Paper Reader
     4|
     5|**学術論文分析 — エージェント非依存パイプライン**
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
    16|## ✨ 概要
    17|
    18|学術論文の自動読解・分析・アーカイブ。インテリジェントな領域検出 + Obsidian 統合。
    19|
    20|エージェント非依存のパイプライン設計。任意のエージェントに対応。適合ファイルは `adapters/` を参照。
    21|
    22|## 🏗️ アーキテクチャ
    23|
    24|5段階パイプライン + 3層コンテンツ取得。
    25|
    26|| 優先度 | ツール | 速度 | カバー |
    27||--------|--------|------|--------|
    28|| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, 大部分のNature |
    29|| Tier 2 | Scrapling | 5-15s | Nature/Elsevier補完 |
    30|| Tier 3 | web_search | 2-5s | ペイウォール |
    31|| ローカル | MinerU | ~2分/40p | ローカルPDF |
    32|
    33|### 領域：🧬 分子動力学 | 🏥 医学 | 🤖 AI/ML | 🔬 バイオインフォ | 💻 プログラミング
    34|
    35|### モード：🔍 クイックスキャン | 📖 ディープリード+アーカイブ | 💬 Q&A | 📦 バッチ
    36|
    37|## 📊 ケース：9論文バッチ処理
    38|
    39|✅ フルテキスト論文 → 100行以上の深いアーカイブ。9編6分。
    40|⚠️ ペイウォール論文 → メタデータのみ。Elsevier は Tier 3。
    41|改善：Jina Reader 導入後 4/7編がメタデータからフルテキストに改善。
    42|
    43|## ⚠️ 正直な限界
    44|
    45|- **ハードペイウォール** (Cell, NEJM, JAMA): 機関ログイン必要 → PDF手動ダウンロード
    46|- **Tier 3論文**: 詳細な方法・定量的結果なし
    47|- ブラウザで公開閲覧可能なコンテンツのみ取得
    48|
    49|## 🚀 インストール
    50|
    51|```bash
    52|git clone https://github.com/Shizukuyu0207/paper-reader.git
    53|```
    54|
    55|## 📄 ライセンス
    56|
    57|MIT License — [LICENSE](../LICENSE) 参照。
    58|
    59|<div align="center">
    60|論文を読みきれない研究者のために ❤️
    61|</div>
    62|