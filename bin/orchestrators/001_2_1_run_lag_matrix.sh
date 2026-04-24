#!/bin/bash
# ==========================================
# 001_2_1_run_lag_matrix.sh
# TLU System: Time-Lag Matrix Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
MAX_LAG="${TLU_OBSERVATION_WINDOW_MONTHS:?Environment variable TLU_OBSERVATION_WINDOW_MONTHS is not set.}"

# 3. Execute pipeline
run_tlu_pipeline "Time-Lag Matrix Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._001_2_1_filter_lag_matrix" "result.001_2_1_filter_lag_matrix.analysis.csv" \
    --max_lag="${MAX_LAG}" \
    --node_map="${TLU_NODE_MAP}"
