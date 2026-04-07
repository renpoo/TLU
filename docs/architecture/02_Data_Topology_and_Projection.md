# 02. Data Topology and Epistemological Projection

> **"To calculate the truth of the system, we must first strip away the illusion of names."**

Before TLU can apply laws of physics or geometry to your data, the data must be purged of its domain-specific context. Algorithms do not understand "Accounts Payable," "Marketing Department," or "Server Region US-East." They only understand topology, mass, and directional flux.

This document defines the strict protocols for transforming raw domain data into a pure mathematical space (Ver 8.0.0).

---

## 1. The Great Filter (Domain Agnosticism)

The first phase of the TLU pipeline is **Phase 1: Projection**. Its sole purpose is epistemological projection: translating the messy, human-readable world into a sterile, computable tensor space.

* **Stripping Vocabulary:** Once data passes through the projector (`_0_2_projector_to_coo.py`), all string-based identifiers and domain logic are eradicated.
* **The COO Tensor Stream:** The pipeline from this point forward only accepts and outputs data in a standard Coordinate (COO) stream format:
  `t_idx, src_idx, tgt_idx, value`
  *(Time Index, Source Node Index, Target Node Index, Flux Volume)*
* **Mathematical Purity:** Core analysis filters (Phase 2) are intentionally "blind." They do not know if they are analyzing a financial ledger, a biological neural network, or a logistics supply chain. This domain agnosticism guarantees that the mathematical rules are applied without human bias.

## 2. Union Topology (Dimensional Consistency)

For matrix operations (like calculating an inverse covariance matrix) to be mathematically valid across time, the spatial dimensions must remain perfectly consistent.

* **Consistent Spatial Coordinates:** The integer ID assigned to a node (e.g., `Node 4`) must represent the exact same entity across all time steps (`t_idx = 0` to `t_idx = N`).
* **The Union of All Elements:** Even if a specific department or account only appears in the final month of your dataset, it is registered in the topological space from the very beginning. TLU builds a "Union Topology"—a spatial matrix sized $N \times N$ where $N$ is the total number of unique nodes that *ever* exist in the entire observed timeline. Missing fluxes are simply treated as zero-energy transfers.

## 3. Ephemeral Dictionaries (The Link to the Human World)

Since the core pipeline destroys all human labels, TLU must maintain a way to translate the final mathematical conclusions back into business insights.

* **Disposable Registries:** During the Projection phase, TLU generates two ephemeral artifacts: `_node_map.csv` and `_time_map.csv`.
* **Dynamic Rebuilding:** These dictionaries are not permanently stored databases. They are disposable and are rebuilt from scratch every single time the projector runs. This guarantees that if your source data categories change, the system adapts instantly without schema migrations.
* **Re-attachment in Phase 3:** These dictionaries are only referenced again at the very end of the pipeline, by the Visualizer layer (Phase 3), to label the 3D graphs and dashboards with human-readable names.

## 4. Fail-Fast Column Mapping

Data ingestion is the most dangerous point of failure in any analytics pipeline. TLU handles ingestion with extreme prejudice.

* **Strict Requirements:** The projector requires explicit CLI arguments defining which columns in the source CSV represent Time, Source, Target, and Value.
* **No Guesses, No Fallbacks:** If a specified column is missing or severely malformed, TLU will not attempt to guess the user's intent or apply default values. It will immediately throw a `KeyError` and crash the pipeline. This **Fail-Fast** design ensures that dirty data is caught at the gate, preventing it from silently corrupting complex downstream physical calculations (Context Bleed).
