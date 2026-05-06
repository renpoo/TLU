# 01. System Philosophy and Operations

## 🔬 Conclusion: Why Does TLU Choose the "Unix Philosophy" and "Containers"?

The absolute design philosophy underlying the TLU architecture is the conclusion that: **"No matter how advanced the physical mathematics used, if the calculation process is a black box and lacks reproducibility, it is entirely worthless as an auditing tool (ensuring falsifiability)."**

By rejecting complex, bloated system designs and adopting the **Unix Philosophy (giving one program one function and linking them)** along with **complete isolation via containers**, TLU mathematically and engineer-wise guarantees that "the exact same conclusion (anomaly detection result)" will be derived regardless of who runs it, when, or in what environment.

---

## Pipeline and Stateless Design

Rather than swallowing the financial data of a corporation or organization into one massive monolithic system, TLU processes it through a finely divided, "transparent pipeline."

### "Stream Processing" of Data

* **Stateless Filter Design:** Each analytical filter (e.g., thermodynamic analysis, kinematic analysis) remembers absolutely nothing about past execution states. It is mathematically guaranteed that if the input data (CSV) is the same, the system will always perform the same tensor calculations and return the same output.
* **Complete Separation of Roles (Application of the Rosetta Stone):**
  * **Wrapper Layer (`filter_*.py`):** Responsible only for reading/writing command-line arguments and CSVs (string and business domain processing). Understanding "accounting terms (like Accounts Receivable)" stops at this layer.
  * **Core Math Layer (`core_*.py`):** Responsible exclusively for pure matrix and tensor calculations. This layer does not recognize the business domain at all; it functions as a pure physics engine calculating only "mass" and "stiffness."

---

## Ensuring Reproducibility and Enforcing Operational Rules

After securing the transparency of the overall structure (macro), we eliminate human errors and noise caused by "environmental differences" at the daily operational level (micro).

### Execution Environment with Zero Local Dependencies

* **Isolation via Containerization:** All libraries required to run TLU, such as Python and NumPy, are completely isolated inside the Docker `tlu-engine` container. The situation where "it worked on my PC, but an error occurred on another auditor's PC" is physically prevented from happening.

### Centralized Configuration Management and Freezing Execution History (Snapshot)

* **Centralized Management via `_sys_params.csv`:** Directly rewriting the source code to change the target data for analysis or the thresholds (parameters) for anomaly detection is strictly prohibited. All conditions are managed in a single CSV file (Single Source of Truth).
* **Archive Preservation:** By running `bash bin/archive_experimental_run.sh` after the pipeline execution, the input data of the time, the configuration files, and all generated graphs are permanently preserved as a single "Snapshot." If an audit firm specifies this archive and re-runs it 3 years later, a result identical to the exact detail of that time will be reproduced.

---

## 🔬 Falsifiability and Model Limits (Application to Practice)

TLU's system philosophy asserts with 100% precision the **engineering reproducibility** that "if these configuration parameters are given in this environment, this calculation result will absolutely be output."
However, the system cannot assert whether that output result equates to a "correct judgment in real-world business."

If incorrect thresholds or wrong target nodes are entered into the configuration file (`_sys_params.csv`), TLU will generate a "perfectly accurate anomaly detection graph based on those incorrect premises." Therefore, auditors and operators are always required not to doubt "how the system operated," but to conduct a field audit (falsification analytics) on whether "the initial conditions (premises) given to the system align with the reality of the business."
