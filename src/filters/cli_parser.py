#!/usr/bin/env python3
# src/filters/cli_parser.py
import argparse
import csv
import sys
from typing import Dict

def load_sys_params(filepath: str) -> Dict[str, float]:
    """_sys_params.csv を読み込み、辞書として返す。"""
    params = {}
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            first_row = next(reader, None)
            if first_row and not first_row[1].replace('.','',1).isdigit():
                pass
            elif first_row:
                params[first_row[0].strip()] = float(first_row[1].strip())
            
            for row in reader:
                if len(row) >= 2:
                    params[row[0].strip()] = float(row[1].strip())
    except FileNotFoundError:
        print(f"[WARN] {filepath} not found. Using defaults.", file=sys.stderr)
    return params

def get_base_parser(description: str) -> argparse.ArgumentParser:
    """すべてのフィルターで共通して使用する基底パーサーを生成する。"""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--time_map", type=str, default="workspace/ephemeral/_time_map.csv")
    parser.add_argument("--node_map", type=str, default="workspace/ephemeral/_node_map.csv")
    parser.add_argument("--sys_params", type=str, default="workspace/config/_sys_params.csv")
    parser.add_argument("--domain_tags", type=str, default="workspace/config/_domain_tags.csv")
    return parser

def parse_projector_args(args_list: list[str]) -> dict:
    """[Phase 1 専用] Projector用のCLI引数をパースし、辞書として返す"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--col_time", type=str, default="")
    parser.add_argument("--col_src", type=str, default="")
    parser.add_argument("--col_tgt", type=str, default="")
    parser.add_argument("--col_val", type=str, default="")
    parser.add_argument("--time_format", type=str, default="%Y/%m/%d")

    parsed, _ = parser.parse_known_args(args_list)
    result = vars(parsed)
    
    for col in ["col_time", "col_src", "col_tgt", "col_val"]:
        val = result.get(col, "")
        if isinstance(val, str) and val.isdigit():
            result[col] = int(val)
            
    return result
