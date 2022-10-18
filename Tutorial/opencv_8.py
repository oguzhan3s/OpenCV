import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("pictures/tank1.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("pictures/tank2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (640, 360))
print(img1.shape)

img2 = cv2.resize(img2, (640, 360))
print(img2.shape)
"""

plt.figure()
plt.imshow(img1)


plt.figure()
plt.imshow(img2)
plt.show()
"""
# karıştırılmış resim = alpha*img1 + beta*img2

blended = cv2.addWeighted(src1 = img1, alpha=0.1, src2=img2, beta = 0.2, gamma=0)
plt.figure()
plt.imshow(blended)
plt.show()


