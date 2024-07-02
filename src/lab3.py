import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt



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
            
            # summa = 0
            # for i in range(-rows_mask // 2, rows_mask // 2 + 1):
            #     for j in range(-cols_mask // 2, cols_mask // 2 + 1):
            #         summa += image[k + i][l + j] * mask[i + rows_mask // 2][j + cols_mask // 2]
            # image_res[k][l] = (1 / d) * summa + b
    return image_res



image = cv.imread('lisa.jpeg', cv.IMREAD_GRAYSCALE)
# image = cv.imread('TEST.jpg', cv.IMREAD_GRAYSCALE)


scale_percent = 30 

width = int(image.shape[1] * scale_percent / 100) 
height = int(image.shape[0] * scale_percent / 100) 

dsize = (width, height) 

image = cv.resize(image, dsize)

mask1 = np.array([[1, 1, 1],
                 [1, -8, 1],
                 [1, 1, 1]])

mask2 = np.array([[0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, -1, 0, 0, 0],
                  [0, 0, 0, -2, 0, 0, 0],
                  [0, -1, -2, 21, -2, -1, 0],
                  [0, 0, 0, -2, 0, 0, 0],
                  [0, 0, 0, -1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0]])

mask3 = np.array([[0, 0, 1, 0, 0],
                  [0, 0, 2, 0, 0],
                  [1, 2, 4, 2, 1],
                  [0, 0, 2, 0, 0],
                  [0, 0, 1, 0, 0]])

mask4 = np.array([[0, 0, 0, 0, 0],
                  [0, 0, -1, 0, 0],
                  [0, -1, 10, -1, 0],
                  [0, 0, -1, 0, 0],
                  [0, 0, 0, 0, 0]])

mask5 = np.array([[-2, 0, 0, -2, 0, 0, -2],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [-2, 0, 0, 16, 0, 0, -2],
                  [0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0],
                  [-2, 0, 0, -2, 0, 0, -2]])

mask6 = np.array([[0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0],
                  [1, 1, 4, 1, 1],
                  [0, 0, 1, 0, 0],
                  [0, 0, 1, 0, 0]])

mask7 = np.array([[0, 1, 2], 
                  [-1, 0, 1], 
                  [-2, -1, 0]]) 

mask8 = np.array([[-1, -2, -1], 
                  [0, 0, 0], 
                  [1, 2, 1]])


masks = [mask1, mask2, mask3, mask4, mask5, mask6, mask7, mask8]
for i in enumerate(masks):
    print(f'Параметр D для маски под номером {i[0]+1} равен {find_d(i[1])}')


# print(*filter_image(image, masks[1]))


fig, ax = plt.subplots(3, 3)
fig.set_figwidth(15)
fig.set_figheight(30)

ax[0, 0].imshow(image, cmap='gray')
ax[0, 0].set_title('Исходное изображение')
ax[0, 0].set_xticks([])
ax[0, 0].set_yticks([])

row = 0
col = 1
for i in range(len(masks)):
    ax[row, col].imshow(filter_image(image, masks[i]), cmap='gray')
    ax[row, col].set_title(f'Результат применения маски {i + 1}')
    ax[row, col].set_xticks([])
    ax[row, col].set_yticks([])
    col += 1
    if col == 3:
        col = 0
        row += 1

# fig, ax = plt.subplots(1, 2)
# fig.set_figwidth(15)
# fig.set_figheight(6)
# filtered_img = filter_image(image, mask3)
# ax[0].imshow(image, cmap='gray')
# ax[0].set_title('Исходное изображение')

# ax[1].imshow(filtered_img, cmap='gray')
# ax[1].set_title('Результат применения маски')


plt.show()

