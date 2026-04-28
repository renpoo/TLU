#!/bin/bash
# ==========================================
# batch_generate_dummy_fmri_stroke.sh
# ==========================================

export TARGET_ENV="samples/Sample_8_fMRI_Stroke/workspace"
mkdir -p "$TARGET_ENV/input_stream"

python3 src/filters/_0_0_generate_dummy_fmri.py --pathology stroke > "$TARGET_ENV/input_stream/Dummy_fMRI_Blood_Flow.csv"

echo "Generated fMRI Stroke data into $TARGET_ENV/input_stream/Dummy_fMRI_Blood_Flow.csv"
