#!/bin/bash
# ==========================================
# 1_6_run_local_thermo.sh
# TLU System: Local Thermodynamics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

run_tlu_pipeline "Local Thermodynamics Filter" \
    "Src" "Tgt" \
    "src.filters._1_6_filter_local_thermo" "result.1_6_filter_local_thermo.analysis.csv" \
    --temp_window=3 --node_map="${TLU_NODE_MAP}"
