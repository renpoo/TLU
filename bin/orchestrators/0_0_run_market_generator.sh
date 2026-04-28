#!/bin/bash
# ==========================================
# 0_0_run_market_generator.sh
# TLU System: Dummy Market Generator Launcher
# ==========================================

# 1. Load environment variables (_tlu_env.sh)
source "$(dirname "$0")/_tlu_env.sh"

# 2. Define output destination
ENV_DIR="${TARGET_ENV:-workspace}"
# Create directory if it doesn't exist
mkdir -p "${TLU_PROJECT_ROOT}/${ENV_DIR}/input_stream"

OUTPUT_FILE="${TLU_PROJECT_ROOT}/${ENV_DIR}/input_stream/Dummy_Market_Stream.csv"

echo "=================================================="
echo "TLU Phase 0: Dummy Market Generator"
echo "=================================================="
echo "Mode: Continuous Market Simulation (N Users x M Stocks)"
echo "Anomalies: Enabled (Wash Trades, Pump & Dump)"
echo "Output: ${OUTPUT_FILE}"
echo "Running..."

# 3. Parameter retrieval
MONTHS="${DUMMY_DURATION_MONTHS:-12}"
SEED="${DUMMY_RANDOM_SEED:-42}"
NUM_USERS="${DUMMY_NUM_USERS:-10}"
NUM_STOCKS="${DUMMY_NUM_STOCKS:-5}"

# 4. Execute generator script
${TLU_PY} -m src.filters._0_0_generate_dummy_market \
    --months "${MONTHS}" \
    --seed "${SEED}" \
    --num-users "${NUM_USERS}" \
    --num-stocks "${NUM_STOCKS}" \
    --wash-trade-prob "${DUMMY_WASH_TRADE_PROB:-0.05}" \
    --pump-dump-prob "${DUMMY_PUMP_DUMP_PROB:-0.02}" \
    > "${OUTPUT_FILE}"

echo "Completed. Dummy market stream has been successfully generated."
echo "=================================================="
