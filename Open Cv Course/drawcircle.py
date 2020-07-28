import cv2

cap = cv2.VideoCapture(0)

mouseClicked = False
pts = (0,0)
def drawon(event,x,y,flags,param):
    global pts,mouseClicked
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseClicked = True
        pts = (x,y)
        
cv2.namedWindow("Draw")
cv2.setMouseCallback("Draw",drawon)



while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    if mouseClicked:
        cv2.circle(frame,pts,20,(0,255,255),3)
    
    cv2.imshow("Draw",frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.destroyAllWindows()