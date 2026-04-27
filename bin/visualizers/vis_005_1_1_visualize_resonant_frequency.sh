#!/bin/bash
# ==========================================
# 005_1_1_visualize_resonant_frequency.sh
# TLU System: Visualize Resonant Frequency
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

run_tlu_visualization "Resonant Frequency & Power" \
    "_005_1_1_visualize_resonant_frequency" \
    "005_1_1_resonant_frequency.png" \
    "result.005_1_1_filter_resonant_frequency.analysis.csv"
