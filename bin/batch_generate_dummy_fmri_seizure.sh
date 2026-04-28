#!/bin/bash
# ==========================================
# batch_generate_dummy_fmri_seizure.sh
# ==========================================

export TARGET_ENV="samples/Sample_9_fMRI_Seizure/workspace"
mkdir -p "$TARGET_ENV/input_stream"

python3 src/filters/_0_0_generate_dummy_fmri.py --pathology seizure > "$TARGET_ENV/input_stream/Dummy_fMRI_Blood_Flow.csv"

echo "Generated fMRI Seizure data into $TARGET_ENV/input_stream/Dummy_fMRI_Blood_Flow.csv"
