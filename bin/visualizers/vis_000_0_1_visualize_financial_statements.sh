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

SEQ_DIR="${TLU_PLOT_DIR}/financial_statements_sequence"
mkdir -p "${SEQ_DIR}"

TOP_K_ARG=""
if [ -n "${TLU_TOP_K:-}" ]; then
    TOP_K_ARG="--top_k ${TLU_TOP_K}"
elif [[ "${TARGET_ENV:-}" == *"Sample_5_Kyoto_Traffic"* ]]; then
    TOP_K_ARG="--top_k 0"
fi

${TLU_PY} -m src.visualizations._000_0_1_visualize_financial_statements \
    --json "$INPUT_JSON" \
    --out_dir "${TLU_PLOT_DIR}" \
    --seq_dir "${SEQ_DIR}" \
    --time_map "${TLU_TIME_MAP:-}" \
    --node_map "${TLU_NODE_MAP:-}" \
    ${TOP_K_ARG}

echo "✅ Saved Financial Statement plots to ${TLU_PLOT_DIR}/"
