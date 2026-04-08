#!/bin/bash
# ==========================================
# 1_3_run_dynamics_state.sh
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

run_tlu_pipeline "Dynamics State Filter" \
    "Src" "Tgt" \
    "src.filters._000_1_1_filter_dynamics_state" "result.000_1_1_filter_dynamics.analysis.csv" \
    --history_window=100 --node_map="${TLU_NODE_MAP}"
