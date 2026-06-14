# LinearHash-Quantile

A dependency-free Python implementation of an open-addressed feature frequency table engineered for tiny edge hardware profiles. By mapping continuous telemetry values into quantized integers, this repository uses a custom **Hash Map with Linear Probing** to maintain streaming data probability profiles.

## ⚡ Data Structure Complexities
* **Collision Handling strategy:** Open addressing via a linear probing sequence ($H(k, i) = (H'(k) + i) \pmod m$).
* **Memory footprint:** Stored as continuous, aligned parallel arrays to optimize memory usage.
* **Inference Lookup:** Constant time $O(1)$ statistical updates.
