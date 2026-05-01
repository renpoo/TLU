#!/usr/bin/env python3
# _01_projector_to_coo.py
import sys
from src.filters.cli_parser import parse_projector_args
from src.filters.stream_processor import IndexRegistry, process_csv_stream, export_registry

def main():
    import os
    env_dir = os.environ.get("TARGET_ENV", "workspace")
    path = f"{env_dir}/ephemeral/"

    # 1. Parse CLI arguments (pass arguments after script name using sys.argv[1:])
    mapping_config = parse_projector_args(sys.argv[1:])

    # 2. Initialize dictionary (registry) (disposable each time: compliant with SDL_05)
    node_registry = IndexRegistry()
    time_registry = IndexRegistry()

    # 3. Main stream processing (Standard Input -> Standard Output)
    process_csv_stream(sys.stdin, sys.stdout, mapping_config, node_registry, time_registry)

    # 4. Physical file output of the audit trail dictionary (compliant with SDL_05)
    # Generated from scratch and overwritten on each execution
    with open(path + "_node_map.csv", "w", encoding="utf-8") as f_node:
        export_registry(node_registry, f_node, "node_idx", "node_label")
        
    with open(path + "_time_map.csv", "w", encoding="utf-8") as f_time:
        export_registry(time_registry, f_time, "t_idx", "time_label")

    # 5. Process Initial State (Day 0) if provided
    in_initial = mapping_config.get("in_initial_state")
    out_initial = mapping_config.get("out_initial_state")
    if in_initial and out_initial and os.path.exists(in_initial):
        import csv
        with open(in_initial, "r", encoding="utf-8") as f_in, open(out_initial, "w", encoding="utf-8") as f_out:
            reader = csv.DictReader(f_in)
            writer = csv.writer(f_out, lineterminator='\n')
            writer.writerow(["node_idx", "initial_X"])
            for row in reader:
                # Force assigning ID in case it never appeared in stream
                idx = node_registry.assign_new_id(row["node_label"])
                writer.writerow([idx, row["initial_X"]])
        
        # We need to rewrite the node_map since new nodes might have been added
        with open(path + "_node_map.csv", "w", encoding="utf-8") as f_node:
            export_registry(node_registry, f_node, "node_idx", "node_label")

if __name__ == "__main__":
    main()
