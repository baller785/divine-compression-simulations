
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
