#!/bin/bash
# ==========================================
# 1_5_run_thermodynamics_macro.sh
# TLU System: Macro Thermodynamics Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 1. 物理的役割（仕事と熱）のドメインラベル定義
# ※カンマ区切り、スペースなしで指定します
WORK_LABELS="ACC_Sales_Revenue"
HEAT_LABELS="ACC_Travel_Exp,ACC_Rent_Exp,ACC_Payroll_Exp,ACC_COGS"

# 2. パイプラインの実行
run_tlu_pipeline "Macro Thermodynamics Filter" \
    "Src" "Tgt" \
    "src.filters._1_5_filter_thermodynamics_macro" "result.1_5_filter_thermodynamics.analysis.csv" \
    --work_labels="${WORK_LABELS}" --heat_labels="${HEAT_LABELS}" --temp_window=3 --node_map="${TLU_NODE_MAP}"
