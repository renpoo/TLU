# TLU Graph Interpretation Guides

> **"A translation layer between mathematical projection and business reality."**

TLU generates over 50 visualizations to capture the structural health of an organization. This directory serves as the official **Rosetta Stone**, providing a highly structured, visual guide for every single graph the system produces.

## How to Use These Guides

These guides are not meant to explain the deep mathematical formulas (for that, please refer to the `docs/physics/` manuals). Instead, these guides are designed for **analysts and end-users** who are looking at a `.png` file and asking:

1. **How do I read this visually?**
2. **What does an anomaly look like?**
3. **What does this mean for the actual business?**

## The Interpretation Directory

The guides are split by the logical Categories (000 - 005) of the Core Analysis (Phase 2) pipeline to prevent cognitive overload.

* **[Financial Statements (Category 000_0)](000_0_Financial_Statements.md)**: Your baseline. How to read the standard B/S and P/L before diving into physics.
* **[Classical Mechanics & Stiffness (Category 000)](000_Classical_Mechanics_and_Stiffness.md)**: Reading the 3D phase spaces of Velocity, Acceleration, and the Structural Stiffness matrices.
* **[Thermodynamics & Entropy (Category 001)](001_Thermodynamics_and_Entropy.md)**: Reading the T-S diagrams and Free Energy stacks.
* **[Info Geometry & Forensics (Category 002)](002_InfoGeometry_and_Forensics.md)**: Reading the Z-Score topologies and Network Manifolds.
* **[Applied Kinematics (Category 003)](003_Kinematics.md)**: Reading the FK and IK robotics simulations.
* **[Control Theory & Stability (Category 004)](004_ControlTheory_and_Stability.md)**: Reading the Spectral Radius and LQR Convergence.
* **[Signals & Noise (Category 005)](005_Signals_and_Noise.md)**: Reading the Phase Drift Heatmaps and Resonant Frequencies.

---

*Note: If you are an auditor or tax accountant, remember that you do not need to memorize these graphs. The AI Meta-Diagnosis Engine (`_99_meta_diagnosis.py`) automatically ingests these mathematical anomalies and translates them into a plain-text business report. Use these visual guides to manually verify the AI's findings.*
