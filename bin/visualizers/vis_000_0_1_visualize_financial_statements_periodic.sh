#!/bin/bash
# ==========================================
# vis_000_0_1_visualize_financial_statements_periodic.sh
# TLU System: Visualize Periodic Financial Statements
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "Running Periodic Financial Statement Visualizer..."

INPUT_JSON="${TLU_OUT_DIR}/_00_financial_statements_periodic.json"

if [ ! -f "$INPUT_JSON" ]; then
    echo "[WARN] Input JSON not found: $INPUT_JSON. Skipping visualization."
    exit 0
fi

SEQ_DIR="${TLU_PLOT_DIR}/financial_statements_periodic_sequence"
mkdir -p "${SEQ_DIR}"

TOP_K_ARG=""
if [[ "${TARGET_ENV:-}" == *"Sample_5_Kyoto_Traffic"* ]]; then
    TOP_K_ARG="--top_k 0"
fi

${TLU_PY} -m src.visualizations._000_0_1_visualize_financial_statements_periodic \
    --json "$INPUT_JSON" \
    --out_dir "${TLU_PLOT_DIR}" \
    --seq_dir "${SEQ_DIR}" \
    ${TOP_K_ARG}

echo "✅ Saved Periodic Financial Statement plots to ${TLU_PLOT_DIR}/"
