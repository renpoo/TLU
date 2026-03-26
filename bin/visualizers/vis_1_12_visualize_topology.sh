#!/bin/bash
# ==========================================
# vis_1_12_visualize_topology.sh
# TLU System: Network Topology Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.12: Network Topology ==="

# 1. ネットワーク・トポロジーとエッジ・ストレス
run_tlu_visualization "Network Topology & Stress" "1_12_visualize_network_topology.py" "1_12__network_topology.png" "result.1_12_filter_network_topology.analysis.csv"
