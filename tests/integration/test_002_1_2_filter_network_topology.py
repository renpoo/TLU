#!/usr/bin/env python3
# test_002_1_2_filter_network_topology.py
import unittest
import numpy as np
from src.filters._002_1_2_filter_network_topology import run_network_topology_analysis

class TestFilterNetworkTopology(unittest.TestCase):
    def test_run_network_topology_analysis_basic(self):
        """
        [Red->Green] When 1 time slice is passed, without depending on I/O,
        verification that the weight and stress of active edges are calculated.
        """
        # Latest slice at t=3
        T_slice = np.array([
            [0.0, 10.0, 5.0],  # Edges 0->1, 0->2 exist
            [0.0,  0.0, 0.0],
            [2.0,  0.0, 0.0]   # Edge 2->0 exists
        ])
        t_idx = 3
        
        # History of the past 2 steps
        T_history = [
            np.array([[0.0, 8.0, 5.0], [0.0, 0.0, 0.0], [2.0, 0.0, 0.0]]),
            np.array([[0.0, 12.0, 5.0], [0.0, 0.0, 0.0], [2.0, 0.0, 0.0]])
        ]

        # Act
        records = run_network_topology_analysis(t_idx, T_slice, T_history)

        # Assert
        # There are 3 edges with weight > 0 (0->1, 0->2, 2->0), so 3 rows should be returned
        self.assertEqual(len(records), 3)

        # Verify edge 0 -> 1
        rec_0_1 = next(r for r in records if r[1] == 0 and r[2] == 1)
        self.assertEqual(rec_0_1[0], t_idx) # t_idx
        
        # Check if the value is formatted as a string
        self.assertTrue(isinstance(rec_0_1[3], str)) # weight
        self.assertTrue(isinstance(rec_0_1[4], str)) # stress

if __name__ == '__main__':
    unittest.main()
