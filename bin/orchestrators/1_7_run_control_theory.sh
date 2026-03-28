#!/bin/bash
# ==========================================
# 1_7_run_control_theory.sh
# TLU System: Control Theory (LQR) Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. LQRのパラメータ定義
# 予算を投下できる(介入可能な)部門
CONTROLLABLE="DPT_Marketing,DPT_Sales,DPT_R&D"

# 達成したい目標状態 (例: 売上高を100,000にする)
TARGETS="ACC_Sales_Revenue_Global:100000"

# 重みパラメータ (Q: 目標達成の執念, R: 予算節約の執念)
Q_WEIGHT=1.0
R_WEIGHT=0.1

# 2. パイプラインの実行
run_tlu_pipeline "Control Theory (LQR) Filter" \
    "Src" "Tgt" \
    "src.filters._1_7_filter_control_theory" "result.1_7_filter_control_theory.analysis.csv" \
    --controllable_labels="${CONTROLLABLE}" \
    --target_state="${TARGETS}" \
    --q_weight=${Q_WEIGHT} \
    --r_weight=${R_WEIGHT} \
    --node_map="${TLU_NODE_MAP}"
