<div align="center">

# 📄 Paper Reader

**MinerU を活用した学術論文分析 Hermes Agent Skill**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概要

[Hermes Agent](https://github.com/henvic/hermes) 用の学術論文読解・分析 Skill。PDF 全文抽出、インテリジェントな分野検出、深い構造化分析をサポートし、Obsidian ボールトに自動アーカイブします。

単一の arXiv プレプリントのスクリーニングから、10本以上の複数出版社の論文の一括処理まで、Paper Reader が抽出・分類・分析・アーカイブを自動で行います。

## 🎯 主要機能

| 機能 | 説明 |
|------|------|
| 🧠 **自動分野検出** | 5分野：分子動力学、医学、AI/ML、バイオインフォマティクス、プログラミング |
| 📊 **3つの読解モード** | クイックスキャン（3分）· 深い読解（全文分析）· Q&A（対話型）|
| ⚡ **一括処理** | 並列ダウンロード + MinerU 抽出 + 並列分析、Paper Alert 対応 |
| 📝 **Obsidian アーカイブ** | YAML frontmatter + 構造化 Markdown ノート |
| 🔍 **図表の視覚分析** | AI による主要図表の記述と分析 |
| 🔓 **ペイウォール対応** | Nature/Elsevier/bioRxiv の有料論文は web_search に自動フォールバック |

## 📖 読解モード

### 🔍 クイックスキャン
3分で概要を把握し、精読する価値があるか判断。タイトル、要約、主要な発見、意義を抽出。アーカイブは作成されません。

### 📖 深い読解
分野固有の分析チェックリストに基づく全文構造化分析。手法の詳細、定量的結果、限界、研究への示唆を含む包括的な Obsidian アーカイブノートを生成します。

### 💬 Q&A モード
対話型の質疑応答。論文の内容、図表、方法論について自由に質問できます。Q&A ログの保存も可能です。

### 📦 一括モード（Paper Alert）
複数の論文を同時処理。複数ソースに対応：
- **arXiv PDF** → 直接ダウンロード + MinerU 全文抽出
- **有料論文**（Nature、Elsevier、bioRxiv）→ web_search メタデータフォールバック
- **GitHub リポジトリ** → README 分析

## 🗂️ 分野別分析チェックリスト

| 分野 | 主な分析ポイント |
|------|----------------|
| 🧬 **分子動力学** | 力場、シミュレーションパラメータ、RMSD/RMSF、自由エネルギー法、軌跡分析 |
| 🏥 **医学** | 研究デザイン、コホート情報、統計手法、臨床アウトカム、ハザード比 |
| 🤖 **AI / ML** | アーキテクチャ詳細、訓練データ、ベンチマーク、SOTA 比較、計算リソース |
| 🔬 **バイオインフォマティクス** | パイプラインツール、統計検定、ゲノムアセンブリ、発現差異、エンリッチメント分析 |
| 💻 **プログラミング** | アルゴリズム複雑度、システム設計、実装詳細、パフォーマンスベンチマーク |

## 🚀 インストール

### 方法1：Git Clone（推奨）

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### 方法2：「ズボラな研究者」メソッド

ターミナルなんて触りたくない？このリポジトリの URL を Hermes Agent に投げて、以下をコピペするだけ：

```
この skill をインストールして：https://github.com/Shizukuyu0207/paper-reader

~/.hermes/skills/paper-reader/ に clone して。
MinerU がインストール済みか確認して（which mineru）、なければスキップして教えて。
終わったらインストール完了を報告して、この skill で何ができるか紹介して。
```

Agent が全部やってくれます。お茶でもどうぞ。🍵

### 方法3：手動インストール

ZIP をダウンロードして `~/.hermes/skills/paper-reader/` に展開。

### 前提条件

| 依存関係 | 必須 | インストール |
|----------|------|-------------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ 必須 | Hermes ドキュメント参照 |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ 必須 | `pip install mineru` または README 参照 |
| Obsidian | オプション | アーカイブノート用 |

## 📋 クイックスタート

```bash
# 1. インストール
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git

# 2. 確認
ls paper-reader/SKILL.md  # 存在するはず

# 3. 使う（Hermes のチャットで）
```

Hermes のチャットで：

```
read this paper https://arxiv.org/abs/2604.18559
```

これだけ。Skill が自動的に分野を検出し、モードを選び、残りを処理します。

## 📝 アーカイブ出力例

ノートは `~/obsidian/papers/{domain}/` に YAML frontmatter 付きで保存：

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

構造化セクションが続きます：基本情報 · 研究問題 · 方法 · 主要結果 · 限界 · 研究への示唆 · 引用ネットワーク

## ⚙️ 設定

| 変数 | デフォルト | 説明 |
|------|-----------|------|
| `MINERU` | MinerU バイナリパス | MinerU 実行ファイルのパス |
| `WORK_BASE` | `/tmp/paper-reader` | 一時作業ディレクトリ |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian アーカイブルート |
| `EXTRACT_SCRIPT` | `scripts/extract.sh` | 抽出ヘルパースクリプトパス |

## 🤝 コントリビュート

バグを見つけた？新しい分野チェックリストを追加したい？PR 大歓迎です。

1. このリポジトリを Fork
2. ブランチを作成 (`git checkout -b feature/my-feature`)
3. コミット (`git commit -m 'Add my feature'`)
4. プッシュ (`git push origin feature/my-feature`)
5. Pull Request を作成

## 📄 ライセンス

MIT License — [LICENSE](../LICENSE) を参照。

## 🙏 謝辞

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 抽出エンジン
- [Hermes Agent](https://github.com/henvic/hermes) — エージェントフレームワーク
- ブラウザに 50 個の未読論文タブを開いているすべての研究者に敬意を込めて

<div align="center">
論文が多すぎて読みきれない研究者のために ❤️
</div>
