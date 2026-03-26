#!/bin/bash
# ==========================================
# 1_12_run_network_topology.sh
# TLU System: Network Topology Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

BASELINE_WINDOW=12

run_tlu_pipeline "Network Topology Filter" \
    "Dept" "AccountName" \
    "src.filters._1_12_filter_network_topology" "result.1_12_filter_network_topology.analysis.csv" \
    --baseline_window=${BASELINE_WINDOW} \
    --node_map="${TLU_NODE_MAP}"
