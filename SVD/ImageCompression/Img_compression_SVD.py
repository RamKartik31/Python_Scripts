# get the image from "https://cdn.pixabay.com/photo/2017/03/27/16/50/beach-2179624_960_720.jpg"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2

# read image in grayscale
img = cv2.imread('nature.jpg', 0)

# obtain svd
U, S, V = np.linalg.svd(img)

# inspect shapes of the matrices
print(U.shape, S.shape, V.shape)

# plot images with different number of components
comps = [638, 500, 400, 300, 200, 100]

plt.figure(figsize = (16, 8))
for i in range(6):
  # print(i)
  low_rank = U[:, :comps[i]] @ np.diag(S[:comps[i]]) @ V[:comps[i], :]
  # print(low_rank)
  if(i  == 0):
     print('if')
     plt.subplot(2, 3, i+1)
     plt.imshow(low_rank, cmap = 'gray')
     plt.axis('off')
     plt.title("Original Image with n_components =" + str(comps[i]))
  else:
     plt.subplot(2, 3, i+1)
     plt.imshow(low_rank, cmap = 'gray')
     plt.axis('off'), plt.title("n_components =" + str(comps[i]))
plt.show()