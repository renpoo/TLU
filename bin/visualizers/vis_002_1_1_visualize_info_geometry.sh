#!/bin/bash
# ==========================================
# vis_002_1_1_visualize_info_geometry.sh
# TLU System: Information Geometry Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.11: Information Geometry ==="

# 1. 3D Info Curvature Manifold (Curvature Field)
run_tlu_visualization "3D Info Curvature Field" "_09_0_visualize_3D_surface_master.py" "002_1_1__3d_info_curvature.png" "result.002_1_1_filter_info_curvature.analysis.csv" --target_col "curvature" --color_col "density"

# 2. Structural Stress Scatter Plot (Structural Stress Matrix)
run_tlu_visualization "Structural Stress Matrix" "_002_1_2_visualize_info_stress_scatter.py" "002_1_2__info_stress_scatter.png" "result.002_1_1_filter_info_curvature.analysis.csv" --top_k 3
