#%%
import matplotlib.pyplot as plt
import numpy as np
from skimage import io,util,color
    
# Read the image, convert it to gray, make it integer with values in [0, 255]

img = io.imread('lena.png')
img = color.rgb2gray(img)
img = np.uint8(img * 256)

# generate the white, gaussian noise to that image
# mean = 0, standard deviation sigma = given by the user 
h, w = img.shape
sigma = 10
N = np.random.normal(0, sigma, (h, w))

# add the noise over the image. 
# Take into account that the resulting image should have integer values in [0, 255] 
img_noise = img + N
plt.figure(), plt.imshow(img_noise, cmap='gray')

# initiate the kernel
mask_size = 3
mask = np.ones([mask_size, mask_size]) / mask_size ** 2

# initiate the output image
img_filtered = np.zeros([h, w])

border = mask_size // 2


for i in range(border, h - border):
    for j in range(border, w - border):
        V = img_noise[ i - border : i + border + 1, j - border : j + border + 1]
        V = V * mask
        img_filtered[i,j] = np.sum(V)
        
plt.figure(), plt.imshow(img_filtered, cmap = 'gray'), plt.colorbar()
# %%
