import cv2
import numpy as np
from sklearn.decomposition import TruncatedSVD
from PIL import Image as im 

ipArray = np.array(
[
[0.985,0.174],
[0.984,0.176],
[0.984,0.178],
[0.984,0.18],
[0.983,0.182],
[0.983,0.184],
[0.982,0.187],
[0.982,0.189],
[0.982,0.191],
[0.981,0.193],
[0.981,0.195],
[0.98,0.197],
[0.98,0.199],
[0.979,0.202],
[0.979,0.204],
[0.979,0.206],
[0.174,0.985],
[0.171,0.985],
[0.169,0.986],
[0.167,0.986],
[0.165,0.986],
[0.163,0.987],
[0.161,0.987],
[0.159,0.987],
[0.156,0.988],
[0.154,0.988],
[0.152,0.988],
[0.15,0.989],
[0.148,0.989],
[0.146,0.989],
[0.143,0.99],
[0.141,0.99]
])
#data = im.fromarray(img) 
#data.save('t22.png')
U, S, V = np.linalg.svd(ipArray)
print(ipArray.shape)
print(U.shape)
print(S.shape)
print(V.shape)
print(S)
