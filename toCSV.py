import numpy as np
import matplotlib.pyplot as plt

# Load the UMAP dimension-reduced data from the .npz file
data = np.load('fractal-embeddings/demo_data/combined_reduced_embeddings.npz')

for key, value in data.items():
    np.savetxt('./' + key + ".csv", value, delimiter=',')