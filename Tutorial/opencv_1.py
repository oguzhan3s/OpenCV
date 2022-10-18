import cv2
img = cv2.imread("pictures/f22.jpg",0)
print(img)
cv2.imshow("ilk resim", img)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
elif k ==ord('s'):
    cv2.imwrite("f22gray.png", img)
    cv2.destroyAllWindows()
