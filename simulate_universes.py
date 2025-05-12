
import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Emergence function parameters
COMPLEXITY_SCALE = 200
ENTROPY_MEAN = 2.5
ENTROPY_VARIANCE = 2

def generate_universe_batch(batch_size, start_id=0):
    universe_ids = np.arange(start_id, start_id + batch_size)
    complexities = np.random.exponential(scale=300, size=batch_size)
    entropies = np.random.normal(loc=2.5, scale=1.2, size=batch_size)

    # Emergence function: Gaussian * Exponential kernel
    emergence_scores = np.exp(-complexities / COMPLEXITY_SCALE) * np.exp(-((entropies - ENTROPY_MEAN) ** 2) / ENTROPY_VARIANCE)
    
    df = pd.DataFrame({
        'universe_id': universe_ids,
        'complexity': complexities,
        'entropy': entropies,
        'emergence_score': emergence_scores
    })
    return df

if __name__ == "__main__":
    batch_size = 1000000  # 1 million universes per batch
    for i in range(10):
        start_id = i * batch_size
        df = generate_universe_batch(batch_size, start_id)
        df.to_csv(f"universe_batch_{i+1}.csv", index=False)
