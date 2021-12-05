import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from sklearn.utils.extmath import randomized_svd
from numpy import linalg as LA

# read image in grayscale
img = cv2.imread('blur_img.JPEG', 0)
print(type(img))

# obtain svd
# U, S, V = np.linalg.svd(img)
U, S, V = randomized_svd(img, n_components = 3)

# inspect shapes of the matrices
print(U.shape, S.shape, V.shape)
print(np.diag(S))