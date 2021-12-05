import cv2
import numpy as np
from sklearn.decomposition import TruncatedSVD
from PIL import Image as im 

img_path = 't1.png'
img = cv2.imread(img_path, 0) # read image as grayscale. Set second parameter to 1 if rgb is required 
img_reverted= cv2.bitwise_not(img)
new_img = img_reverted / 255.0 # now all values are ranging from 0 to 1, where white equlas 0.0 and black equals 1.0 
print(type(new_img))
data = im.fromarray(img_reverted) 
data.save('t2.png')
U, S, V = np.linalg.svd(new_img)
'''
print('Left singular')
print(U)
print('Singular')
print(S)
print(type(S))
print('Right singular')
print(V)
'''
# result = np.where(S<0, 0, S) 
# print('New Singular matrix')
# print(result)
#print(U.shape)
#print(S.shape)
#print(V.shape)
T = np.zeros([324, 391])

T[0,0]  = S[0]
T[1,1]  = S[1]
T[2,2]  = S[2]

#print(T)
res  = np.dot(U,T) 
res1  = np.dot(res,V) 
print(res1)
print(res1.shape)

