import cv2

img = cv2.imread("pictures/f22.jpg",0)

print("resim boyutu: ", img.shape)
cv2.imshow("original", img)

#resized
imgResized =  cv2.resize(img, (80,80))
print("yeniden : " , imgResized.shape)
cv2.imshow("yeniden şekil", imgResized)

#kırp
imgCropped = img[100,:600] # height width opencv de boyle
cv2.imshow("kırpılan resim", imgCropped)

k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.release()
    cv2.destroyAllWindows()