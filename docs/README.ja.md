<div align="center">

# 📄 Paper Reader

**学術論文分析 Hermes Agent Skill — MinerU + Jina Reader + Scrapling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概要

[Hermes Agent](https://github.com/henvic/hermes) 用の学術論文読解スキル。URL・PDFパス・10+編のバッチ入力に対応し、コンテンツ取得・領域分類・深い分析・アーカイブを自動化します。

## 🏗️ アーキテクチャ

5段階パイプライン + 3層コンテンツ取得戦略。各段階はモジュラー設計。

```
取得(3層) → 領域検出(5領域) → モード選択(4モード) → 領域チェックリスト駆動分析 → Obsidianアーカイブ
```

### 3層コンテンツ取得

| 優先度 | ツール | 速度 | カバー範囲 |
|--------|--------|------|-----------|
| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, ほとんどのNature |
| Tier 2 | Scrapling + Camoufox | 5-15s | Tier 1で不完全なNature/Elsevier |
| Tier 3 | web_search | 2-5s | ハードペイウォール (Cell, NEJM) |
| ローカル | MinerU | ~2分/40p | ローカルPDF全文+画像 |

### 領域別分析チェックリスト

| 領域 | 主要分析ポイント |
|------|-----------------|
| 🧬 分子動力学 | 力場、シミュレーション参数、RMSD/RMSF、自由エネルギー |
| 🏥 医学 | 研究デザイン、コホート、統計方法、臨床転帰、ハザード比 |
| 🤖 AI / ML | アーキテクチャ、訓練データ、ベンチマーク、SOTA比較 |
| 🔬 バイオインフォマティクス | 分析パイプライン、統計検定、配列解析、発現差分析 |
| 💻 プログラミング | アルゴリズム複雑度、システム設計、パフォーマンス |

## 📊 ケース：9論文バッチ処理（2026年5月）

| # | 論文 | ソース | 方法 | 時間 | 品質 |
|---|------|--------|------|------|------|
| 1 | Allosteric Switches | Nature NBT | MinerU | 93s | ★★★★★ 全文494行+36図 |
| 2 | ConforNets | arXiv | MinerU | 118s | ★★★★★ 全文646行+75図 |
| 3-8 | 6編ペイウォール/プレプリント | 混合 | web_search | ~5s各 | ★★☆☆☆ メタデータのみ |
| 9 | lightning-boltz | GitHub | README | ~3s | ★★☆☆☆ リポ情報 |

**合計**: ~6分 | Jina Reader導入後、7編中4編が全文取得可能に改善

### 客観的評価

✅ PDF利用可能論文の深い分析は優秀 | ✅ バッチ9編6分処理 | ⚠️ ペイウォール論文は方法詳細不足 | ⚠️ Elsevierは依然Tier 3

## ⚠️ 正直な限界

- **ハードペイウォール**（Cell, NEJM, JAMA）: 機関ログインが必要 → PDFを手動ダウンロード
- **Tier 3論文**: アーカイブノートに詳細な方法・定量的結果なし
- **arXiv要約ページ**: PDFリンクより内容が少ない

### 法的・倫理的立場

ブラウザで公開閲覧可能なコンテンツのみ取得。ログインが必要なものは自身でログインしてください。

## 🚀 インストール

```bash
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git
```

## 📄 ライセンス

MIT License — [LICENSE](../LICENSE) 参照。

<div align="center">
論文を読みきれない研究者のために ❤️
</div>
