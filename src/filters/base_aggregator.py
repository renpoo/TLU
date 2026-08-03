#!/usr/bin/env python3
# ==========================================
# src/filters/base_aggregator.py
# TLU Base Aggregator Framework
# ==========================================
"""!
@file base_aggregator.py
@brief Standard Base Framework for TLU Temporal & Spatial Stream Aggregators.
@details Unifies CLI parsing, temporal binning, spatial SUM aggregation, and CSV output stream handling.
"""

import sys
import argparse
import pandas as pd
from typing import Optional

from src.core.core_temporal_binning import apply_temporal_binning

class BaseAggregator:
    """!
    @brief Abstract Base Class for TLU COO Stream Aggregators.
    """
    cli_description: str = "TLU Temporal & Spatial Stream Aggregator"
    default_interval: str = "week"

    def __init__(self):
        self.parser = argparse.ArgumentParser(description=self.cli_description)
        self.add_common_arguments()
        self.add_arguments(self.parser)

    def add_common_arguments(self):
        self.parser.add_argument("--interval", default=self.default_interval, help="Aggregation interval (e.g. 'day', 'week', 'month', 'quarter', 'year', 'none')")
        self.parser.add_argument("--col_time", default="t_idx", help="Name of time column")
        self.parser.add_argument("--col_src", default="src_idx", help="Name of source node column")
        self.parser.add_argument("--col_tgt", default="tgt_idx", help="Name of target node column")
        self.parser.add_argument("--col_val", default="value", help="Name of value column")

    def add_arguments(self, parser: argparse.ArgumentParser):
        """Override in subclass if additional arguments are needed."""
        pass

    def read_stream(self) -> Optional[pd.DataFrame]:
        try:
            df = pd.read_csv(sys.stdin)
            if df.empty:
                return None
            return df
        except Exception as e:
            sys.stderr.write(f"[ERROR] Failed to read input stream: {e}\n")
            sys.exit(1)

    def process_aggregation(self, df: pd.DataFrame, args: argparse.Namespace) -> pd.DataFrame:
        src_cols = [c.strip() for c in args.col_src.split(',')]
        tgt_cols = [c.strip() for c in args.col_tgt.split(',')]
        
        # Contract validation
        for c in [args.col_time, args.col_val] + src_cols + tgt_cols:
            if c not in df.columns:
                sys.stderr.write(f"[ERROR] Missing required column: {c}\n")
                sys.exit(1)

        # Apply temporal binning
        df['_Agg_Time'] = apply_temporal_binning(df[args.col_time], args.interval)

        is_multi = len(src_cols) > 1 or len(tgt_cols) > 1
        if is_multi:
            expanded_dfs = []
            for s_col in src_cols:
                for t_col in tgt_cols:
                    sub_df = df[['_Agg_Time', s_col, t_col, args.col_val]].copy()
                    sub_df = sub_df.rename(columns={s_col: 'src_idx', t_col: 'tgt_idx'})
                    expanded_dfs.append(sub_df)
            expanded_df = pd.concat(expanded_dfs, ignore_index=True)
            summary = expanded_df.groupby(['_Agg_Time', 'src_idx', 'tgt_idx'], sort=False)[args.col_val].sum().reset_index()
            summary = summary.rename(columns={'_Agg_Time': 't_idx'})
        else:
            grouped = df.groupby(['_Agg_Time', args.col_src, args.col_tgt], sort=False)[args.col_val].sum().reset_index()
            summary = grouped.rename(columns={'_Agg_Time': args.col_time, args.col_src: 'src_idx', args.col_tgt: 'tgt_idx'})

        return summary

    def run(self):
        args = self.parser.parse_args()
        df = self.read_stream()
        if df is None or df.empty:
            sys.exit(0)

        summary_df = self.process_aggregation(df, args)
        summary_df.to_csv(sys.stdout, index=False)
