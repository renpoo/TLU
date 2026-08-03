#!/usr/bin/env python3
# ==========================================
# src/visualizations/base_visualizer.py
# TLU Base Visualizer Framework
# ==========================================
"""!
@file base_visualizer.py
@brief Standard Base Framework for TLU Visualization & Plot rendering.
@details Unifies CLI parsing, theme color initialization, stdin streaming, plot rendering, and file saving.
"""

import sys
import os
import argparse
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, Any, Optional

from src.visualizations.visualizer_utils import (
    get_base_parser,
    apply_theme,
    save_plot,
    load_node_labels,
    load_time_labels
)

class BaseVisualizer:
    """!
    @brief Abstract Base Class for TLU Visualization Scripts.
    """
    cli_description: str = "TLU Visualization Render Engine"
    default_filename: str = "plot_output.png"

    def __init__(self):
        self.parser = get_base_parser(self.cli_description)
        self.parser.set_defaults(filename=self.default_filename)
        self.add_arguments(self.parser)

    def add_arguments(self, parser: argparse.ArgumentParser):
        """Override in subclass to add plot-specific CLI arguments."""
        pass

    def read_stream(self) -> Optional[pd.DataFrame]:
        try:
            df = pd.read_csv(sys.stdin)
            if df.empty:
                return None
            return df
        except Exception as e:
            sys.stderr.write(f"[ERROR] Failed to read stream for visualization: {e}\n")
            sys.exit(1)

    def render_plot(self, df: pd.DataFrame, theme_cfg: dict, args: argparse.Namespace) -> plt.Figure:
        """!
        @brief Render logic. Must be implemented by subclass and return matplotlib.figure.Figure.
        """
        raise NotImplementedError("Subclasses must implement render_plot()")

    def run(self):
        args = self.parser.parse_args()
        theme_cfg = apply_theme(args.theme)

        df = self.read_stream()
        if df is None or df.empty:
            sys.exit(0)

        fig = self.render_plot(df, theme_cfg, args)
        if fig is not None:
            save_plot(fig, args.out_dir, args.filename)
            plt.close(fig)
