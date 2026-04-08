#!/bin/bash
# ==========================================
# 000_2_1_run_structural_stiffness.sh
# TLU System: Structural Stiffness Matrix Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

HISTORY_WINDOW=12

run_tlu_pipeline "Structural Stiffness Matrix Filter" \
    "Src" "Tgt" \
    "src.filters._000_2_1_filter_structural_stiffness" "result.000_2_1_filter_structural_stiffness.analysis.csv" \
    --history_window=${HISTORY_WINDOW} \
    --node_map="${TLU_NODE_MAP}"
