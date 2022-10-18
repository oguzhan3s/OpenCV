import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("pictures/dag.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")


#esikleme

_, thresh_img = cv2.threshold(img, thresh=60, maxval=255, type=cv2.THRESH_BINARY) #60-255 arasını beyaz yapıyor tersi için type=cv2.THRESH_BINARY_INV
plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")


#uyarlamalı eşik değeri
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
# (resim, max value, adaptive thresh için kullanacağımız yöntem,
#  binary vieya binary_inv eşik değerini belirtir, 11 de blok_size eşik değeri hesaplamak için ,c sabitine göre ortalama alınır)
plt.figure()
plt.imshow(thresh_img2, cmap="gray")
plt.axis("off")
plt.show()