# 06. Signals & Noise (Phase 1.10 - 1.14)

This phase treats the ledger like a radio signal or a vibrating machine. By analyzing the frequencies, lags, and noise spectrums of the money flow, TLU can detect deep, systemic process changes that are completely invisible in standard aggregate totals.

---

### 1. Phase Drift Heatmap (`005_1_2__phase_drift_heatmap.png`)

* **📊 Visual Structure**: A matrix heatmap where the X-axis is time (e.g., weeks) and the Y-axis lists specific account pairs (e.g., `Accounts_Receivable vs Cash`).
* **📐 Physics Theory**: Cross-Correlation Signal Processing. It measures the "time lag" (phase shift) between two correlated signals. If Sales usually turn into Cash 3 weeks later, the baseline lag is 3.
* **🚨 Anomaly Detection**: 
  * Look for deep **Red** or deep **Blue** cells appearing in the timeline.
  * **Red** = Lag is stretching (it's taking longer than normal).
  * **Blue** = Lag is compressing (it's happening faster than normal).
* **💼 Business Translation**: **Severe Cash Flow Bottlenecks**. If the AR vs Cash line suddenly turns bright Red, it means "Collections are slowing down." Even if the total B/S assets look healthy, the actual velocity of cash conversion is grinding to a halt, serving as a powerful early warning for an impending liquidity crisis.

### 2. Resonant Frequency (`005_1_1__resonant_frequency.png`)

* **📊 Visual Structure**: A spectral density graph (like an audio equalizer) showing peaks at specific frequencies.
* **📐 Physics Theory**: Fourier Transform. Identifies the natural "vibrational frequencies" of the organization (e.g., bi-weekly payroll cycles, quarterly tax payments).
* **🚨 Anomaly Detection**: 
  * A massive, unexpected peak appearing at an unnatural frequency (e.g., a massive spike at exactly "3 days" that has never existed before).
* **💼 Business Translation**: **Automated Fraud or Process Hijacking**. If a new, highly regular high-frequency transaction cycle appears, it strongly suggests a programmed bot or an automated embezzlement script is siphoning micro-amounts of money at exact intervals.

### 3. Fractal Noise Spectrum (`005_2_1__fractal_noise_spectrum.png`)

* **📊 Visual Structure**: A scatter plot on a logarithmic scale showing the Power Spectral Density (PSD) decay.
* **📐 Physics Theory**: Power Law / 1/f Noise Analysis. Healthy natural systems (including human organizations) exhibit $1/f$ (pink noise) scaling. Pure randomness is $1/f^0$ (white noise).
* **🚨 Anomaly Detection**: 
  * The slope of the decay line suddenly flattens out, changing from Pink Noise (structured human behavior) to White Noise (pure randomness).
* **💼 Business Translation**: **Data Fabrication or complete loss of control**. Humans are very bad at faking natural variance. If an accountant manually fabricates thousands of fake ledger entries to hide a loss, the resulting data will mathematically look like "White Noise." This graph catches data fabrication by looking at the "texture" of the numbers.
