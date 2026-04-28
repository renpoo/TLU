#!/bin/bash
# ==========================================
# 002_1_2_run_network_topology.sh
# TLU System: Network Topology Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

# 2. Parameter retrieval and Fail-Fast verification
BASELINE_WINDOW="${TLU_OBSERVATION_WINDOW_STEPS:?Environment variable TLU_OBSERVATION_WINDOW_STEPS is not set.}"

# 3. Execute pipeline
run_tlu_pipeline "Network Topology Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._002_1_2_filter_network_topology" "result.002_1_2_filter_network_topology.analysis.csv" \
    --baseline_window="${BASELINE_WINDOW}" \
    --node_map="${TLU_NODE_MAP}"
