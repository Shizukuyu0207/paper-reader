#!/bin/bash
# paper-reader MinerU extraction wrapper
# Usage: extract.sh <pdf_path> <output_dir> [lang] [start_page] [end_page]
set -euo pipefail

MINERU="/home/user/.hermes/hermes-agent/venv/bin/mineru"
PDF_PATH="${1:?Usage: extract.sh <pdf_path> <output_dir> [lang] [start_page] [end_page]}"
OUTPUT_DIR="${2:?Output dir required}"
LANG="${3:-en}"
START="${4:-}"
END="${5:-}"

# Validate input
if [ ! -f "$PDF_PATH" ]; then
    echo "❌ File not found: $PDF_PATH" >&2
    exit 1
fi

FILE_TYPE=$(file -b "$PDF_PATH" | head -1)
if echo "$FILE_TYPE" | grep -qi "PDF"; then
    : # OK
else
    echo "❌ Not a PDF file: $FILE_TYPE" >&2
    exit 1
fi

# Build command
CMD=("$MINERU" -p "$PDF_PATH" -o "$OUTPUT_DIR" -b pipeline -l "$LANG")

# Add page range if specified
if [ -n "$START" ]; then
    CMD+=(-s "$START")
fi
if [ -n "$END" ]; then
    CMD+=(-e "$END")
fi

echo "▶ Extracting: $(basename "$PDF_PATH")"
echo "  Output: $OUTPUT_DIR"
echo "  Lang: $LANG"
[ -n "$START" ] && echo "  Pages: $START-$END"

# Run extraction
"${CMD[@]}"
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    # Find and report output files
    MD_FILE=$(find "$OUTPUT_DIR" -name "*.md" -path "*/auto/*" | head -1)
    CL_FILE=$(find "$OUTPUT_DIR" -name "*content_list.json" | head -1)
    IMG_COUNT=$(find "$OUTPUT_DIR" \( -name "*.jpg" -o -name "*.png" \) 2>/dev/null | wc -l)
    echo "✅ Extraction complete"
    echo "  Markdown: $MD_FILE"
    echo "  Content list: $CL_FILE"
    echo "  Images: $IMG_COUNT"
else
    echo "❌ Extraction failed (exit: $EXIT_CODE)" >&2
    exit $EXIT_CODE
fi
