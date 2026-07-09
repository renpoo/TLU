# 000_1. Dynamics & State-Space

This guide explains kinematics in Tensor-Link Utility (TLU).

---

## 000_1: Kinematics & State-Space

### 5. 3D Trajectory Ribbon & Phase Portrait Plots (e.g., `000_1_8__phase_portrait_3d.png`)

These plots display 3D phase-space trajectories constructed from position $X, velocity $\dot{X}, and acceleration $\ddot{X}, or 3D dynamic properties under external force (`000_1_6__3d_dynamics_external_force.png`). We use them to determine dynamic stability and chaos.

#### 🟢 Sample 0 (Healthy Metabolism)

**Clinical Interpretation:**
The trajectory ribbon converges to a stable attractor (limit cycle). The system elastically absorbs external shocks to maintain a steady orbit. Time-series changes and 3D phase trajectories remain regular.

- ![Sample 0 Dynamics Position](../../samples/Sample_0_Healthy/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 0 Dynamics Velocity](../../samples/Sample_0_Healthy/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 0 Dynamics Acceleration](../../samples/Sample_0_Healthy/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 0 Phase Portrait](../../samples/Sample_0_Healthy/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 0 Dynamics External Force](../../samples/Sample_0_Healthy/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟡 Sample 1 (Wash Trade)

**Clinical Interpretation:**
The trajectory ribbon loses multi-dimensional volume. It collapses into flat, 2D back-and-forth cycles. This indicates a severe loss of degrees of freedom (loop lock).

- ![Sample 1 Dynamics Position](../../samples/Sample_1_Wash_Trade/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 1 Dynamics Velocity](../../samples/Sample_1_Wash_Trade/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 1 Dynamics Acceleration](../../samples/Sample_1_Wash_Trade/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 1 Phase Portrait](../../samples/Sample_1_Wash_Trade/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 1 Dynamics External Force](../../samples/Sample_1_Wash_Trade/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 2 (Embezzlement Leak)

**Clinical Interpretation:**
Active mass within the system is lost due to cash leaks. Connection stiffness collapses, causing pathological resonance under external excitation. The phase space loses smooth attractor paths and distorts.

- ![Sample 2 Dynamics Position](../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 2 Dynamics Velocity](../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 2 Dynamics Acceleration](../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 2 Phase Portrait](../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 2 Dynamics External Force](../../samples/Sample_2_Embezzlement_Leak/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟡 Sample 3 (Unbalanced Bookkeeping Mistake)

**Clinical Interpretation:**
The trajectory is knocked away from equilibrium at the moment of the bookkeeping error. Since there is no pathological structure, it self-heals back to the healthy attractor in the next period. Sharp fluctuations appear in position, velocity, and acceleration. A temporary loop is logged in phase space.

- ![Sample 3 Dynamics Position](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 3 Dynamics Velocity](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 3 Dynamics Acceleration](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 3 Phase Portrait](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 3 Dynamics External Force](../../samples/Sample_3_Unbalanced_Mistake/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 4 (Composite Chaos)

**Clinical Interpretation:**
Forced synchronization from circular trades and mass dissipation from embezzlement occur together. The attractor collapses, and the trajectory enters chaotic, infinite divergence. Position, velocity, and acceleration diverge step by step. The phase space trajectory shows a non-closing spiral.

- ![Sample 4 Dynamics Position](../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 4 Dynamics Velocity](../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 4 Dynamics Acceleration](../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 4 Phase Portrait](../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 4 Dynamics External Force](../../samples/Sample_4_Composite_Chaos/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 5 (Kyoto Traffic)

**Clinical Interpretation:**
Intersection capacity saturates (viscous damping becomes infinite). The trajectory freezes on a singular plane, indicating a traffic deadlock. Position, velocity, and acceleration converge to fixed values. The phase space trajectory is sucked into a single fixed point.

- ![Sample 5 Dynamics Position](../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 5 Dynamics Velocity](../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 5 Dynamics Acceleration](../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 5 Phase Portrait](../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 5 Dynamics External Force](../../samples/Sample_5_Kyoto_Traffic/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟢 Sample 6 (Market Stock Flow)

**Clinical Interpretation:**
Stable stock convection in the stock market. Viscosity and inertia balance, and position, velocity, and acceleration tie together smoothly. A closed, 3D limit cycle is maintained in phase space.

- ![Sample 6 Dynamics Position](../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 6 Dynamics Velocity](../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 6 Dynamics Acceleration](../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 6 Phase Portrait](../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 6 Dynamics External Force](../../samples/Sample_6_Market_Stock_Flow/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟢 Sample 7 (Market Cash Flow)

**Clinical Interpretation:**
Cash convection within the market network. Steady cash flows minimize frictional heat. The system elastically recovers from sudden shocks. Time-series changes are periodic. The phase space shows a harmonized, compact attractor.

- ![Sample 7 Dynamics Position](../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 7 Dynamics Velocity](../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 7 Dynamics Acceleration](../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 7 Phase Portrait](../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 7 Dynamics External Force](../../samples/Sample_7_Market_Cash_Flow/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 8 (fMRI Stroke)

**Clinical Interpretation:**
At the stroke onset ( $t=30$ ), active mass in the motor cortex vanishes. The trajectory jumps discontinuously (phase transition) to a lower functioning attractor. The collapse and reshaping of the attractor are captured across position, velocity, acceleration, and 3D phase space plots.

- ![Sample 8 Dynamics Position](../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 8 Dynamics Velocity](../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 8 Dynamics Acceleration](../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 8 Phase Portrait](../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 8 Dynamics External Force](../../samples/Sample_8_fMRI_Stroke/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 9 (fMRI Seizure)

**Clinical Interpretation:**
The entire brain is hijacked by abnormal frequencies. The 3D trajectory ribbon loses complexity and freezes into a simple circular orbit (hyper-synchrony). Position, velocity, acceleration, and 3D phase space plots show abnormal regularity and lack of complexity.

- ![Sample 9 Dynamics Position](../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 9 Dynamics Velocity](../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 9 Dynamics Acceleration](../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 9 Phase Portrait](../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 9 Dynamics External Force](../../samples/Sample_9_fMRI_Seizure/readme_plots/000_1_6__3d_dynamics_external_force.png)

---

### 6. Jerk and Snap Time-Series Trends (`000_1_9__3d_dynamics_jerk.png` / `000_1_10__3d_dynamics_snap.png`)

Jerk (rate of change of acceleration $\dddot{X}$) and Snap (rate of change of Jerk $\ddddot{X}$) are higher-order derivative metrics used to capture sudden transitions (shocks) or transient high-frequency oscillations (knocking resonance) within the flow dynamics.

#### 🟢 Sample 0 (Healthy)
* **Clinical Interpretation:** Jerk and Snap remain completely flat (zero-mean stationary) across the entire timeline, proving the absence of abrupt transaction shocks or physical bottlenecks.

#### 🟡 Sample 1 (Wash Trade)
* **Clinical Interpretation:** Jerk and Snap exhibit narrow spike impulses at the exact moments the cyclic wash trades are synchronized or terminated, capturing the artificial flow direction reversal shock.

#### 🔴 Sample 2 (Embezzlement Leak)
* **Clinical Interpretation:** Significant Jerk and Snap impulses (deceleration shocks) spike at the start of the leak (t=4) and expand in the final steps as system mass depletes, indicating topological tearing.

#### 🟡 Sample 3 (Unbalanced Mistake)
* **Clinical Interpretation:** High-amplitude Jerk and Snap spikes appear strictly at t=1 (error injection) and t=2 (self-correction), proving a localized transient shock and prompt recovery.

#### 🔴 Sample 4 (Composite Chaos)
* **Clinical Interpretation:** Multi-frequency Jerk and Snap oscillations (system knocking) amplify from mid-to-late steps, signaling systemic resonance prior to final collapse.

#### 🔴 Sample 5 (Kyoto Traffic)
* **Clinical Interpretation:** Following the capacity restriction at t=12, sudden braking impulses (Jerk) and gridlock propagation ripples (Snap) spike persistently, freezing the urban traffic flow.

#### 🟢 Sample 6 (Market Stock Flow) & 🟢 Sample 7 (Market Cash Flow)
* **Clinical Interpretation:** Both Jerk and Snap remain flat and close to zero, validating that the order execution and cash settlements are smooth without sudden market panics.

#### 🔴 Sample 8 (fMRI Stroke)
* **Clinical Interpretation:** A massive Jerk deceleration shock spikes at the stroke onset (t=30) in the motor cortex, followed by transient Snap waves rippling through adjacent ROIs as the tissue deactivates.

#### 🔴 Sample 9 (fMRI Seizure)
* **Clinical Interpretation:** Post-onset (t=30), Jerk and Snap are locked into rigid, high-frequency sinusoidal oscillations, reflecting the synchronized, hyper-active firing pattern of epilepsy.

