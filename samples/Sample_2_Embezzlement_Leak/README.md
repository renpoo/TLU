# Sample 2: Embezzlement Leak (Sales / Purchase Concealment)

## Dataset Overview
This dataset contains anomalies where funds that should naturally flow into the network (ledger) are **intentionally concealed and leaked to the outside (e.g., embezzlement)**.

- **Sales Leak (Concealment)**: 1.0% probability
- **Purchase Leak (Concealment)**: 1.0% probability
- **Wash Trade**: 0%
- **Unbalanced Journal Entries**: 0%

Because the perpetrators manipulate the debits and credits to match, the accounting system raises no syntax errors. However, this causes a depletion of the "blood" (cash) required for the corporate network to function.

## TLU Analysis Results (What to look for)

TLU visualizes this "depletion of energy necessary for corporate activities" through the lens of **Thermodynamics**.

### Key Graphs to Check
**▶ Thermodynamics (Free Energy)**
- `001_1_3__thermodynamics_ts_diagram.png`

**▶ Micro Forensics (Local Singularities)**
- `002_2_2_2__micro_Z_Score_heatmap.png`

### Why can TLU detect this? (Physical Interpretation)
TLU classifies transactions between nodes into "Heat" and "Work" and calculates the "Free Energy ($F$)" of the entire system. Free Energy represents the system's "remaining capacity to perform the next action (work)."

When a Leak occurs, the transaction volume and activity (Temperature) remain high, but the actual available funds plummet. As a result, the **Free Energy graph in the bottom right sinks below the zero baseline into the "negative zone (red)"**.
This accurately captures the hidden pathology of a corporation: "On the surface, sales and activities appear vibrant, but internally, the energy is completely depleted, and the system is heading toward structural death."
Simultaneously, the Micro Forensics Z-Score heatmap reveals "highly localized abnormal spikes" in the specific departments where the concealment took place.
