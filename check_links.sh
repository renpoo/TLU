#!/bin/bash
cd /Users/renpoo/Documents/GitHub/TLU
files=$(find docs/ja/samples -name "README.md")
for f in $files; do
  dir=$(dirname "$f")
  grep -o '\[.*\](.[^)]*)' "$f" | grep '\.png' | while read -r line; do
    path=$(echo "$line" | sed -n 's/.*(\(.*\)).*/\1/p')
    # Resolve relative path from the dir of README.md
    abs_path=$(cd "$dir" && echo $(python3 -c "import os, sys; print(os.path.normpath(os.path.join(sys.argv[1], sys.argv[2])))" "$PWD" "$path"))
    if [ ! -f "$abs_path" ]; then
      echo "DEAD LINK in $f: $path"
      echo "  -> Expected at: $abs_path"
    fi
  done
done
