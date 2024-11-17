#%%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# the image is
img = np.array([[0,1,2],[3,4,5],[26,7,8]])

# a colormap with colors
colormap = np.array([[1.0,0.0,0.0],[0.0,1.0,0.0],[0.0,0.0,1.0],[0,0,0],[0.5,0.5,0.5],[1,1,1],[1,0,1],[0,1,1],[0.5,1,0.25]])
colormap = mpl.colors.ListedColormap(colormap)

# display with gray colormap
# notice that the imshow function automatically scaled the colormap 
# so that the values from 0 to 8 to cover all the range of colors from black to white
plt.figure(), plt.imshow(img,cmap='gray')
plt.colorbar()

# modify the colormap for pseudocoloring
plt.figure(), plt.imshow(img,cmap=colormap)
plt.colorbar()
# %%
