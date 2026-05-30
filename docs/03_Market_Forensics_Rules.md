# 03. Market Forensics & Compliance Rules

The stock market is one of the most challenging networks for forensics due to massive order book updates at millisecond intervals and multiple colluding accounts complexly intertwined.

This document outlines audit and surveillance protocols for uncovering market manipulation (wash trading, matched orders, bot recirculation trading) using two mechanical lenses specialized for the stock market domain: **"Bipartite Graph Projection (Ticker-User)"** and **"Direct Graph Projection (User-User)."**

---

## 🧭 Table of Contents

1. [Dual Projections in Market Forensics](#1-dual-projections-in-market-forensics)
2. [Bipartite Graph Analysis (Ticker-User)](#2-bipartite-graph-analysis-ticker-user)
3. [Direct Graph Analysis (User-User)](#3-direct-graph-analysis-user-user)
4. [Compliance Audit Protocol](#4-compliance-audit-protocol)

---

## 1. Dual Projections in Market Forensics

In their raw form, transaction logs (execution logs) hide "who is colluding with whom" and "which ticker is manipulated" under multi-dimensional noise. TLU extracts and projects two contrasting graphs from the same raw logs:

```text
                     [Raw Trades (Execution Logs)]
                                │
        ┌───────────────────────┴───────────────────────┐
        ▼ (Tickers on the left, Users on the right)      ▼ (Discard tickers, project onto direct funds transfer)
[Bipartite Graph Projection]                    [Direct User-User Graph Projection]
        │                                               │
        ├──► Objective: Identify "manipulated tickers"   ├──► Objective: Identify "collusive syndicates (users)"
        └──► Verification: Sample 6 (Market Bipartite)  └──► Verification: Sample 7 (Market Users)
```

By overlaying these two perspectives, we completely surround the full picture of market manipulation, covering both volume fabrication on the ticker side (Sample 6) and backroom fund transfers on the user side (Sample 7).

---

## 2. Bipartite Graph Analysis (Ticker-User)

### 🔬 Auditing Perspective

In a bipartite graph (Bipartite Graph), the left nodes are "Tickers (Stocks)," the right nodes are "Users," and executed orders connect them as edges.

#### Key Anomaly Signatures

1. **Maximum Spectral Radius Saturation ($\rho = 1.00$):**
    When a closed trading loop is established between a specific bot cluster and a specific ticker, the eigenvalue spectral radius clings to its limit of **`1.00`**. This signals that normal outside investors are shut out, and orders are idling inside a closed circuit.
2. **Collapse of Edge Stress (Edge Stress = `0.00`):**
    In a normal market, since many participants' orders clash, mechanical tension (Edge Stress) is present on each edge (trade path). However, when bots perfectly synchronize their orders behind the scenes, transaction uncertainty drops to zero, and edge stress collapses to its extreme limit of **`0.00`**.
    * *Reference:* In Bipartite Graph verification (Sample 6), while the binding stiffness between specific bot groups and the manipulated ticker abnormally solidifies, the edge stress plunges to `0.00`, capturing a "hollow recirculation" where topological tension vanishes.

---

## 3. Direct Graph Analysis (User-User)

### 🔬 Auditing Perspective

In a direct user graph (Direct User Graph), we discard all intermediate ticker nodes and connect only the "substantive round-trip movement of funds" between accounts as edges.

#### Key Anomaly Signatures

1. **Eigenvector Evolution Stiffness Lock (PCA Stiffness Lock):**
    At the moment colluding accounts execute matched orders, the PC1 explanation ratio of the Principal Component Analysis (PCA) spikes to nearly 100% (**`99.67%`** in Sample 7). In this phase, PCA eigenvector loadings abnormally concentrate on the colluding accounts (`USR_003` and `USR_004`), showing that other healthy transaction relationships are mechanically overwhelmed and constrained (Stiffness Lock).
2. **Uncovering "Evacuation" to PC2 During Calm Periods:**
    To evade audit detection, colluders may temporarily pause circular trading (calm period). In this state, they disappear from the PC1 loadings. However, the Physics-Mathematics-Mathematics Engine exposes this "residual collusion" by showing that they have evacuated and are hiding inside **PC2 (Second Principal Component)**, maintaining strong loadings of **`-0.6965`** and **`0.6921`** (specifically at `t=42 / 2020-W43`).
3. **Catastrophic Collapse of Free Energy Skewness:**
    When circular trading hijacks overall market liquidity and shuts out normal external investment opportunities, the overall free energy distribution of the system becomes heavily skewed. The free energy skewness (F-Skewness) rapidly drops to extreme negative values, such as **`-2.72`**.

---

## 4. Compliance Audit Protocol

When a warning alert is triggered, compliance officers must evaluate and compare ("triage") physical parameters using the following steps to confirm fraudulent transactions:

### 🚨 Triage Flow

```text
[Z-Score Warning Triggered (Z > 3.0)]
           │
           ├──► System Conservation Residual > 0.00?
           │     ├──► YES: 🔴 CRITICAL (Off-book leakage/embezzlement anomaly outside the system)
           │
           └──► Spectral Radius (Spectral Radius) ≧ 0.95?
                 ├──► NO: 🟢 NORMAL (Dismissed as a statistical false positive due to seasonal/temporary volume spikes)
                 └──► YES: 🟡 HIGH (Recirculation lock detected. Proceed to wave analysis below)
                             │
                             └──► Phase Coherence of specific pair ≈ 1.0 & Phase Drift ≈ 0.0?
                                   ├──► NO: Normal trading circulation (congestion at gateway nodes)
                                   └──► YES: 🔴 CRITICAL (High-speed Matched Orders / Confirmed market manipulation)
```

### Request Rules for Rebuttal Documents (Physical Evidence)

When a pathological collusion anomaly (Matched Orders) is confirmed, the audit department obligates the involved parties to present the following "objective physical evidence from outside the database boundary" to disprove collusion:

1. **Original SWIFT / Banking API Transaction Records:** Proof from financial institutions that actual, independent, real-time fund settlements of equivalent amounts were executed between the respective bank accounts (not just book-entry offsetting).
2. **Original IP/MAC Address Connection Logs:** Network log proof showing that the terminals executing transactions for each account were operating from physically separate locations and infrastructures, under independent decision-making.
