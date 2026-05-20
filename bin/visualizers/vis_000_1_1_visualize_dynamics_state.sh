#!/bin/bash
# ==========================================
# vis_000_1_1_visualize_dynamics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.3: Dynamics ==="

run_tlu_visualization "3D Position" "_09_1_visualize_3D_ribbon_master.py" "000_1_1__3d_dynamics_position.png" "result.000_1_1_filter_dynamics.analysis.csv" --target_col "state_X"
run_tlu_visualization "3D Velocity" "_09_1_visualize_3D_ribbon_master.py" "000_1_2__3d_dynamics_velocity.png" "result.000_1_1_filter_dynamics.analysis.csv" --target_col "velocity_v"
run_tlu_visualization "3D Acceleration" "_09_1_visualize_3D_ribbon_master.py" "000_1_3__3d_dynamics_acceleration.png" "result.000_1_1_filter_dynamics.analysis.csv" --target_col "acceleration_a"
run_tlu_visualization "3D Inertia" "_09_1_visualize_3D_ribbon_master.py" "000_1_4__3d_dynamics_inertia.png" "result.000_1_1_filter_dynamics.analysis.csv" --target_col "inertia_M"
run_tlu_visualization "3D Viscosity" "_09_1_visualize_3D_ribbon_master.py" "000_1_5__3d_dynamics_viscosity.png" "result.000_1_1_filter_dynamics.analysis.csv" --target_col "viscosity_C"
run_tlu_visualization "3D External Force" "_09_1_visualize_3D_ribbon_master.py" "000_1_6__3d_dynamics_external_force.png" "result.000_1_1_filter_dynamics.analysis.csv" --target_col "external_force_F"
run_tlu_visualization "Inertia-Viscosity Scatter" "_000_1_7_visualize_inertia_viscosity.py" "000_1_7__inertia_viscosity_scatter.png" "result.000_1_1_filter_dynamics.analysis.csv" --top_k 3
run_tlu_visualization "Phase Portrait 3D" "_000_1_8_visualize_phase_portrait.py" "000_1_8__phase_portrait_3d.png" "result.000_1_1_filter_dynamics.analysis.csv" --max_legend 11
