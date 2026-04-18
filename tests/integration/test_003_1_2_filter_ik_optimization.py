#!/usr/bin/env python3
# test_003_1_2_filter_ik_optimization.py
import unittest
import numpy as np
from src.filters._003_1_2_filter_ik_optimization import run_ik_analysis

class TestFilterIKOptimization(unittest.TestCase):
    def setUp(self):
        self.N = 3
        # Node 0 -> Node 1 (10.0), Node 1 -> Node 2 (5.0)
        self.T_slice = np.array([
            [0.0, 10.0, 0.0],
            [0.0,  0.0, 5.0],
            [0.0,  0.0, 0.0]
        ])
        self.t_idx = 1
        # Mock at least 3 history records to allow calculation of K_safe
        self.q_history = [
            np.array([-5.0, 5.0, 0.0]),
            np.array([-8.0, 3.0, 5.0]),
            np.array([-10.0, 5.0, 5.0])
        ]
        self.gamma = 0.85
        self.max_k = 5

    def test_run_ik_analysis(self):
        """[Red->Green] Pure function test of IK system"""
        target_ids = [2] # Target Node 2
        target_dr_values = np.array([50.0]) # Request +50 arrival at Node 2

        records, q_current = run_ik_analysis(
            t_idx=self.t_idx, 
            T_slice=self.T_slice, 
            q_history=self.q_history,
            target_ids=target_ids, 
            target_dr_values=target_dr_values,
            gamma=self.gamma, 
            max_k=self.max_k
        )
        
        self.assertEqual(len(records), self.N)
        
        # Record structure: [t_idx, node_idx, ik_suggested_delta, ik_strain_energy]
        node0_rec = records[0]
        self.assertEqual(node0_rec[0], self.t_idx)
        self.assertEqual(node0_rec[1], 0)
        
        # IK output (index 2) and strain energy (index 3) should be calculated
        self.assertNotEqual(node0_rec[2], "0.0000")
        self.assertNotEqual(node0_rec[3], "0.0000")

if __name__ == '__main__':
    unittest.main()
