#!/bin/bash
# ==========================================
# vis_002_2_2_visualize_micro_forensics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.9: Micro Forensics ==="

# 1. KL Drift 3D Surface
run_tlu_visualization "Micro KL Drift 3D Surface" "_09_0_visualize_3D_surface_master.py" "002_2_2_1__micro_KL_drift_3d_surface.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --target_col "node_kl_drift" --z_label "KL Drift (Bits)" --c_label "KL Drift Intensity"

# 2. Z-Score 3D Surface
run_tlu_visualization "Micro Z-Score 3D Surface" "_09_0_visualize_3D_surface_master.py" "002_2_2_2__micro_Z_Score_3d_surface.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --target_col "node_univariate_z_score" --z_label "Z-Score (sigma)" --c_label "Z-Score Intensity"

# 3. Anomaly Detection Portfolio (Execute the target script here / input file changed to 1.9)
run_tlu_visualization "Micro Forensics Phase Space" "_002_2_2_visualize_micro_forensics_scatter.py" "002_2_2_3__micro_forensics_scatter.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --max_legend 11 --z_thresh 10.0 --kl_thresh 0.25
