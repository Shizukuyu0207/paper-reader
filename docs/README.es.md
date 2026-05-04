<div align="center">

# 📄 Paper Reader

**Análisis de artículos académicos — Multi-Agente Compatible**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-green.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Codex](https://img.shields.io/badge/Codex-Compatible-blue.svg)](https://github.com/openai/codex)
[![OpenCode](https://img.shields.io/badge/OpenCode-Compatible-orange.svg)](https://opencode.ai)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ Resumen

Paper Reader analiza automáticamente artículos académicos con detección de dominio y archivo Obsidian.

**Compatible con 4 agentes de IA**: Hermes (nativo), Claude Code, OpenAI Codex, OpenCode.

## 🤖 Soporte Multi-Agente

| Agente | Adaptador | Instalación | Estado |
|--------|-----------|------------|--------|
| **Hermes** | `SKILL.md` (nativo) | `~/.hermes/skills/paper-reader/` | ✅ Soporte completo |
| **Claude Code** | `adapters/claude-code/` | `~/.claude/commands/paper-reader.md` | ✅ Probado |
| **Codex** | `adapters/codex/` | `AGENTS.md` del proyecto | ✅ Probado |
| **OpenCode** | `adapters/opencode/` | Config de agente `opencode.json` | ✅ Probado |

### Comparación de Funciones

| Función | Hermes | Claude Code | Codex | OpenCode |
|---------|--------|-------------|-------|----------|
| 3 niveles de adquisición | ✅ Integrado | ✅ bash | ✅ bash | ✅ bash |
| Detección de dominio | ✅ Nativo | ✅ Prompt | ✅ Prompt | ✅ Prompt |
| Lote paralelo | ✅ Integrado | ⚠️ Manual | ⚠️ Manual | ⚠️ Manual |
| Análisis visual | ✅ Integrado | ✅ Integrado | ❌ | ❌ |

## 🏗️ Arquitectura

5 etapas + 3 niveles de adquisición de contenido.

| Nivel | Herramienta | Velocidad | Cobertura |
|-------|------------|-----------|-----------|
| Nivel 1 | Jina Reader | 1-2s | arXiv, bioRxiv, la mayoría de Nature |
| Nivel 2 | Scrapling | 5-15s | Nature/Elsevier |
| Nivel 3 | web_search | 2-5s | Muros de pago |
| Local | MinerU | ~2min/40p | PDFs locales |

### Dominios: 🧬 Dinámica Molecular | 🏥 Medicina | 🤖 AI/ML | 🔬 Bioinformática | 💻 Programación

## ⚠️ Limitaciones Honestas

- **Muros de pago duros** (Cell, NEJM, JAMA): Requieren acceso institucional → descargar PDF manualmente
- Solo adquirimos contenido públicamente visible en el navegador.

## 🚀 Instalación

```bash
# Hermes (recomendado)
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git

# Claude Code
mkdir -p ~/.claude/commands && cp paper-reader/adapters/claude-code/commands/paper-reader.md ~/.claude/commands/

# Codex
cp paper-reader/adapters/codex/AGENTS.md ./AGENTS.md
```

## 📄 Licencia

MIT License — ver [LICENSE](../LICENSE).

<div align="center">
Hecho con ❤️ para investigadores con demasiados artículos sin leer
</div>
