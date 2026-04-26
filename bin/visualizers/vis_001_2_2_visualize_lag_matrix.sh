#!/bin/bash
# ==========================================
# vis_001_2_1_visualize_lag_matrix.sh
# TLU System: Lag Matrix Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.10: Lag Matrix ==="

run_tlu_visualization "Lag Matrix (Correlation)" "_001_2_2_visualize_lag_matrix_correlation.py" "001_2_1_1__lag_matrix_correlation.png" "result.001_2_1_filter_lag_matrix.analysis.csv"
run_tlu_visualization "Lag Matrix (Optimal Lag)" "_001_2_2_visualize_lag_matrix_lag.py" "001_2_1_2__lag_matrix_optimal_lag.png" "result.001_2_1_filter_lag_matrix.analysis.csv" --corr_thresh 0.5
