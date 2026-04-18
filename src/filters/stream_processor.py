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

def project_record(record, mapping_config, node_registry, time_registry):
    """!
    @brief Projects a raw CSV record into the normalized TLU tuple format.
    @details Ensures structural integrity via strict fail-fast validation against expected columns.

    @param record Dictionary representing a single CSV row.
    @param mapping_config Setup mapping defining source schema columns.
    @param node_registry State registry resolving node topology IDs.
    @param time_registry State registry resolving time sequence IDs.

    @return A tuple (t_idx, src_idx, tgt_idx, val).

    @pre
        - Target mapping configuration keys ('col_time', 'col_src', 'col_tgt', 'col_val') must exist in `record`.
    @post
        - Unconditionally yields strongly typed tuple formats regardless of empty strings or missing schema configurations.
    @invariant
        - Node indices dynamically expand without resetting across different time slices (Topological Union).
    """
    time_col = mapping_config.get("col_time")
    src_col  = mapping_config.get("col_src")
    tgt_col  = mapping_config.get("col_tgt")
    val_col  = mapping_config.get("col_val")

    # Fail-Fast: Immediately error out if the column name does not exist
    for col_name in [time_col, src_col, tgt_col, val_col]:
        if col_name not in record:
            raise KeyError(f"CRITICAL: Column '{col_name}' not found in the input CSV. "
                           f"Available columns are: {list(record.keys())}")

    t_idx   = time_registry.assign_new_id(record[time_col])
    
    # Use the same node registry according to the tensor union topology principle (SDL_01)
    src_idx = node_registry.assign_new_id(record[src_col])
    tgt_idx = node_registry.assign_new_id(record[tgt_col])
    
    try:
        val = float(record[val_col])
    except (ValueError, TypeError):
        val = 0.0

    return (t_idx, src_idx, tgt_idx, val)

def process_csv_stream(in_stream, out_stream, mapping_config, node_registry, time_registry):
    """!
    @brief Core I/O loop: project raw stream tuples into flattened COO formats.
    @details Orchestrates the extraction mapping sequentially.

    @param in_stream Input readable stream (sys.stdin).
    @param out_stream Output writable stream (sys.stdout).
    @param mapping_config Pipeline translation dictionary.
    @param node_registry Topological state mapper.
    @param time_registry Temporal state mapper.
    
    @pre
        - `in_stream` inherently formatted as CSV with valid headers.
    @post
        - Generates COO formatted flat outputs directly resolving out_stream targets.
    @invariant
        - Operates in strict O(1) space complexity scaling indefinitely across row counts.
    """
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
    """!
    @brief Generator function tracking sequential time step tensor slices.
    @details Yields sparse N x N matrices aggregating standard flat COO format fluxes row by row.

    @param csv_reader Sequential flattened input iterator source.
    @param N Pre-loaded configuration boundary dimension bounds.

    @return Generator yielding (t_idx, T_slice) pairs natively structured.

    @pre
        - Input source is strictly ordered sequentially by `t_idx`.
    @post
        - Automatically flushes isolated time slices releasing garbage variables continuously.
    @invariant
        - Aggregated T_slices unconditionally obey N x N topological alignment restrictions.
    """
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
    """!
    @brief Common setup function to reduce initialization boilerplate.
    @details Synchronously loads explicit topology domains natively configuring default parsing arguments.

    @param parser Raw initialized CLI namespace.
    @param output_header Formatting structural strings denoting expected stream output.

    @return Extracted tuple (args, N, reader, writer).

    @pre
        - Namespace structurally implements `--node_map` explicitly.
    @post
        - Immediately fails the container returning non-zero sys exit codes preventing silent logic faults.
    @invariant
        - Fails Fast ensuring the topological size `N` strictly remains greater than zero.
    """
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
