#!/bin/bash
# ==========================================
# vis_002_2_2_visualize_micro_forensics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.9: Micro Forensics ==="

# 1. 3D Micro KL Drift
run_tlu_visualization "3D Micro KL Drift" "_09_1_visualize_3D_ribbon_master.py" "002_2_2_1__3d_micro_kl_drift.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --target_col "local_kl_drift"

# 2. 3D Micro Z-Score (State / Growth)
run_tlu_visualization "3D Micro Z-Score (State)" "_09_1_visualize_3D_ribbon_master.py" "002_2_2_2__3d_micro_z_score_X.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --target_col "z_score_X"

# 3. 3D Micro Z-Score (Velocity)
run_tlu_visualization "3D Micro Z-Score (Velocity)" "_09_1_visualize_3D_ribbon_master.py" "002_2_2_3__3d_micro_z_score_v.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --target_col "z_score_v"

# 4. Anomaly Detection Portfolio
run_tlu_visualization "Micro Forensics Phase Space" "_002_2_2_visualize_micro_forensics_scatter.py" "002_2_2_4__micro_forensics_scatter.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --max_legend 11 --z_thresh 10.0 --kl_thresh 0.25
