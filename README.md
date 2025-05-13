# The Divine Compression Hypothesis

This repository contains the complete scientific protocols, simulation code, and empirical results supporting the Divine Compression Hypothesis — a theory proposing that our universe is the simplest computable structure that supports emergence and observer-viable complexity.

---

## 🧠 Core Thesis

We posit that our universe is not random, but compressibly optimized. This principle is testable: real-world data (e.g. the CMB, DNA) should exhibit greater symbolic compressibility than matched stochastic simulations. This repository enables full reproduction of those tests.

---

## 📁 Contents

### `/scripts/`
Contains all core Python simulation and analysis scripts:
- `cmb_compression_test_protocol.py` – Gzip-based test comparing Planck CMB maps vs. Gaussian mocks.
- `symbolic_emergence_heatmap_generator.py` – Simulates symbolic universes and scores their emergence.
- `dna_compression_test_script.py` – Tests real vs. shuffled DNA sequences.
- `selector_function_simulation.py` – Simulates the Ω Selector Function over entropy-complexity space.

### `/data/`
Includes raw or compressed datasets from the simulations. See comments in each `.csv` for field descriptions.

### `/figures/`
Final result visualizations used in the published paper:
- Emergence vs. Complexity Heatmap
- CMB Compression Bar Graphs
- Real vs. Synthetic Compressibility Comparisons

### `/protocols/`
Detailed markdown documentation of each test and its scientific justification. Includes a collider reinterpretation strategy memo for the `Betsyon` scalar.

---

## 📦 Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt


_____________________________
# Symbolic Universe Simulation

This repository simulates symbolic universes based on entropy and complexity,
computes an emergence score, and outputs the results in CSV format.

## Description

Each universe is defined by two properties:

- **Complexity**: Simulated using an exponential distribution.
- **Entropy**: Simulated using a normal distribution.

Emergence is computed using a symbolic emergence function:
```
E(γ) = exp(-complexity / 200) * exp(-((entropy - 2.5)^2) / 4)
```

## How to Run

```bash
python simulate_universes.py
```

This will generate 10 CSV files, each with 1 million simulated universes.

## Requirements


- numpy
- pandas
- tqdm
- matplotlib
- scipy

## License

MIT License
