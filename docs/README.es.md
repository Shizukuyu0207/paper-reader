<div align="center">

# 📄 Paper Reader

**Análisis de artículos académicos para Hermes Agent — MinerU + Jina Reader + Scrapling**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-purple.svg)](https://github.com/henvic/hermes)
[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)

[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)

</div>

---

## ✨ Descripción general

Un skill de [Hermes Agent](https://github.com/henvic/hermes) que lee, analiza y archiva artículos académicos con adquisición de contenido en 3 niveles, detección inteligente de dominio e integración con Obsidian.

## 🎯 Características principales

| Característica | Descripción |
|----------------|-------------|
| 🧠 **Detección automática de dominio** | 5 dominios: Dinámica Molecular, Medicina, IA/ML, Bioinformática, Programación |
| 📊 **3 modos de lectura** | Escaneo rápido (3 min) · Lectura profunda · Preguntas y respuestas |
| ⚡ **Adquisición en 3 niveles** | Jina Reader → Scrapling navegador oculto → web_search fallback |
| 📝 **Archivo en Obsidian** | YAML frontmatter + notas Markdown estructuradas |
| 🔍 **Análisis visual de figuras** | Descripciones de figuras mediante IA |
| 📦 **Procesamiento por lotes** | Obtención paralela + análisis paralelo |

## 🔗 Adquisición de contenido — Estrategia de 3 niveles

No hay magia — solo fallbacks escalonados con compensaciones honestas.

| Nivel | Herramienta | Velocidad | Salida | Para |
|-------|-------------|-----------|--------|------|
| **1** | [Jina Reader](https://github.com/jina-ai/reader) | 1-2s | Markdown | arXiv, bioRxiv, acceso abierto, mayoría de Nature |
| **2** | [Scrapling](https://github.com/D4Vinci/Scrapling) + Camoufox | 5-15s | HTML texto | Nivel 1 falla, contenido parcial Nature/Elsevier |
| **3** | web_search | 2-5s | Solo metadatos | Paywalls duros (Cell, NEJM, Lancet) |

### Rendimiento medido (datos reales, mayo 2026)

| Fuente | Nivel | Resultado | Tiempo | Contenido |
|--------|-------|-----------|--------|-----------|
| arXiv PDF | Nivel 1 | ✅ Texto completo | 0.8s | Todas las secciones |
| bioRxiv PDF | Nivel 1 | ✅ Texto completo | 0.8s | Todas las secciones |
| Nature Biotechnology | Nivel 1 | ✅ Texto completo | 1.0s | 117K caracteres |
| Nature Machine Intelligence | Nivel 1→2 | ✅ Texto completo | 6.3s | Jina parcial → Scrapling completo |
| Elsevier/ScienceDirect | Nivel 3 | ⚠️ Metadatos | 3s | Solo resumen + citas |

## ⚠️ Limitaciones honestas

Esta herramienta es útil pero **no es omnipotente**.

### Lo que NO puede romper

| Escenario | Realidad | Solución |
|-----------|----------|----------|
| **Paywalls duros** (Cell, NEJM, JAMA) | Requieren login institucional o suscripción personal | Use VPN de su universidad, descargue PDF manualmente y proporcione como archivo local |
| **Autenticación institucional** (SSO, Shibboleth) | Login al portal universitario está fuera del alcance | Descargue PDF manualmente y proporcione a Paper Reader |
| **Artículos recién publicados** | Pueden tardar días/semanas en ser indexados | Espere disponibilidad de preprint o acceda vía institución |
| **Materiales suplementarios** | Normalmente alojados por separado | Proporcione archivos suplementarios separadamente |

### Consideraciones legales y éticas

- Obtenemos **solo lo que es públicamente visible en un navegador**. Si necesitas iniciar sesión para verlo — inicia sesión tú mismo.
- Artículos de acceso abierto: los editores permiten explícitamente la obtención.
- Contenido de pago: no intentamos eludir la autenticación. Retrocedemos a metadatos públicos.
- Limitación de tasa: Jina Reader gratis 20 RPM. No bombardeamos servidores de editores.

## 🚀 Instalación

### Opción 1: Git Clone (Recomendado)

```bash
cd ~/.hermes/skills/
git clone https://github.com/Shizukuyu0207/paper-reader.git
```

### Opción 2: El método del "Investigador Perezoso"

```
Instala este skill: https://github.com/Shizukuyu0207/paper-reader

Clonalo en ~/.hermes/skills/paper-reader/,
verifica que MinerU esté instalado, si no lo está sáltalo y avísame.
Cuando termines, confírmame la instalación y cuéntame qué puede hacer.
```

Ve a por un café. ☕

### Requisitos previos

| Dependencia | Requerido | Instalación |
|-------------|-----------|-------------|
| [Hermes Agent](https://github.com/henvic/hermes) | ✅ Sí | Ver documentación de Hermes |
| [MinerU](https://github.com/opendatalab/MinerU) | ✅ Sí | `pip install mineru` |
| [Jina Reader](https://github.com/jina-ai/reader) | Integrado | Usa API `r.jina.ai`, sin instalación |
| [Scrapling](https://github.com/D4Vinci/Scrapling) | Recomendado | `pip install scrapling camoufox && python -m camoufox fetch` |
| Obsidian | Opcional | Para notas de archivo |

## ⚙️ Configuración

| Variable | Predeterminado | Descripción |
|----------|---------------|-------------|
| `MINERU` | Ruta binaria MinerU | Ruta al ejecutable de MinerU |
| `WORK_BASE` | `/tmp/paper-reader` | Directorio de trabajo temporal |
| `ARCHIVE_BASE` | `~/obsidian/papers` | Raíz del archivo Obsidian |
| `JINA_READER` | `https://r.jina.ai` | Endpoint de la API Jina Reader |

## 🤝 Contribuir

¿Encontraste un bug? ¿Quieres añadir un checklist de dominio? Los PR son bienvenidos.

## 📄 Licencia

MIT License — ver [LICENSE](../LICENSE).

## 🙏 Agradecimientos

- [MinerU](https://github.com/opendatalab/MinerU) — Motor de extracción de PDF
- [Jina Reader](https://github.com/jina-ai/reader) — Conversión URL a Markdown
- [Scrapling](https://github.com/D4Vinci/Scrapling) — Fetching oculto con Camoufox
- [Hermes Agent](https://github.com/henvic/hermes) — Framework de agentes
- Para todos los investigadores con 50 pestañas de artículos sin leer

<div align="center">
Hecho con ❤️ para investigadores que leen demasiados artículos
</div>
