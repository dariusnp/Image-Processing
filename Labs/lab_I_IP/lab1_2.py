# Import matplotlib, pyplot (separate from matplotlib, since that is the way we will use it), and numpy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# How to create an array filled with zeros
img = np.zeros([256,256])
colormap = np.zeros([256,3])

# Create the image here
for i in range(256):
  for j in range(256):
    img[i, j] = j
# Create the colormap here
for i in range(256):
  colormap[i, 0] = i / 255
colormap = mpl.colors.ListedColormap(colormap)
# Display the image
plt.figure(), plt.imshow(img, cmap = colormap), plt.colorbar()