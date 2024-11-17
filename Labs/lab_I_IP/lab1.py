# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:19:06 2024

@author: Darius
"""

# Import matplotlib, pyplot (separate from matplotlib, since that is the way we will use it), and numpy
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# How to create an array filled with zeros
img = np.zeros([128,128])
colormap = np.zeros([128,3])

# Create the image here



# Create the colormap here

# Display the image

plt.figure(), plt.imshow(img, cmap=colormap), plt.colorbar()