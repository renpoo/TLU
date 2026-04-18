#!/usr/bin/env python3
# test_001_1_1_filter_macro_thermodynamics.py
import unittest
import numpy as np
from src.filters._001_1_1_filter_macro_thermodynamics import run_thermodynamics_analysis

class TestFilterThermodynamicsMacro(unittest.TestCase):
    def test_run_thermodynamics_analysis_basic(self):
        """
        [Red->Green] Verify that the pure mathematical logic layer correctly calculates and returns
        thermodynamic indicators (U, S, T, W, Q, F) completely independently of I/O.
        """
        # Arrange
        # Transfer of 10.0 from Node 0 to Node 1
        T_slice = np.array([
            [0.0, 10.0],
            [0.0,  0.0]
        ])
        q_history = []
        work_indices = [1] # Consider inflow to Node 1 as "work"
        heat_indices = [0] # Consider inflow to Node 0 as "dissipated heat"
        t_idx = 0

        # Act
        records, q_current = run_thermodynamics_analysis(
            t_idx, T_slice, q_history, work_indices, heat_indices
        )

        # Assert
        # Since it's a macro thermodynamic indicator, the output record is only 1 row for the entire system
        self.assertEqual(len(records), 1)
        self.assertEqual(q_current.shape, (2,))
        
        # Record structure: [t_idx, U, S, T, W, Q, gradT, F]
        rec = records[0]
        self.assertEqual(len(rec), 8)
        self.assertEqual(rec[0], 0)
        self.assertTrue(isinstance(rec[1], str)) # Check if U etc. are formatted as string

        # Simple check of specific values (total activity U of T_slice should be 10.0)
        self.assertEqual(float(rec[1]), 10.0)

if __name__ == '__main__':
    unittest.main()
