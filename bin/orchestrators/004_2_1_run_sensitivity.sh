#!/bin/bash
# ==========================================
# 004_2_1_run_sensitivity.sh
# TLU System: Sensitivity & Trade-off Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
GAMMA="${TLU_DAMPING_FACTOR:?Environment variable TLU_DAMPING_FACTOR is not set.}"
MAX_K="${TLU_KINEMATICS_MAX_K:?Environment variable TLU_KINEMATICS_MAX_K is not set.}"
DELTA="${TLU_SENSITIVITY_DELTA:?Environment variable TLU_SENSITIVITY_DELTA is not set.}"

# 3. Execute pipeline
run_tlu_pipeline "Sensitivity & Trade-off Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._004_2_1_filter_sensitivity" "result.004_2_1_filter_sensitivity.analysis.csv" \
    --delta="${DELTA}" --gamma="${GAMMA}" --max_k="${MAX_K}" --node_map="${TLU_NODE_MAP}"
