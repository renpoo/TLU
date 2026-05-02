#!/usr/bin/env python3
# ==========================================
# _99_semantic_hydrator.py
# TLU System: Semantic Hydration Layer
# ==========================================
import sys
import pandas as pd
import argparse

def load_map(filepath, key_col, val_col):
    """Loads a mapping CSV and returns a dictionary. Returns empty dict on failure."""
    try:
        df = pd.read_csv(filepath)
        return dict(zip(df[key_col], df[val_col]))
    except Exception as e:
        print(f"[WARN] Hydrator failed to load map {filepath}: {e}", file=sys.stderr)
        return {}

def main():
    parser = argparse.ArgumentParser(description="Injects semantic labels into mathematical analysis CSVs.")
    parser.add_argument('--node_map', required=True, help="Path to _node_map.csv")
    parser.add_argument('--time_map', required=True, help="Path to _time_map.csv")
    args = parser.parse_args()

    # Load dictionaries
    time_map = load_map(args.time_map, 't_idx', 'time_label')
    node_map = load_map(args.node_map, 'node_idx', 'node_label')

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"[ERROR] Hydrator failed to read stdin: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        df.to_csv(sys.stdout, index=False)
        sys.exit(0)

    # Inject 'time_label' right after 't_idx'
    if 't_idx' in df.columns:
        idx_pos = df.columns.get_loc('t_idx')
        df.insert(idx_pos + 1, 'time_label', df['t_idx'].map(time_map))

    # Inject 'node_label' right after 'node_idx'
    if 'node_idx' in df.columns:
        idx_pos = df.columns.get_loc('node_idx')
        df.insert(idx_pos + 1, 'node_label', df['node_idx'].map(node_map))

    # Inject 'src_label' right after 'src_idx' (Matrix format)
    if 'src_idx' in df.columns:
        idx_pos = df.columns.get_loc('src_idx')
        df.insert(idx_pos + 1, 'src_label', df['src_idx'].map(node_map))

    # Inject 'tgt_label' right after 'tgt_idx' (Matrix format)
    if 'tgt_idx' in df.columns:
        idx_pos = df.columns.get_loc('tgt_idx')
        df.insert(idx_pos + 1, 'tgt_label', df['tgt_idx'].map(node_map))

    # Output hydrated CSV to stdout
    df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
