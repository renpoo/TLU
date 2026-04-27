# 005. Signal Processing & Wave Mechanics

> **"A ledger is not a static block of numbers; it is a vibrating machine. To find the anomaly, we must listen to its frequency."**

Category **005** departs from the spatial and thermodynamic models of previous categories, entering the realm of **Frequency Domain Analysis**. 

Rather than looking at the total volume of transactions (mass) or the rigidity of the network (stiffness), this paradigm treats the flow of resources as continuous, oscillating waves. By applying advanced signal processing techniques—such as Fourier transforms, cross-coherence, and fractal noise analysis—TLU can detect deep, systemic process changes, automated bot activity, or data fabrication that are completely invisible when looking at standard aggregate totals.

---

## 1. Autocorrelation & Resonant Frequency (005_1_1)
*Implementation: `src/filters/_005_1_1_filter_resonant_frequency.py`*

Every healthy organization has a natural "heartbeat" or operational rhythm—for example, bi-weekly payroll cycles, end-of-month invoicing rushes, or quarterly tax payments. TLU uses Autocorrelation and spectral analysis to find the **Dominant Resonant Frequency** of every node.

* **Dominant Frequency:** The specific periodic cycle at which the node vibrates most strongly.
* **Spectral Power:** The intensity or strength of that specific frequency relative to the rest of the noise.

![005_1_1__resonant_frequency](../readme_plots/005_1_1_resonant_frequency.png)

### Pathological Resonance
If a massive, unexpected spectral peak appears at an unnatural frequency (e.g., a massive spike at exactly "3 days" that has never existed before in the company's history), it strongly suggests an artificial process has been introduced. In financial data, this is the fingerprint of a programmed bot or an automated embezzlement script siphoning micro-amounts of money at exact, mechanical intervals.

## 2. Phase Shift & Coherence (005_1_2)
*Implementation: `src/filters/_005_1_2_filter_phase_shift_coherence.py`*

While Category 001 uses simple time-lag correlation, Category 005 evaluates the **Phase Shift** and **Coherence** between two nodes at specific target frequencies using cross-spectral density.

* **Coherence:** A measure of how well the wave patterns of two nodes match each other at a specific frequency (a value from 0 to 1). High coherence means the two departments are moving perfectly in sync.
* **Phase Shift ($\Delta \phi$):** The angular difference (time lag) between the two coherent waves. 

![005_1_2__phase_drift_heatmap](../readme_plots/005_1_2__phase_drift_heatmap.png)

### Detecting Process Bottlenecks
By plotting the Phase Shift over time in a rolling window, TLU creates a **Phase Drift Heatmap**. If the phase shift between "Sales" and "Cash Collection" suddenly begins to stretch (drift positively), it means the collection cycle is slowing down. The total assets on the Balance Sheet might look perfectly healthy, but the *velocity* of cash conversion is grinding to a halt—a critical early warning for an impending liquidity crisis.

## 3. Fractal Dimensionality & 1/f Noise (005_2_1)
*Implementation: `src/filters/_005_2_1_filter_fractal_noise.py`*

Not all random noise is created equal. Healthy natural systems (including human organizations, heartbeats, and stock markets) exhibit complex, self-similar fractal patterns known as **Pink Noise ($1/f$)**. 

TLU calculates the Power Spectral Density (PSD) decay and extracts the **Spectral Exponent ($\beta$)** to classify the "texture" of the data's variance.

* **White Noise ($\beta \approx 0$):** Pure, uncorrelated randomness. Every event is completely independent of the past.
* **Pink Noise ($\beta \approx 1$):** Fractal, long-memory processes. The hallmark of complex human and organic systems.
* **Brown Noise ($\beta \approx 2$):** A random walk. Highly correlated short-term movements, but drifting aimlessly over the long term.

![005_2_1__fractal_noise_spectrum](../readme_plots/005_2_1_fractal_noise_spectrum.png)

### Detecting Data Fabrication
Humans are notoriously terrible at generating true random variance. If an accountant manually fabricates thousands of fake ledger entries to hide a loss, or if a crude random number generator is used to pad a dataset, the resulting data will mathematically collapse into "White Noise." 

By mapping the fractal dimensionality of the network, TLU catches data fabrication not by looking at the total amounts, but by proving that the *texture* of the numbers is physically impossible for a group of humans to have generated naturally.

## 4. Business Implications

By utilizing Signal Processing and Wave Mechanics, analysts can answer:

1. **Are automated bots tampering with our system?** (Spikes in unnatural Resonant Frequencies).
2. **Is our cash conversion cycle secretly slowing down?** (Stretching Phase Shifts between operational nodes).
3. **Has this ledger been artificially fabricated?** (The collapse of natural Pink Noise into artificial White Noise).
