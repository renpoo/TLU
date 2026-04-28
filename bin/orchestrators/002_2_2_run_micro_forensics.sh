#!/bin/bash
# ==========================================
# 002_2_2_run_micro_forensics.sh
# TLU System: Micro Forensics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
BASELINE_WINDOW="${TLU_OBSERVATION_WINDOW_STEPS:?Environment variable TLU_OBSERVATION_WINDOW_STEPS is not set.}"
KL_DRIFT_THRESH="${TLU_KL_DRIFT_THRESH:?Environment variable TLU_KL_DRIFT_THRESH is not set.}"
Z_SCORE_THRESH="${TLU_ANOMALY_Z_SCORE_THRESHOLD:?Environment variable TLU_ANOMALY_Z_SCORE_THRESHOLD is not set.}"

# 3. Execute pipeline
run_tlu_pipeline "Micro Forensics Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._002_2_2_filter_micro_forensics" "result.002_2_2_filter_micro_forensics.analysis.csv" \
    --baseline_window="${BASELINE_WINDOW}" \
    --kl_drift_thresh="${KL_DRIFT_THRESH}" \
    --z_score_thresh="${Z_SCORE_THRESH}" \
    --node_map="${TLU_NODE_MAP}"
