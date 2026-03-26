#!/bin/bash
# ==========================================
# vis_1_2_visualize_inverse_kinematics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.2: Inverse Kinematics ==="

run_tlu_visualization "3D Kinematics (IK Impact)" "9_0_visualize_3D_surface_master.py" "1_2__3d_kinematics_ik.png" "result.1_2_filter_ik.analysis.csv" --target_col "ik_suggested_delta"
