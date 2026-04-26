# TLU System CAUTION: Mathematical Boundary Effects (Edge Effects)

When analyzing aggregated time-series data with the TLU (Tensor-Link Utility) system, it is crucial to understand that **strong mathematical and physical distortions (Edge Effects) inherently occur at both boundaries (the start and the end) of the observation window.**

These distortions are **not bugs specific to stream processing or the TLU system itself.** They are universal mathematical principles encountered whenever a causal system with time lags is constrained within a finite observation window.

Please keep the following characteristics in mind when interpreting analysis results, anomaly scores, and visualization graphs.

---

## 1. The Left Edge: Mathematical Degeneration (Burn-in Period)

**[Scope]: $t=0, t=1$ (The first 1-2 months of the aggregation period)**

### Phenomenon

At the very beginning of the aggregation period, external forces ($F_{ext}$) may artificially lock to unnatural constants (e.g., $\pm 2.0$) regardless of the actual financial scale. Additionally, parameters like viscosity and acceleration may fail to calculate properly.

### Root Cause (Degeneration due to missing past)

This is a universal problem for any algorithm that calculates rates of change (derivatives/differentials). TLU computes velocity and acceleration using backward differences (comparing the present to the past). At $t=0$ and $t=1$, there is insufficient historical data. Specifically at $t=1$, the variance of a 2-point velocity history mathematically degenerates, causing the viscosity coefficient to overfit perfectly, artificially canceling out the financial scale.

### Action / Interpretation

* **Completely ignore anomaly scores and extreme metric fluctuations during the first 2-3 months (Burn-in period).**
* This period must be treated as a "warm-up phase" necessary for the engine to accumulate enough historical memory to stabilize the phase space topology.

---

## 2. The Right Edge: Right-Censoring of Causality

**[Scope]: The latest 1-3 months (or the terminal end of any bounded dataset)**

### Phenomenon

Near the end of the aggregation period (or the "present" month in real-time streams), Principal Component Analysis (PCA) eigenvalues may explode to massive values, Macro Forensics Z-Scores may spike abnormally, and Lag Matrix correlations may completely collapse.

### Root Cause (Fracture of causality due to unobserved futures)

In double-entry bookkeeping and real-world economics, there is always a time lag between a "Cause" (e.g., generating Sales/Accounts Receivable) and its "Effect" (e.g., Cash Collection).
Whenever an observation window is cut off (whether it's "Today" in a real-time stream, or "December 31st" in a batch dataset), this causality is forcefully severed. The cause exists within the data, but the effect belongs to the unobserved future.
TLU does not cheat by peeking into the future or smoothing over missing data. Instead, it mathematically evaluates this severed causality exactly as it is: **a massive structural fault line (strain) between two accounts (e.g., Cash and Accounts Payable).**

### Action / Interpretation

* **A massive anomaly score at the latest month does not immediately indicate "fraud" or "bankruptcy."**
* It is a mathematically accurate visualization of **"Future Uncertainty" (Risk)** caused by unresolved lags (uncollected cash, unpaid bills) resting exactly on the boundary.
* Analysts must mentally discount these terminal spikes as "Right-Censored Noise" or apply accrual-based adjustments in their interpretation, recognizing that the system's causal loops have not yet landed.

---

## Conclusion

The TLU engine does not artificially smooth data to make charts look pretty. It is a strict physical engine that exposes the structural uncertainty inherent in finite data.
By understanding the "Left Edge Warm-up" and the "Right Edge Unresolved Future," analysts can safely filter out mathematical boundary artifacts and focus on extracting true systemic anomalies from the stable core of the timeline.
