#!/bin/bash
# ==========================================
# batch_generate_dummy_erp_data.sh
# TLU Launcher: ERP Dummy Journal Generation & Preprocessing
# Usage: bash bin/batch_generate_dummy_erp_data.sh [allocation_mode: traditional|abc|tabc] [months]
# ==========================================
set -euo pipefail

ALLOCATION_MODE="${1:-tabc}"
MONTHS="${2:-12}"

bash bin/orchestrators/0_0_run_dummy_generator_erp.sh "${ALLOCATION_MODE}" "${MONTHS}"
bash bin/orchestrators/00_0_run_preprocess_journal_dept.sh "month"
