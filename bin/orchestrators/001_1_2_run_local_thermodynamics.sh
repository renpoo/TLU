#!/bin/bash
# ==========================================
# 1_6_run_local_thermo.sh
# TLU System: Local Thermodynamics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. パラメータの取得と Fail-Fast 検証
TEMP_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?環境変数 TLU_OBSERVATION_WINDOW_MONTHS が設定されていません。}"

# 2. パイプラインの実行
run_tlu_pipeline "Local Thermodynamics Filter" \
    "Src" "Tgt" \
    "src.filters._001_1_2_filter_local_thermodynamics" "result.001_1_2_filter_local_thermodynamics.analysis.csv" \
    --temp_window="${TEMP_WINDOW}" --node_map="${TLU_NODE_MAP}"
