<div align="center">

# 📄 Paper Reader

**Análisis de artículos académicos — Pipeline agnóstico de agentes**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ Resumen

Análisis automático de artículos académicos con detección de dominio y archivo Obsidian.

Pipeline agnóstico de agentes. Compatible con cualquier agente. Ver `adapters/`.

## 🏗️ Arquitectura

5 etapas + 3 niveles de adquisición.

| Nivel | Herramienta | Velocidad | Cobertura |
|-------|------------|-----------|-----------|
| Nivel 1 | Jina Reader | 1-2s | arXiv, bioRxiv, mayoría de Nature |
| Nivel 2 | Scrapling | 5-15s | Nature/Elsevier |
| Nivel 3 | web_search | 2-5s | Muros de pago |
| Local | MinerU | ~2min/40p | PDFs locales |

### Dominios: 🧬 Dinámica Molecular | 🏥 Medicina | 🤖 AI/ML | 🔬 Bioinformática | 💻 Programación

## 📊 Caso: Procesamiento de 9 artículos

✅ Artículos con texto completo → notas de 100+ líneas. 9 artículos en 6 min.
⚠️ Artículos con muro de pago → solo metadatos. Elsevier sigue en Nivel 3.

## ⚠️ Limitaciones

- **Muros de pago duros** (Cell, NEJM, JAMA): Requieren acceso institucional
- Solo adquirimos contenido públicamente visible en el navegador

## 🚀 Instalación

```bash
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

## 📄 Licencia

MIT License — ver [LICENSE](../LICENSE).

<div align="center">
Hecho con ❤️ para investigadores con demasiados artículos sin leer
</div>
