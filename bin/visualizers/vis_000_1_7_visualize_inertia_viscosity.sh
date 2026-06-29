#!/bin/bash
# ==========================================
# vis_000_1_7_visualize_inertia_viscosity.sh
# TLU System: Dynamics Phase Space (Inertia vs Viscosity)
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 000_1_7: Inertia vs Viscosity ==="

run_tlu_visualization "Inertia vs Viscosity" "_000_1_7_visualize_inertia_viscosity.py" "000_1_7__inertia_viscosity_scatter.png" "result.000_1_1_filter_dynamics.analysis.csv"
