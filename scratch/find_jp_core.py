import os
import re

dir_paths = ["src/core", "src/filters", "src/visualizations", "tests/unit", "tests/integration"]
files = []
for dir_path in dir_paths:
    if os.path.exists(dir_path):
        for f in os.listdir(dir_path):
            if f.endswith(".py"):
                files.append(os.path.join(dir_path, f))

pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]')

for file in files:
    with open(file, "r") as f:
        content = f.read()
    if pattern.search(content):
        print(f"--- {file} ---")
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if pattern.search(line):
                print(f"{i+1}: {line.strip()}")
