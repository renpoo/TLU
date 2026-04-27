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

### Detecting Business Model Collapse & Artificial Intervention
This acts as an early warning system for structural collapse. If a company claims their business model is stable, but their resonant frequency suddenly shifts from a "30-day cycle" (normal billing) to a chaotic "14-day cycle," it mathematically proves a cash flow crisis forcing early collections. Furthermore, if a massive, unexpected spectral peak appears at an unnatural frequency, it is the fingerprint of a programmed bot or an automated embezzlement script siphoning micro-amounts of money at exact, mechanical intervals.

## 2. Phase Shift & Coherence (005_1_2)
*Implementation: `src/filters/_005_1_2_filter_phase_shift_coherence.py`*

While Category 001 uses simple time-lag correlation, Category 005 evaluates the **Phase Shift** and **Coherence** between nodes at specific target frequencies using cross-spectral density.

* **Coherence:** A measure of how well the wave patterns of two nodes match each other at a specific frequency (a value from 0 to 1). High coherence means the two departments are moving perfectly in sync.
* **Phase Shift ($\Delta \phi$):** The angular difference (time lag) between the two coherent waves, measured in radians from $-\pi$ to $+\pi$.

### PC1 Auto-Master Tracking
To provide a dataset-agnostic "center of gravity," TLU mathematically extracts the 1st Principal Component (PC1) to identify the true "Main Engine" of the system (e.g., Cash, or the busiest traffic intersection). It then calculates the Phase Drift of *all other nodes* against this beating heart.

![005_1_2__phase_drift_heatmap](../readme_plots/005_1_2__phase_drift_heatmap.png)

### Reading the Phase Drift Heatmap: The Viscosity Rentgen
The heatmap visualizes Phase Shift over time (X-axis). It utilizes a diverging colormap (e.g., Red-White-Blue).
* **White (0 radians):** Perfect synchronization with the Main Engine. No delay.
* **Blue/Red ($+\pi$ / $-\pi$):** Lagging behind or leading ahead of the Main Engine. The darker the color, the closer the delay is to a half-cycle phase inversion.

An anomaly ("going out of order") is detected not by a specific color, but by a **horizontal color band suddenly shifting its hue or intensity at a specific time index ($t\_idx$)**:

* **Pattern A (Process Collapse):** A node that was historically synced with Cash (a clean, continuous **White** band) suddenly turns **Dark Blue**. The process has decoupled. For example, Sales are made, but Collections have suddenly stalled, exposing massive organizational friction (viscosity).
* **Pattern B (Lag Deepening):** A node that historically ran with a fixed 1-week delay (a pale **Light Blue** band) suddenly darkens to **Deep Blue**. A known process has critically deteriorated.
* **Pattern C (Bot/Algorithmic Hijacking):** A historically noisy, unrelated node (a flickering mix of colors) suddenly turns perfectly **White**, locking in perfect synchronization with the Main Engine. This implies an artificial mechanism (like wash trading) has forcibly hijacked the account to pump volume synchronously.

## 3. Fractal Dimensionality & 1/f Noise (005_2_1)
*Implementation: `src/filters/_005_2_1_filter_fractal_noise.py`*

Not all random noise is created equal. Healthy natural systems (including human organizations, heartbeats, and stock markets) exhibit complex, self-similar fractal patterns known as **Pink Noise ($1/f$)**. 

TLU calculates the Power Spectral Density (PSD) decay and extracts the **Spectral Exponent ($\beta$)** to classify the "texture" of the data's variance.

* **White Noise ($\beta \approx 0$):** Pure, uncorrelated randomness. Every event is completely independent of the past.
* **Pink Noise ($\beta \approx 1$):** Fractal, long-memory processes. The hallmark of complex human and organic systems.
* **Brown Noise ($\beta \approx 2$):** A random walk. Highly correlated short-term movements, but drifting aimlessly over the long term.

![005_2_1__fractal_noise_spectrum](../readme_plots/005_2_1_fractal_noise_spectrum.png)

### The Ultimate Fabrication Detector
Humans are notoriously terrible at generating true random variance. If an accountant manually fabricates thousands of fake ledger entries to hide a loss, or if a crude random number generator is used to pad a dataset, the resulting data will mathematically collapse into "White Noise." Or, if an automated script pumps identical amounts daily, it forms unnatural, rigid spikes.

By mapping the fractal dimensionality of the network, TLU catches data fabrication not by looking at the total *amounts* (which can be easily forged to balance the books), but by proving that the *texture* of the numbers' fluctuation is physically impossible for a group of humans to have generated naturally. 

---

## 4. Business Implications

By utilizing Signal Processing and Wave Mechanics, analysts can definitively answer:

1. **Are automated bots tampering with our system?** (Spikes in unnatural Resonant Frequencies).
2. **Is our cash conversion cycle secretly slowing down?** (Stretching/shifting color bands in the Phase Drift Heatmap indicating severe process friction).
3. **Has this ledger been artificially fabricated?** (The collapse of organic Pink Noise into artificial White Noise).
