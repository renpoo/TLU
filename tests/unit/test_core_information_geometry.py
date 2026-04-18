#!/usr/bin/env python3
# test_core_information_geometry.py
import unittest
import numpy as np
from src.core.core_information_geometry import compute_shannon_entropy, compute_kl_divergence

class TestInformationGeometry(unittest.TestCase):
    def test_compute_shannon_entropy_basic(self):
        """
        Test to calculate Shannon entropy per node from the transition probability matrix (P).
        """
        # P: Transition probability matrix (N x N)
        # Node 0: [1.0, 0.0, 0.0] -> 100% concentrated on one node (entropy should be 0)
        # Node 1: [0.5, 0.5, 0.0] -> Evenly distributed to two nodes
        # Node 2: [0.0, 0.0, 0.0] -> Isolated node that doesn't flow anywhere (safely return 0)
        P_matrix = np.array([
            [1.0, 0.0, 0.0],
            [0.5, 0.5, 0.0],
            [0.0, 0.0, 0.0]
        ])
        
        # Shannon entropy H = - sum(p * log2(p))
        # 0*log2(0) is treated as 0 by taking the limit.
        # Node 0: -(1 * 0) = 0.0
        # Node 1: -(0.5 * -1 + 0.5 * -1) = 1.0
        # Node 2: All 0 so 0.0
        expected_entropy = np.array([0.0, 1.0, 0.0])
        
        actual_entropy = compute_shannon_entropy(P_matrix)
        
        np.testing.assert_array_almost_equal(actual_entropy, expected_entropy)


    def test_compute_shannon_entropy_2(self):
        # Node 0: Completely deterministic (100% concentrated on one route -> entropy 0)
        # Node 1: Completely equal probability distribution to two routes -> maximum entropy (1.0 if base is 2)
        # Node 2: All elements zero (safety check for node with no flow -> return entropy 0.0)
        P = np.array([
            [1.0, 0.0],
            [0.5, 0.5],
            [0.0, 0.0]
        ])
        
        entropy = compute_shannon_entropy(P)
        
        self.assertAlmostEqual(entropy[0], 0.0)
        self.assertAlmostEqual(entropy[1], 1.0)
        self.assertAlmostEqual(entropy[2], 0.0)


    def test_compute_kl_divergence_basic(self):
        """
        Test to calculate the KL divergence (information-theoretic distance) per node
        between the current transition probability (P_current) and the past baseline (P_baseline).
        """
        
        # P_current: Current distribution
        P_current = np.array([
            [0.5, 0.5],  # Node 0: Evenly distributed
            [1.0, 0.0]   # Node 1: 100% concentrated on Node 0
        ])
        
        # P_baseline: Past average distribution
        P_baseline = np.array([
            [0.5, 0.5],  # Node 0: Evenly distributed in the past as well (no change)
            [0.5, 0.5]   # Node 1: Evenly distributed in the past (drastic change!)
        ])
        
        # Expected KL divergence
        # Node 0: 0.5*log2(0.5/0.5) + 0.5*log2(0.5/0.5) = 0.0 (no change)
        # Node 1: 1.0*log2(1.0/0.5) + 0.0*log2(...) = 1.0*log2(2.0) + 0 = 1.0
        expected_kl = np.array([0.0, 1.0])
        
        actual_kl = compute_kl_divergence(P_current, P_baseline)
        
        np.testing.assert_array_almost_equal(actual_kl, expected_kl)


    def test_compute_kl_divergence_2(self):
        # Comparison of current transition probability and past baseline
        P_current = np.array([
            [0.5, 0.5], # Node 0: No change
            [0.5, 0.5], # Node 1: Change from baseline
            [1.0, 0.0], # Node 2: Currently includes 0 (zero division tolerance test for numerator)
            [0.0, 0.0]  # Node 3: All elements zero (safety check)
        ])
        
        P_baseline = np.array([
            [0.5, 0.5], # Node 0: No change
            [0.8, 0.2], # Node 1: Past had a bias of [0.8, 0.2]
            [0.5, 0.5], # Node 2: Past was distributed
            [0.0, 0.0]  # Node 3: Past was also zero
        ])
        
        kl_div = compute_kl_divergence(P_current, P_baseline)
        
        # Node 0: Distribution perfectly matches, so distance is zero
        self.assertAlmostEqual(kl_div[0], 0.0)
        
        # Node 1: Distribution differs, so distance has a positive value
        # Calculation: 0.5*log2(0.5/0.8) + 0.5*log2(0.5/0.2) ≒ 0.3219
        self.assertGreater(kl_div[1], 0.0)
        self.assertAlmostEqual(kl_div[1], 0.321928, places=4)
        
        # Node 2: Even if an element of P_current is 0, it is safely calculated and distance is obtained
        # Calculation: 1.0*log2(1.0/0.5) + 0.0 = 1.0
        self.assertAlmostEqual(kl_div[2], 1.0)
        
        # Node 3: Zero matrices against each other return zero
        self.assertAlmostEqual(kl_div[3], 0.0)


if __name__ == '__main__':
    unittest.main()
