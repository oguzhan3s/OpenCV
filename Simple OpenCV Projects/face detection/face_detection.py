from unittest import result
import cv2
import mediapipe as mp

cap = cv2.VideoCapture("videos/facevideo3.mp4")

mpFaceDetection =  mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection()

mpDraw = mp.solutions.drawing_utils


while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    resultS = faceDetection.process(imgRGB)

    #print(resultS.detections)

    if resultS.detections:
        for id, detection in enumerate(resultS.detections):
            bboxC = detection.location_data.relative_bounding_box
            #print(bboxC)

            h, w, _ = img.shape
            bbox = int(bboxC.xmin*w), int(bboxC.ymin*h), int(bboxC.width*w), int(bboxC.height*h)
            #print(bbox)
            cv2.rectangle(img, bbox, (0,255,255),2)
            
    cv2.imshow("img", img)
    
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
