#!/bin/bash
# ==========================================
# 00_0_run_preprocess_journal_dept.sh
# TLU Orchestrator: ERP Department-Coupled Journal Preprocessing
# ==========================================
set -euo pipefail

source "$(dirname "$0")/_tlu_env.sh"

INTERVAL="${1:-month}"

echo "Running ERP Department-Coupled Preprocessor (Interval: ${INTERVAL})..."

${TLU_PY} src/filters/00_1_parse_journal_dept.py --interval "${INTERVAL}" < "${TLU_INPUT_DIR}/Dummy_Journal_Stream.csv" \
    > "${TLU_INPUT_DIR}/Aggregated_Journal_Stream.csv"

echo "ERP Department-Coupled Preprocessor completed. Aggregated stream saved to ${TLU_INPUT_DIR}/Aggregated_Journal_Stream.csv."
