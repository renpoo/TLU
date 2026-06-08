# 000_1. Dynamics & State-Space

This guide explains kinematics in Tensor-Link Utility (TLU).

---

## 000_1: Kinematics & State-Space

### 5. 3D Trajectory Ribbon & Phase Portrait Plots (e.g., `000_1_8__phase_portrait_3d.png`)

These plots display 3D phase-space trajectories constructed from position $X$, velocity $\dot{X}$, and acceleration $\ddot{X}$, or 3D dynamic properties under external force (`000_1_6__3d_dynamics_external_force.png`). We use them to determine dynamic stability and chaos.

#### 🟢 Sample 0 (Healthy Metabolism)

**Clinical Interpretation:**
The trajectory ribbon converges to a stable attractor (limit cycle). The system elastically absorbs external shocks to maintain a steady orbit. Time-series changes and 3D phase trajectories remain regular.

- ![Sample 0 Dynamics Position](Sample_0_Healthy/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 0 Dynamics Velocity](Sample_0_Healthy/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 0 Dynamics Acceleration](Sample_0_Healthy/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 0 Phase Portrait](Sample_0_Healthy/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 0 Dynamics External Force](Sample_0_Healthy/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟡 Sample 1 (Wash Trade)

**Clinical Interpretation:**
The trajectory ribbon loses multi-dimensional volume. It collapses into flat, 2D back-and-forth cycles. This indicates a severe loss of degrees of freedom (loop lock).

- ![Sample 1 Dynamics Position](Sample_1_Wash_Trade/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 1 Dynamics Velocity](Sample_1_Wash_Trade/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 1 Dynamics Acceleration](Sample_1_Wash_Trade/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 1 Phase Portrait](Sample_1_Wash_Trade/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 1 Dynamics External Force](Sample_1_Wash_Trade/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 2 (Embezzlement Leak)

**Clinical Interpretation:**
Active mass within the system is lost due to cash leaks. Connection stiffness collapses, causing pathological resonance under external excitation. The phase space loses smooth attractor paths and distorts.

- ![Sample 2 Dynamics Position](Sample_2_Embezzlement_Leak/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 2 Dynamics Velocity](Sample_2_Embezzlement_Leak/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 2 Dynamics Acceleration](Sample_2_Embezzlement_Leak/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 2 Phase Portrait](Sample_2_Embezzlement_Leak/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 2 Dynamics External Force](Sample_2_Embezzlement_Leak/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟡 Sample 3 (Unbalanced Bookkeeping Mistake)

**Clinical Interpretation:**
The trajectory is knocked away from equilibrium at the moment of the bookkeeping error. Since there is no pathological structure, it self-heals back to the healthy attractor in the next period. Sharp fluctuations appear in position, velocity, and acceleration. A temporary loop is logged in phase space.

- ![Sample 3 Dynamics Position](Sample_3_Unbalanced_Mistake/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 3 Dynamics Velocity](Sample_3_Unbalanced_Mistake/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 3 Dynamics Acceleration](Sample_3_Unbalanced_Mistake/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 3 Phase Portrait](Sample_3_Unbalanced_Mistake/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 3 Dynamics External Force](Sample_3_Unbalanced_Mistake/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 4 (Composite Chaos)

**Clinical Interpretation:**
Forced synchronization from circular trades and mass dissipation from embezzlement occur together. The attractor collapses, and the trajectory enters chaotic, infinite divergence. Position, velocity, and acceleration diverge step by step. The phase space trajectory shows a non-closing spiral.

- ![Sample 4 Dynamics Position](Sample_4_Composite_Chaos/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 4 Dynamics Velocity](Sample_4_Composite_Chaos/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 4 Dynamics Acceleration](Sample_4_Composite_Chaos/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 4 Phase Portrait](Sample_4_Composite_Chaos/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 4 Dynamics External Force](Sample_4_Composite_Chaos/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 5 (Kyoto Traffic)

**Clinical Interpretation:**
Intersection capacity saturates (viscous damping becomes infinite). The trajectory freezes on a singular plane, indicating a traffic deadlock. Position, velocity, and acceleration converge to fixed values. The phase space trajectory is sucked into a single fixed point.

- ![Sample 5 Dynamics Position](Sample_5_Kyoto_Traffic/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 5 Dynamics Velocity](Sample_5_Kyoto_Traffic/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 5 Dynamics Acceleration](Sample_5_Kyoto_Traffic/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 5 Phase Portrait](Sample_5_Kyoto_Traffic/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 5 Dynamics External Force](Sample_5_Kyoto_Traffic/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟢 Sample 6 (Market Stock Flow)

**Clinical Interpretation:**
Stable stock convection in the stock market. Viscosity and inertia balance, and position, velocity, and acceleration tie together smoothly. A closed, 3D limit cycle is maintained in phase space.

- ![Sample 6 Dynamics Position](Sample_6_Market_Stock_Flow/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 6 Dynamics Velocity](Sample_6_Market_Stock_Flow/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 6 Dynamics Acceleration](Sample_6_Market_Stock_Flow/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 6 Phase Portrait](Sample_6_Market_Stock_Flow/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 6 Dynamics External Force](Sample_6_Market_Stock_Flow/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🟢 Sample 7 (Market Cash Flow)

**Clinical Interpretation:**
Cash convection within the market network. Steady cash flows minimize frictional heat. The system elastically recovers from sudden shocks. Time-series changes are periodic. The phase space shows a harmonized, compact attractor.

- ![Sample 7 Dynamics Position](Sample_7_Market_Cash_Flow/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 7 Dynamics Velocity](Sample_7_Market_Cash_Flow/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 7 Dynamics Acceleration](Sample_7_Market_Cash_Flow/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 7 Phase Portrait](Sample_7_Market_Cash_Flow/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 7 Dynamics External Force](Sample_7_Market_Cash_Flow/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 8 (fMRI Stroke)

**Clinical Interpretation:**
At the stroke onset ( $t=30$ ), active mass in the motor cortex vanishes. The trajectory jumps discontinuously (phase transition) to a lower functioning attractor. The collapse and reshaping of the attractor are captured across position, velocity, acceleration, and 3D phase space plots.

- ![Sample 8 Dynamics Position](Sample_8_fMRI_Stroke/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 8 Dynamics Velocity](Sample_8_fMRI_Stroke/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 8 Dynamics Acceleration](Sample_8_fMRI_Stroke/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 8 Phase Portrait](Sample_8_fMRI_Stroke/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 8 Dynamics External Force](Sample_8_fMRI_Stroke/readme_plots/000_1_6__3d_dynamics_external_force.png)

#### 🔴 Sample 9 (fMRI Seizure)

**Clinical Interpretation:**
The entire brain is hijacked by abnormal frequencies. The 3D trajectory ribbon loses complexity and freezes into a simple circular orbit (hyper-synchrony). Position, velocity, acceleration, and 3D phase space plots show abnormal regularity and lack of complexity.

- ![Sample 9 Dynamics Position](Sample_9_fMRI_Seizure/readme_plots/000_1_1__3d_dynamics_position.png)
- ![Sample 9 Dynamics Velocity](Sample_9_fMRI_Seizure/readme_plots/000_1_2__3d_dynamics_velocity.png)
- ![Sample 9 Dynamics Acceleration](Sample_9_fMRI_Seizure/readme_plots/000_1_3__3d_dynamics_acceleration.png)
- ![Sample 9 Phase Portrait](Sample_9_fMRI_Seizure/readme_plots/000_1_8__phase_portrait_3d.png)
- ![Sample 9 Dynamics External Force](Sample_9_fMRI_Seizure/readme_plots/000_1_6__3d_dynamics_external_force.png)
