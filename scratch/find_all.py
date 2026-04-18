import os, re
pattern = re.compile(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]')
def scan(d):
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith(".py"):
                path = os.path.join(root, f)
                with open(path) as file:
                    cnt = file.read()
                if pattern.search(cnt):
                    print(f"--- {path} ---")
                    for i, line in enumerate(cnt.splitlines()):
                        if pattern.search(line):
                            print(f"{i+1}: {line.strip()}")
scan("src")
