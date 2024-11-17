#%%
# Import matplotlib, pyplot (separate from matplotlib, since that is the way we will use it), and numpy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

size = 256
# How to create an array filled with zeros
img = np.zeros([256,256])
colormap = np.zeros([256,3])

# Create the image here
for i in range(256):
  for j in range(256):
    img[i, j] = j
# Create the colormap here


for i in range(0, 128):
    colormap[i, 0] = i / 128 # making first half red
j = 0
for i in range(128, 256):
   j = j + 1 # brute-forcing the green column in colormap
   colormap[i, 0] = 1
   colormap[i, 1] = j / 128 # the green column goes from 0 to 1 in second half
   


colormap = mpl.colors.ListedColormap(colormap)
# Display the image
plt.figure(), plt.imshow(img, cmap = colormap), plt.colorbar()
# %%
