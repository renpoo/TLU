#!/bin/bash
# ==========================================
# run_basic_statistics.sh
# TLU System: SDL_007 Classical Statistical Baseline
# Category: Pre-analysis / Baseline Validation
# ==========================================
source "$(dirname "$0")/orchestrators/_tlu_env.sh"

START_TIME=${1:-}
END_TIME=${2:-}
TARGET_ENV=${TARGET_ENV:-"workspace"}

INPUT_CSV="${TLU_PROJECT_ROOT}/${TARGET_ENV}/output_data/result.000_1_1_filter_dynamics.analysis.csv"
OUTPUT_MD="${TLU_PROJECT_ROOT}/${TARGET_ENV}/output_data/_00_basic_statistics_profile.md"

if [ ! -f "$INPUT_CSV" ]; then
    echo "[ERROR] Input data not found: $INPUT_CSV"
    echo "Please ensure the sample has been processed through the dynamics filter first."
    exit 1
fi

echo "=================================================="
echo "TLU Phase 0.5: Classical Statistics Baseline (SDL_007)"
echo "=================================================="
echo "Target Environment: ${TARGET_ENV}"

CMD="${TLU_PY} src/filters/_00_basic_statistics_profile.py --output_md \"${OUTPUT_MD}\""

if [ -n "$START_TIME" ]; then
    CMD="$CMD --start_time \"$START_TIME\""
    echo "Time Window Start: $START_TIME"
fi

if [ -n "$END_TIME" ]; then
    CMD="$CMD --end_time \"$END_TIME\""
    echo "Time Window End: $END_TIME"
fi

eval "cat \"$INPUT_CSV\" | $CMD"

echo "Completed. Baseline report saved to: ${OUTPUT_MD}"
echo "=================================================="
