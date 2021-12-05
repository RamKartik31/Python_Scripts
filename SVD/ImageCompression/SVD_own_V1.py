import cv2
import numpy as np
from sklearn.decomposition import TruncatedSVD
from PIL import Image as im 

img_path = 'nature.jpg'
img = cv2.imread(img_path, 0) # read image as grayscale. Set second parameter to 1 if rgb is required 
#data = im.fromarray(img) 
#data.save('t22.png')
U, S, V = np.linalg.svd(img)
print(U.shape)
print(V.shape)
T = np.zeros([638, 960])

T[0,0]  = S[0]


res  = np.dot(U,T) 
res1  = np.dot(res,V) 
print(type(res1))
#data = im.fromarray(res1) 
new_p = im.fromarray(res1)
new_p = new_p.convert("L")
new_p.save('t1_l1.png')

T[0,0]  = S[0]
T[1,1]  = S[1]


res  = np.dot(U,T) 
res1  = np.dot(res,V) 
print(type(res1))
#data = im.fromarray(res1) 
new_p = im.fromarray(res1)
new_p = new_p.convert("L")
new_p.save('t1_l2.png')



T[0,0]  = S[0]
T[1,1]  = S[1]
T[2,2]  = S[2]

res  = np.dot(U,T) 
res1  = np.dot(res,V) 
print(type(res1))
#data = im.fromarray(res1) 
new_p = im.fromarray(res1)
new_p = new_p.convert("L")
new_p.save('t1_l3.png')


T[0,0]  = S[0]
T[1,1]  = S[1]
T[2,2]  = S[2]
T[3,3]  = S[3]

res  = np.dot(U,T) 
res1  = np.dot(res,V) 
print(type(res1))
#data = im.fromarray(res1) 
new_p = im.fromarray(res1)
new_p = new_p.convert("L")
new_p.save('t1_l4.png')

for i in range(51):
    T[i,i]  = S[i]
# T[1,1]  = S[1]
# T[2,2]  = S[2]
# T[3,3]  = S[3]
# T[4,4]  = S[4]
# T[5,5]  = S[5]
# T[6,6]  = S[6]
# T[7,7]  = S[7]

res  = np.dot(U,T) 
res1  = np.dot(res,V) 
print(type(res1))
#data = im.fromarray(res1) 
new_p = im.fromarray(res1)
new_p = new_p.convert("L")
new_p.save('t1_l7.png')