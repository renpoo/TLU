#!/bin/bash
# ==========================================
# vis_002_1_2_visualize_network_topology.sh
# TLU System: Network Topology Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.12: Network Topology ==="

# 1. Network Topology and Edge Stress
run_tlu_visualization "Network Topology & Stress" "_002_1_2_visualize_network_topology.py" "002_1_2__network_topology.png" "result.002_1_2_filter_network_topology.analysis.csv"
