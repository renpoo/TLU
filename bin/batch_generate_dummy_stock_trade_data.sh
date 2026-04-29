#!/bin/bash
# ==========================================
# batch_generate_dummy_stock_trade_data.sh
# TLU System: Dummy Market/Stock Trade Data Generation Pipeline
# ==========================================

# 1. Load environment variables
source "$(dirname "$0")/orchestrators/_tlu_env.sh"
ENV_DIR="${TARGET_ENV:-workspace}"

# 2. Run the master transaction log generator
bash bin/orchestrators/0_0_run_market_generator.sh

# 3. Pre-aggregate (Project) to Weekly User Network
# We specify col_multiplier="Price" so that Value = Volume * Price (Transaction Amount)
echo "Aggregating master stream into Weekly User Network..."
${TLU_PY} -m src.filters._0_1_aggregate_stream \
    --col_time "Timestamp" \
    --col_src "Seller_ID" \
    --col_tgt "Buyer_ID" \
    --col_val "Volume" \
    --col_multiplier "Price" \
    --interval "week" \
    < "${ENV_DIR}/input_stream/Dummy_Market_Stream.csv" \
    > "${ENV_DIR}/input_stream/Dummy_Market_Weekly_User_Graph.csv"

echo "Weekly User Network generated at ${ENV_DIR}/input_stream/Dummy_Market_Weekly_User_Graph.csv"

# 4. Generate Weekly Bipartite Graph (User-to-Stock)
echo "Aggregating master stream into Weekly Bipartite Graph..."
cat "${ENV_DIR}/input_stream/Dummy_Market_Stream.csv" \
    | ${TLU_PY} -m src.filters._0_0_split_bipartite \
    | ${TLU_PY} -m src.filters._0_1_aggregate_stream \
        --col_time "Timestamp" \
        --col_src "Src" \
        --col_tgt "Tgt" \
        --col_val "Volume" \
        --col_multiplier "Price" \
        --interval "week" \
    > "${ENV_DIR}/input_stream/Dummy_Market_Weekly_Bipartite_Graph.csv"

echo "Weekly Bipartite Graph generated at ${ENV_DIR}/input_stream/Dummy_Market_Weekly_Bipartite_Graph.csv"
