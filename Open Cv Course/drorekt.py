import cv2

cap = cv2.VideoCapture(0)

firstClick = False
secondClick = False
upperLeft = (0,0)
lowerRight= (0,0)

def drawrekt(event,x,y,flags,param):
    global firstClick,secondClick,upperLeft,lowerRight
    if event == cv2.EVENT_LBUTTONDOWN:
        if (not firstClick) & (not secondClick):
            firstClick = True
            upperLeft = (x,y)
        elif firstClick & (not secondClick):
            secondClick = True
            lowerRight = (x,y)
        else:
            firstClick = False
            secondClick = False

cv2.namedWindow("Rekt")
cv2.setMouseCallback("Rekt",drawrekt)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    
    if firstClick & secondClick:
        cv2.rectangle(frame,upperLeft,lowerRight,(255,0,0),3)
    
    cv2.imshow("Rekt",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()