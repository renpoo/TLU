#!/bin/bash
# ==========================================
# vis_003_1_3_visualize_jacobian_trajectory.sh
# ==========================================
source "$(dirname "$0")/../orchestrators/_tlu_env.sh"

echo "=== Visualizing Phase 4.3: Jacobian Trajectories ==="

run_tlu_visualization "Jacobian 1st Heatmap" "_003_1_4_visualize_jacobian_heatmap.py" "jacobian_order_1st.png" "result.003_1_3_jacobian_1st.analysis.csv" --order 1
run_tlu_visualization "Jacobian 2nd Heatmap" "_003_1_4_visualize_jacobian_heatmap.py" "jacobian_order_2nd.png" "result.003_1_3_jacobian_2nd.analysis.csv" --order 2
run_tlu_visualization "Jacobian 3rd Heatmap" "_003_1_4_visualize_jacobian_heatmap.py" "jacobian_order_3rd.png" "result.003_1_3_jacobian_3rd.analysis.csv" --order 3
