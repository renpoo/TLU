#!/bin/bash
# ==========================================
# vis_1_7_visualize_control_theory.sh
# TLU System: Control Theory Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.7: Control Theory ==="

run_tlu_visualization "Control Input Trajectory" "1_7_visualize_control_input_trajectory.py" "1_7_1__control_input_trajectory.png" "result.1_7_filter_control_theory.analysis.csv"
run_tlu_visualization "State Error Convergence" "1_7_visualize_error_convergence.py" "1_7_2__control_error_convergence.png" "result.1_7_filter_control_theory.analysis.csv"
run_tlu_visualization "LQR Performance Space" "1_7_visualize_lqr_performance_space.py" "1_7_3__control_lqr_performance_space.png" "result.1_7_filter_control_theory.analysis.csv"
