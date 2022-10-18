from tkinter import W
from turtle import width
import cv2
import numpy as np


img = cv2.imread("pictures/f22.jpg")
cv2.imshow("original",img)

width = 600
height = 400

pts1 = np.float32(([403,450], [409,282], [1003, 651], [1011, 263]))
pts2 = np.float32(([463,108], [463, 168], [width,600], [height,width]))


matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("nihai", imgOutput)



k = cv2.waitKey(0) & 0xFF
if k == 27:
    cv2.release()
    cv2.destroyAllWindows()
