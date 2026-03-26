#!/usr/bin/env python3
# src/filters/stream_processor.py
import sys
import csv
import argparse
import pandas as pd
import numpy as np

class IndexRegistry:
    def __init__(self):
        self.labels = dict()
        self.next_id = 0

    def assign_new_id(self, label):
        safe_label = str(label) if label is not None else "UNKNOWN"
        if safe_label not in self.labels:
            self.labels[safe_label] = self.next_id
            self.next_id += 1
        return self.labels[safe_label]

# 【重要修正】クラスの外（独立した関数）に出しました
def project_record(record, mapping_config, node_registry, time_registry):
    time_col = mapping_config.get("col_time")
    src_col  = mapping_config.get("col_src")
    tgt_col  = mapping_config.get("col_tgt")
    val_col  = mapping_config.get("col_val")

    t_idx   = time_registry.assign_new_id(record.get(time_col))
    src_idx = node_registry.assign_new_id(record.get(src_col))
    tgt_idx = node_registry.assign_new_id(record.get(tgt_col))
    
    try:
        val = float(record.get(val_col))
    except (ValueError, TypeError):
        val = 0.0

    return (t_idx, src_idx, tgt_idx, val)

def process_csv_stream(in_stream, out_stream, mapping_config, node_registry, time_registry):
    reader = csv.DictReader(in_stream)
    writer = csv.writer(out_stream, lineterminator='\n')
    writer.writerow(["t_idx", "src_idx", "tgt_idx", "value"])

    for record in reader:
        writer.writerow(project_record(record, mapping_config, node_registry, time_registry))
    out_stream.flush()

def export_registry(registry, out_stream, idx_col_name, label_col_name):
    writer = csv.writer(out_stream, lineterminator='\n')
    writer.writerow([idx_col_name, label_col_name])
    for label, idx in registry.labels.items():
        writer.writerow([idx, label])
    out_stream.flush()

def yield_time_slices(csv_reader, N: int):
    current_t_idx = None
    T_slice = np.zeros((N, N), dtype=float)

    for row in csv_reader:
        if not row or row[0].startswith('t_idx'):
            continue
            
        t_idx = int(float(row[0]))
        src_idx = int(float(row[1]))
        tgt_idx = int(float(row[2]))
        val = float(row[3])

        if current_t_idx is not None and t_idx != current_t_idx:
            yield current_t_idx, T_slice
            T_slice = np.zeros((N, N), dtype=float)

        current_t_idx = t_idx
        if src_idx < N and tgt_idx < N:
            T_slice[src_idx, tgt_idx] += val

    if current_t_idx is not None:
        yield current_t_idx, T_slice

def setup_pipeline(parser: argparse.ArgumentParser, output_header: list[str]):
    """ボイラープレートを削減するための共通セットアップ関数"""
    args = parser.parse_args()
    try:
        df_map = pd.read_csv(args.node_map)
        N = len(df_map)
        if N <= 0: raise ValueError("Node map is empty.")
    except Exception as e:
        print(f"Error loading node map: {e}", file=sys.stderr)
        sys.exit(1)

    writer = csv.writer(sys.stdout, lineterminator='\n')
    writer.writerow(output_header)
    reader = csv.reader(sys.stdin)
    return args, N, reader, writer
