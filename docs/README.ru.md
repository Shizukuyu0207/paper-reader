<div align="center">

# 📄 Paper Reader

**Анализ научных статей — Агенто-независимый пайплайн**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ Обзор

Автоматический анализ научных статей с определением домена и интеграцией Obsidian.

Агенто-независимый пайплайн. Совместим с любым агентом. См. `adapters/`.

## 🏗️ Архитектура

5 этапов + 3 уровня получения контента.

| Уровень | Инструмент | Скорость | Покрытие |
|---------|-----------|----------|----------|
| Уровень 1 | Jina Reader | 1-2с | arXiv, bioRxiv, большинство Nature |
| Уровень 2 | Scrapling | 5-15с | Nature/Elsevier |
| Уровень 3 | web_search | 2-5с | Пейволлы |
| Локальный | MinerU | ~2мин/40с | Локальные PDF |

### Домены: 🧬 Мол. динамика | 🏥 Медицина | 🤖 AI/ML | 🔬 Биоинформатика | 💻 Программирование

## 📊 Кейс: Пакетная обработка 9 статей

✅ Полный текст → архив 100+ строк. 9 статей за 6 мин.
⚠️ Пейволл → только метаданные. Elsevier — Уровень 3.

## ⚠️ Ограничения

- **Жёсткие пейволлы** (Cell, NEJM, JAMA): Требуют институциональный доступ
- Получаем только публично доступный контент

## 🚀 Установка

```bash
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

## 📄 Лицензия

MIT License — см. [LICENSE](../LICENSE).

<div align="center">
Создано с ❤️ для исследователей с слишком большим количеством непрочитанных статей
</div>
