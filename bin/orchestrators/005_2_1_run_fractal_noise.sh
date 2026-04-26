#!/bin/bash
# ==========================================
# 005_2_1_run_fractal_noise.sh
# TLU System: Fractal Dimensionality & 1/f Noise Orchestrator
# ==========================================
source "$(dirname "$0")/_tlu_env.sh"

run_tlu_pipeline "Fractal Noise Filter" \
    "${TLU_COL_SRC:?}" "${TLU_COL_TGT:?}" \
    "src.filters._005_2_1_filter_fractal_noise" "result.005_2_1_filter_fractal_noise.analysis.csv"

run_tlu_visualization "Fractal Noise Spectrum" \
    "_005_2_1_visualize_fractal_noise" \
    "005_2_1_fractal_noise_spectrum.png" \
    "result.005_2_1_filter_fractal_noise.analysis.csv"
