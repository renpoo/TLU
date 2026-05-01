#!/bin/bash
# ==========================================
# batch_generate_dummy_fmri_seizure.sh
# ==========================================

source "$(dirname "$0")/orchestrators/_tlu_env.sh"
export TARGET_ENV="samples/Sample_9_fMRI_Seizure"
mkdir -p "$TARGET_ENV/input_stream"
mkdir -p "$TARGET_ENV/ephemeral"

${TLU_PY} -m src.filters._0_0_generate_dummy_fmri --pathology seizure --out-initial-state "$TARGET_ENV/ephemeral/_initial_state_labels.csv" \
| ${TLU_PY} -m src.filters._0_1_aggregate_stream \
    --col_time "Trans_Date" --col_src "Src" --col_tgt "Tgt" --col_val "Amount" \
    --interval "10s" \
> "$TARGET_ENV/input_stream/Dummy_fMRI_Blood_Flow.csv"

echo "Generated fMRI Seizure data into $TARGET_ENV/input_stream/Dummy_fMRI_Blood_Flow.csv"
