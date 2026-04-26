#!/bin/bash
# ==========================================
# vis_001_2_1_visualize_local_thermo.sh
# TLU System: Local Thermodynamics Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.6: Local Thermodynamics ==="

run_tlu_visualization "3D Local Entropy Field" "_09_0_visualize_3D_surface_master.py" "001_1_2_1__3d_local_entropy.png" "result.001_1_2_filter_local_thermodynamics.analysis.csv" --target_col "local_entropy_s"
run_tlu_visualization "3D Local Temperature Field" "_09_0_visualize_3D_surface_master.py" "001_1_2_2__3d_local_temperature.png" "result.001_1_2_filter_local_thermodynamics.analysis.csv" --target_col "local_temperature_t"
run_tlu_visualization "3D Local Temperature Gradient Field" "_09_0_visualize_3D_surface_master.py" "001_1_2_3__3d_local_gradient.png" "result.001_1_2_filter_local_thermodynamics.analysis.csv" --target_col "local_grad_t"
run_tlu_visualization "Local Thermo: Scale vs Volatility" "_001_2_1_visualize_local_thermo_scatter.py" "001_1_2_4__local_thermo_volatility.png" "result.001_1_2_filter_local_thermodynamics.analysis.csv" --mode "temperature" --top_k 3
run_tlu_visualization "Local Thermo: Scale vs Complexity" "_001_2_1_visualize_local_thermo_scatter.py" "001_1_2_5__local_thermo_complexity.png" "result.001_1_2_filter_local_thermodynamics.analysis.csv" --mode "entropy" --top_k 3
run_tlu_visualization "Local Thermo: Scale vs Thermal Gradient" "_001_2_1_visualize_local_thermo_scatter.py" "001_1_2_6__local_thermo_gradient.png" "result.001_1_2_filter_local_thermodynamics.analysis.csv" --mode "gradient" --top_k 3
