#!/bin/bash
# ==========================================
# 002_1_2_run_network_topology.sh
# TLU System: Network Topology Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. パラメータの取得と Fail-Fast 検証
BASELINE_WINDOW="${TLU_OBSERVATION_WINDOW_MONTHS:?環境変数 TLU_OBSERVATION_WINDOW_MONTHS が設定されていません。}"

# 3. パイプラインの実行
run_tlu_pipeline "Network Topology Filter" \
    "Src" "Tgt" \
    "src.filters._002_1_2_filter_network_topology" "result.002_1_2_filter_network_topology.analysis.csv" \
    --baseline_window="${BASELINE_WINDOW}" \
    --node_map="${TLU_NODE_MAP}"
