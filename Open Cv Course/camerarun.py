import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter("myvideo.mp4",cv2.VideoWriter_fourcc(*'VIDX'),60,(width,height))

while True:
    ret,frame = cap.read()
    
    # FOR BLACK AND WHITE VIDEO
#     frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
    
    # FOR FLIPPING THE  VIDEO
    frame = cv2.flip(frame,1)
    
    writer.write(frame)
    cv2.imshow('My Cam',frame)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()