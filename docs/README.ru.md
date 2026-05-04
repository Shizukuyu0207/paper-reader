<div align="center">

# 📄 Paper Reader

**Анализ научных статей — Мульти-агентная совместимость**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-green.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex](https://img.shields.io/badge/Codex-Compatible-blue.svg)](https://github.com/openai/codex)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-orange.svg)](https://opencode.ai)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ Обзор

Paper Reader автоматически читает, анализирует и архивирует научные статьи с определением домена и интеграцией Obsidian.

**Совместим с 4 ИИ-агентами**: Hermes (встроенный), Claude Code, OpenAI Codex, OpenCode.

## 🤖 Мульти-агентная поддержка

| Агент | Адаптер | Установка | Статус |
|-------|---------|-----------|--------|
| **Hermes** | `SKILL.md` (встроенный) | `~/.hermes/skills/paper-reader/` | ✅ Полная поддержка |
| **Claude Code** | `adapters/claude-code/` | `~/.claude/commands/paper-reader.md` | ✅ Протестирован |
| **Codex** | `adapters/codex/` | `AGENTS.md` проекта | ✅ Протестирован |
| **OpenCode** | `adapters/opencode/` | Конфиг агента `opencode.json` | ✅ Протестирован |

### Сравнение функций

| Функция | Hermes | Claude Code | Codex | OpenCode |
|---------|--------|-------------|-------|----------|
| 3 уровня получения | ✅ Встроено | ✅ bash | ✅ bash | ✅ bash |
| Определение домена | ✅ Нативное | ✅ Промпт | ✅ Промпт | ✅ Промпт |
| Пакетная обработка | ✅ Встроена | ⚠️ Вручную | ⚠️ Вручную | ⚠️ Вручную |
| Визуальный анализ | ✅ Встроен | ✅ Встроен | ❌ | ❌ |

## 🏗️ Архитектура

5 этапов + 3 уровня получения контента.

| Уровень | Инструмент | Скорость | Покрытие |
|---------|-----------|----------|----------|
| Уровень 1 | Jina Reader | 1-2с | arXiv, bioRxiv, большинство Nature |
| Уровень 2 | Scrapling | 5-15с | Nature/Elsevier |
| Уровень 3 | web_search | 2-5с | Пейволлы |
| Локальный | MinerU | ~2мин/40с | Локальные PDF |

### Домены: 🧬 Мол. динамика | 🏥 Медицина | 🤖 AI/ML | 🔬 Биоинформатика | 💻 Программирование

## ⚠️ Честные ограничения

- **Жёсткие пейволлы** (Cell, NEJM, JAMA): Требуют институциональный доступ → скачайте PDF вручную
- Получаем только публично доступный контент браузера.

## 🚀 Установка

```bash
# Hermes (рекомендуется)
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git

# Claude Code
mkdir -p ~/.claude/commands && cp paper-reader/adapters/claude-code/commands/paper-reader.md ~/.claude/commands/

# Codex
cp paper-reader/adapters/codex/AGENTS.md ./AGENTS.md
```

## 📄 Лицензия

MIT License — см. [LICENSE](../LICENSE).

<div align="center">
Создано с ❤️ для исследователей, у которых слишком много непрочитанных статей
</div>
