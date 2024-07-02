import numpy as np
import math
import cv2 as cv
import matplotlib.pyplot as plt

def generate_gaussian_mask(size, sigma):
   
    center = size // 2

    
    mask = np.zeros((size, size))

    
    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            exponent = -(x**2 + y**2) / (2 * sigma**2)
            mask[i, j] = (1 / (2 * math.pi * sigma**2)) * math.exp(exponent)

   
    mask /= np.sum(mask)

    return mask

size = 3
sigma = 10

gaussian_mask = generate_gaussian_mask(size, sigma)
print(gaussian_mask)





def find_d(arr):
    res = np.sum(arr)
    return res if res != 0 else 1


def filter_image(image, mask, b=0):
    d = find_d(mask)
    rows_im, cols_im = image.shape
    image_res = np.zeros((rows_im, cols_im))
    rows_mask, cols_mask = mask.shape

    for k in range(rows_mask // 2, rows_im - rows_mask // 2):
        for l in range(cols_mask // 2, cols_im - cols_mask // 2):
            im_shape = image[k - rows_mask // 2 : k + (rows_mask // 2) + 1,
                             l - cols_mask // 2 : l + (cols_mask // 2) + 1]
            new = (1 / d) * np.sum(np.multiply(im_shape, mask)) + b
            image_res[k][l] = new 
            
         
    return image_res

image = cv.imread('lisa.jpeg', cv.IMREAD_GRAYSCALE)

mask1 = gaussian_mask

filtered_image = filter_image(image, mask1)

# Display the original and filtered images
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(filtered_image, cmap='gray'), plt.title('Filtered Image')
plt.show()

print(find_d(gaussian_mask))