<div align="center">

# 📄 Paper Reader

**Análisis de artículos académicos para Hermes Agent — MinerU + Jina Reader + Scrapling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ Resumen

Un skill de [Hermes Agent](https://github.com/henvic/hermes) para lectura y análisis de artículos académicos. Acepta URLs, PDFs locales o lotes de 10+ artículos — adquisición automática, clasificación por dominio, análisis profundo y archivado.

## 🏗️ Arquitectura

Pipeline de 5 etapas + estrategia de adquisición de contenido en 3 niveles. Cada etapa es modular e independiente.

```
Adquisición(3 niveles) → Detección(5 dominios) → Selección(4 modos) → Análisis → Archivo Obsidian
```

### 3 Niveles de Adquisición

| Prioridad | Herramienta | Velocidad | Cobertura |
|-----------|------------|-----------|-----------|
| Nivel 1 | Jina Reader | 1-2s | arXiv, bioRxiv, la mayoría de Nature |
| Nivel 2 | Scrapling + Camoufox | 5-15s | Nature/Elsevier cuando Nivel 1 es parcial |
| Nivel 3 | web_search | 2-5s | Muros de pago (Cell, NEJM) |
| Local | MinerU | ~2min/40p | PDFs locales con imágenes |

### Dominios de Análisis

🧬 Dinámica Molecular | 🏥 Medicina | 🤖 AI/ML | 🔬 Bioinformática | 💻 Programación

## 📊 Caso: Procesamiento de 9 artículos (Mayo 2026)

| # | Artículo | Fuente | Método | Tiempo | Calidad |
|---|---------|--------|--------|--------|---------|
| 1 | Allosteric Switches | Nature NBT | MinerU | 93s | ★★★★★ Texto completo, 494 líneas + 36 figuras |
| 2 | ConforNets | arXiv | MinerU | 118s | ★★★★★ Texto completo, 646 líneas + 75 figuras |
| 3-8 | 6 artículos con muro de pago | Varias | web_search | ~5s c/u | ★★☆☆☆ Solo metadatos |
| 9 | lightning-boltz | GitHub | README | ~3s | ★★☆☆☆ Info del repo |

**Total**: ~6 minutos | Tras integrar Jina Reader, 4/7 artículos de solo metadatos → texto completo

### Evaluación Objetiva

✅ Análisis profundo excelente para PDFs disponibles | ✅ 9 artículos en 6 min | ⚠️ Artículos con muro de pago carecen de detalles de métodos | ⚠️ Elsevier sigue en Nivel 3

## ⚠️ Limitaciones Honestas

- **Muros de pago duros** (Cell, NEJM, JAMA): Requieren acceso institucional → descargar PDF manualmente
- **Artículos Nivel 3**: Notas sin métodos detallados ni resultados cuantitativos
- Solo adquirimos contenido públicamente visible en el navegador.

## 🚀 Instalación

```bash
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git
```

## 📄 Licencia

MIT License — ver [LICENSE](../LICENSE).

<div align="center">
Hecho con ❤️ para investigadores con demasiados artículos sin leer
</div>
