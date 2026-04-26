#!/usr/bin/env python3
# ==========================================
# test_filter_traversing_ccf.py
# TLU System: Unit Tests for Traversing Phase Shift
# ==========================================
import unittest
import numpy as np

try:
    from src.core.core_signal_processing import compute_traversing_phase_shift
except ImportError:
    compute_traversing_phase_shift = None

class TestTraversingCCF(unittest.TestCase):
    def setUp(self):
        # Create a time series of 120 weeks
        self.N = 120
        self.t = np.arange(self.N)
        self.period = 4
        self.f_true = 1.0 / self.period
        
        # Signal X: pure sine wave
        self.x = np.sin(2 * np.pi * self.f_true * self.t)
        
        # Signal Y: starts with 0 phase shift, then shifts to -pi/2 halfway
        self.y = np.zeros_like(self.x)
        half = self.N // 2
        
        # First half: perfectly synced
        self.y[:half] = np.sin(2 * np.pi * self.f_true * self.t[:half])
        
        # Second half: lagging by pi/2 (1 week)
        self.y[half:] = np.sin(2 * np.pi * self.f_true * self.t[half:] - np.pi/2)
        
        # Add noise
        np.random.seed(42)
        self.x_noisy = self.x + np.random.normal(0, 0.1, self.N)
        self.y_noisy = self.y + np.random.normal(0, 0.1, self.N)

    def test_compute_traversing_phase_shift(self):
        """Test if traversing CCF can detect a dynamic shift in phase."""
        # Red Phase: Fail if not implemented
        self.assertIsNotNone(compute_traversing_phase_shift, "compute_traversing_phase_shift is not implemented.")
        
        window_size = 24
        step_size = 4
        target_freq = 0.25
        
        t_indices, coherences, phase_shifts = compute_traversing_phase_shift(
            self.x_noisy, self.y_noisy, window_size, step_size, target_freq
        )
        
        self.assertTrue(len(t_indices) > 0, "No time indices returned.")
        self.assertEqual(len(t_indices), len(phase_shifts))
        
        # Check first window (entirely in first half)
        # Should have phase shift near 0
        self.assertTrue(abs(phase_shifts[0]) < 0.2, f"Expected ~0 phase shift at start, got {phase_shifts[0]}")
        
        # Check last window (entirely in second half)
        # Should have phase shift near -pi/2 (-1.57)
        # Using angle diff to avoid wrapping issues
        diff = np.angle(np.exp(1j * (phase_shifts[-1] - (-np.pi/2))))
        self.assertTrue(abs(diff) < 0.2, f"Expected ~-1.57 phase shift at end, got {phase_shifts[-1]}")

if __name__ == '__main__':
    unittest.main()
