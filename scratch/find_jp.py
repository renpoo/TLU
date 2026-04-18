import os
import re

dir_path = "bin/visualizers"
files = [os.path.join(dir_path, f) for f in os.listdir(dir_path) if f.endswith(".sh")]

# Unicode regex for Hiragana, Katakana, and Kanji
pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]')

for file in files:
    with open(file, "r") as f:
        content = f.read()
    if pattern.search(content):
        print(f"--- {file} ---")
        for i, line in enumerate(content.splitlines()):
            if pattern.search(line):
                print(f"{i+1}: {line.strip()}")
