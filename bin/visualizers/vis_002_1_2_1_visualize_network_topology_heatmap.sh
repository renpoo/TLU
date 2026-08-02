#!/bin/bash
# ==========================================
# vis_002_1_2_1_visualize_network_topology_heatmap.sh
# TLU System: Network Topology Sequential Matrix Heatmaps (Weight & Stress)
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.12.1: Network Topology Matrix Heatmaps ==="

# 1. Transaction Flux Weight Matrix Heatmaps
run_tlu_visualization "Topology Flux Weight Heatmap" "_002_1_3_visualize_network_topology_heatmap.py" "27_topology_weight_heatmap.png" "result.002_1_2_filter_network_topology.analysis.csv" --metric weight

# 2. Edge Stress Z-Score Matrix Heatmaps
run_tlu_visualization "Topology Edge Stress Heatmap" "_002_1_3_visualize_network_topology_heatmap.py" "27_topology_stress_heatmap.png" "result.002_1_2_filter_network_topology.analysis.csv" --metric stress
