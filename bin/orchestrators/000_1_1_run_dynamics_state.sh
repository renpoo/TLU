#!/bin/bash
# ==========================================
# 1_3_run_dynamics_state.sh
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. Parameter retrieval and Fail-Fast verification
HISTORY_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?Environment variable TLU_OBSERVATION_WINDOW_MONTHS is not set.}"

# 2. Execute pipeline
run_tlu_pipeline "Dynamics State Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._000_1_1_filter_dynamics_state" "result.000_1_1_filter_dynamics.analysis.csv" \
    --history_window="${HISTORY_WINDOW}" --node_map="${TLU_NODE_MAP}"
