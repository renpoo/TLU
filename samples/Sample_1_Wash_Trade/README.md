# Sample 1: Wash Trade

## Dataset Overview
This dataset introduces a specific anomaly: **Wash Trades (meaningless cyclical transactions among group companies or specific departments)**.

- **Wash Trade**: 1.0% probability
- **Embezzlement / Leaks**: 0%
- **Unbalanced Journal Entries**: 0%

Wash trades are often executed to artificially inflate "fictitious sales." Because the debits and credits of these transactions match perfectly, they are extremely difficult to detect using traditional anomaly detection (outlier detection) or simple aggregations.

## TLU Analysis Results (What to look for)

TLU detects this "abnormal loop of funds within the ledger" as an anomaly in the **network topology**, analyzed from the perspective of Control Theory.

### Key Graphs to Check
**▶ System Stability (Control Theory)**
- `004_1_2__system_stability.png`

### Why can TLU detect this? (Physical Interpretation)
TLU treats the ledger network as a matrix and computes its "Eigenvalues."
When an infinite "money-spinning loop" is formed within the network, the system becomes highly prone to oscillation (infinite amplification) along that loop. This "tendency to oscillate" is represented by the **maximum eigenvalue (Spectral Radius)** of the matrix.

Looking at the graph, the Spectral Radius normally stabilizes around `0.6` (as seen in the Healthy baseline). However, the moment a Wash Trade occurs, the radius **spikes sharply toward `1.0` (the critical limit of instability)**.
The system captures the mathematical structural change—"an artificial feedback loop was created in the graph topology"—regardless of the monetary amount involved.
