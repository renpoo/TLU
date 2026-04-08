#!/bin/bash
# ==========================================
# vis_003_1_1_visualize_fk_simulation.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.1: Forward Kinematics ==="

run_tlu_visualization "3D Kinematics (FK Impact)" "9_0_visualize_3D_surface_master.py" "003_1_1__3d_kinematics_fk.png" "result.003_1_1_filter_fk.analysis.csv" --target_col "fk_echo_impact"
