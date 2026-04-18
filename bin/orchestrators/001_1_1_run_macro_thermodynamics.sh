#!/bin/bash
# ==========================================
# 001_1_1_run_thermodynamics_macro.sh
# TLU System: Macro Thermodynamics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. パラメータの取得と Fail-Fast 検証
WORK_LABELS="${TLU_THERMO_WORK_LABELS:?環境変数 TLU_THERMO_WORK_LABELS が設定されていません。}"
HEAT_LABELS="${TLU_THERMO_HEAT_LABELS:?環境変数 TLU_THERMO_HEAT_LABELS が設定されていません。}"
TEMP_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?環境変数 TLU_OBSERVATION_WINDOW_MONTHS が設定されていません。}"

# 2. パイプラインの実行
run_tlu_pipeline "Macro Thermodynamics Filter" \
    "Src" "Tgt" \
    "src.filters._001_1_1_filter_macro_thermodynamics" "result.001_1_1_filter_macro_thermodynamics.analysis.csv" \
    --work_labels="${WORK_LABELS}" --heat_labels="${HEAT_LABELS}" --temp_window="${TEMP_WINDOW}" --node_map="${TLU_NODE_MAP}"
