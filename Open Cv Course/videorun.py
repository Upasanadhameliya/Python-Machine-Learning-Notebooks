import cv2
import time

cap = cv2.VideoCapture("myvideo.mp4")

if cap.isOpened():
    print("Successfully opened video")
else:
    print("Can't open!")
    sys.exit()
    
rate = 60
while cap.isOpened():
    ret, frame = cap.read()
    
    if ret:
        cv2.imshow("Showing A twerk",frame)
        time.sleep(1/rate)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()