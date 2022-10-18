import cv2
import numpy as np

#resim olustur
img = np.zeros((512,512,3), np.uint8) #siyah bir resim
print(img.shape)

cv2.imshow("siyah", img)

#çizgi
cv2.line(img, (100,100), (412,100), (0,255,0), 3)  # (resim, baslangıç noktası,bitis noktası, renk, kalınlık )
cv2.imshow("cizgi", img)

#dikdörtgen
# (resim, başlangıc , biris, renk )
cv2.rectangle(img, (0,0), (256,256), (255,0,0), cv2.FILLED)
cv2.imshow("dikdortgen",img)

#cember
# (resim, merkez, yarıcap , renk)
cv2.circle(img, (300,300), 45, (0,0,255))
cv2.imshow("cember", img)

#metin
#(resim, baslangıc noktası, font, kalınlığı, renk)
cv2.putText(img, "resim", (350,350), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow("yazi", img)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.release()
    cv2.destroyAllWindows()
