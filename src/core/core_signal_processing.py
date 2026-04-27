#!/usr/bin/env python3
# ==========================================
# core_signal_processing.py
# TLU System: Signal Processing and Wave Mechanics
# ==========================================
import numpy as np
from scipy import signal

def compute_autocorrelation(x: np.ndarray, max_tau: int) -> np.ndarray:
    """
    Computes the Auto-Correlation Function (ACF) for a given 1D signal.
    
    Args:
        x: 1D numpy array of the signal
        max_tau: maximum lag to compute
        
    Returns:
        1D numpy array of the ACF up to max_tau
    """
    if len(x) == 0:
        return np.array([])
        
    # Subtract mean to compute autocovariance/autocorrelation
    x_centered = x - np.mean(x)
    
    # Compute using scipy correlate
    acf = signal.correlate(x_centered, x_centered, mode='full')
    
    # The middle element is tau=0
    mid_idx = len(acf) // 2
    
    # Extract the positive lags up to max_tau
    acf_positive = acf[mid_idx:mid_idx + max_tau + 1]
    
    # Normalize so that ACF at lag 0 is 1.0 (if variance > 0)
    if acf_positive[0] > 1e-10:
        acf_positive = acf_positive / acf_positive[0]
        
    return acf_positive

def compute_resonant_frequency(x: np.ndarray, max_tau: int) -> tuple[float, float]:
    """
    Computes the dominant (resonant) frequency of a signal using Welch's method for PSD.
    
    Args:
        x: 1D numpy array of the signal
        max_tau: Not strictly used for Welch's method, but kept for interface consistency
                 Can be used to set nperseg (window size)
                 
    Returns:
        A tuple of (dominant_frequency, max_spectral_power)
    """
    if len(x) < 2:
        return 0.0, 0.0
        
    # Use Welch's method to estimate the power spectral density
    # nperseg controls the resolution. Use min(len(x), max_tau * 2) as window size
    window_size = min(len(x), max(16, max_tau * 2))
    
    # If the signal is very short, just do a standard periodogram
    if len(x) < window_size:
        f, Pxx = signal.periodogram(x, fs=1.0)
    else:
        f, Pxx = signal.welch(x, fs=1.0, nperseg=window_size)
        
    # Skip the DC component (frequency 0) to find the actual resonant cycle
    if len(f) > 1:
        f = f[1:]
        Pxx = Pxx[1:]
    else:
        return 0.0, 0.0
        
    # Find the peak frequency
    max_idx = np.argmax(Pxx)
    dominant_freq = f[max_idx]
    max_power = Pxx[max_idx]
    
    return dominant_freq, max_power

def compute_phase_shift_coherence(x: np.ndarray, y: np.ndarray, target_freq: float) -> tuple[float, float]:
    """
    Computes the coherence and phase shift between two signals at a specific target frequency.
    
    Args:
        x: 1D numpy array of signal 1
        y: 1D numpy array of signal 2
        target_freq: The frequency to evaluate at (in cycles per sample, e.g. 0.25 for a period of 4)
        
    Returns:
        A tuple of (coherence, phase_shift_radians)
    """
    if len(x) < 2 or len(y) < 2 or len(x) != len(y):
        return 0.0, 0.0
        
    # Use Welch's method for coherence and cross-spectral density (CSD)
    window_size = min(len(x), 32)
    
    if len(x) < window_size:
        # For very short signals, use periodogram/fft directly
        X = np.fft.fft(x)
        Y = np.fft.fft(y)
        f = np.fft.fftfreq(len(x))
        # Simple cross spectrum
        Pxy = X * np.conj(Y)
        Pxx = X * np.conj(X)
        Pyy = Y * np.conj(Y)
        # Coherence is always 1 for a single FFT realization, so this is just an approximation
        Cxy = np.ones_like(f) if np.sum(np.abs(Pxx)*np.abs(Pyy)) > 0 else np.zeros_like(f)
    else:
        with np.errstate(divide='ignore', invalid='ignore'):
            f, Cxy = signal.coherence(x, y, fs=1.0, nperseg=window_size)
            f, Pxy = signal.csd(x, y, fs=1.0, nperseg=window_size)
            
            # Replace NaN with 0.0 (or default) in case of zero division (flat signals)
            Cxy = np.nan_to_num(Cxy, nan=0.0)
            Pxy = np.nan_to_num(Pxy)
        
    # Find the frequency bin closest to target_freq
    idx = np.argmin(np.abs(f - target_freq))
    
    coherence_at_f = Cxy[idx]
    
    # Phase shift is the angle of the cross spectrum
    # angle(Pxy) gives the phase of x relative to y
    phase_shift_at_f = np.angle(Pxy[idx])
    
    return coherence_at_f, phase_shift_at_f

def compute_traversing_phase_shift(x: np.ndarray, y: np.ndarray, window_size: int, step_size: int, target_freq: float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Computes Traversing CCF (sliding window phase shift and coherence) over time.
    
    Args:
        x: 1D numpy array of signal 1
        y: 1D numpy array of signal 2
        window_size: Length of the sliding window
        step_size: Step size to move the window
        target_freq: The frequency to evaluate at (cycles per sample)
        
    Returns:
        tuple of (t_indices, coherences, phase_shifts)
    """
    if len(x) < window_size or len(y) < window_size or len(x) != len(y):
        return np.array([]), np.array([]), np.array([])
        
    N = len(x)
    t_indices = []
    coherences = []
    phase_shifts = []
    
    # Slide the window
    for start_idx in range(0, N - window_size + 1, step_size):
        end_idx = start_idx + window_size
        
        # Center time of the window
        t_center = start_idx + window_size // 2
        
        x_sub = x[start_idx:end_idx]
        y_sub = y[start_idx:end_idx]
        
        # Apply window function (e.g., Hann)
        win = signal.windows.hann(window_size)
        x_sub = x_sub * win
        y_sub = y_sub * win
        
        c, p = compute_phase_shift_coherence(x_sub, y_sub, target_freq)
        
        t_indices.append(t_center)
        coherences.append(c)
        phase_shifts.append(p)
        
    return np.array(t_indices), np.array(coherences), np.array(phase_shifts)

def compute_spectral_exponent_beta(x: np.ndarray) -> float:
    """
    Computes the spectral exponent beta of a 1D signal.
    Power Spectral Density S(f) ~ 1/f^beta.
    Fits a linear regression to log10(S(f)) vs log10(f).
    
    Args:
        x: 1D numpy array of the signal
        
    Returns:
        The spectral exponent beta.
    """
    if len(x) < 4:
        return 0.0
        
    # Use Welch's method to estimate the power spectral density
    # We use a reasonably large nperseg to get good low-frequency resolution,
    # but not too large so we can average over segments to reduce variance.
    nperseg = min(len(x), 256)
    f, Pxx = signal.welch(x, fs=1.0, nperseg=nperseg)
    
    # Exclude DC component (f=0) because log10(0) is undefined
    valid_idx = (f > 0) & (Pxx > 0)
    f = f[valid_idx]
    Pxx = Pxx[valid_idx]
    
    if len(f) < 2:
        return 0.0
        
    # Log-Log transformation
    log_f = np.log10(f)
    log_Pxx = np.log10(Pxx)
    
    # Linear regression: log_Pxx = alpha * log_f + intercept
    # Since S(f) ~ 1/f^beta = f^(-beta), then log_S(f) = -beta * log_f + C
    # Therefore, beta = -alpha
    slope, intercept = np.polyfit(log_f, log_Pxx, 1)
    
    beta = -slope
    
    return beta
