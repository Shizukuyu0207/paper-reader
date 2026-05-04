# MinerU Quirks & Validation Notes

> Validated 2026-05-04 with MinerU v3.1.4 on real papers.

## Language Flag (`-l`)

**CRITICAL**: `-l auto` is NOT supported. MinerU will error with exit code 2.

Supported values: `en`, `ch`, `ch_server`, `ch_lite`, `korean`, `japan`, `chinese_cht`, `ta`, `te`, `ka`, `th`, `el`, `latin`, `arabic`, `east_slavic`, `cyrillic`, `devanagari`

**Default strategy**:
- arXiv papers → `-l en` (99% English)
- Chinese filename or Chinese text detected → `-l ch`
- User override always takes priority

## Output Structure

MinerU creates nested output: `$OUTPUT_DIR/$BASENAME/auto/$BASENAME.md`

Key files:
- `*.md` — Full text (~2KB/page for text-heavy papers)
- `*_content_list.json` — Structured elements with type/text/bbox/page_idx
- `*_content_list_v2.json` — Alternative format (less useful)
- `*_middle.json` — Internal pipeline data
- `*_model.json` — Model outputs
- `*_layout.pdf` / `*_span.pdf` / `*_origin.pdf` — Debug PDFs
- `images/` — Extracted figures (hash filenames like `30ba32d7...jpg`)

## content_list.json Types

| Type | Count (30pg paper) | Key Fields |
|------|-------------------|------------|
| text | 177 | type, text, bbox, page_idx |
| table | 11 | type, img_path, table_caption, table_body, table_footnote, bbox, page_idx |
| equation | 21 | type, img_path, text (LaTeX), text_format, bbox, page_idx |
| image | 2 | type, img_path, image_caption, image_footnote, bbox, page_idx |
| chart | 5 | Similar to image |
| list | 5 | type, text, bbox, page_idx |
| page_number | 29 | Minimal |
| page_footnote | 9 | type, text, bbox, page_idx |

**Priority**: Use content_list.json for structured analysis (tables, equations, figures); fall back to .md for full text.

## Performance

- **Speed**: ~13s/page on CPU (RTX 5060, pipeline mode doesn't use GPU)
- **30-page paper**: ~395s (~6.5 min) for full extraction
- **3-page scan**: ~30s — sufficient for domain detection
- **Strictly serial**: Never run multiple MinerU processes simultaneously

## Image Handling

- Images saved with SHA-256 hash filenames
- To map images to figures: use content_list.json `image_caption` field
- For rename: match caption → figure number → descriptive name
- Typical yield: ~1-2 images per page for figure-heavy papers

## Page Range (`-s` / `-e`)

- `-s 0 -e 3` extracts pages 0-3 (4 pages, NOT 3)
- MinerU may process slightly more pages than specified (observed: `-e 3` produced 4 pages)
- For exact 3-page domain detection scan, use `-s 0 -e 2` if strictness needed

## PDF Compatibility

- arXiv vector PDFs: Excellent quality (~99% success)
- Nature/science journal PDFs: Good quality (19-page Nature paper extracted 14 text pages + full figures)
- Some full-page figure pages may be skipped (expected behavior)
- Scanned/OCRed PDFs: Use `-l ch` or appropriate language flag

## Vision Analysis

**Known limitation**: GLM-5.1 (and other non-multimodal models) cannot use `vision_analyze`.
- When running on non-vision models: figure descriptions rely entirely on content_list.json captions + md text
- Switch to multimodal model (Claude, GPT-4o) for figure depth analysis
