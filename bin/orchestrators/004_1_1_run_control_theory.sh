#!/bin/bash
# ==========================================
# 004_1_1_run_control_theory.sh
# TLU System: Control Theory (LQR) Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. Intervention / Target parameter retrieval and Fail-Fast verification
CONTROLLABLE="${TLU_LQR_CONTROLLABLE_LABELS:?Environment variable TLU_LQR_CONTROLLABLE_LABELS is not set.}"
TARGETS="${TLU_LQR_TARGET_STATE:?Environment variable TLU_LQR_TARGET_STATE is not set.}"
Q_WEIGHT="${TLU_LQR_Q_WEIGHT:?Environment variable TLU_LQR_Q_WEIGHT is not set.}"
R_WEIGHT="${TLU_LQR_R_WEIGHT:?Environment variable TLU_LQR_R_WEIGHT is not set.}"

# 2. Execute pipeline
run_tlu_pipeline "Control Theory (LQR) Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._004_1_1_filter_control_theory" "result.004_1_1_filter_control_theory.analysis.csv" \
    --controllable_labels="${CONTROLLABLE}" \
    --target_state="${TARGETS}" \
    --q_weight="${Q_WEIGHT}" \
    --r_weight="${R_WEIGHT}" \
    --node_map="${TLU_NODE_MAP}"
