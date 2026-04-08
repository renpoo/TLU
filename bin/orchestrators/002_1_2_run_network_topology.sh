#!/bin/bash
# ==========================================
# 002_1_2_run_network_topology.sh
# TLU System: Network Topology Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

BASELINE_WINDOW=12

run_tlu_pipeline "Network Topology Filter" \
    "Src" "Tgt" \
    "src.filters._002_1_2_filter_network_topology" "result.002_1_2_filter_network_topology.analysis.csv" \
    --baseline_window=${BASELINE_WINDOW} \
    --node_map="${TLU_NODE_MAP}"
