#!/usr/bin/env python3
# ==========================================
# test_filter_phase_shift.py
# TLU System: Unit Tests for Phase Shift & Coherence
# ==========================================
import unittest
import numpy as np

# We expect this module to exist after the Green Phase
try:
    from src.core.core_signal_processing import compute_phase_shift_coherence
except ImportError:
    # Dummy mock to allow test to fail normally
    compute_phase_shift_coherence = None

class TestPhaseShiftCoherence(unittest.TestCase):
    def setUp(self):
        # Create two signals with a known phase shift
        self.N = 100
        self.t = np.arange(self.N)
        
        # Period = 4 weeks, Freq = 0.25
        self.period = 4
        self.f_true = 1.0 / self.period
        
        # Signal X: pure sine wave
        self.x = np.sin(2 * np.pi * self.f_true * self.t)
        
        # Signal Y: sine wave shifted by pi/2 (1/4 of a period, which is 1 week)
        # y(t) = sin(2*pi*f*t - pi/2)
        # Note: phase shift definition depends on convention (Y relative to X)
        self.phase_shift_rad = -np.pi / 2
        self.y = np.sin(2 * np.pi * self.f_true * self.t + self.phase_shift_rad)
        
        # Add slight noise to both
        np.random.seed(42)
        self.x_noisy = self.x + np.random.normal(0, 0.1, self.N)
        self.y_noisy = self.y + np.random.normal(0, 0.1, self.N)

    def test_compute_phase_shift_coherence(self):
        """Test if the coherence and phase shift can be correctly extracted."""
        # Red Phase: Fail if not implemented
        self.assertIsNotNone(compute_phase_shift_coherence, "compute_phase_shift_coherence is not implemented.")
        
        # Green Phase: Actual test
        # We target frequency 0.25
        target_freq = 0.25
        
        coherence, phase_shift = compute_phase_shift_coherence(self.x_noisy, self.y_noisy, target_freq)
        
        # Coherence should be very high (close to 1.0) because they are basically the same wave
        self.assertTrue(coherence > 0.8, f"Coherence {coherence} is too low for highly correlated signals.")
        
        # Phase shift should be close to -pi/2
        # Use angle normalization to avoid wrap-around issues if any
        diff = np.angle(np.exp(1j * (phase_shift - self.phase_shift_rad)))
        self.assertTrue(abs(diff) < 0.2, f"Phase shift {phase_shift} is not close to true shift {self.phase_shift_rad}")

if __name__ == '__main__':
    unittest.main()
