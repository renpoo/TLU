#!/bin/bash
# ==========================================
# vis_001_1_1_visualize_macro_thermodynamics.sh
# TLU System: Macro Thermodynamics Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.5: Macro Thermodynamics ==="

run_tlu_visualization "Macro Thermodynamics Dashboard" "001_1_1_visualize_thermodynamics_dashboard.py" "001_1_1__thermodynamics_dashboard.png" "result.001_1_1_filter_macro_thermodynamics.analysis.csv"
run_tlu_visualization "Macro Thermodynamics Energy Stack" "001_1_2_visualize_thermodynamics_energy_stack.py" "001_1_2__thermodynamics_energy_stack.png" "result.001_1_1_filter_macro_thermodynamics.analysis.csv"
run_tlu_visualization "Macro Thermodynamics T-S Diagram" "001_1_3_visualize_thermodynamics_ts_diagram.py" "001_1_3__thermodynamics_ts_diagram.png" "result.001_1_1_filter_macro_thermodynamics.analysis.csv"
