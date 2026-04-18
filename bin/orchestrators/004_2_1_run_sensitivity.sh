#!/bin/bash
# ==========================================
# 004_2_1_run_sensitivity.sh
# TLU System: Sensitivity & Trade-off Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
GAMMA="${TLU_DAMPING_FACTOR:?Environment variable TLU_DAMPING_FACTOR is not set.}"
DELTA=10.0

# 3. Execute pipeline
run_tlu_pipeline "Sensitivity & Trade-off Filter" \
    "Src" "Tgt" \
    "src.filters._004_2_1_filter_sensitivity" "result.004_2_1_filter_sensitivity.analysis.csv" \
    --delta="${DELTA}" --gamma="${GAMMA}" --max_k=5 --node_map="${TLU_NODE_MAP}"
