#!/usr/bin/env python3
# test_003_1_3_filter_jacobian_trajectory.py
import unittest
import numpy as np
import io
import csv
import os
import tempfile
import pandas as pd

from src.filters._003_1_3_filter_jacobian_trajectory import run_jacobian_trajectory_analysis

class TestJacobianTrajectoryFilter(unittest.TestCase):
    def setUp(self):
        # Create a simple 3x3 transition matrix slice for testing
        # N=3
        self.T_slice = np.array([
            [10.0,  5.0,  0.0],
            [ 0.0, 15.0,  5.0],
            [ 5.0,  0.0, 10.0]
        ], dtype=float)

    def test_run_jacobian_trajectory_all_nodes(self):
        """
        Verify that Jacobian extraction without target labels outputs all N x N values.
        """
        # When target_ids is empty, we expect full M_echo (N x N)
        target_ids = []
        t_idx = 1
        gamma = 0.8
        max_k = 2

        records = run_jacobian_trajectory_analysis(
            t_idx=t_idx,
            T_slice=self.T_slice,
            target_ids=target_ids,
            gamma=gamma,
            max_k=max_k
        )

        # Expected output shape: N x N = 3 x 3 = 9 records
        self.assertEqual(len(records), 9)

        # Confirm data format
        # Record columns: [t_idx, src_idx, dst_idx, jacobian_value]
        for rec in records:
            self.assertEqual(rec[0], t_idx)
            self.assertTrue(0 <= rec[1] < 3)
            self.assertTrue(0 <= rec[2] < 3)
            val = float(rec[3])
            self.assertTrue(val >= 0.0)

    def test_run_jacobian_trajectory_targeted(self):
        """
        Verify that Jacobian extraction with target labels outputs only the columns matching target_ids (size: N x len(target_ids)).
        """
        # Specify node 1 as target
        target_ids = [1]
        t_idx = 4
        gamma = 0.85
        max_k = 3

        records = run_jacobian_trajectory_analysis(
            t_idx=t_idx,
            T_slice=self.T_slice,
            target_ids=target_ids,
            gamma=gamma,
            max_k=max_k
        )

        # Expected output shape: N x len(target_ids) = 3 x 1 = 3 records
        self.assertEqual(len(records), 3)

        # Check values match expectation
        # target_ids = [1] means J = M_echo[:, [1]].T, so we get M_echo[i, 1] for each node i
        # Output columns: [t_idx, src_idx, dst_idx, jacobian_value]
        # In this target scenario, dst_idx will be 1
        for rec in records:
            self.assertEqual(rec[0], t_idx)
            self.assertEqual(rec[2], 1) # dst_idx must be the target index 1

    def test_run_jacobian_trajectory_orders(self):
        """
        Verify that Jacobian extraction with explicit orders (1st, 2nd, 3rd) outputs P, P^2, and P^3 scaling.
        """
        t_idx = 1
        gamma = 0.9
        max_k = 5

        # 1st-Order (order=1) -> matches gamma * P
        records_1st = run_jacobian_trajectory_analysis(
            t_idx=t_idx, T_slice=self.T_slice, target_ids=[], gamma=gamma, max_k=max_k, order=1
        )
        # Parse output value back to matrix
        M_1st = np.zeros((3, 3))
        for rec in records_1st:
            M_1st[rec[1], rec[2]] = float(rec[3])
            
        # P[0, 1] = 5 / 15 = 1/3, gamma * P[0, 1] = 0.9 * (1/3) = 0.3
        self.assertAlmostEqual(M_1st[0, 1], 0.3, places=5)
        # P[1, 2] = 5 / 20 = 0.25, gamma * P[1, 2] = 0.9 * 0.25 = 0.225
        self.assertAlmostEqual(M_1st[1, 2], 0.225, places=5)

        # 2nd-Order (order=2) -> matches gamma^2 * P^2
        records_2nd = run_jacobian_trajectory_analysis(
            t_idx=t_idx, T_slice=self.T_slice, target_ids=[], gamma=gamma, max_k=max_k, order=2
        )
        M_2nd = np.zeros((3, 3))
        for rec in records_2nd:
            M_2nd[rec[1], rec[2]] = float(rec[3])
            
        # P^2[0, 1] = (2/3)*(1/3) + (1/3)*(3/4) = 17/36
        # gamma^2 * P^2[0, 1] = 0.81 * (17/36) = 0.3825
        self.assertAlmostEqual(M_2nd[0, 1], 0.3825, places=5)

if __name__ == '__main__':
    unittest.main()

