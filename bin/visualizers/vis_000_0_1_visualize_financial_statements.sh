#!/bin/bash
# ==========================================
# vis_000_0_1_visualize_financial_statements.sh
# TLU System: Visualize Traditional Financial Statements
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "Running Financial Statement Visualizer..."

INPUT_JSON="${TLU_OUT_DIR}/_00_financial_statements.json"

if [ ! -f "$INPUT_JSON" ]; then
    echo "[WARN] Input JSON not found: $INPUT_JSON. Skipping visualization."
    exit 0
fi

${TLU_PY} -m src.visualizations._000_0_1_visualize_financial_statements \
    --json "$INPUT_JSON" \
    --out_dir "${TLU_PLOT_DIR}"

echo "✅ Saved Financial Statement plots to ${TLU_PLOT_DIR}/"
