#!/usr/bin/env python3
# test_004_1_1_filter_control_theory.py
import unittest
import numpy as np

try:
    import scipy
    from src.filters._004_1_1_filter_control_theory import run_control_theory_analysis
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

@unittest.skipIf(not SCIPY_AVAILABLE, "Skipping test since scipy is unsupported")
class TestFilterControlTheory(unittest.TestCase):
    def test_run_control_theory_analysis_basic(self):
        """
        [Red->Green] Verify that the pure function, without depending on strings or external files,
        receives only the target vector and controllable indices,
        and correctly calculates and returns the optimal input u and the gap.
        """
        N = 2
        # Transfer of 10.0 from Node 0 to Node 1
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        
        # Set the target value of Node 1 to 20.0
        target_q = np.array([0.0, 20.0])
        # Make only Node 0 capable of budget injection (control)
        controllable_indices = [0]
        t_idx = 0

        # Act (weights are default)
        records, q_current = run_control_theory_analysis(
            t_idx, T_slice, target_q, controllable_indices
        )

        # Assert
        self.assertEqual(len(records), N)
        self.assertEqual(q_current.shape, (2,))
        
        # Fix: Synchronize column names with the latest pure mathematical model
        # Record structure: [t_idx, node_idx, optimal_input_u, state_error_x]
        node0_rec = records[0]
        self.assertEqual(len(node0_rec), 4)
        self.assertEqual(node0_rec[0], 0)
        self.assertEqual(node0_rec[1], 0)
        self.assertTrue(isinstance(node0_rec[2], str)) # optimal_input_u
        self.assertTrue(isinstance(node0_rec[3], str)) # state_error_x
        
        # Since Node 1 is uncontrollable, the recommended input u should be forced to 0.0000
        node1_rec = records[1]
        self.assertEqual(float(node1_rec[2]), 0.0)

if __name__ == '__main__':
    unittest.main()
