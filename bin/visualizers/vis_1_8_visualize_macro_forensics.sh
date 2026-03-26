#!/bin/bash
# ==========================================
# vis_1_8_visualize_macro_forensics.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 1.8: Macro Forensics ==="

run_tlu_visualization "Macro Forensics Dashboard" "1_8_visualize_macro_forensics_dashboard.py" "1_8__macro_forensics_dashboard.png" "result.1_8_filter_forensics.analysis.csv" --max_legend=11
