#!/bin/bash
# ==========================================
# vis_002_2_1_visualize_macro_forensics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.8: Macro Forensics ==="

run_tlu_visualization "Macro Forensics Dashboard" "002_2_1_visualize_macro_forensics_dashboard.py" "002_2_1__macro_forensics_dashboard.png" "result.002_2_1_filter_macro_forensics.analysis.csv" --max_legend=11
