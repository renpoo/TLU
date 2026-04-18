#!/bin/bash
# ==========================================
# 004_1_1_run_control_theory.sh
# TLU System: Control Theory (LQR) Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. 介入・目標パラメータの取得と Fail-Fast 検証
CONTROLLABLE="${TLU_LQR_CONTROLLABLE_LABELS:?環境変数 TLU_LQR_CONTROLLABLE_LABELS が設定されていません。}"
TARGETS="${TLU_LQR_TARGET_STATE:?環境変数 TLU_LQR_TARGET_STATE が設定されていません。}"
Q_WEIGHT="${TLU_LQR_Q_WEIGHT:?環境変数 TLU_LQR_Q_WEIGHT が設定されていません。}"
R_WEIGHT="${TLU_LQR_R_WEIGHT:?環境変数 TLU_LQR_R_WEIGHT が設定されていません。}"

# 2. パイプラインの実行
run_tlu_pipeline "Control Theory (LQR) Filter" \
    "Src" "Tgt" \
    "src.filters._004_1_1_filter_control_theory" "result.004_1_1_filter_control_theory.analysis.csv" \
    --controllable_labels="${CONTROLLABLE}" \
    --target_state="${TARGETS}" \
    --q_weight="${Q_WEIGHT}" \
    --r_weight="${R_WEIGHT}" \
    --node_map="${TLU_NODE_MAP}"
