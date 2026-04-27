#!/bin/bash
# ==========================================
# 000_0_1_run_financial_statements.sh
# TLU System: Generate Traditional B/S and P/L
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

echo "Running Financial Statement Generator..."

INPUT_CSV="${TARGET_ENV:-workspace}/input_stream/Dummy_Journal_Stream_Amount.Aggregated.csv"
MAPPING_CSV="${TARGET_ENV:-workspace}/config/_account_mapping.csv"

# Fallback to global workspace mapping if the specific sample doesn't have one
if [ ! -f "$MAPPING_CSV" ]; then
    MAPPING_CSV="workspace/config/_account_mapping.csv"
fi

OUTPUT_MD="${TLU_OUT_DIR}/_00_financial_statements.md"

if [ ! -f "$INPUT_CSV" ]; then
    echo "[WARN] Input CSV not found: $INPUT_CSV. Skipping Financial Statements."
    exit 0
fi

if [ ! -f "$MAPPING_CSV" ]; then
    echo "[WARN] Mapping CSV not found: $MAPPING_CSV. Skipping Financial Statements."
    exit 0
fi

${TLU_PY} -m src.filters._0_2_generate_financial_statements \
    --mapping "$MAPPING_CSV" \
    --output "$OUTPUT_MD" \
    < "$INPUT_CSV"

echo "Financial Statement Generator completed. Output saved to $OUTPUT_MD."
