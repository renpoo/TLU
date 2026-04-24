#!/bin/bash
# ==========================================
# 000_2_1_run_structural_stiffness.sh
# TLU System: Structural Stiffness Matrix Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
HISTORY_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?Environment variable TLU_OBSERVATION_WINDOW_MONTHS is not set.}"

# 3. Execute pipeline
run_tlu_pipeline "Structural Stiffness Matrix Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._000_2_1_filter_structural_stiffness" "result.000_2_1_filter_structural_stiffness.analysis.csv" \
    --history_window="${HISTORY_WINDOW}" \
    --node_map="${TLU_NODE_MAP}"
