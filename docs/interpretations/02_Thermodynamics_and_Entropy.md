# 02. Thermodynamics & Entropy (Phase 1.5 - 1.6)

This phase applies statistical mechanics to the financial ledger. It treats money as "energy" and measures how efficiently the organization uses that energy (Work) versus how much is lost to chaos, friction, or poor processes (Entropy/Heat).

---

### 1. Thermodynamics Dashboard (`001_1_1__thermodynamics_dashboard.png`)

* **📊 Visual Structure**: A multi-panel dashboard. Key panels include the T-S (Temperature vs. Entropy) diagram and the Global Free Energy trend line.
* **📐 Physics Theory**: Calculates Helmholtz Free Energy ($F = U - TS$). It measures the "useful" monetary energy available to do actual business work, minus the energy lost to systemic chaos ($T \times S$).
* **🚨 Anomaly Detection**: 
  * Look at the Free Energy ($F$) line. A sudden, sharp drop.
  * Look at the Entropy ($S$) line. A sustained, inexplicable rise.
* **💼 Business Translation**: **Severe Operational Inefficiency**. The organization is burning cash, but that cash is not generating structured returns. Instead, the money is scattering randomly across the network (e.g., panicked uncoordinated spending, rampant unstructured expenses, or embezzlement).

### 2. T-S Diagram (`001_1_1__thermodynamics_ts_diagram.png`)

* **📊 Visual Structure**: A scatter plot where the X-axis is Entropy ($S$) and the Y-axis is Temperature ($T$). 
* **📐 Physics Theory**: Visualizes the thermodynamic state of the system over time. Temperature represents the "volatility" or magnitude of transaction fluctuations.
* **🚨 Anomaly Detection**: 
  * The trajectory drifts heavily into the **Upper-Right Quadrant** (High Temperature, High Entropy).
* **💼 Business Translation**: The business is highly volatile AND highly chaotic. Transactions are large and erratic, with no discernible structured process. This is the signature of a company losing control of its finances.

### 3. Local Thermodynamics (`001_2_1__local_thermodynamics_dashboard.png`)

* **📊 Visual Structure**: A bar chart or heatmap breaking down the Free Energy and Entropy *per specific account* (local nodes).
* **📐 Physics Theory**: Maps the global thermodynamic waste down to the specific nodes generating the heat.
* **🚨 Anomaly Detection**: 
  * A specific account (e.g., `ACC_Travel_Exp` or `ACC_Accounts_Payable`) showing a massive, disproportionate red bar (High Local Entropy).
* **💼 Business Translation**: **Pinpointing the Leak**. While the Global dashboard tells you the company is bleeding efficiency, this local dashboard tells you *exactly which department or account* is causing the chaos. It highlights where internal controls have completely failed.

### 4. Lag Matrix Heatmap (`001_2_2__lag_matrix_heatmap.png`)

* **📊 Visual Structure**: A matrix showing the correlation/time-lag relationship between accounts.
* **📐 Physics Theory**: Calculates the delayed response (temporal memory) of the network.
* **🚨 Anomaly Detection**: 
  * A breakdown or blurring of historically clear correlation patterns.
* **💼 Business Translation**: **Broken causal chains**. For example, if Cash usually closely follows Accounts Receivable (with a short lag), but the matrix suddenly shows no correlation, it means the collections process has detached from reality. Cash is no longer reliably following sales.
