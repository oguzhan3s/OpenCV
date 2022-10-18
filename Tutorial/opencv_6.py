import cv2
import numpy as np

img = cv2.imread("pictures/f22.jpg")
cv2.imshow("orijin", img)

#yatay
hor = np.hstack((img,img))
cv2.imshow("horizontal",hor)

#dikey
ver = np.vstack((img,img))
cv2.imshow("vertical", ver)



k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.release()
    cv2.destroyAllWindows()
