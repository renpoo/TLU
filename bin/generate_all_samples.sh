generate_sample 4_Composite_Chaos 0.005 0.01 0.005 0.005

# 5_Kyoto_Traffic
echo "==================================="
echo "Generating Sample 5_Kyoto_Traffic..."
export TARGET_ENV="samples/Sample_5_Kyoto_Traffic"
# We need to run batch_generate_dummy_traffic_data.sh but modify it first to support TARGET_ENV
