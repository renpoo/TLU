#!/bin/bash
# ==========================================
# vis_004_1_1_visualize_control_theory.sh
# TLU System: Control Theory Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.7: Control Theory ==="

run_tlu_visualization "Control Input Trajectory" "004_1_1_visualize_control_input_trajectory.py" "004_1_1__control_input_trajectory.png" "result.004_1_1_filter_control_theory.analysis.csv"
run_tlu_visualization "State Error Convergence" "004_1_2_visualize_error_convergence.py" "004_1_2__control_error_convergence.png" "result.004_1_1_filter_control_theory.analysis.csv"
run_tlu_visualization "LQR Performance Space" "004_1_3_visualize_lqr_performance_space.py" "004_1_3__control_lqr_performance_space.png" "result.004_1_1_filter_control_theory.analysis.csv"
