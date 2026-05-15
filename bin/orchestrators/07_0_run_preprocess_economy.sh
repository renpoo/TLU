#!/bin/bash
# ==========================================
# 07_0_run_preprocess_economy.sh
# TLU/WMU System: Orchestrator for Economic Data Harvester (Local CSV)
# ==========================================
set -euo pipefail

# Ensure we run from project root
cd "$(dirname "$0")/../.."
source "bin/orchestrators/_tlu_env.sh"

INTERVAL=${1:-month}
INPUT_CSV=${2:-"scratch/global_economics_data_2000_2024.csv"}
COLUMNS=${3:-"US10Y,SP500,US_Unemployment,US_Inflation,US_Production,Copper,Oil"}
DUMMY_SRC=${4:-"US_Economy"}
FLOW_DIRECTION=${5:-"dummy_to_col"} # Default: US_Economy -> US10Y

OUTPUT_FILE="${TARGET_ENV:-workspace}/input_stream/Aggregated_Economy_Stream.csv"
mkdir -p "$(dirname "${OUTPUT_FILE}")"

echo "=================================================="
echo "WMU Phase 07: Preprocessing Economic Data"
echo "=================================================="
echo "Input CSV: ${INPUT_CSV}"
echo "Columns: ${COLUMNS}"
echo "Dummy Source: ${DUMMY_SRC}"
echo "Flow: ${FLOW_DIRECTION}"
echo "Output: ${OUTPUT_FILE}"
echo "Interval: ${INTERVAL}"
echo "Running thin adapter pipeline..."

# 1. We need a small python script to read the CSV, filter the columns, and calculate the diff
# Since we don't have a modular script for reading and diffing a local CSV yet, we can do it inline
# or write a generic `07_1_parse_local_csv.py`
$TLU_PY src/fetchers/07_1_parse_local_csv.py --input_csv "${INPUT_CSV}" --columns "${COLUMNS}" \
  | $TLU_PY src/filters/06_2_timeseries_to_coo.py --dummy_src "${DUMMY_SRC}" --flow_direction "${FLOW_DIRECTION}" \
  | $TLU_PY src/filters/06_3_aggregate_market.py --interval "${INTERVAL}" \
  > "${OUTPUT_FILE}"

echo "Done."
