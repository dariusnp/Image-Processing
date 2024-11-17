#%%
import matplotlib.pyplot as plt
import numpy as np
from skimage import io, util, color

img = io.imread('lena.png')

print(img.dtype)

img = color.rgb2gray(img)

print(img.dtype)

img = np.uint8(img * 256)

print(img.min())
print(img.max())

plt.figure(), plt.imshow(img, cmap='gray'), plt.colorbar()

sigma = 10

N = np.random.normal(0, sigma, (img.shape[0], img.shape[1]))

plt.figure(), plt.imshow(N, cmap = 'grey')

img_noise = img + N

plt.figure(), plt.imshow(img_noise, cmap = 'grey'), plt.colorbar()

# if we modify mask_size we increase blur and frame
mask_size = 8

mask = np.ones ([mask_size, mask_size]) / mask_size**2

h, w = img.shape

img_filtered = np.zeros([h, w])

for i in range (mask_size // 2, w - (mask_size // 2)):
    for j in range (mask_size // 2, h - (mask_size // 2)):
        T = img_noise[i - mask_size // 2 : i + mask_size // 2, j - mask_size // 2 : j + mask_size // 2]
        T = T * mask
        img_filtered[i, j] = np.sum(T)

plt.figure(), plt.imshow(img_filtered, cmap='grey'), plt.colorbar()
# %%