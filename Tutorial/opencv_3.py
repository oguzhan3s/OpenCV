import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)


writer = cv2.VideoWriter("video_kaydı.mp4", cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))

while True:

    ret, frame = cap.read()
    cv2.imshow("video", frame)

    #save
    writer.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()