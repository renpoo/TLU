# Sample 3: Unbalanced Mistake

## Dataset Overview
This dataset contains anomalies where the **Debit and Credit amounts of a journal entry do not match**, typically caused by human input errors or system glitches.

- **Unbalanced Mistake**: 1.0% probability
- **Wash Trade**: 0%
- **Embezzlement / Leaks**: 0%

The fundamental principle of double-entry bookkeeping, "balance," is broken. From the system's perspective, funds have either "disappeared into the void outside the ledger" or "materialized out of nowhere." In conventional ETL or aggregation systems, these unbalanced entries are often discarded as errors and silently "laundered" away.

## How to Visualize
To keep the repository lightweight, pre-rendered graph images (.png) are excluded. You can generate the full suite of visualizations for this specific dataset by running the following command from the project root:
```bash
bash bin/batch_visualize_graphs.sh --target_env samples/Sample_3_Unbalanced_Mistake
```
The generated graphs will be saved in the `samples/Sample_3_Unbalanced_Mistake/output_plots/` directory.

## TLU Analysis Results (What to look for)

TLU adopts an "Open System (a system with boundary conditions)" physical model. By treating these "disappearing amounts" as flows to a special virtual node (`UNKNOWN_LEAK`), TLU flawlessly detects them as **violations of the Law of Mass Conservation**.

### Key Metrics to Check
**▶ Macro Forensics (Conservation Law)**
- **Data**: `output_data/002_2_1__macro_forensics.csv`
- **Graph**: `output_plots/002_2_1__macro_forensics_dashboard.png` (if generated)

### Why can TLU detect this? (Physical Interpretation)
TLU calculates the net inflow (Flux) of the entire network for each period. In a closed system, one node's gain is exactly another node's loss, so the total sum must always be exactly "zero." This is the First Law of Physics (**Law of Mass Conservation / Kirchhoff's Current Law**).

Observe the `conservation_residual` in the data.
During normal periods, it is perfectly `0.0`. However, in the exact weeks where unbalanced mistakes occur, **it sharply spikes up (or down) from zero**. This is not a "statistical outlier" like a Z-Score, but a "deterministic error" indicating a breakdown of physical laws, accurately capturing the leaked amount down to the last cent.
