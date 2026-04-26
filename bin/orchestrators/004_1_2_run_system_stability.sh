#!/bin/bash
# ==========================================
# 004_1_2_run_system_stability.sh
# TLU System: System Stability Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

run_tlu_pipeline "System Stability Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._004_1_2_filter_system_stability" "result.004_1_2_filter_system_stability.analysis.csv" \
    --node_map="${TLU_NODE_MAP}"
