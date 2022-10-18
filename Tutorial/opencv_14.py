
from random import gauss
import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread("pictures/dd.jpg",0)

#plt.figure(), plt.imshow(img, cmap="gray")

print(img.shape)

img_resize = cv2.resize(img, (400,400))
#plt.figure(), plt.imshow(img_resize, cmap="gray")

cv2.putText(img, "pictures/doga", (400,400), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
#plt.figure(), plt.imshow(img, cmap="gray")

_, img_thresh = cv2.threshold(img, thresh=50, maxval=255, type=cv2.THRESH_BINARY)
#plt.figure(), plt.imshow(img_thresh, cmap="gray")

img_thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure(), plt.imshow(img_thresh2, cmap="gray")

def gauus_noise(image):
    row, col, ch = image.shape
    mean  = 0
    var = 0.05
    sigma = var**0.5

    gauss = np.random.normal(mean,sigma, (row, col ,ch))
    noisy = image + gauss
    return noisy

img = cv2.imread("pictures/dd.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
#plt.figure(), plt.imshow(img)

gaussnaois = gauus_noise(img)
#plt.figure(), plt.imshow(gaussnaois)

gauss_image1 = cv2.GaussianBlur(gaussnaois, ksize=(3,3), sigmaX=7)
#plt.figure(), plt.imshow(gauss_image1), plt.show()

img = cv2.imread("pictures/logo.jpg",0)
#plt.figure(), plt.imshow(img, cmap="gray")

laplacian = cv2.Laplacian(img, ddepth= cv2.CV_16S)
#plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("laplace "), plt.show()


img = cv2.imread("pictures/dd.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hist =  cv2.calcHist([img], channels=[0], mask=None, histSize= [256], ranges=[0,256])
plt.figure(), plt.imshow(img_hist), plt.show()
