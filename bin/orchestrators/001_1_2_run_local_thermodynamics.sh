#!/bin/bash
# ==========================================
# 1_6_run_local_thermo.sh
# TLU System: Local Thermodynamics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. Parameter retrieval and Fail-Fast verification
TEMP_WINDOW="${TLU_OBSERVATION_WINDOW_STEPS:?Environment variable TLU_OBSERVATION_WINDOW_STEPS is not set.}"

# 2. Execute pipeline
run_tlu_pipeline "Local Thermodynamics Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._001_1_2_filter_local_thermodynamics" "result.001_1_2_filter_local_thermodynamics.analysis.csv" \
    --temp_window="${TEMP_WINDOW}" --node_map="${TLU_NODE_MAP}"
