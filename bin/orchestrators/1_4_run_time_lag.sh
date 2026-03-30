#!/bin/bash
# ==========================================
# 1_4_run_time_lag.sh
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. 解析対象のシグナルペアをドメインラベルで指定 (LabelA:LabelB,LabelC:LabelD)
# 例: マーケティング部門の活動が、売上にどう波及するか
SIGNAL_PAIRS="ACC_Sales_Revenue:ACC_Cash,ACC_Sales_Revenue:ACC_Accounts_Receivable"

run_tlu_pipeline "Time Lag Analysis Filter" \
    "Src" "Tgt" \
    "src.filters._1_4_filter_time_lag" "result.1_4_filter_time_lag.analysis.csv" \
    --signal_pairs_labels="${SIGNAL_PAIRS}" --max_lag=6 --node_map="${TLU_NODE_MAP}"
