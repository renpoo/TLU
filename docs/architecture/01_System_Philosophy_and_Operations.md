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

## 4. Invisible GitOps & Audit Trails (:FUTURE IMPLEMENTATIONS)

In corporate strategy and forensics, the *provenance* of an insight is just as important as the insight itself. If a structural anomaly was detected last month, you must be able to prove exactly what parameters and data triggered that alert.

* **No Manual Versioning:** Users are not trusted to consistently version their configuration files or source data manually.
* **Automated Pre-flight Commits:** Before any batch execution (e.g., `batch_processing.sh`), the system automatically executes a `git commit` encompassing the entire `workspace/` (input data streams, system parameters, and ephemeral dictionaries).
* **Immutable Truth:** By anchoring every execution to a specific Git hash, TLU ensures 100% reproducibility. You can always revert to a previous commit and re-run the pipeline to achieve the exact same state and visual dashboards.
