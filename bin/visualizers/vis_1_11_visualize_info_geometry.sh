#!/bin/bash
# ==========================================
# vis_1_11_visualize_info_geometry.sh
# TLU System: Information Geometry Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.11: Information Geometry ==="

# 1. 3D情報曲率多様体 (Curvature Field)
run_tlu_visualization "3D Info Curvature Field" "9_0_visualize_3D_surface_master.py" "1_11_1__3d_info_curvature.png" "result.1_11_filter_info_curvature.analysis.csv" --target_col "curvature" --color_col "density"

# 2. 構造ストレス散布図 (Structural Stress Matrix)
run_tlu_visualization "Structural Stress Matrix" "1_11_visualize_info_stress_scatter.py" "1_11_2__info_stress_scatter.png" "result.1_11_filter_info_curvature.analysis.csv" --top_k 3
