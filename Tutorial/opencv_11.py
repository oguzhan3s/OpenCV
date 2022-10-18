from pickletools import uint8
from unittest import result
import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
MORFOLOJİK OPERASYONLAR

Erezyon, genişleme, açma, kapatma ve morfolojik gradyan gibi
morfolojik operasyonların ne olduklarını öğreneceğiz.

Erozyon:
Erozyonun temel fikri sadece toprak erozyonu gibidir, ön plandaki nesnenin sınırlarını aşındırır.

Genişleme:
Erozyonun tam tersidir.
Görüntüdeki beyaz bölgeyi arıtırır.

Açma:
Açılma, erozyonun + genişlemedir.
Gürültünün giderilmesinde faydalıdır.

Kapatma:
kapanış, açmanın tam tersidir.
Genişleme + erozyondur.(önce genişleme sonra erozyon işlemi yapılır)
Ön plandaki nesnelerin içindeki küçük delikleri veya nesne üzerindeki küçük siyah noktaları kapatmak için kullanışlıdır.

Morfolojik Gradyan:
Bir görüntünün genişlemesi ve erozyonu arasındaki farktır.

"""

#resmi içe aktar
img = cv2.imread("pictures/logo.jpg",0)
plt.figure(), plt.imshow(img, cmap= "gray"), plt.axis("off"), plt.title("original image")

#erozyon
kernel = np.ones((5,5), dtype=np.uint8)
result = cv2.erode(img, kernel, iterations=6)
plt.figure(), plt.imshow(result, cmap= "gray"), plt.axis("off"), plt.title("Erozyon image")

#Genişleme (dilation)
result2 = cv2.dilate(img, kernel, iterations=6)
plt.figure(), plt.imshow(result2, cmap= "gray"), plt.axis("off"), plt.title("genisleme image")

#white noise
whiteNoise = np.random.randint(0,2, size = img.shape[:2])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap="gray"), plt.axis("off"), plt.title("white noise")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap="gray"), plt.axis("off"), plt.title("img whit white noise")

#açılma
openning = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(openning, cmap="gray"), plt.axis("off"), plt.title("acilma")

#black noise
blackNoise = np.random.randint(0,2, size = img.shape[:2])
blackNoise = blackNoise*-255
plt.figure(), plt.imshow(blackNoise, cmap="gray"), plt.axis("off"), plt.title("black noise")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap="gray"), plt.axis("off"), plt.title("black noise image ")

# kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap="gray"), plt.axis("off"), plt.title("kapanma")

#gradient 
gradient =  cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap="gray"), plt.axis("off"), plt.title("grad"), plt.show() 



