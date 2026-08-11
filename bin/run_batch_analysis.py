#!/usr/bin/env python3
# ==========================================
# bin/run_batch_analysis.py
# Pure Python Orchestrator for Dynamic TLU Batch Analysis & Graph Rendering
# ==========================================

import os
import sys
import time
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

def find_target_samples():
    """!
    @brief Dynamically locate all sample directories under samples/ or scratch/samples/
    @return List of relative Path objects sorted by sample index
    """
    sample_dirs = []
    
    # 1. Official samples/ directory
    official_dir = PROJECT_ROOT / "samples"
    if official_dir.exists():
        for p in official_dir.glob("Sample_*"):
            if p.is_dir():
                sample_dirs.append(p.relative_to(PROJECT_ROOT))

    # 2. Fallback or legacy scratch/samples/ directory
    scratch_dir = PROJECT_ROOT / "scratch" / "samples"
    if scratch_dir.exists():
        for p in scratch_dir.glob("Sample_*"):
            if p.is_dir() and p.relative_to(PROJECT_ROOT) not in sample_dirs:
                sample_dirs.append(p.relative_to(PROJECT_ROOT))
                
    # Sort naturally
    sample_dirs.sort(key=lambda path: path.name)
    return sample_dirs

def get_git_info():
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=PROJECT_ROOT, text=True).strip()
    except Exception:
        branch = "unknown"
    try:
        commit = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=PROJECT_ROOT, text=True).strip()
    except Exception:
        commit = "unknown"
    return branch, commit

def record_to_journal(total: int, passed: int, failed: int, status: str):
    ledger_dir = PROJECT_ROOT / "tlu_dev_history"
    ledger_file = ledger_dir / "journal.jsonl"
    
    if not ledger_dir.exists():
        return

    branch, commit = get_git_info()
    record = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "record_type": "run_record",
        "tool": "run_batch_analysis",
        "branch": branch,
        "commit_hash": commit,
        "counts": {
            "total": total,
            "passed": passed,
            "failed": failed
        },
        "status": status
    }
    
    with open(ledger_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    print(f"📜 Recorded batch analysis run to {ledger_file}")

def main():
    os.chdir(PROJECT_ROOT)
    sample_dirs = find_target_samples()
    
    print("=" * 65)
    print(f"🔬 TLU Dynamic Orchestrator: Processing {len(sample_dirs)} Target Samples")
    print("=" * 65)
    
    total_start = time.time()
    passed_count = 0
    failed_count = 0
    failed_samples = []
    
    for idx, sample_rel in enumerate(sample_dirs, 1):
        sample_name = sample_rel.name
        print(f"\n▶️  [{idx}/{len(sample_dirs)}] Processing Target: {sample_name} ({sample_rel})")
        print("-" * 65)
        
        env = os.environ.copy()
        env["TARGET_ENV"] = str(sample_rel)
        env["PYTHONPATH"] = f"{PROJECT_ROOT}:{env.get('PYTHONPATH', '')}"
        
        # Step 1: Physics-Math Engine
        print("  [1/2] Running Physics-Math Engine...")
        t0 = time.time()
        cmd_proc = ["bash", "bin/batch_processing.sh", "--target_env", str(sample_rel)]
        res_proc = subprocess.run(cmd_proc, cwd=PROJECT_ROOT, env=env)
        t1 = time.time()
        
        if res_proc.returncode != 0:
            print(f"  ❌ Physics Engine failed for {sample_name} (exit code {res_proc.returncode})")
            failed_count += 1
            failed_samples.append(sample_name)
            continue
        print(f"  ✅ Physics Engine completed in {t1 - t0:.1f}s")
        
        # Step 2: Visualizer Pipeline (If script exists)
        viz_script = PROJECT_ROOT / "bin" / "batch_visualize_graphs.sh"
        if viz_script.exists():
            print("  [2/2] Rendering Diagnostic Graphs...")
            t2 = time.time()
            cmd_viz = ["bash", "bin/batch_visualize_graphs.sh", "--target_env", str(sample_rel)]
            res_viz = subprocess.run(cmd_viz, cwd=PROJECT_ROOT, env=env)
            t3 = time.time()
            
            if res_viz.returncode != 0:
                print(f"  ❌ Visualizer failed for {sample_name} (exit code {res_viz.returncode})")
                failed_count += 1
                failed_samples.append(sample_name)
                continue
            print(f"  ✅ Graphs rendered in {t3 - t2:.1f}s")
            
        passed_count += 1
        print(f"  🎉 Completed {sample_name} in {time.time() - t0:.1f}s")

    total_end = time.time()
    overall_status = "PASSED" if failed_count == 0 else "FAILED"
    
    record_to_journal(len(sample_dirs), passed_count, failed_count, overall_status)
    
    print("\n" + "=" * 65)
    print(f"Execution Summary: {passed_count}/{len(sample_dirs)} samples passed in {total_end - total_start:.1f}s")
    if failed_count > 0:
        print(f"❌ Failed samples: {', '.join(failed_samples)}")
        sys.exit(1)
    else:
        print("🎉 All target samples analyzed successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
