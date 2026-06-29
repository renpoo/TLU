#!/bin/bash
# ==========================================
# vis_000_1_7_1_visualize_viscosity_trend.sh
# TLU System: Local Viscosity Temporal Evolution Heatmap
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 000_1_7_1: Local Viscosity Trend ==="

run_tlu_visualization "Local Viscosity Trend" "_000_1_7_1_visualize_viscosity_trend.py" "000_1_7_1__viscosity_trend.png" "result.000_1_1_filter_dynamics.analysis.csv"
