#!/bin/bash
# ==========================================
# 000_2_4_run_stiffness_difference.sh
# TLU System: Orchestrator to extract stiffness temporal difference
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

INPUT_CSV="${TLU_OUT_DIR}/result.000_2_1_filter_structural_stiffness.analysis.csv"
OUTPUT_CSV="${TLU_OUT_DIR}/result.000_2_4_stiffness_diff.analysis.csv"

if [ ! -f "${INPUT_CSV}" ]; then
    echo "Error: Input file ${INPUT_CSV} not found." >&2
    exit 1
fi

echo "==> Extracting Stiffness Difference..."
python3 -m src.filters._000_2_4_filter_stiffness_difference < "${INPUT_CSV}" > "${OUTPUT_CSV}"
echo "Stiffness Difference saved to: ${OUTPUT_CSV}"
