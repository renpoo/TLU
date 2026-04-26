#!/usr/bin/env python3
# ==========================================
# test_filter_fractal_noise.py
# TLU System: Unit Tests for Fractal Dimensionality & 1/f Noise
# ==========================================
import unittest
import numpy as np

try:
    from src.core.core_signal_processing import compute_spectral_exponent_beta
except ImportError:
    compute_spectral_exponent_beta = None

def generate_noise(length, beta):
    """
    Generates synthetic noise with a given spectral exponent beta.
    beta=0: White noise
    beta=1: Pink noise
    beta=2: Brownian noise (random walk)
    """
    # Create white noise
    white = np.random.normal(0, 1, length)
    
    # FFT
    X = np.fft.rfft(white)
    
    # Frequencies
    f = np.fft.rfftfreq(length)
    f[0] = 1e-10  # Avoid division by zero
    
    # Scale amplitudes by 1 / f^(beta/2) since Power S ~ 1/f^beta, Amplitude ~ 1/f^(beta/2)
    X = X / (f ** (beta / 2.0))
    X[0] = 0 # Remove DC component
    
    # IFFT back to time domain
    return np.fft.irfft(X, n=length)

class TestFractalNoise(unittest.TestCase):
    def setUp(self):
        np.random.seed(42)
        self.N = 10000
        
        # We don't generate perfect noise with exactly beta=0.000, 
        # but the estimator should be reasonably close.
        self.white_noise = np.random.normal(0, 1, self.N)
        self.pink_noise = generate_noise(self.N, beta=1.0)
        self.brown_noise = generate_noise(self.N, beta=2.0)

    def test_compute_spectral_exponent(self):
        """Test if the spectral exponent beta can be correctly estimated."""
        # Red Phase: Fail if not implemented
        self.assertIsNotNone(compute_spectral_exponent_beta, "compute_spectral_exponent_beta is not implemented.")
        
        beta_white = compute_spectral_exponent_beta(self.white_noise)
        beta_pink = compute_spectral_exponent_beta(self.pink_noise)
        beta_brown = compute_spectral_exponent_beta(self.brown_noise)
        
        # Allow some tolerance due to the stochastic nature of Welch's method and finite data
        self.assertTrue(abs(beta_white - 0.0) < 0.3, f"White noise beta should be near 0, got {beta_white}")
        self.assertTrue(abs(beta_pink - 1.0) < 0.3, f"Pink noise beta should be near 1, got {beta_pink}")
        self.assertTrue(abs(beta_brown - 2.0) < 0.3, f"Brown noise beta should be near 2, got {beta_brown}")

if __name__ == '__main__':
    unittest.main()
