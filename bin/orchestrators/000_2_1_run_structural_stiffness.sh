#!/bin/bash
# ==========================================
# 000_2_1_run_structural_stiffness.sh
# TLU System: Structural Stiffness Matrix Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. パラメータの取得と Fail-Fast 検証
HISTORY_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?環境変数 TLU_OBSERVATION_WINDOW_MONTHS が設定されていません。}"

# 3. パイプラインの実行
run_tlu_pipeline "Structural Stiffness Matrix Filter" \
    "Src" "Tgt" \
    "src.filters._000_2_1_filter_structural_stiffness" "result.000_2_1_filter_structural_stiffness.analysis.csv" \
    --history_window="${HISTORY_WINDOW}" \
    --node_map="${TLU_NODE_MAP}"
