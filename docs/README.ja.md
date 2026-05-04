<div align="center">

# 📄 Paper Reader

**学術論文分析 Hermes Agent Skill — MinerU + Jina Reader + Scrapling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概要

[Hermes Agent](https://github.com/henvic/hermes) 用の学術論文読解・分析 Skill。3段階のコンテンツ取得、インテリジェントな分野検出、Obsidian ボールトへの自動アーカイブをサポートします。

## 🎯 主要機能

| 機能 | 説明 |
|------|------|
| 🧠 **自動分野検出** | 5分野：分子動力学、医学、AI/ML、バイオインフォマティクス、プログラミング |
| 📊 **3つの読解モード** | クイックスキャン（3分）· 深い読解（全文分析）· Q&A（対話型）|
| ⚡ **3段階コンテンツ取得** | Jina Reader → Scrapling ステルスブラウザ → web_search フォールバック |
| 📝 **Obsidian アーカイブ** | YAML frontmatter + 構造化 Markdown ノート |
| 🔍 **図表の視覚分析** | AI による主要図表の記述と分析 |
| 📦 **一括処理** | 並列取得 + 並列分析、Paper Alert 対応 |

## 🔗 コンテンツ取得 — 3段階戦略

魔法はありません — レイヤー化されたフォールバックと正直なトレードオフだけです。

| 段階 | ツール | 速度 | 出力 | 対象 |
|------|--------|------|------|------|
| **第1段階** | [Jina Reader](https://github.com/jina-ai/reader) | 1-2秒 | Markdown | arXiv, bioRxiv, オープンアクセス, ほとんどの Nature 論文 |
| **第2段階** | [Scrapling](https://github.com/D4Vinci/Scrapling) + Camoufox | 5-15秒 | HTML テキスト | 第1段階失敗時, Nature/Elsevier の部分コンテンツ |
| **第3段階** | web_search | 2-5秒 | メタデータのみ | ハードペイウォール（Cell, NEJM, Lancet） |

### ベンチマーク（2026年5月実測データ）

| ソース | 段階 | 結果 | 時間 | コンテンツ量 |
|--------|------|------|------|-------------|
| arXiv PDF | 第1段階 | ✅ 全文 | 0.8秒 | 全セクション |
| bioRxiv PDF | 第1段階 | ✅ 全文 | 0.8秒 | 全セクション |
| Nature Biotechnology | 第1段階 | ✅ 全文 | 1.0秒 | 117K文字 |
| Nature Machine Intelligence | 第1→2段階 | ✅ 全文 | 6.3秒 | Jina部分→Scrapling補完 |
| Elsevier/ScienceDirect | 第3段階 | ⚠️ メタデータ | 3秒 | 要約+引用のみ |

## ⚠️ 正直な限界

このツールは有用ですが、**万能ではありません**。

### 突破できないもの

| シナリオ | 現実 | 回避策 |
|----------|------|--------|
| **ハードペイウォール**（Cell, NEJM, JAMA） | 機関ログインまたは個人購読が必要 | 大学/研究所のVPNを使用、PDFを手動ダウンロードしてローカルファイルとして提供 |
| **機関認証**（SSO, Shibboleth） | 大学ポータルへのログインは Skill の範囲外 | 手動でPDFをダウンロードして Paper Reader に提供 |
| **出版直後の論文** | インデックスされるまで数日〜数週間かかる場合がある | プレプリントの公開を待つか、機関経由でアクセス |
| **補足資料** | 通常は別ホスト | 補足ファイルを個別に提供 |

### 法的・倫理的考慮事項

- ブラウザで**公開されているコンテンツのみ**を取得します。ログインが必要なものは、自分でログインしてください。
- オープンアクセス論文：出版社が明示的に取得を許可。
- ペイウォールコンテンツ：認証の回避やペイウォールの突破は試みません。公開メタデータにフォールバック。
- レート制限：Jina Reader 無料枠 20 RPM。出版社サーバーを攻撃しません。

## 🚀 インストール

### 方法1：Git Clone（推奨）

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### 方法2：「ズボラな研究者」メソッド

```
この skill をインストールして：https://github.com/Shizukuyu0207/paper-reader

~/.hermes/skills/paper-reader/ に clone して。
MinerU がインストール済みか確認して、なければスキップして教えて。
終わったらインストール完了を報告して、この skill で何ができるか紹介して。
```

お茶でもどうぞ。🍵

### 前提条件

| 依存関係 | 必須 | インストール |
|----------|------|-------------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ 必須 | Hermes ドキュメント参照 |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ 必須 | `pip install mineru` |
| [Jina Reader](https://github.com/jina-ai/reader) | 組み込み | `r.jina.ai` API 使用、インストール不要 |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | 推奨 | `pip install scrapling camoufox && python -m camoufox fetch` |
| Obsidian | オプション | アーカイブノート用 |

## ⚙️ 設定

| 変数 | デフォルト | 説明 |
|------|-----------|------|
| `MINERU` | MinerU バイナリパス | MinerU 実行ファイルのパス |
| `WORK_BASE` | `/tmp/paper-reader` | 一時作業ディレクトリ |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Obsidian アーカイブルート |
| `JINA_READER` | `https://r.jina.ai` | Jina Reader API エンドポイント |

## 🤝 コントリビュート

バグを見つけた？新しい分野チェックリストを追加したい？PR 大歓迎。

## 📄 ライセンス

MIT License — [LICENSE](../LICENSE) を参照。

## 🙏 謝辞

- [MinerU](https://github.com/opendatalab/MinerU) — PDF 抽出エンジン
- [Jina Reader](https://github.com/jina-ai/reader) — URL → Markdown 変換
- [Scrapling](https://github.com/D4Vinci/Scrapling) — ステルスブラウザフェッチ + Camoufox
- [Hermes Agent](https://github.com/henvic/hermes) — エージェントフレームワーク
- ブラウザに 50 個の未読論文タブを開いているすべての研究者に敬意を込めて

<div align="center">
論文が多すぎて読みきれない研究者のために ❤️
</div>
