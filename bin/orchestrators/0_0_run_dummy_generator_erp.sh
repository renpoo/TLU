#!/bin/bash
# ==========================================
# 0_0_run_dummy_generator_erp.sh
# TLU Orchestrator: ERP Dummy Journal Generator (Traditional, ABC, T-ABC)
# ==========================================
set -euo pipefail

source "$(dirname "$0")/_tlu_env.sh"

ALLOCATION_MODE="${1:-tabc}"
MONTHS="${2:-12}"

echo "Running ERP Dummy Journal Generator (Mode: ${ALLOCATION_MODE}, Months: ${MONTHS})..."

mkdir -p "${TLU_INPUT_DIR}" "${TLU_EPHEMERAL_DIR}"

${TLU_PY} src/filters/_0_0_generate_dummy_journal_erp.py \
    --months "${MONTHS}" \
    --allocation-mode "${ALLOCATION_MODE}" \
    --seed 42 \
    --out-initial-state "${TLU_EPHEMERAL_DIR}/_initial_state_labels.csv" \
    > "${TLU_INPUT_DIR}/Dummy_Journal_Stream.csv"

cp "${TLU_INPUT_DIR}/Dummy_Journal_Stream.csv" "${TLU_INPUT_DIR}/stream_journal.csv"

echo "ERP Dummy Journal Generator completed. Stream saved to ${TLU_INPUT_DIR}/stream_journal.csv."
