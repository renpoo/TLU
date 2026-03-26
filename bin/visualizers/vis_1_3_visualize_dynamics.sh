#!/bin/bash
# ==========================================
# vis_1_3_visualize_dynamics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.3: Dynamics ==="

run_tlu_visualization "3D Velocity" "9_0_visualize_3D_surface_master.py" "1_3_1__3d_dynamics_velocity.png" "result.1_3_filter_dynamics.analysis.csv" --target_col "velocity_v"
run_tlu_visualization "3D Acceleration" "9_0_visualize_3D_surface_master.py" "1_3_2__3d_dynamics_acceleration.png" "result.1_3_filter_dynamics.analysis.csv" --target_col "acceleration_a"
run_tlu_visualization "3D Inertia" "9_0_visualize_3D_surface_master.py" "1_3_3__3d_dynamics_inertia.png" "result.1_3_filter_dynamics.analysis.csv" --target_col "inertia_M"
run_tlu_visualization "3D Viscosity" "9_0_visualize_3D_surface_master.py" "1_3_4__3d_dynamics_viscosity.png" "result.1_3_filter_dynamics.analysis.csv" --target_col "viscosity_C"
run_tlu_visualization "3D Entropy" "9_0_visualize_3D_surface_master.py" "1_3_5__3d_dynamics_entropy.png" "result.1_3_filter_dynamics.analysis.csv" --target_col "external_force_F"
run_tlu_visualization "3D Complexity" "9_0_visualize_3D_surface_master.py" "1_3_6__3d_dynamics_complexity.png" "result.1_3_filter_dynamics.analysis.csv" --target_col "net_flux_q"
run_tlu_visualization "Inertia-Viscosity Space" "1_3_visualize_inertia_viscosity.py" "1_3_7__inertia_viscosity_scatter.png" "result.1_3_filter_dynamics.analysis.csv" --top_k 3
run_tlu_visualization "Phase Portrait 3D" "1_3_visualize_phase_portrait.py" "1_3_8__phase_portrait_3d.png" "result.1_3_filter_dynamics.analysis.csv" --max_legend 11
