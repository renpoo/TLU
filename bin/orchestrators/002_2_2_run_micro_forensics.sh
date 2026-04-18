#!/bin/bash
# ==========================================
# 002_2_2_run_micro_forensics.sh
# TLU System: Micro Forensics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. パラメータの取得と Fail-Fast 検証
BASELINE_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?環境変数 TLU_OBSERVATION_WINDOW_MONTHS が設定されていません。}"
KL_DRIFT_THRESH="${TLU_KL_DRIFT_THRESH:?環境変数 TLU_KL_DRIFT_THRESH が設定されていません。}"
Z_SCORE_THRESH="${TLU_ANOMALY_Z_SCORE_THRESHOLD:?環境変数 TLU_ANOMALY_Z_SCORE_THRESHOLD が設定されていません。}"

# 3. パイプラインの実行
run_tlu_pipeline "Micro Forensics Filter" \
    "Src" "Tgt" \
    "src.filters._002_2_2_filter_micro_forensics" "result.002_2_2_filter_micro_forensics.analysis.csv" \
    --baseline_window="${BASELINE_WINDOW}" \
    --kl_drift_thresh="${KL_DRIFT_THRESH}" \
    --z_score_thresh="${Z_SCORE_THRESH}" \
    --node_map="${TLU_NODE_MAP}"
