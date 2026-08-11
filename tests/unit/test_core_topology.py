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

    def test_compute_univariate_z_score_vector_and_options(self):
        """Verify 1D vector Z-score computation with absolute and signed modes"""
        from src.core.core_topology import compute_univariate_z_score

        current_v = np.array([10.0, -2.0])
        history_v = [
            np.array([4.0, 0.0]),
            np.array([2.0, 0.0])
        ]
        # Mean: [3.0, 0.0], Std: [1.0, 0.0]
        # Deviation: [7.0, -2.0] -> Z-score for index 0: 7.0/1.0 = 7.0, for index 1: std=0 -> 0.0

        abs_z = compute_univariate_z_score(current_v, history_v, absolute_deviation=True)
        self.assertEqual(abs_z.shape, (2,))
        self.assertAlmostEqual(abs_z[0], 7.0)
        self.assertEqual(abs_z[1], 0.0)

        signed_z = compute_univariate_z_score(current_v, history_v, absolute_deviation=False)
        self.assertAlmostEqual(signed_z[0], 7.0)

if __name__ == '__main__':
    unittest.main()
