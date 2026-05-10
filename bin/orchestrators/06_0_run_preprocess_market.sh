#!/bin/bash
# ==========================================
# 06_0_run_preprocess_market.sh
# TLU System: Orchestrator for Market Data Harvester
# ==========================================
set -euo pipefail

# Ensure we run from project root
cd "$(dirname "$0")/../.."
source "bin/orchestrators/_tlu_env.sh"

INTERVAL=${1:-week}
TICKERS=${2:-"^GSPC,^VIX"}
START_DATE=${3:-"2020-01-01"}
END_DATE=${4:-"2025-01-01"}
DUMMY_SRC=${5:-"Market_Offset"}

OUTPUT_FILE="${TARGET_ENV:-workspace}/input_stream/Aggregated_Market_Stream.csv"
mkdir -p "$(dirname "${OUTPUT_FILE}")"

echo "=================================================="
echo "TLU Phase 06: Preprocessing Market Data (A1 | A2)"
echo "=================================================="
echo "Tickers: ${TICKERS}"
echo "Dummy Source: ${DUMMY_SRC}"
echo "Output: ${OUTPUT_FILE}"
echo "Interval: ${INTERVAL}"
echo "Running thin adapter pipeline..."

$TLU_PY src/fetchers/06_1_a_fetch_market.py --tickers "${TICKERS}" --start "${START_DATE}" --end "${END_DATE}" --only_close \
  | $TLU_PY src/filters/06_2_timeseries_to_coo.py --dummy_src "${DUMMY_SRC}" \
  | $TLU_PY src/filters/06_3_aggregate_market.py --interval "${INTERVAL}" \
  > "${OUTPUT_FILE}"

echo "Done."
