import numpy as np
import matplotlib.pyplot as plt
from noise import pnoise2

# Define the size of the height map
width, height = 2048, 2048  # Double resolution for more detail
scale = 50  # Decrease scale to increase feature density

# Create an empty array for height values
height_map = np.zeros((height, width))

# Populate the height map using Perlin noise with increased detail
for i in range(height):
    for j in range(width):
        # Adjust the scale to control the level of detail
        height_map[i][j] = pnoise2(i / scale, j / scale, octaves=8, persistence=0.6, lacunarity=2.5, repeatx=width, repeaty=height, base=42)

# Normalize height values to range [0, 1]
height_map = (height_map - height_map.min()) / (height_map.max() - height_map.min())

# Save the height map as a PNG file
plt.imsave('detailed_terrain.png', height_map, cmap='gray')
