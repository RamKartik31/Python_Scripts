import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import seaborn as sns
# %matplotlib inline

# ny_file = "5_Boroughs_Labels_New_York_City_Map.svg.png"
ny_file = "oneplus.jpg"
img = Image.open(ny_file)
# view the image from Python
# img.show()
print(img.size)

# img_data = img.getdata(band=0)
red_band =img.getdata(band=0)
print(type(red_band))

# convert to numpy array 
img_mat = np.array(list(red_band), float) 
print(type(img_mat))
print(img_mat.size)

# get image shape
img_mat.shape = (img.size[1], img.size[0])
# conver to 1d-array to matrix
img_mat = np.matrix(img_mat)
print('img_mat')
print(img_mat)

# plt.imshow(img_mat)
plt.show()

fig, axs = plt.subplots(1, 2,figsize=(10,10))
axs[0].imshow(img)
axs[0].set_title('Original Image', size=16)
axs[1].imshow(img_mat)
axs[1].set_title(' "R" band image', size=16)
plt.tight_layout()
plt.savefig('Original_image_and_R_band_image_for_SVD.jpg',dpi=150)

# scale the image matrix befor SVD
img_mat_scaled= (img_mat-img_mat.mean())/img_mat.std()
print('img_mat_scaled')
print(img_mat_scaled)

# Perform SVD using np.linalg.svd
U, s, V = np.linalg.svd(img_mat_scaled) 
print(U.shape)
print(s.shape)
print(V.shape)

print(s)

# Compute Variance explained by each singular vector
var_explained = np.round(s**2/np.sum(s**2), decimals=3)
print(var_explained[0:20])

sns.barplot(x=list(range(1,21)),
            y=var_explained[0:20], color="dodgerblue")
plt.xlabel('Singular Vector', fontsize=16)
plt.ylabel('Variance Explained', fontsize=16)
plt.tight_layout()
plt.savefig('svd_scree_plot.png',dpi=150)
#plt.savefig("Line_Plot_with_Pandas_Python.jpg")

num_components = 5
reconst_img_5 = np.matrix(U[:, :num_components]) * np.diag(s[:num_components]) * np.matrix(V[:num_components, :])
plt.imshow(reconst_img_5)
plt.savefig('reconstructed_image_with_5_SVs.png',dpi=150)

num_components = 50
reconst_img_50 = np.matrix(U[:, :num_components]) * np.diag(s[:num_components]) * np.matrix(V[:num_components, :])
plt.imshow(reconst_img_50)
plt.title('Reconstructed Image: 50 SVs', size=16)
plt.savefig('reconstructed_image_with_50_SVs.png',dpi=150)

num_components = 100
reconst_img_100 = np.matrix(U[:, :num_components]) * np.diag(s[:num_components]) * np.matrix(V[:num_components, :])
plt.imshow(reconst_img_100)
plt.title('Reconstructed Image: 100 SVs', size=16)
plt.savefig('reconstructed_image_with_100_SVs.png',dpi=150)

num_components = 600
reconst_img_600 = np.matrix(U[:, :num_components]) * np.diag(s[:num_components]) * np.matrix(V[:num_components, :])
plt.imshow(reconst_img_600)
plt.title('Reconstructed Image: 600 SVs', size=16)
plt.savefig('reconstructed_image_with_600_SVs.png',dpi=150)

fig, axs = plt.subplots(2, 2,figsize=(10,10))
axs[0, 0].imshow(reconst_img_5)
axs[0, 0].set_title('Reconstructed Image: 5 SVs', size=16)
axs[0, 1].imshow(reconst_img_50)
axs[0, 1].set_title('Reconstructed Image: 50 SVs', size=16)
axs[1, 0].imshow(reconst_img_100)
axs[1, 0].set_title('Reconstructed Image: 100 SVs', size=16)
axs[1, 1].imshow(reconst_img_600)
axs[1, 1].set_title('Reconstructed Image: 600 SVs', size=16)
plt.tight_layout()
plt.savefig('reconstructed_images_using_different_SVs.jpg',dpi=150)

plt.show()

