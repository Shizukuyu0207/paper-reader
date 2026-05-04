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

### Opción 1: Git Clone (Recomendado)

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### Opción 2: El método del "Investigador Perezoso"

¿No quieres tocar la terminal? Simplemente lanza la URL de este repo a tu Hermes Agent y copia-pega esto:

```
Instala este skill: https://github.com/Shizukuyu0207/paper-reader

Clonalo en ~/.hermes/skills/paper-reader/,
verifica que MinerU esté instalado (which mineru), si no lo está sáltalo y avísame.
Cuando termines, confírmame la instalación y cuéntame qué puede hacer.
```

Tu Agent se encargará del resto. Ve a por un café. ☕

### Opción 3: Instalación manual

Descarga el ZIP y extrae en `~/.hermes/skills/paper-reader/`.

### Requisitos previos

| Dependencia | Requerido | Instalación |
|-------------|-----------|-------------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ Sí | Ver documentación de Hermes |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ Sí | `pip install mineru` o ver su README |
| Obsidian | Opcional | Para notas de archivo |

## 📋 Inicio rápido

```bash
# 1. Instalar
cd ~/.hermes/skills/ && git clone https://github.com/Shizukuyu0207/paper-reader.git

# 2. Verificar
ls paper-reader/SKILL.md  # debería existir

# 3. Usar (en el chat de Hermes)
```

Luego en tu conversación con Hermes:

```
read this paper https://arxiv.org/abs/2604.18559
```

Eso es todo. El skill detectará automáticamente el dominio, preguntará el modo y hará el resto.

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

## 🤝 Contribuir

¿Encontraste un bug? ¿Quieres añadir un checklist de dominio? Los PR son bienvenidos.

1. Haz Fork de este repo
2. Crea tu rama (`git checkout -b feature/my-feature`)
3. Haz commit (`git commit -m 'Add my feature'`)
4. Haz push (`git push origin feature/my-feature`)
5. Abre un Pull Request

## 📄 Licencia

MIT License — ver [LICENSE](../LICENSE).

## 🙏 Agradecimientos

- [MinerU](https://github.com/opendatalab/MinerU) — Motor de extracción de PDF
- [Hermes Agent](https://github.com/henvic/hermes) — Framework de agentes
- Para todos los investigadores con 50 pestañas de artículos sin leer en su navegador

<div align="center">
Hecho con ❤️ para investigadores que leen demasiados artículos
</div>
