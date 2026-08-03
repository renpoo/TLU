#!/usr/bin/env python3
# ==========================================
# tests/unit/test_base_visualizer.py
# Unit tests for BaseVisualizer framework
# ==========================================
import unittest
import pandas as pd
import matplotlib.pyplot as plt
import argparse

from src.visualizations.base_visualizer import BaseVisualizer

class DummyVisualizer(BaseVisualizer):
    cli_description = "Dummy Test Visualizer"
    default_filename = "dummy_test.png"

    def render_plot(self, df: pd.DataFrame, theme_cfg: dict, args: argparse.Namespace) -> plt.Figure:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(df['x'], df['y'])
        return fig

class TestBaseVisualizer(unittest.TestCase):
    def test_dummy_visualizer_render(self):
        vis = DummyVisualizer()
        df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]})
        theme_cfg = {
            'mode': 'dark',
            'ui_canvas': {
                'text_primary': '#FFFFFF',
                'legend_bg': '#000000',
                'legend_edge': '#333333'
            },
            'forensics': {'colors': {'z_score_shock': '#FF0000', 'anomaly_outlier': '#FF4444'}}
        }
        args = argparse.Namespace(
            theme="dark",
            out_dir="/tmp",
            filename="dummy_test.png"
        )
        
        fig = vis.render_plot(df, theme_cfg, args)
        self.assertIsNotNone(fig)
        plt.close(fig)

if __name__ == '__main__':
    unittest.main()
