#!/bin/bash
# ==========================================
# vis_005_2_1_visualize_fractal_noise.sh
# TLU System: Fractal Noise Visualizer
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

run_tlu_visualization "Fractal Noise Spectrum" \
    "_005_2_1_visualize_fractal_noise" \
    "005_2_1_fractal_noise_spectrum.png" \
    "result.005_2_1_filter_fractal_noise.analysis.csv"
