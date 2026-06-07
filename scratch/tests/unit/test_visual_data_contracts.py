import unittest
import pandas as pd
import numpy as np

# We assume visualizer_data_utils.py will be created
from src.visualizations.visualizer_data_utils import (
    extract_histogram_data,
    extract_box_plot_epochs,
    extract_stacked_bar_data
)

class TestVisualDataContracts(unittest.TestCase):
    def setUp(self):
        # Create a dummy dynamics DataFrame
        np.random.seed(42)
        n_times = 30
        n_nodes = 3
        
        t_idx = np.repeat(np.arange(n_times), n_nodes)
        node_label = np.tile(["NodeA", "NodeB", "NodeC"], n_times)
        velocity_v = np.random.normal(10, 2, size=n_times * n_nodes)
        
        # Add a massive outlier to NodeA at t_idx=10
        outlier_idx = (t_idx == 10) & (node_label == 'NodeA')
        velocity_v[outlier_idx] = 100.0 
        
        self.df_dyn = pd.DataFrame({
            't_idx': t_idx,
            'node_label': node_label,
            'velocity_v': velocity_v
        })

    def test_histogram_outlier_handling(self):
        """Contract 1: Histogram KDE should not fail due to massive outliers"""
        df_a = self.df_dyn[self.df_dyn['node_label'] == 'NodeA']
        clean_data, outliers = extract_histogram_data(df_a['velocity_v'], z_thresh=3.0)
        
        # Check that the massive outlier (100.0) is separated
        self.assertTrue(len(outliers) > 0)
        self.assertTrue(100.0 in outliers.values)
        self.assertTrue(max(clean_data) < 100.0)

    def test_box_plot_epoch_split(self):
        """Contract 2: Box plots must split by epochs correctly"""
        # Split into 3 epochs
        df_a = self.df_dyn[self.df_dyn['node_label'] == 'NodeA']
        epochs_dict = extract_box_plot_epochs(df_a, n_epochs=3)
        
        self.assertEqual(len(epochs_dict), 3)
        self.assertTrue("Epoch 1" in epochs_dict)
        self.assertTrue("Epoch 3" in epochs_dict)
        # Ensure total data points remain the same
        total_len = sum([len(v) for v in epochs_dict.values()])
        self.assertEqual(total_len, len(df_a))

    def test_stacked_bar_normalization(self):
        """Contract 3: Stacked Bar Data must sum to 1.0 (100%) at each t_idx"""
        df_stacked = extract_stacked_bar_data(self.df_dyn)
        
        # Group by t_idx and sum the normalized shares
        for t, group in df_stacked.groupby('t_idx'):
            total_share = group['normalized_share'].sum()
            self.assertAlmostEqual(total_share, 1.0, places=5)

if __name__ == '__main__':
    unittest.main()
