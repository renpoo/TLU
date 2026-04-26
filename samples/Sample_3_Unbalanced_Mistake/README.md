# Sample 3: Unbalanced Mistake

## Dataset Overview
This dataset contains anomalies where the **Debit and Credit amounts of a journal entry do not match**, typically caused by human input errors or system glitches.

- **Unbalanced Mistake**: 1.0% probability
- **Wash Trade**: 0%
- **Embezzlement / Leaks**: 0%

The fundamental principle of double-entry bookkeeping, "balance," is broken. From the system's perspective, funds have either "disappeared into the void outside the ledger" or "materialized out of nowhere." In conventional ETL or aggregation systems, these unbalanced entries are often discarded as errors and silently "laundered" away.

## TLU Analysis Results (What to look for)

TLU adopts an "Open System (a system with boundary conditions)" physical model. By treating these "disappearing amounts" as flows to a special virtual node (`UNKNOWN_LEAK`), TLU flawlessly detects them as **violations of the Law of Mass Conservation**.

### Key Graphs to Check
**▶ Macro Forensics (Conservation Law)**
- `002_2_1__macro_forensics_dashboard.png`

### Why can TLU detect this? (Physical Interpretation)
TLU calculates the net inflow (Flux) of the entire network for each period. In a closed system, one node's gain is exactly another node's loss, so the total sum must always be exactly "zero." This is the First Law of Physics (**Law of Mass Conservation / Kirchhoff's Current Law**).

Observe the `Conservation Residual` at the top of the graph.
During normal periods, it is perfectly flat at `0.0`. However, in the exact weeks where unbalanced mistakes occur, **it sharply spikes up (or down) from the zero baseline**. This is not a "statistical outlier" like a Z-Score, but a "deterministic error" indicating a breakdown of physical laws, accurately capturing the leaked amount down to the last cent.
