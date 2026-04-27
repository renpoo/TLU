#!/bin/bash
# ==========================================
# 0_0_run_auto_calibrate.sh
# TLU System: Auto-Calibration Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

echo "Running Auto-Calibration (Burn-in) Filter..."

# Generate initial COO stream just for calibration
cat "${TLU_INPUT_CSV}" \
| $TLU_PY -m src.filters._0_2_projector_to_coo \
    --col_time="${TLU_COL_TRANS_DATE:?}" --col_src="${TLU_COL_SRC:?}" --col_tgt="${TLU_COL_TGT:?}" --col_val="${TLU_COL_AMOUNT:?}" \
> "${TLU_TMP_COO}"

# Run the auto-calibrate script
$TLU_PY -m src.filters._0_3_auto_calibrate

echo "Auto-Calibration completed."
echo ""
