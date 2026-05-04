<div align="center">

# 📄 Paper Reader

**Análisis de artículos académicos basado en MinerU para Hermes Agent**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ Descripción general

Un skill de [Hermes Agent](https://github.com/henvic/hermes) que lee, analiza y archiva artículos académicos en PDF con detección inteligente de dominio e integración estructurada con Obsidian.

Ya sea filtrando un solo preprint de arXiv o procesando más de 10 artículos de diferentes editoriales, Paper Reader maneja la extracción, clasificación, análisis profundo y archivado automáticamente.

## 🎯 Características principales

| Característica | Descripción |
|----------------|-------------|
| 🧠 **Detección automática de dominio** | 5 dominios: Dinámica Molecular, Medicina, IA/ML, Bioinformática, Programación |
| 📊 **3 modos de lectura** | Escaneo rápido (3 min) · Lectura profunda (análisis completo) · Preguntas y respuestas (interactivo) |
| ⚡ **Procesamiento por lotes** | Descarga paralela + extracción MinerU + análisis paralelo para Paper Alerts |
| 📝 **Archivo en Obsidian** | YAML frontmatter + notas Markdown estructuradas en tu bóveda |
| 🔍 **Análisis visual de figuras** | Descripciones y análisis de figuras clave mediante IA |
| 🔓 **Gestión de paywalls** | Fallback automático a web_search para Nature/Elsevier/bioRxiv |

## 📖 Modos de lectura

### 🔍 Escaneo rápido
Resumen en 3 minutos para decidir si vale la pena una lectura profunda. Extrae título, resumen, hallazgos clave y relevancia. No crea archivo.

### 📖 Lectura profunda
Análisis estructurado completo con listas de verificación específicas por dominio. Genera una nota de archivo Obsidian completa con análisis de métodos, resultados cuantitativos, limitaciones e implicaciones para la investigación.

### 💬 Modo Q&A
Sesión interactiva de preguntas y respuestas. Pregunta sobre el contenido, figuras o metodología del artículo. Opcionalmente guarda un registro de Q&A.

### 📦 Modo por lotes (Paper Alert)
Procesa múltiples artículos simultáneamente. Maneja fuentes mixtas:
- **PDFs de arXiv** → Descarga directa + extracción completa con MinerU
- **Artículos de pago** (Nature, Elsevier, bioRxiv) → Fallback a metadatos vía web_search
- **Repositorios de GitHub** → Análisis del README

## 🗂️ Listas de verificación por dominio

| Dominio | Puntos clave de análisis |
|---------|------------------------|
| 🧬 **Dinámica Molecular** | Campos de fuerza, parámetros de simulación, RMSD/RMSF, métodos de energía libre, análisis de trayectorias |
| 🏥 **Medicina** | Diseño del estudio, información de cohortes, métodos estadísticos, resultados clínicos, hazard ratios |
| 🤖 **IA / ML** | Detalles de arquitectura, datos de entrenamiento, benchmarks, comparaciones SOTA, recursos computacionales |
| 🔬 **Bioinformática** | Herramientas de pipeline, pruebas estadísticas, ensamblaje genómico, expresión diferencial, análisis de enriquecimiento |
| 💻 **Programación** | Complejidad algorítmica, diseño del sistema, detalles de implementación, benchmarks de rendimiento |

## 🚀 Instalación

```bash
# Clonar en el directorio de skills de Hermes
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

O copiar manualmente la carpeta `paper-reader/` a `~/.hermes/skills/paper-reader/`.

### Requisitos previos

- [MinerU](https://github.com/opendatalab/MinerU) — Motor de extracción de PDF
- [Hermes Agent](https://github.com/henvic/hermes) — Framework de agentes
- Bóveda de Obsidian (opcional, para notas de archivo)

## 📋 Uso

```
# Artículo individual — archivo local
读论文 /ruta/al/articulo.pdf

# Artículo individual — arXiv
read this paper https://arxiv.org/abs/2604.18559

# Por lotes — Paper Alert
Paper Alert:
1. Allosteric Switches https://www.nature.com/articles/s41587-026-03081-9
2. ConforNets https://arxiv.org/abs/2604.18559
3. trRosettaRNA2 https://doi.org/10.1038/s42256-026-01223-x
```

El skill: obtiene/verifica el PDF → detecta el dominio → selecciona el modo → analiza → archiva

## 📝 Ejemplo de salida archivada

Las notas se guardan en `~/obsidian/papers/{domain}/` con YAML frontmatter completo:

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

Seguido de secciones estructuradas: Información básica · Pregunta de investigación · Métodos · Resultados clave · Limitaciones · Implicaciones · Red de citaciones

## ⚙️ Configuración

| Variable | Predeterminado | Descripción |
|----------|---------------|-------------|
| `MINERU` | Ruta del binario MinerU | Ruta al ejecutable de MinerU |
| `WORK_BASE` | `/tmp/paper-reader` | Directorio de trabajo temporal |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Raíz del archivo Obsidian |
| `EXTRACT_SCRIPT` | `scripts/extract.sh` | Ruta del script auxiliar de extracción |

## 📄 Licencia

MIT License — ver [LICENSE](../LICENSE).

## 🙏 Agradecimientos

- [MinerU](https://github.com/opendatalab/MinerU) — Motor de extracción de PDF
- [Hermes Agent](https://github.com/henvic/hermes) — Framework de agentes
- Hecho para investigadores que tienen demasiados artículos para leer

<div align="center">
Hecho con ❤️ para investigadores que leen demasiados artículos
</div>
