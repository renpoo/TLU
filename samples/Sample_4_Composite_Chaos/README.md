# Sample 4: Composite Chaos (Real-World Scenario)

## Dataset Overview
This dataset simulates the **chaos of real-world ledgers**. All the anomalies explained previously are injected simultaneously at random intervals.

- **Wash Trade**: 0.5% probability
- **Sales Leak**: 0.5% probability
- **Purchase Leak**: 1.0% probability
- **Unbalanced Mistake**: 0.5% probability

When data is this chaotic, traditional anomaly detection models struggle to identify causality, simply flagging the entire dataset as "too noisy."

## TLU Analysis Results (What to look for)

This sample demonstrates the true **dissection and discrimination capability** of TLU.
Even when all anomalies are mixed together, TLU's diverse physical filters perfectly isolate and capture each underlying pathology.

### 1. Extracting Mass Conservation Violations (Journaling Mistakes)
- `002_2_1__macro_forensics_dashboard.png`
- Regardless of what other anomalies are occurring, the exact moment a spike appears in the `Conservation Residual` at the top, an "unbalanced debit/credit error" definitely exists. This metric is completely unaffected by other phenomena.

### 2. Extracting Topological Loops (Wash Trades)
- `004_1_2__system_stability.png`
- Whether funds are being concealed or journaling mistakes are happening, the `Spectral Radius` spikes toward `1.0` *only* when an artificial "loop" is formed in the network.

### 3. Extracting Energy Depletion (Embezzlement / Leaks)
- `001_1_3__thermodynamics_ts_diagram.png`
- While localized anomalies (like Z-Score spikes) occur throughout the system, the specific periods where the `Free Energy` (bottom right) sinks below the baseline indicate that "necessary operational funds are actively leaking to the outside."

### Conclusion
TLU is not a black-box model that spits out a single "anomaly score." By observing the data through **multiple lenses of physics**, it elegantly untangles complex, intertwined pathologies—much like a doctor simultaneously running an MRI, an ECG, and a blood test on a patient.
