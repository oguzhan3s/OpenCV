import cv2
import time

video_name = "videos/capadokia.mp4"

cap = cv2.VideoCapture(video_name)

#print("genişlik: ",cap.get(3))
#print("yükseklik: ",cap.get(4))

"""
if cap.isOpened() == False:
    print("hata")
"""

while True:

    ret, frame = cap.read()

    if ret == True:

        #time.sleep(0.01) #kullanmaz isek çok hızlı akar

        cv2.imshow("ilk video", frame) 
    else : 
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


