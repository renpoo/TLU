#!/bin/bash
# ==========================================
# 005_1_2_run_phase_shift.sh
# TLU System: Phase Shift & Coherence Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# Read dynamic frequency from sys_params (defaults to 0.25)
TARGET_FREQ="${TLU_TARGET_PHASE_FREQUENCY:-0.25}"
WINDOW_SIZE="24"
STEP_SIZE="4"
MASTER_NODE="6"

run_tlu_pipeline "Phase Shift & Coherence Filter (Traversing)" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._005_1_2_filter_phase_shift_coherence" "result.005_1_2_filter_phase_shift_coherence.analysis.csv" \
    --target_freq="${TARGET_FREQ}" \
    --window_size="${WINDOW_SIZE}" \
    --step_size="${STEP_SIZE}"

