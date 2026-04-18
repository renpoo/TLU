#!/usr/bin/env python3
# src/filters/cli_parser.py
import argparse
import csv
import sys
from typing import Dict

def load_sys_params(filepath: str) -> Dict[str, float]:
    """!
    @brief Load system context parameters into a mapped dictionary.
    @details Recursively aggregates configuration baseline bounds eliminating missing variable bugs.

    @param filepath Absolute or relative configurations structure path.

    @return Extracted parameter dictionary instance.

    @pre
        - Struct is generally expected to exist (although logic allows default fallbacks).
    @post
        - Bypasses header rows safely while coercing implicit type definitions to float bounds.
    @invariant
        - Degrades gracefully emitting explicit [WARN] traces returning cleanly initialized dictionaries natively.
    """
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
    """!
    @brief Generate a base parser commonly configured across all sequential filters.
    @details Asserts expected boundaries preventing missing explicit arguments structurally.

    @param description Meta string characterizing the execution target domain.

    @return Core ArgumentParser populated identically with namespace foundations.

    @pre
        - Standard execution depends implicitly on `--time_map` and `--node_map`.
    @post
        - Defines configuration variables targeting standard workspace ephemeral data outputs.
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("--time_map", type=str, default="workspace/ephemeral/_time_map.csv")
    parser.add_argument("--node_map", type=str, default="workspace/ephemeral/_node_map.csv")
    parser.add_argument("--sys_params", type=str, default="workspace/config/_sys_params.csv")
    parser.add_argument("--domain_tags", type=str, default="workspace/config/_domain_tags.csv")
    return parser

def parse_projector_args(args_list: list[str]) -> dict:
    """!
    @brief Parse CLI arguments explicitly overriding extraction projection limits.
    @details Generates mapped representations natively executing early stream phase parameters.

    @param args_list The system argv parameter list mapping source targets.

    @return Parsed parameter mapping configurations targeting dynamic variables.

    @pre
        - Target list dynamically configured.
    @post
        - Implicitly coerces strictly integer representations scaling strings naturally.
    """
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
