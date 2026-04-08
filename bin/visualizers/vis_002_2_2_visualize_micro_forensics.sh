#!/bin/bash
# ==========================================
# vis_002_2_2_visualize_micro_forensics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.9: Micro Forensics ==="

# 1. KLドリフト ヒートマップ
run_tlu_visualization "Micro KL Drift Heatmap" "002_2_2_visualize_micro_forensics_kl_drift_heatmap.py" "002_2_2_1__micro_KL_drift_heatmap.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --top_k 3

# 2. Zスコア ヒートマップ
run_tlu_visualization "Micro Z-Score Heatmap" "002_2_2_visualize_micro_forensics_z_score_heatmap.py" "002_2_2_2__micro_forensics_Z_Score_heatmap.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --top_k 3

# 3. 異常検知ポートフォリオ（問題のスクリプトをここで実行・入力ファイルを1.9に変更）
run_tlu_visualization "Micro Forensics Phase Space" "002_2_2_visualize_micro_forensics_scatter.py" "002_2_2_3__micro_forensics_scatter.png" "result.002_2_2_filter_micro_forensics.analysis.csv" --max_legend 11 --z_thresh 10.0 --kl_thresh 0.25
