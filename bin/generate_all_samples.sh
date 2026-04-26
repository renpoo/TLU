#!/bin/bash
set -e

echo "Starting Sample Generation..."

# Common setup
cp workspace/config/_sys_params.csv samples/Sample_0_Healthy/config/
cp workspace/config/_sys_params.csv samples/Sample_1_Wash_Trade/config/
cp workspace/config/_sys_params.csv samples/Sample_2_Embezzlement_Leak/config/
cp workspace/config/_sys_params.csv samples/Sample_3_Unbalanced_Mistake/config/
cp workspace/config/_sys_params.csv samples/Sample_4_Composite_Chaos/config/
cp workspace/config/_sys_params.csv samples/Sample_5_Kyoto_Traffic/config/

# Fix Kyoto config to use traffic data
sed -i '' 's|input_csv,input_stream/Dummy_Journal_Stream_Amount.Aggregated.csv|input_csv,input_stream/Dummy_Kyoto_Traffic_Journal_Aggregated.csv|' samples/Sample_5_Kyoto_Traffic/config/_sys_params.csv
sed -i '' 's|thermo_work_labels,ACC_Sales_Revenue|thermo_work_labels,Higashiyama_Sanjo|' samples/Sample_5_Kyoto_Traffic/config/_sys_params.csv
sed -i '' 's|thermo_heat_labels,.*|thermo_heat_labels,Gion,Kiyomizu_dera|' samples/Sample_5_Kyoto_Traffic/config/_sys_params.csv
sed -i '' 's|lqr_controllable_labels,.*|lqr_controllable_labels,Kyoto_Station,Karasuma_Oike|' samples/Sample_5_Kyoto_Traffic/config/_sys_params.csv

# Generate samples
generate_sample() {
    local i=$1
    local leak_prob=$2
    local purchase_prob=$3
    local wash_prob=$4
    local unbal_prob=$5

    echo "==================================="
    echo "Generating Sample ${i}..."
    export TARGET_ENV="samples/Sample_${i}"
    export TLU_SALES_LEAK_PROB=$leak_prob
    export TLU_PURCHASE_LEAK_PROB=$purchase_prob
    export TLU_WASH_TRADE_PROB=$wash_prob
    export TLU_UNBALANCED_PROB=$unbal_prob

    bash bin/batch_generate_dummy_journal_data.sh
    bash bin/batch_processing.sh
    bash bin/batch_visualize_graphs.sh
}

# 0_Healthy
generate_sample 0_Healthy 0.0 0.0 0.0 0.0

# 1_Wash_Trade
generate_sample 1_Wash_Trade 0.0 0.0 0.01 0.0

# 2_Embezzlement_Leak
generate_sample 2_Embezzlement_Leak 0.01 0.01 0.0 0.0

# 3_Unbalanced_Mistake
generate_sample 3_Unbalanced_Mistake 0.0 0.0 0.0 0.01

# 4_Composite_Chaos
generate_sample 4_Composite_Chaos 0.005 0.01 0.005 0.005

# 5_Kyoto_Traffic
echo "==================================="
echo "Generating Sample 5_Kyoto_Traffic..."
export TARGET_ENV="samples/Sample_5_Kyoto_Traffic"
# We need to run batch_generate_dummy_traffic_data.sh but modify it first to support TARGET_ENV
bash bin/batch_generate_dummy_traffic_data.sh
bash bin/batch_processing.sh
bash bin/batch_visualize_graphs.sh

echo "All samples generated."
