# TLU Meta-Diagnosis Report (Descriptive Statistics V3)

**Target Environment:** `samples/Sample_7_Market_Cash_Flow`
**Date Analyzed:** 2026-07-06 07:18:02

## 1. Final Diagnosis

### 🟠 Topological Feedback Loop (Wash Trade / Resonance)
- **Severity:** HIGH
- **Evidence:** Max Spectral Radius: 1.0000.
- **Interpretation:** An artificial loop of funds or extreme resonance has formed in the network.

---
## 2. Comprehensive Descriptive Statistics Table

The table below details the descriptive statistics computed individually for all active analytical scales across the TLU mathematical modules:

| Measure / Scale | Mean | Median | Mode (count / total, %) | Min | Max | Range | IQR | Std Dev | Skewness | Kurtosis | Z-Exceed |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Dynamics: acceleration_a | 0.0000 | 0.0000 | 0.0000 (12/288, 4.2%) | -80055533.8300 | 75800079.0000 | 155855612.8300 | 1518155.4275 | 12847883.7815 | -0.1705 | 17.8639 | 13 |
| Dynamics: state_X | 113286439.6717 | 5148177.0600 | 15315870.0000 (2/288, 0.7%) | -189828.7400 | 676738389.8100 | 676928218.5500 | 107213577.3325 | 199394814.8487 | 1.8403 | 2.1118 | 0 |
| Dynamics: velocity_v | 0.0000 | 63349.4550 | -65981464.0000 (1/288, 0.3%) | -65981464.0400 | 67943130.8100 | 133924594.8500 | 1188295.0500 | 9145476.0798 | 0.2696 | 31.5154 | 8 |
| Dynamics: viscosity_C | 11328676.9235 | 483794.7314 | 4208.0200 (1/288, 0.3%) | 4208.0180 | 67673838.9810 | 67669630.9630 | 10409806.9815 | 19939076.1672 | 1.8564 | 2.1774 | 0 |
| Forensics: conservation_residual | 0.0000 | 0.0000 | 0.0000 (24/24, 100.0%) | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | nan | nan | 0 |
| Forensics: kl_divergence_drift | 12.0794 | 11.5775 | 0.0000 (1/24, 4.2%) | 0.0000 | 36.1212 | 36.1212 | 7.0521 | 8.1880 | 1.3003 | 1.9428 | 0 |
| Stability: spectral_radius | 0.9037 | 0.9874 | 0.9980 (4/24, 16.7%) | 0.1348 | 1.0000 | 0.8652 | 0.0858 | 0.1990 | -2.8394 | 7.7087 | 1 |
| Stiffness: partial_corr | 0.1078 | 0.1337 | 1.0000 (520/3456, 15.0%) | -1.0000 | 1.0000 | 2.0000 | 1.8974 | 0.8399 | -0.2144 | -1.6748 | 0 |
| Stiffness: stiffness_k | 0.0000 | 0.0000 | 0.0000 (3456/3456, 100.0%) | -0.0000 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 58.7622 | 3451.0003 | 1 |
| Thermo: entropy_S | 5.7599 | 5.7643 | 3.6000 (3/24, 12.5%) | 3.5940 | 8.6044 | 5.0104 | 1.5983 | 1.4295 | 0.2451 | -0.6611 | 0 |
| Thermo: free_energy_F | 1169328455.9 | 1224979815.2 | 799866295.0 (1/24, 4.2%) | 799866295.4 | 1359437276.1 | 559570980.6 | 210086628.1 | 168927543.5 | -0.9471 | -0.2941 | 0 |
| Thermo: gross_activity_U | 1359453095.1 | 1359437276.1 | 1359437276.0 (23/24, 95.8%) | 1359437276.1 | 1359816933.5 | 379657.5 | 0.0 | 77497.3 | 4.5873 | 19.0435 | 1 |
| Thermo: temperature_T | 32127842.0305 | 22877913.1784 | 0.0000 (1/24, 4.2%) | 0.0000 | 81072369.2168 | 81072369.2168 | 39818161.6183 | 25596882.3031 | 0.6176 | -0.9836 | 0 |
| Topology: stress | 88.1665 | 0.9102 | 0.0000 (98/843, 11.6%) | 0.0000 | 13948.0940 | 13948.0940 | 1.7727 | 788.6127 | 12.3048 | 175.2058 | 10 |
| Topology: weight | 7620349.5743 | 110819.5900 | 7230.9000 (7/843, 0.8%) | 13.8600 | 441354259.5500 | 441354245.6900 | 407140.8250 | 45267315.2744 | 7.6744 | 61.9536 | 17 |

---
## 3. Structural Evolution (Viscosity Classification)

- **Viscosity Range:** `135943727.61 ~ 135953219.04`
  - 🩸 **Diagnosis:** Thrombosis / High-Friction (Old-Generation Structure). The system relies on manual/human friction.

---
## 4. Quartile-based Diagnostic Candidates

### ⚠️ Shoulder Stiffness (Chronic Delay/Viscosity >= Q3: `9426682.5826`)
| Node | Average Viscosity | Peak Time | Peak Viscosity |
| :--- | :---: | :---: | :---: |
| `00_ACC_Input_From_Outside` | 66249781.7932 | `2020-01` | 67673838.9810 |
| `02_USR_001` | 38082430.7902 | `2020-08` | 39305218.4085 |
| `03_USR_002` | 19569642.3796 | `2021-12` | 22875661.1960 |

### 🎯 Acupuncture Points (Tsubo/Strain <= Q1: `3.5761`)
| Node | Average Strain Energy |
| :--- | :---: |
| `05_USR_004` | 0.1748 |
| `04_USR_003` | 0.1836 |
| `01_ACC_Output_To_Outside` | 3.2431 |

### 🚫 Contraindications (Kinki/Strain >= Q3: `4.0376` or limit)
| Node | Average Strain Energy |
| :--- | :---: |
| `00_ACC_Input_From_Outside` | 4.1658 |
| `03_USR_002` | 4.1122 |
| `02_USR_001` | 4.0934 |

> *Generated automatically by the TLU Meta-Diagnosis Engine (Descriptive Statistics V3).* 

