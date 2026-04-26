# Sample 1: Wash Trade

## Dataset Overview
This dataset introduces a specific anomaly: **Wash Trades (meaningless cyclical transactions among group companies or specific departments)**.

- **Wash Trade**: 1.0% probability
- **Embezzlement / Leaks**: 0%
- **Unbalanced Journal Entries**: 0%

Wash trades are often executed to artificially inflate "fictitious sales." Because the debits and credits of these transactions match perfectly, they are extremely difficult to detect using traditional anomaly detection (outlier detection) or simple aggregations.

## How to Visualize
To keep the repository lightweight, pre-rendered graph images (.png) are excluded. You can generate the full suite of visualizations for this specific dataset by running the following command from the project root:
```bash
bash bin/batch_visualize_graphs.sh --target_env samples/Sample_1_Wash_Trade
```
The generated graphs will be saved in the `samples/Sample_1_Wash_Trade/output_plots/` directory.

## TLU Analysis Results (What to look for)

TLU detects this "abnormal loop of funds within the ledger" as an anomaly in the **network topology**, analyzed from the perspective of Control Theory.

### Key Metrics to Check
**▶ System Stability (Control Theory)**
- **Data**: `output_data/004_1_2__system_stability.csv`
- **Graph**: `output_plots/004_1_2__system_stability.png` (if generated)

### Why can TLU detect this? (Physical Interpretation)
TLU treats the ledger network as a matrix and computes its "Eigenvalues."
When an infinite "money-spinning loop" is formed within the network, the system becomes highly prone to oscillation (infinite amplification) along that loop. This "tendency to oscillate" is represented by the **maximum eigenvalue (Spectral Radius)** of the matrix.

Looking at the data, the `spectral_radius` normally stabilizes around `0.6` (as seen in the Healthy baseline). However, the moment a Wash Trade occurs, the value **spikes sharply toward `1.0` (the critical limit of instability)**.
The system captures the mathematical structural change—"an artificial feedback loop was created in the graph topology"—regardless of the monetary amount involved.
