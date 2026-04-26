# Sample 4: Composite Chaos (Real-World Scenario)

## Dataset Overview
This dataset simulates the **chaos of real-world ledgers**. All the anomalies explained previously are injected simultaneously at random intervals.

- **Wash Trade**: 0.5% probability
- **Sales Leak**: 0.5% probability
- **Purchase Leak**: 1.0% probability
- **Unbalanced Mistake**: 0.5% probability

When data is this chaotic, traditional anomaly detection models struggle to identify causality, simply flagging the entire dataset as "too noisy."

## How to Visualize
To keep the repository lightweight, pre-rendered graph images (.png) are excluded. You can generate the full suite of visualizations for this specific dataset by running the following command from the project root:
```bash
bash bin/batch_visualize_graphs.sh --target_env samples/Sample_4_Composite_Chaos
```
The generated graphs will be saved in the `samples/Sample_4_Composite_Chaos/output_plots/` directory.

## TLU Analysis Results (What to look for)

This sample demonstrates the true **dissection and discrimination capability** of TLU.
Even when all anomalies are mixed together, TLU's diverse physical filters perfectly isolate and capture each underlying pathology.

### 1. Extracting Mass Conservation Violations (Journaling Mistakes)
- **Data**: `output_data/002_2_1__macro_forensics.csv`
- **Graph**: `output_plots/002_2_1__macro_forensics_dashboard.png` (if generated)
- Regardless of what other anomalies are occurring, the exact moment a non-zero value appears in the `conservation_residual`, an "unbalanced debit/credit error" definitely exists. This metric is completely unaffected by other phenomena.

### 2. Extracting Topological Loops (Wash Trades)
- **Data**: `output_data/004_1_2__system_stability.csv`
- **Graph**: `output_plots/004_1_2__system_stability.png` (if generated)
- Whether funds are being concealed or journaling mistakes are happening, the `spectral_radius` spikes toward `1.0` *only* when an artificial "loop" is formed in the network.

### 3. Extracting Energy Depletion (Embezzlement / Leaks)
- **Data**: `output_data/001_1_1__macro_thermodynamics.csv`
- **Graph**: `output_plots/001_1_3__thermodynamics_ts_diagram.png` (if generated)
- While localized anomalies (like Z-Score spikes) occur throughout the system, the specific periods where the `Free_Energy_F` sinks into negative values indicate that "necessary operational funds are actively leaking to the outside."

### Conclusion
TLU is not a black-box model that spits out a single "anomaly score." By observing the numerical data through **multiple lenses of physics**, it elegantly untangles complex, intertwined pathologies—much like a doctor simultaneously analyzing MRI, ECG, and blood test results.
