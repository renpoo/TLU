#!/bin/bash
# ==========================================
# 002_1_1_run_info_curvature.sh
# TLU System: Information Curvature Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. Parameter retrieval and Fail-Fast verification
WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?Environment variable TLU_OBSERVATION_WINDOW_MONTHS is not set.}"

# 2. Execute pipeline
run_tlu_pipeline "Information Curvature Filter" \
    "Src" "Tgt" \
    "src.filters._002_1_1_filter_info_curvature" "result.002_1_1_filter_info_curvature.analysis.csv" \
    --window="${WINDOW}" \
    --node_map="${TLU_NODE_MAP}"
