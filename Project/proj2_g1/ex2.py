#%%
import matplotlib.pyplot as plt
import numpy as np
from skimage import io,util,color
import math

def filt_weighted_mean(img, r, c, border, mask):
    # given the input image and the kernel, return the filtered image
    img_new = np.zeros([r - (border * 2), c - (border * 2)])

    for i in range(border, r - border):
        for j in range(border, c - border):
            V = img[i - border : i + border + 1, j - border : j + border + 1]
            img_new[i - border, j - border] = np.sum(V * mask)
        return img_new
   
    
def MSE(img, img_filtered, r, c, border):
    # given the initial image and the processed image, return the MSE value
    
    mse = 0
    mse = np.sum(((img[border : r - border, border : c - border] - img_filtered) ** 2)) // (r * c)
    
    # in 2 for loops going from pixel to pixel compute the result
    # 1/(r*c) suma(0,r)suma(0,c) (F-F0)^2
    #  you can try to do it without the for loop (not mandatory)
    return mse
    
# read the image, transform to gray and integers in [0, 255]     

img = io.imread('lena.png')
img = color.rgb2gray(img)
img = np.uint8(img*256)
# generate noise and add it to the image
r, c = img.shape
N = np.random.normal(0, 10, (r, c))
# initialize the kernel
#[[0.075,0.124,0.075], [0.124,0.2,0.124], [0.075,0.124,0.075]]
kernel_weighted_mean = np.array([[0.075,0.124,0.075], [0.124,0.2,0.124], [0.075,0.124,0.075]])

kernel_aritmetic_mean = np.ones([3, 3]) / 9


# apply the 2 linear functions on the noisy image 

img_filtered_weighted = filt_weighted_mean(img, r, c, 1, kernel_weighted_mean)
img_filtered_arithmetic = filt_weighted_mean(img, r, c, 1, kernel_aritmetic_mean)

#compute the MSE for the 2 resulting images (compared to the ideal image)

mse_noise = MSE(img, img + N, r, c, 1)
mse1 = MSE(img, img_filtered_weighted, r, c, 1)
mse2 = MSE(img, img_filtered_arithmetic, r, c, 1)

# visualize the resulting images and print the 2 MSE

plt.figure(), plt.imshow(img_filtered_weighted, cmap='gray'), plt.colorbar()
plt.figure(), plt.imshow(img_filtered_arithmetic, cmap='gray'), plt.colorbar()
plt.figure(), plt.imshow(img, cmap='gray')

print('MSE noise = ' + mse_noise + '\n')
print('MSE img 1 = ' + mse1 + '\n')
print('MSE img 2 = ' + mse2 + '\n')
# %%
