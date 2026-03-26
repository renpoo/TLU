#!/bin/bash
# ==========================================
# vis_1_5_visualize_thermodynamics_macro.sh
# TLU System: Macro Thermodynamics Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.5: Macro Thermodynamics ==="

run_tlu_visualization "Macro Thermodynamics Dashboard" "1_5_visualize_thermodynamics_dashboard.py" "1_5_1__thermodynamics_dashboard.png" "result.1_5_filter_thermodynamics.analysis.csv"
run_tlu_visualization "Macro Thermodynamics Energy Stack" "1_5_visualize_thermodynamics_energy_stack.py" "1_5_2__thermodynamics_energy_stack.png" "result.1_5_filter_thermodynamics.analysis.csv"
run_tlu_visualization "Macro Thermodynamics T-S Diagram" "1_5_visualize_thermodynamics_ts_diagram.py" "1_5_3__thermodynamics_ts_diagram.png" "result.1_5_filter_thermodynamics.analysis.csv"
