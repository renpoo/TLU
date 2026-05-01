import os
import shutil

REPO_ROOT = "/Users/renpoo/Documents/GitHub/TLU"
DOCS_PLOTS_DIR = os.path.join(REPO_ROOT, "docs/readme_plots")
SAMPLES_DIR = os.path.join(REPO_ROOT, "samples")

for sample_name in ["Sample_8_fMRI_Stroke", "Sample_9_fMRI_Seizure"]:
    src_plots = os.path.join(SAMPLES_DIR, sample_name, "plots")
    dest_plots = os.path.join(DOCS_PLOTS_DIR, sample_name)
    if os.path.isdir(src_plots):
        if not os.path.exists(dest_plots):
            print(f"Copying {src_plots} to {dest_plots}")
            shutil.copytree(src_plots, dest_plots, dirs_exist_ok=True)
        else:
            print(f"Updating {dest_plots}")
            shutil.copytree(src_plots, dest_plots, dirs_exist_ok=True)

