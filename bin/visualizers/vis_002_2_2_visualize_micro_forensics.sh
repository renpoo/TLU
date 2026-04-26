#!/bin/bash
# ==========================================
# vis_002_2_2_visualize_micro_forensics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.9: Micro Forensics ==="

# 1. KL Drift Heatmap
run_tlu_visualization "Micro KL Drift Heatmap" "_002_2_2_visualize_micro_forensics_kl_drift_heatmap.py" "002_2_2_1__micro_KL_drift_heatmap.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --top_k 3

# 2. Z-Score Heatmap
run_tlu_visualization "Micro Z-Score Heatmap" "_002_2_2_visualize_micro_forensics_z_score_heatmap.py" "002_2_2_2__micro_forensics_Z_Score_heatmap.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --top_k 3

# 3. Anomaly Detection Portfolio (Execute the target script here / input file changed to 1.9)
run_tlu_visualization "Micro Forensics Phase Space" "_002_2_2_visualize_micro_forensics_scatter.py" "002_2_2_3__micro_forensics_scatter.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --max_legend 11 --z_thresh 10.0 --kl_thresh 0.25
