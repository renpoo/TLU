# Sample 0: Healthy (Baseline)

## Dataset Overview
This dataset serves as the baseline, containing **zero** intentional anomalies (fraud or mistakes).

- **Wash Trade**: 0%
- **Embezzlement / Leaks**: 0%
- **Unbalanced Journal Entries**: 0%

While it includes natural business seasonality (e.g., quarterly sales increases) and systemic pink noise, the physical and logical structure of the system is perfectly preserved.

## TLU Analysis Results (What to look for)

This sample acts as a reference point to understand **what the graphs look like when the system is completely healthy**.

1. **Macro Forensics (Law of Mass Conservation)**
   - `002_2_1__macro_forensics_dashboard.png`
   - **Key Observation**: The `Conservation Residual` at the top of the dashboard is completely flat at `0.0`. This indicates that debits and credits match perfectly, and not a single cent has leaked out of the ledger.

2. **System Stability (Control Theory / Stability)**
   - `004_1_2__system_stability.png`
   - **Key Observation**: The Spectral Radius fluctuates between `0.5` and `0.8` but never reaches `1.0`. This means the network structure is healthy and there are no artificial infinite feedback loops (such as wash trades) present.

3. **Thermodynamics (Free Energy)**
   - `001_1_3__thermodynamics_ts_diagram.png`
   - **Key Observation**: The Free Energy ($F$) plot in the bottom right stably remains in the positive territory. This means the corporation has sufficient "capacity to perform work" (cash flow) to sustain its operations.
