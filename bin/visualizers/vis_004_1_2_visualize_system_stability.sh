#!/bin/bash
# ==========================================
# vis_004_1_2_visualize_system_stability.sh
# TLU System: System Stability Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 004_1_2: System Stability ==="

run_tlu_visualization "System Stability" "_004_1_2_visualize_system_stability.py" "004_1_2__system_stability.png" "result.004_1_2_filter_system_stability.analysis.csv"
