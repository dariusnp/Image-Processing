#%%
# Import skimage and matplotlib
from skimage import io,color
import matplotlib.pyplot as plt

# read the image
img = io.imread('lena.png')
# Check the type of data in the image
print(img.dtype)
# Show the original image
plt.figure(),plt.imshow(img)

# convert to graylevels
img_gray = color.rgb2gray(img)
# check the type of data in the image after conversion
print(img_gray.dtype)
# Show the image with gray levels
plt.figure(),plt.imshow(img_gray,cmap='gray')
# Pseudocolor with different colormap
plt.figure(),plt.imshow(img_gray,cmap='jet')

print(img.shape)

print(img[0,0])

print(img_gray.shape)

print(img_gray[0,0])
# %%
