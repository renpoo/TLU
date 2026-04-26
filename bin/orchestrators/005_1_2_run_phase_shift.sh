#!/bin/bash
# ==========================================
# 005_1_2_run_phase_shift.sh
# TLU System: Phase Shift & Coherence Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# We will set a fixed target frequency for Phase 005_1_2 for now.
# Frequency = 0.25 (Period = 4 weeks / 1 month)
TARGET_FREQ="0.25"
WINDOW_SIZE="24"
STEP_SIZE="4"
MASTER_NODE="6"

run_tlu_pipeline "Phase Shift & Coherence Filter (Traversing)" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._005_1_2_filter_phase_shift_coherence" "result.005_1_2_filter_phase_shift_coherence.analysis.csv" \
    --target_freq="${TARGET_FREQ}" \
    --window_size="${WINDOW_SIZE}" \
    --step_size="${STEP_SIZE}"

run_tlu_visualization "Phase Drift Heatmap (Node)" \
    "_005_1_2_visualize_phase_drift_heatmap" \
    "005_1_2_phase_drift_heatmap.png" \
    "result.005_1_2_filter_phase_shift_coherence.analysis.csv" \
    --master_node="${MASTER_NODE}"
