# 04. Applied Kinematics (Phase 1.1 & 1.2)

Kinematics allows us to simulate the ripple effects of business decisions. By treating the accounting ledger as a robotic arm (where accounts are joints and money flow is the linkage), we can predict how injecting cash into one account will structurally move the rest of the organization.

---

### 1. 3D Kinematics: Forward (FK) (`003_1_1__3d_kinematics_fk.png`)

* **📊 Visual Structure**: A 3D spatial plot showing a network of interconnected points. The "Original State" is shown alongside the "Displaced State."
* **📐 Physics Theory**: Forward Kinematics. If I apply a known force (e.g., inject $1M into Sales), how will the rest of the accounts physically move and adjust based on their historical stiffness?
* **🚨 Anomaly Detection**: 
  * Look at the displacement vectors (arrows). If injecting cash into Sales causes an unexpectedly massive, violent displacement in a completely unrelated account.
* **💼 Business Translation**: **Simulating Interventions**. Use this to visually verify the "blast radius" of a business decision. If a marketing budget increase (Force) causes a chaotic ripple that destabilizes the Accounts Payable node, your organization's internal processes are too fragile to handle the growth.

### 2. 3D Kinematics: Inverse (IK) (`003_1_2__3d_kinematics_ik.png`)

* **📊 Visual Structure**: Similar to the FK plot, but working backward from a target destination.
* **📐 Physics Theory**: Inverse Kinematics via Gradient Descent. If I want the organization to reach a specific financial state (e.g., Net Income = $2M), what exact forces must I apply to the various input accounts to get there, while minimizing structural strain?
* **🚨 Anomaly Detection**: 
  * The IK solver fails to converge, or the resulting "required force" vectors are astronomically large.
* **💼 Business Translation**: **Reality Check on KPIs**. If management sets an aggressive target for next quarter, the IK engine simulates the required effort. If the required forces are impossibly huge, it mathematically proves that the management target is a fantasy and will break the organization's structure if attempted.
