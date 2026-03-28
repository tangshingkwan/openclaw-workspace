#!/bin/bash
# Read the mapping file and create sed replacements

INPUT_FILE="/root/.openclaw/workspace/data/input.txt"
OUTPUT_FILE="/root/.openclaw/workspace/data/output.txt"
MAPPING_FILE="/root/.openclaw/workspace/data/mapping.tsv"

# Create sed script from mapping
SED_SCRIPT=$(mktemp)
while IFS=$'\t' read -r old new; do
    echo "s|$old|$new|g" >> "$SED_SCRIPT"
done < "$MAPPING_FILE"

# Apply replacements
if [ -f "$INPUT_FILE" ]; then
    sed -f "$SED_SCRIPT" "$INPUT_FILE" > "$OUTPUT_FILE"
    echo "Replacements applied. Output: $OUTPUT_FILE"
    echo "Lines processed: $(wc -l < "$INPUT_FILE")"
    rm "$SED_SCRIPT"
else
    echo "Input file not found: $INPUT_FILE"
    echo "Please provide the input data file"
fi
