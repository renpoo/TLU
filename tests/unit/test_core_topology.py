#!/usr/bin/env python3
# test_core_topology.py
import unittest
import numpy as np
from src.core.core_topology import compute_edge_stress

class TestCoreTopology(unittest.TestCase):
    def test_compute_edge_stress_normal(self):
        """[Green] Verify that the Z-score (stress) is calculated correctly from a normal history"""
        T_current = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        # Data such that the history mean=4.0, standard deviation=2.0
        T_history = [
            np.array([[0.0, 6.0], [0.0, 0.0]]),
            np.array([[0.0, 2.0], [0.0, 0.0]])
        ]
        
        stress = compute_edge_stress(T_current, T_history)
        
        # Expected value: |10.0 - 4.0| / 2.0 = 3.0
        self.assertEqual(stress.shape, (2, 2))
        self.assertAlmostEqual(stress[0, 1], 3.0)

    def test_compute_edge_stress_insufficient_history(self):
        """[Green] Safely return a zero matrix if history is less than 2"""
        T_current = np.array([[0.0, 10.0], [0.0, 0.0]])
        T_history = [np.array([[0.0, 5.0], [0.0, 0.0]])] # 1 case only
        
        stress = compute_edge_stress(T_current, T_history)
        
        self.assertEqual(stress[0, 1], 0.0)
        self.assertTrue(np.all(stress == 0.0))

    def test_compute_edge_stress_zero_division(self):
        """[Green] If past standard deviation is 0 (constant transaction), avoid division by zero and return 0.0"""
        T_current = np.array([[0.0, 10.0], [0.0, 0.0]])
        # History has all the same values (standard deviation = 0.0)
        T_history = [
            np.array([[0.0, 5.0], [0.0, 0.0]]),
            np.array([[0.0, 5.0], [0.0, 0.0]])
        ]
        
        stress = compute_edge_stress(T_current, T_history)
        
        # Due to the where clause of np.divide, 0.0 should be returned safely
        self.assertEqual(stress[0, 1], 0.0)

if __name__ == '__main__':
    unittest.main()
