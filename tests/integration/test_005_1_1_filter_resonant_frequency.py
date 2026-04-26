#!/usr/bin/env python3
# ==========================================
# test_filter_resonant_frequency.py
# TLU System: Unit Tests for Signal Processing
# ==========================================
import unittest
import numpy as np

# We expect this module to exist after the Green Phase
try:
    from src.core.core_signal_processing import compute_resonant_frequency
except ImportError:
    # Dummy mock to allow test to fail normally rather than syntax error on import
    compute_resonant_frequency = None

class TestResonantFrequency(unittest.TestCase):
    def setUp(self):
        # Create a dummy time series with a known dominant frequency
        # length = 100, fs (sampling frequency) = 1 (1 step = 1 week)
        self.N = 100
        self.t = np.arange(self.N)
        
        # Create a sine wave with a period of 4 weeks (frequency = 1/4 = 0.25)
        self.period = 4
        self.f_true = 1.0 / self.period
        self.clean_signal = np.sin(2 * np.pi * self.f_true * self.t)
        
        # Add some random noise
        np.random.seed(42)
        self.noise = np.random.normal(0, 0.5, self.N)
        self.noisy_signal = self.clean_signal + self.noise

    def test_compute_resonant_frequency(self):
        """Test if the ACF+PSD algorithm can extract the true dominant frequency."""
        # Red Phase: Fail if not implemented
        self.assertIsNotNone(compute_resonant_frequency, "compute_resonant_frequency is not implemented.")
        
        # Green Phase: Actual test
        max_tau = 24
        dominant_freq, spectral_power = compute_resonant_frequency(self.noisy_signal, max_tau)
        
        # Check if the extracted frequency is close to the true frequency (0.25)
        # Allow some tolerance due to discrete FFT bins
        self.assertTrue(abs(dominant_freq - self.f_true) < 0.05, 
                        f"Extracted frequency {dominant_freq} is not close to true frequency {self.f_true}")
        
        # Power should be significantly greater than 0
        self.assertTrue(spectral_power > 0.1, "Spectral power is too low")

if __name__ == '__main__':
    unittest.main()
