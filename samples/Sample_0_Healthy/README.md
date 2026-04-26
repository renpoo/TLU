# Sample 0: Healthy (Baseline)

## Dataset Overview
This dataset serves as the baseline, containing **zero** intentional anomalies (fraud or mistakes).

- **Wash Trade**: 0%
- **Embezzlement / Leaks**: 0%
- **Unbalanced Journal Entries**: 0%

While it includes natural business seasonality (e.g., quarterly sales increases) and systemic pink noise, the physical and logical structure of the system is perfectly preserved.

## How to Visualize
To keep the repository lightweight, pre-rendered graph images (.png) are excluded. You can generate the full suite of visualizations for this specific dataset by running the following command from the project root:
```bash
bash bin/batch_visualize_graphs.sh --target_env samples/Sample_0_Healthy
```
The generated graphs will be saved in the `samples/Sample_0_Healthy/output_plots/` directory.

## TLU Analysis Results (What to look for)
This sample acts as a reference point to understand **what the data looks like when the system is completely healthy**.

1. **Macro Forensics (Law of Mass Conservation)**
   - **Data**: `output_data/002_2_1__macro_forensics.csv`
   - **Graph**: `output_plots/002_2_1__macro_forensics_dashboard.png` (if generated)
   - **Key Observation**: The `conservation_residual` is completely flat at `0.0`. This indicates that debits and credits match perfectly, and not a single cent has leaked out of the ledger.

2. **System Stability (Control Theory / Stability)**
   - **Data**: `output_data/004_1_2__system_stability.csv`
   - **Graph**: `output_plots/004_1_2__system_stability.png` (if generated)
   - **Key Observation**: The `spectral_radius` fluctuates between `0.5` and `0.8` but never reaches `1.0`. This means the network structure is healthy and there are no artificial infinite feedback loops (such as wash trades) present.

3. **Thermodynamics (Free Energy)**
   - **Data**: `output_data/001_1_1__macro_thermodynamics.csv`
   - **Graph**: `output_plots/001_1_3__thermodynamics_ts_diagram.png` (if generated)
   - **Key Observation**: The `Free_Energy_F` stably remains in the positive territory. This means the corporation has sufficient "capacity to perform work" (cash flow) to sustain its operations.
