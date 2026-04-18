#!/bin/bash
# ==========================================
# 004_2_1_run_sensitivity.sh
# TLU System: Sensitivity & Trade-off Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. パラメータの取得と Fail-Fast 検証
GAMMA="${TLU_DAMPING_FACTOR:?環境変数 TLU_DAMPING_FACTOR が設定されていません。}"
DELTA=10.0

# 3. パイプラインの実行
run_tlu_pipeline "Sensitivity & Trade-off Filter" \
    "Src" "Tgt" \
    "src.filters._004_2_1_filter_sensitivity" "result.004_2_1_filter_sensitivity.analysis.csv" \
    --delta="${DELTA}" --gamma="${GAMMA}" --max_k=5 --node_map="${TLU_NODE_MAP}"
