#!/bin/bash
# ==========================================
# 1_3_run_dynamics_state.sh
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. パラメータの取得と Fail-Fast 検証
HISTORY_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?環境変数 TLU_OBSERVATION_WINDOW_MONTHS が設定されていません。}"

# 2. パイプラインの実行
run_tlu_pipeline "Dynamics State Filter" \
    "Src" "Tgt" \
    "src.filters._000_1_1_filter_dynamics_state" "result.000_1_1_filter_dynamics.analysis.csv" \
    --history_window="${HISTORY_WINDOW}" --node_map="${TLU_NODE_MAP}"
