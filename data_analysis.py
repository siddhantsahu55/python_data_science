import numpy as np

# Without seed (different each run)
print("No seed:", np.random.rand(3))

# With seed (always identical)
np.random.seed(42)
print("Seed 42:", np.random.rand(3))  # [0.37454012 0.95071431 0.73199394]
