import os
import shutil
import re
import glob

REPO_ROOT = "/Users/renpoo/Documents/GitHub/TLU"
DOCS_PLOTS_DIR = os.path.join(REPO_ROOT, "docs/readme_plots")
SAMPLES_DIR = os.path.join(REPO_ROOT, "samples")
JA_SAMPLES_DIR = os.path.join(REPO_ROOT, "docs/ja/samples")

# 1. Copy images
for sample_name in os.listdir(SAMPLES_DIR):
    if not sample_name.startswith("Sample_"):
        continue
        
    src_plots = os.path.join(SAMPLES_DIR, sample_name, "readme_plots")
    if os.path.isdir(src_plots):
        dest_plots = os.path.join(DOCS_PLOTS_DIR, sample_name)
        
        # In Sample 0, images are directly in docs/readme_plots, but we will also copy to Sample_0_Healthy for safety/cleanliness, 
        # but the markdown for Sample 0 currently points to the root of docs/readme_plots.
        # Actually, let's just create the folders for all samples to keep it uniform.
        if not os.path.exists(dest_plots):
            print(f"Copying {src_plots} to {dest_plots}")
            shutil.copytree(src_plots, dest_plots, dirs_exist_ok=True)
        else:
            print(f"Updating {dest_plots}")
            shutil.copytree(src_plots, dest_plots, dirs_exist_ok=True)

# 2. Update markdown files in docs/ja/samples/
ja_sample_mds = glob.glob(os.path.join(JA_SAMPLES_DIR, "**", "*.md"), recursive=True)
for md_file in ja_sample_mds:
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace Sample_0_Healthy to point to the root of docs/readme_plots
    content = content.replace("../../../../samples/Sample_0_Healthy/readme_plots/", "../../../readme_plots/")
    
    # Replace Sample_X to point to docs/readme_plots/Sample_X/
    # Pattern: ../../../../samples/Sample_X/readme_plots/ or ../../../../samples/Sample_X/plots/
    # Sometimes it's readme_plots, sometimes plots (like Sample_8/plots/)
    content = re.sub(r"\.\./\.\./\.\./\.\./samples/(Sample_[^/]+)/(?:readme_plots|plots)/", r"../../../readme_plots/\1/", content)
    
    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Updated {md_file}")

# 3. Update docs/ja/README.md
ja_readme = os.path.join(REPO_ROOT, "docs/ja/README.md")
if os.path.exists(ja_readme):
    with open(ja_readme, "r", encoding="utf-8") as f:
        content = f.read()
    content = content.replace("docs/readme_plots/", "../readme_plots/")
    with open(ja_readme, "w", encoding="utf-8") as f:
        f.write(content)
        print(f"Updated {ja_readme}")

print("Done!")
