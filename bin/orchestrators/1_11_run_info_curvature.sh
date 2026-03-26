#!/bin/bash
# ==========================================
# 1_11_run_info_curvature.sh
# TLU System: Information Curvature Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

WINDOW=3

run_tlu_pipeline "Information Curvature Filter" \
    "Dept" "AccountName" \
    "src.filters._1_11_filter_info_curvature" "result.1_11_filter_info_curvature.analysis.csv" \
    --window=${WINDOW} \
    --node_map="${TLU_NODE_MAP}"
