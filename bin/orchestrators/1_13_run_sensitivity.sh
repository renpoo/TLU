#!/bin/bash
# ==========================================
# 1_13_run_sensitivity.sh
# TLU System: Sensitivity & Trade-off Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 仮想投資 / 目標変位量（Delta）
DELTA=10.0

run_tlu_pipeline "Sensitivity & Trade-off Filter" \
    "Src" "Tgt" \
    "src.filters._1_13_filter_sensitivity" "result.1_13_filter_sensitivity.analysis.csv" \
    --delta=${DELTA} --gamma=0.85 --max_k=5 --node_map="${TLU_NODE_MAP}"
