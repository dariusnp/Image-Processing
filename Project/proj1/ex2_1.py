#%%
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
import time

# the function that applies the transform for a pixel in the image
def new_val_current_pixel(a, b, T1, T2, p, L):
    if (p >= 0 and p < a):
        v = (T1 / a) * p
    elif (p >= a and p < b):
        v = T1 + ((T2 - T1) / (b - a)) * (p - a)
    elif (p >= b and p < L):
        v = T2 + ((L-1-T2) / (L-1-b)) * (p - b)  

    return v  
    ### the input parameters should be (a,b,T1,T2), current value of the pixel, total number of gray levels 
    ### the output should be the new value in the current pixel

# function that will apply the transform on all the image
def apply_linear_contrast(a, b, T1, T2, L, img_in, h, w):
    new_image = np.zeros([h, w])

    for i in range(h):
        for j in range(w):
            new_image[i, j] = new_val_current_pixel(a, b, T1, T2, img_in[i,j], L)
    
    return new_image 
    ### the input parameters should be (a,b,T1,T2), total number of gray levels, input image and image shape
    ### the output should be the enhanced image

    
    
# read the image
img = io.imread('lena_gray.jpeg')

# show the original image
plt.figure(),plt.imshow(img, cmap='gray')

# process the image
h = img.shape[0]
w = img.shape[1]

# show the resulting image
img2 = apply_linear_contrast(140, 200, 70, 230, 256, img, h, w)

plt.figure(), plt.imshow(img2, cmap='gray')

# second point

img3 = apply_linear_contrast(20, 220, 70, 160, img, h, w)
# %%
