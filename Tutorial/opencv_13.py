import cv2
import matplotlib.pyplot as plt
import numpy as np

"""
histogram
-- görüntü histogramı, dijital görüntüdeki ton dağılımının grafiksel bir temsili olarak
işlev gören bir histogram türüdür.
-- her bir ton değeri için piksel sayısını içerir.
-- belirli bir görüntü için histograma bakılarak, ton sağılımı anlaşılabilir.

"""
img = cv2.imread("pictures/f22.jpg")
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#plt.figure(), plt.imshow(img_vis)

print(img.shape)

img_hist = cv2.calcHist([img], channels=[0], mask=None, histSize= [256], ranges=[0,256])
print(img_hist.shape)
#plt.figure(), plt.imshow(img_hist)

color = ("b", "g", "r")
#plt.figure()
for i, c in enumerate(color):

    hist = cv2.calcHist([img], channels=[i], mask=None, histSize= [256], ranges=[0,256])
    #plt.plot(hist, color = c)


golden_gate = cv2.imread("pictures/kopru.jpg")
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
#plt.figure(), plt.imshow(golden_gate_vis)

print(golden_gate.shape)

mask = np.zeros(golden_gate.shape[:2], np.uint8)
#plt.figure(), plt.imshow(mask, cmap="gray"), plt.show()

mask[300:900, 600:900] = 255
#plt.figure(), plt.imshow(mask, cmap="gray")

masked_img_vis = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask = mask)
#plt.figure(), plt.imshow(masked_img_vis, cmap="gray")

masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask = mask)
masked_img_hist = cv2.calcHist([golden_gate], channels=[0], mask=mask, histSize= [256], ranges=[0,256])
#plt.figure(), plt.plot(masked_img_hist), plt.show()


#histogram eşitleme
#karşıtlık artırma
img = cv2.imread("pictures/soluk.jpg",0)
plt.figure(), plt.imshow(img, cmap = "gray")

img_hist =  cv2.calcHist([img], channels=[0], mask=None, histSize= [256], ranges=[0,256])
plt.figure(), plt.imshow(img_hist)

eq_hist = cv2.equalizeHist(img)
plt.figure(), plt.imshow(eq_hist, cmap="gray")

eq_img_hist =  cv2.calcHist([img], channels=[0], mask=None, histSize= [256], ranges=[0,256])
plt.figure(), plt.imshow(eq_img_hist), plt.show()
