     1|<div align="center">
     2|
     3|# 📄 Paper Reader
     4|
     5|**Análisis de artículos académicos — Pipeline agnóstico de agentes**
     6|
     7|[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
     8|[![MinerU](https://img.shields.io/badge/Powered%20by-MinerU-orange.svg)](https://github.com/opendatalab/MinerU)
     9|
    10|[English](../README.md) · [简体中文](README.zh-CN.md) · [繁體中文](README.zh-TW.md) · [日本語](README.ja.md) · [Español](README.es.md) · [Русский](README.ru.md)
    11|
    12|</div>
    13|
    14|---
    15|
    16|## ✨ Resumen
    17|
    18|Análisis automático de artículos académicos con detección de dominio y archivo Obsidian.
    19|
    20|Pipeline agnóstico de agentes. Compatible con cualquier agente. Ver `adapters/`.
    21|
    22|## 🏗️ Arquitectura
    23|
    24|5 etapas + 3 niveles de adquisición.
    25|
    26|| Nivel | Herramienta | Velocidad | Cobertura |
    27||-------|------------|-----------|-----------|
    28|| Nivel 1 | Jina Reader | 1-2s | arXiv, bioRxiv, mayoría de Nature |
    29|| Nivel 2 | Scrapling | 5-15s | Nature/Elsevier |
    30|| Nivel 3 | web_search | 2-5s | Muros de pago |
    31|| Local | MinerU | ~2min/40p | PDFs locales |
    32|
    33|### Dominios: 🧬 Dinámica Molecular | 🏥 Medicina | 🤖 AI/ML | 🔬 Bioinformática | 💻 Programación
    34|
    35|## 📊 Caso: Procesamiento de 9 artículos
    36|
    37|✅ Artículos con texto completo → notas de 100+ líneas. 9 artículos en 6 min.
    38|⚠️ Artículos con muro de pago → solo metadatos. Elsevier sigue en Nivel 3.
    39|
    40|## ⚠️ Limitaciones
    41|
    42|- **Muros de pago duros** (Cell, NEJM, JAMA): Requieren acceso institucional
    43|- Solo adquirimos contenido públicamente visible en el navegador
    44|
    45|## 🚀 Instalación
    46|
    47|```bash
    48|git clone https://github.com/nowa277/paper-reader.git
    49|```
    50|
    51|## 📄 Licencia
    52|
    53|MIT License — ver [LICENSE](../LICENSE).
    54|
    55|<div align="center">
    56|Hecho con ❤️ para investigadores con demasiados artículos sin leer
    57|</div>
    58|