#!/usr/bin/env python3
# _01_projector_to_coo.py
import sys
from src.filters.cli_parser import parse_projector_args
from src.filters.stream_processor import IndexRegistry, process_csv_stream, export_registry

def main():

    path = "workspace/ephemeral/"

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

if __name__ == "__main__":
    main()
