#!/bin/bash
# ==========================================
# 001_2_1_run_lag_matrix.sh
# TLU System: Time-Lag Matrix Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

MAX_LAG=6

run_tlu_pipeline "Time-Lag Matrix Filter" \
    "Src" "Tgt" \
    "src.filters._001_2_1_filter_lag_matrix" "result.001_2_1_filter_lag_matrix.analysis.csv" \
    --max_lag=${MAX_LAG} \
    --node_map="${TLU_NODE_MAP}"
