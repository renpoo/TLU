#!/bin/bash
# ==========================================
# 002_2_1_run_forensics.sh
# TLU System: Forensics & Anomaly Detection Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 異常検知の閾値パラメータ
BASELINE_WINDOW=12
LEAK_TOLERANCE=1.0
KL_DRIFT_THRESH=2.0
Z_SCORE_THRESH=3.0

run_tlu_pipeline "Forensics Filter" \
    "Src" "Tgt" \
    "src.filters._002_2_1_filter_macro_forensics" "result.002_2_1_filter_macro_forensics.analysis.csv" \
    --baseline_window=${BASELINE_WINDOW} \
    --leak_tolerance=${LEAK_TOLERANCE} \
    --kl_drift_thresh=${KL_DRIFT_THRESH} \
    --z_score_thresh=${Z_SCORE_THRESH} \
    --node_map="${TLU_NODE_MAP}"
