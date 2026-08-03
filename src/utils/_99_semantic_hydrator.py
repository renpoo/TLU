#!/usr/bin/env python3
# ==========================================
# _99_semantic_hydrator.py
# TLU System: Semantic Hydration Layer
# Version: 6.0.0 (Refactored with AccountTaxonomy Integration)
# ==========================================
"""!
@file _99_semantic_hydrator.py
@brief Injects semantic labels and AccountTaxonomy categories into mathematical analysis CSV streams.
"""

import sys
import os
import pandas as pd
import argparse
from typing import Dict, Any

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.core.core_accounting_taxonomy import AccountTaxonomy, AccountCategory

def load_map(filepath: str, key_col: str, val_col: str) -> Dict[Any, Any]:
    """Loads a mapping CSV and returns a dictionary. Returns empty dict on failure."""
    if not filepath or not os.path.exists(filepath):
        return {}
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
    parser.add_argument('--account_mapping', default="", help="Optional path to _account_mapping.csv")
    args = parser.parse_args()

    time_map = load_map(args.time_map, 't_idx', 'time_label')
    
    custom_map = {}
    if args.account_mapping and os.path.exists(args.account_mapping):
        try:
            df_acc = pd.read_csv(args.account_mapping)
            custom_map = dict(zip(df_acc['Account_Name'], df_acc['Category']))
        except Exception as e:
            print(f"[WARN] Failed to load account mapping {args.account_mapping}: {e}", file=sys.stderr)

    taxonomy = AccountTaxonomy(custom_map)

    raw_node_map = {}
    try:
        df_nodes = pd.read_csv(args.node_map)
        raw_node_map = dict(zip(df_nodes['node_idx'].astype(int), df_nodes['node_label']))
        formatted_node_map = {int(row['node_idx']): f"{int(row['node_idx']):02d}_{row['node_label']}" for _, row in df_nodes.iterrows()}
    except Exception as e:
        print(f"[WARN] Hydrator failed to load node map {args.node_map}: {e}", file=sys.stderr)
        formatted_node_map = {}

    try:
        df = pd.read_csv(sys.stdin)
    except Exception as e:
        print(f"[ERROR] Hydrator failed to read stdin: {e}", file=sys.stderr)
        sys.exit(1)

    if df.empty:
        df.to_csv(sys.stdout, index=False)
        sys.exit(0)

    if 't_idx' in df.columns:
        idx_pos = df.columns.get_loc('t_idx')
        df.insert(idx_pos + 1, 'time_label', df['t_idx'].map(time_map))

    if 'node_idx' in df.columns:
        idx_pos = df.columns.get_loc('node_idx')
        df.insert(idx_pos + 1, 'node_label', df['node_idx'].map(formatted_node_map))
        
        # Inject account_category
        categories = df['node_idx'].map(lambda idx: taxonomy.classify_account(raw_node_map.get(idx, "")).value)
        df.insert(idx_pos + 2, 'account_category', categories)

    if 'src_idx' in df.columns:
        idx_pos = df.columns.get_loc('src_idx')
        df.insert(idx_pos + 1, 'src_label', df['src_idx'].map(formatted_node_map))

    if 'tgt_idx' in df.columns:
        idx_pos = df.columns.get_loc('tgt_idx')
        df.insert(idx_pos + 1, 'tgt_label', df['tgt_idx'].map(formatted_node_map))

    df.to_csv(sys.stdout, index=False)

if __name__ == "__main__":
    main()
