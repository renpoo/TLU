# 003_2. Multi-Order Jacobian & Trajectory Sensitivity

## 🔬 Multi-Order Jacobian Physical Mathematics Theory

TLU utilizes "Multi-Order Jacobians" to analyze structural sensitivity across distinct network connections (hop counts), expanding the traditional Jacobian matrix ($J$) which describes the relationship between small joint angle adjustments and end-effector position changes.

$$J^{(1)} = \gamma P$$
$$J^{(2)} = \gamma^2 P^2$$
$$J^{(3)} = \gamma^3 P^3$$

Where $P$ is the network transition probability matrix, and $\gamma$ is the damping factor.

1. **1st-Order ($J^{(1)}$):** Sensitivity across direct adjacent connections (1-hop transactions, neighbor intersections, direct synapses).
2. **2nd-Order ($J^{(2)}$):** Sensitivity across 1-hop indirect paths containing one intermediate broker node (e.g., shell corporations, transit intersections).
3. **3rd-Order ($J^{(3)}$):** Sensitivity across 2-hop indirect paths (e.g., multi-hop detours).

### 📊 Structural Topology Diagnostic Values
* **Wash Trade Detection (Even-Odd Alternating Coherence):**
  Occurs when self-sensitivity $J^{(k)}[i, i]$ spikes exclusively at even orders (e.g., $k=2$) but drops to exactly zero at odd orders (e.g., $k=1, 3$), where it instead targets a counterpart node. This is a mathematical fingerprint of circular sham trading.
* **Leak Audit (Terminal Sink / Jing-Well Node):**
  Identified when a node displays non-zero sensitivity in 1st and 2nd orders but drops to exactly `0.0` in 3rd order. It absorbs system mass without re-propagating it (e.g., embezzlement offshore leak).
* **Structural Gridlock ($\rho \ge 1.0$):**
  Indicated when sensitivities fail to decay as the order increases (1st → 2nd → 3rd) and instead saturate uniformly across the network. The maximum spectral radius $\rho$ locks at `1.0000`, making all nodes behave as a single rigid body (e.g., traffic deadlocks, seizure hyper-synchrony).

---

## 📊 Multi-Order Jacobian Analysis Results

This section outlines the order-wise Jacobian heatmap analysis results (`jacobian_order_1st.t*.png`, `2nd`, `3rd`) across the 10 validation samples.

### 🟢 Sample 0 (Healthy)
* **Order-wise Jacobian:** Sensitivity matrices decay rapidly as the order increases (1st → 2nd → 3rd). No circular loops or terminal sinks are detected, validating a healthy, decentralized circulation.

### 🟡 Sample 1 (Wash Trade)
* **Order-wise Jacobian:** Shows strong self-sensitivity $J^{(2)}[i,i]$ at even-orders (2nd-order) on the `Cash` ↔ `Accounts_Receivable` diagonal, while reverting to zero at odd-orders (1st and 3rd) where it targets the counterpart node (Even-Odd Alternating Coherence). This mathematically exposes the two-step circular trade loop.

### 🔴 Sample 2 (Embezzlement Leak)
* **Order-wise Jacobian:** Strong one-way sensitivity from Cash to `UNKNOWN_LEAK` exists in 1st and 2nd orders. In 3rd-order, the sensitivity originating from `UNKNOWN_LEAK` drops to exactly `0.0` (Terminal Sink), confirming off-book siphon behavior.

### 🟡 Sample 3 (Unbalanced Mistake)
* **Order-wise Jacobian:** An asymmetric sensitivity noise appears briefly between the affected journal accounts at the error step (t=1), but decays instantly in the next step (t=2), demonstrating transient imbalance and recovery.

### 🔴 Sample 4 (Composite Chaos)
* **Order-wise Jacobian:** Displays even-order wash trade coherence in the 2nd-order map, coupled with one-way sink absorption to `UNKNOWN_LEAK` in the 3rd-order map. This mathematically confirms the coexistence of circular trading and active embezzlement.

### 🔴 Sample 5 (Kyoto Traffic)
* **Order-wise Jacobian:** Due to the spectral radius $\rho = 1.0$ saturation, sensitivity values do not decay. The 3rd-order map remains saturated (white) across almost all node pairs, proving that a local bottleneck at Shijo-Karasuma propagates eternally as a gridlock wave.

### 🟢 Sample 6 (Market Stock Flow) & 🟢 Sample 7 (Market Cash Flow)
* **Order-wise Jacobian:** Order execution and cash settlement sensitivities decay smoothly as the hop count increases. No locking loops or sinks exist, indicating a healthy, decentralized distribution.

### 🔴 Sample 8 (fMRI Stroke)
* **Order-wise Jacobian:** Sensitivity in the motor cortex (`Motor_Cortex`) drops to zero in the 1st-order map due to the stroke onset (t=30). No sensitivity is restored in 2nd or 3rd orders, showing localized path block and signal sink.

### 🔴 Sample 9 (fMRI Seizure)
* **Order-wise Jacobian:** Saturated sensitivity is maintained without decay from 1st to 3rd orders due to the spectral radius $\rho = 1.0$位相同期. The network behaves as a single rigid body, proving that the brain is locked in a hyper-synchronous epileptic state.
