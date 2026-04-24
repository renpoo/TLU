#!/bin/bash
# ==========================================
# 001_1_1_run_thermodynamics_macro.sh
# TLU System: Macro Thermodynamics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. Parameter retrieval and Fail-Fast verification
WORK_LABELS="${TLU_THERMO_WORK_LABELS:?Environment variable TLU_THERMO_WORK_LABELS is not set.}"
HEAT_LABELS="${TLU_THERMO_HEAT_LABELS:?Environment variable TLU_THERMO_HEAT_LABELS is not set.}"
TEMP_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?Environment variable TLU_OBSERVATION_WINDOW_MONTHS is not set.}"

# 2. Execute pipeline
run_tlu_pipeline "Macro Thermodynamics Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._001_1_1_filter_macro_thermodynamics" "result.001_1_1_filter_macro_thermodynamics.analysis.csv" \
    --work_labels="${WORK_LABELS}" --heat_labels="${HEAT_LABELS}" --temp_window="${TEMP_WINDOW}" --node_map="${TLU_NODE_MAP}"
