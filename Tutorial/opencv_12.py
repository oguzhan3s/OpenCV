import cv2
import numpy as np
import matplotlib.pyplot as plt

"""
Gradyanlar 
-- Görüntü gradyanı, görüntüdeki yoğunluk veya renkteki yönlü bir değişikliktir.
-- Kenar algılamada kullanılır.

"""
#resmi içe aktar

img = cv2.imread("pictures/sudoku.jpg", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("orijinal img")

#x gradyan
sobelx = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0, ksize= 5)
plt.figure(), plt.imshow(sobelx, cmap = "gray"), plt.axis("off"), plt.title("sobel x ")

#x gradyan
sobely = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1, ksize= 5)
plt.figure(), plt.imshow(sobely, cmap = "gray"), plt.axis("off"), plt.title("sobel y ")
#laplace gradyan
laplacian = cv2.Laplacian(img, ddepth= cv2.CV_16S)
plt.figure(), plt.imshow(laplacian, cmap = "gray"), plt.axis("off"), plt.title("laplace "), plt.show()