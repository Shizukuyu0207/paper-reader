<div align="center">

# 📄 Paper Reader

**学術論文分析 — マルチエージェント対応**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-green.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex](https://img.shields.io/badge/Codex-Compatible-blue.svg)](https://github.com/openai/codex)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-orange.svg)](https://opencode.ai)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ 概要

Paper Reader は学術論文の自動読解・分析・アーカイブツールです。

**4種類のAIエージェントに対応**：Hermes（ネイティブ）、Claude Code、OpenAI Codex、OpenCode。

## 🤖 マルチエージェント対応

| エージェント | アダプター | インストール | 状態 |
|------------|-----------|-------------|------|
| **Hermes** | `SKILL.md`（ネイティブ） | `~/.hermes/skills/paper-reader/` | ✅ フルサポート |
| **Claude Code** | `adapters/claude-code/` | `~/.claude/commands/paper-reader.md` | ✅ テスト済み |
| **Codex** | `adapters/codex/` | プロジェクト `AGENTS.md` | ✅ テスト済み |
| **OpenCode** | `adapters/opencode/` | `opencode.json` エージェント設定 | ✅ テスト済み |

### 機能比較

| 機能 | Hermes | Claude Code | Codex | OpenCode |
|------|--------|-------------|-------|----------|
| 3層取得 | ✅ 内蔵 | ✅ bash | ✅ bash | ✅ bash |
| 領域検出 | ✅ ネイティブ | ✅ プロンプト | ✅ プロンプト | ✅ プロンプト |
| バッチ並列 | ✅ 内蔵 | ⚠️ 手動 | ⚠️ 手動 | ⚠️ 手動 |
| 画像ビジョン | ✅ 内蔵 | ✅ 内蔵 | ❌ | ❌ |

## 🏗️ アーキテクチャ

5段階パイプライン + 3層コンテンツ取得。

| 優先度 | ツール | 速度 | カバー範囲 |
|--------|--------|------|-----------|
| Tier 1 | Jina Reader | 1-2s | arXiv, bioRxiv, ほとんどのNature |
| Tier 2 | Scrapling | 5-15s | Nature/Elsevier |
| Tier 3 | web_search | 2-5s | ペイウォール |
| ローカル | MinerU | ~2分/40p | ローカルPDF |

### 領域：🧬 分子動力学 | 🏥 医学 | 🤖 AI/ML | 🔬 バイオインフォマティクス | 💻 プログラミング

## 📊 ケース：9論文バッチ処理（2026年5月）

✅ PDF利用可能論文の深い分析は優秀 | ✅ 9編6分処理 | ⚠️ ペイウォール論文は方法詳細不足

## ⚠️ 正直な限界

- **ハードペイウォール**（Cell, NEJM, JAMA）: 機関ログインが必要 → PDFを手動ダウンロード
- **Tier 3論文**: 詳細な方法・定量的結果なし
- ブラウザで公開閲覧可能なコンテンツのみ取得

## 🚀 インストール

```bash
# Hermes (推奨)
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git

# Claude Code
mkdir -p ~/.claude/commands && cp paper-reader/adapters/claude-code/commands/paper-reader.md ~/.claude/commands/

# Codex
cp paper-reader/adapters/codex/AGENTS.md ./AGENTS.md
```

## 📄 ライセンス

MIT License — [LICENSE](../LICENSE) 参照。

<div align="center">
論文を読みきれない研究者のために ❤️
</div>
