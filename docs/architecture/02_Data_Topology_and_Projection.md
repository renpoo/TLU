# 02. Data Topology and Projection

## 🔬 Conclusion: Why Strip "Words (Business Context)" from Mathematics?

The ultimate conclusion of the "Data Projection" phase in the TLU architecture is: **"If human societal context (words) such as 'Accounts Receivable' or 'Kyoto Branch' are mixed into mathematical calculations, bias will arise, making objective auditing impossible. Therefore, data must be forcibly translated and isolated into a pure 'network of points and lines (tensor space)'."**

The system guarantees overwhelming objectivity—un-distortable by human hands—by performing purely physical and geometric calculations without understanding "meaning," and only re-translating (via a Rosetta Stone) back into human words during the final visualization phase.

---

## Elimination of Business Context and Union Topology

Raw data (journal data in CSV, etc.) is stripped of all human identifiers as it passes through Phase 1 (`_0_2_projector_to_coo.py`).

### Domain Independence and Unification to COO Format

* The conversion filter transforms data like "Sales to Company A" into a pure COO (Coordinate) format tensor array: `[Node 12] -> [Node 45]: Weight 5000`.
* The core calculation filters (Thermodynamics, Kinematics) do not know at all whether they are "analyzing financial data" or "analyzing brainwave data." This design proves the universality that the exact same physics engine operates across all domains, including finance, traffic, and medicine.

### Consistency of Spatial Coordinates (Union Topology)

* In order to correctly perform physical matrix calculations along a timeline, the dimensions of space must not be distorted.
* Even if an account only existed in "Week 12", TLU secures the dimension (slot) for that account from "Week 1" and treats it as zero. This prevents shifts in the calculation axes across time series (dimensional incompatibility errors).

---

## Fail-Fast and the Re-translation Mechanism

After securing the integrity of the macro calculation space, we construct error handling and the micro mechanisms for final report generation.

### Strict Data Validation (Immediate Halt)

* The ingestion of external data is where errors are most likely to occur. When TLU detects a "mismatch between debits and credits" or "missing dates," it completely avoids making supplementary guesses and immediately forces the pipeline to shut down (Fail-Fast).
* This is a safety mechanism designed to physically block the risk that "corrupted data silently contaminates downstream calculations, causing auditors to blindly believe erroneous anomaly detection results."

### Reverse Mapping (Re-translation into Human Words)

* During the projection phase, a "disposable mapping table (`_node_map.csv`)" correlating the stripped string IDs to tensor IDs is generated behind the scenes.
* After the physics engine outputs a calculation result stating, "Rigid Lock (collapse of stiffness) occurred at Node 45," the final visualization program refers to this mapping table and re-translates it into a business narrative (report) stating, "An uncollectible event has occurred in the Accounts Receivable for Company A."

---

## 🔬 Falsifiability and Model Limits

The data projection architecture asserts the **computer science fact** that "the input dataset was mapped into a pure tensor space with 100% accuracy without any loss."
However, TLU's projection engine cannot verify the data provenance—that is, "whether the input CSV data itself was intentionally fabricated or deleted outside the system to begin with."

Therefore, before accepting the anomaly detection results calculated by TLU, auditors have the responsibility to secure an IT General Controls (ITGC) field audit (falsification analytics) to answer: "Was the journal CSV input into the system truly extracted directly from an untampered master database?"
