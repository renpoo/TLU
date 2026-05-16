import os
import re

base_path = "/Users/renpoo/Documents/GitHub/TLU"

for i in range(12):
    sample_dirs = [d for d in os.listdir(f"{base_path}/samples") if d.startswith(f"Sample_{i}_") and "Raw" not in d]
    if not sample_dirs: continue
    sample_dir = sample_dirs[0]
    
    readme_path = f"{base_path}/docs/ja/samples/{sample_dir}/README.md"
    if not os.path.exists(readme_path): continue
    
    with open(readme_path, "r") as f:
        content = f.read()

    # Find any sequence of ../ and replace with exactly 4
    content = re.sub(r'(\.\./)+samples/', '../../../../samples/', content)

    with open(readme_path, "w") as f:
        f.write(content)
    print(f"Fixed paths in {readme_path}")
