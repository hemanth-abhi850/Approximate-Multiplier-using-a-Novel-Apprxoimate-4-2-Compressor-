import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("image1.png")

img2 = cv2.imread("image2.png")


product_img_exact = np.zeros(img1.shape)

for i in range(img1.shape[0]):
    for j in range(img1.shape[1]):
        for k in range(img1.shape[2]):

            pxl_1 = DTB(img1[i, j, k]) # each pixel converted into binary
            pxl_2 = DTB(img2[i, j, k])

            product_pxl = Binary_Multiply8(pxl_1, pxl_2)        #performing pixel to pixel multiplication using approximate multiplier
            product_img_exact[i, j, k] = decimal(product_pxl)   # again conveting from binary to decimal
product_img = (product_img_exact*255)/np.max(product_img_exact) # reback to original pixel size
product_img_exact = np.round(product_img).astype("int")
#plt.imshow(product_img)
fig = plt.imshow(product_img_exact)
#plt.savefig('comparision_plot.png', format='png')
fig.set_cmap('hot')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)





