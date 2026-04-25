# 01. System Philosophy and Operations

> **"Complexity is the enemy of execution. Purity of function is its antidote."**

The Tensor-Link Utility (TLU) is intentionally designed to reject the modern trend of building monolithic, stateful, and heavily entangled applications. Instead, it embraces a rigorous, classical approach rooted in the **Unix Philosophy**.

This document outlines the core architectural principles and operational protocols that govern the system (Ver 8.0.0).

---

## 1. The Unix Pipeline Architecture

TLU processes data as a continuous flow of information, treating organizational dynamics as a literal "stream."

* **Stateless Filters:** Each mathematical filter (e.g., Thermodynamics, Kinematics) is a standalone executable. It reads a standard COO (Coordinate) tensor stream from `Standard Input (stdin)`, applies a single paradigm of physics, appends its findings as new columns, and flushes the result to `Standard Output (stdout)`.
* **No Hidden State:** Filters do not maintain internal databases or memory between runs. If the input stream is identical, the output is mathematically guaranteed to be identical.
* **Piping (`|`):** Complex analysis is achieved not by writing convoluted classes, but by chaining simple, pure functions together.

## 2. Separation of Concerns: I/O vs. Pure Math

To achieve maximum testability (via Test-Driven Development) and reduce cognitive load for developers, TLU enforces a strict physical separation between data handling and mathematical computation.

* **The Wrapper Layer (`filter_*.py`):** These scripts are intentionally "dirty." They handle CLI argument parsing, reading CSVs from `sys.stdin`, resolving domain dictionaries, and writing back to `sys.stdout`. **No physics, geometry, or business logic is allowed in this layer.**
* **The Core Math Layer (`core_*.py`):** These are pure mathematical functions. They know nothing about CSVs, domain vocabularies, or filesystems. They accept pure NumPy arrays (`np.ndarray`) and scalars, and return NumPy arrays. This makes unit testing trivial and ensures mathematical rigor.

## 3. Zero Local Dependency

"It works on my machine" is an unacceptable excuse in a high-fidelity analytics environment.

* **Host Sterilization:** The user's host operating system requires only `Docker` and `bash`. Python, NumPy, SciPy, NetworkX, and Matplotlib are strictly confined within the `tlu-engine` container.
* **Transparent Wrapper (`_tlu_env.sh`):** TLU provides a shell wrapper that transparently translates local commands into containerized executions (e.g., `docker compose exec -T tlu-engine python3`). The data flows seamlessly between the host's filesystem and the isolated container via standard streams, making the container feel like a native binary.

## 4. Declarative Experiment Control (SSOT)

In complex corporate simulations, the *provenance* of an insight is just as important as the insight itself. To guarantee reproducibility, TLU relies on a Single Source of Truth (SSOT).

* **The `_sys_params.csv` Paradigm:** Users are strictly forbidden from modifying shell scripts or python source code to change experimental conditions (e.g., input data sources, target simulation nodes, anomaly thresholds). Every single boundary condition and constraint is declaratively defined in `workspace/config/_sys_params.csv`.
* **Parameter as Code:** This configuration file serves as the definitive "blueprint" for the experiment. By isolating parameters from execution logic, the system prevents accidental configuration drift.

## 5. Immutable Archive Reproducibility

To enforce complete auditability without relying on external Git repositories, TLU employs a local snapshotting architecture.

* **Workspace Snapshots:** Upon executing a significant pipeline run, the entire `workspace/` directory (which includes the input streams, the precise `_sys_params.csv` used, and all output data) can be snapshotted into an `archives/run_YYYYMMDD_HHMMSS/` directory by simply running:
  ```bash
  bash bin/archive_experimental_run.sh
  ```
  *(Note: Output plots are excluded from the archive to save disk space, as they can be deterministically regenerated).*
* **Time-Travel Execution:** Because the pipeline dynamically references the configuration relative to its target environment, a user can effortlessly reproduce past calculations or regenerate dashboards. By pointing the orchestration scripts to a past archive, the pipeline behaves exactly as it did at the exact moment of that historical snapshot:
  ```bash
  # Regenerate 3D visualization dashboards from a past experiment
  bash bin/batch_visualize_graphs.sh dark --target_env archives/run_20260425_094806/workspace
  ```
