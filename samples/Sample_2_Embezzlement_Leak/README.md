# Sample 2: Embezzlement Leak (Sales / Purchase Concealment)

## Dataset Overview
This dataset contains anomalies where funds that should naturally flow into the network (ledger) are **intentionally concealed and leaked to the outside (e.g., embezzlement)**.

- **Sales Leak (Concealment)**: 1.0% probability
- **Purchase Leak (Concealment)**: 1.0% probability
- **Wash Trade**: 0%
- **Unbalanced Journal Entries**: 0%

Because the perpetrators manipulate the debits and credits to match, the accounting system raises no syntax errors. However, this causes a depletion of the "blood" (cash) required for the corporate network to function.

## How to Visualize
To keep the repository lightweight, pre-rendered graph images (.png) are excluded. You can generate the full suite of visualizations for this specific dataset by running the following command from the project root:
```bash
bash bin/batch_visualize_graphs.sh --target_env samples/Sample_2_Embezzlement_Leak
```
The generated graphs will be saved in the `samples/Sample_2_Embezzlement_Leak/output_plots/` directory.

## TLU Analysis Results (What to look for)

TLU visualizes this "depletion of energy necessary for corporate activities" through the lens of **Thermodynamics**.

### Key Metrics to Check
**▶ Thermodynamics (Free Energy)**
- **Data**: `output_data/001_1_1__macro_thermodynamics.csv`
- **Graph**: `output_plots/001_1_3__thermodynamics_ts_diagram.png` (if generated)

**▶ Micro Forensics (Local Singularities)**
- **Data**: `output_data/002_2_2__micro_forensics.csv`
- **Graph**: `output_plots/002_2_2_2__micro_Z_Score_heatmap.png` (if generated)

### Why can TLU detect this? (Physical Interpretation)
TLU classifies transactions between nodes into "Heat" and "Work" and calculates the "Free Energy ($F$)" of the entire system. Free Energy represents the system's "remaining capacity to perform the next action (work)."

When a Leak occurs, the transaction volume and activity (Temperature) remain high, but the actual available funds plummet. As a result, the **`Free_Energy_F` sinks below the zero baseline into negative values**.
This accurately captures the hidden pathology of a corporation: "On the surface, sales and activities appear vibrant, but internally, the energy is completely depleted, and the system is heading toward structural death."
Simultaneously, the Micro Forensics data reveals "highly localized abnormal spikes" in the `Z_Score` for the specific departments where the concealment took place.
