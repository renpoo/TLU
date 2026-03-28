#!/bin/bash
# ==========================================
# 1_9_run_micro_forensics.sh
# TLU System: Micro Forensics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 異常検知の閾値パラメータ (ミクロ用)
BASELINE_WINDOW=12
KL_DRIFT_THRESH=3.0
Z_SCORE_THRESH=3.0

run_tlu_pipeline "Micro Forensics Filter" \
    "Src" "Tgt" \
    "src.filters._1_9_filter_micro_forensics" "result.1_9_filter_micro_forensics.analysis.csv" \
    --baseline_window=${BASELINE_WINDOW} \
    --kl_drift_thresh=${KL_DRIFT_THRESH} \
    --z_score_thresh=${Z_SCORE_THRESH} \
    --node_map="${TLU_NODE_MAP}"
