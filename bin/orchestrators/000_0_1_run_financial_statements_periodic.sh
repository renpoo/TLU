#!/bin/bash
# ==========================================
# 000_0_1_run_financial_statements_periodic.sh
# TLU System: Generate Periodic Non-Cumulative B/S and P/L
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

echo "Running Periodic Financial Statement Generator..."

INPUT_CSV="${TLU_INPUT_CSV}"
MAPPING_CSV="${TLU_ACCOUNT_MAPPING:-${TARGET_ENV:-workspace}/config/_account_mapping.csv}"

# Fallback to global workspace mapping if the specific sample doesn't have one
if [ ! -f "$MAPPING_CSV" ]; then
    MAPPING_CSV="workspace/config/_account_mapping.csv"
fi

OUTPUT_MD="${TLU_OUT_DIR}/_00_financial_statements_periodic.md"

if [ ! -f "$INPUT_CSV" ]; then
    echo "[WARN] Input CSV not found: $INPUT_CSV. Skipping Periodic Financial Statements."
    exit 0
fi

if [ ! -f "$MAPPING_CSV" ]; then
    echo "[WARN] Mapping CSV not found: $MAPPING_CSV. Skipping Periodic Financial Statements."
    exit 0
fi

${TLU_PY} -m src.filters._0_2_generate_financial_statements_periodic \
    --mapping "$MAPPING_CSV" \
    --initial_state "${TARGET_ENV}/ephemeral/_initial_state_labels.csv" \
    --output "$OUTPUT_MD" \
    < "$INPUT_CSV"

echo "Periodic Financial Statement Generator completed. Output saved to $OUTPUT_MD."
