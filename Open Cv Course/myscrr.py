import cv2
import numpy as np

# greybk = np.zeros((512,512,3),dtype='int8')
img = cv2.imread("../DATA/dog_backpack.jpg")

def empty_rekt(event,x,y,flag,params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,center=(x,y),radius=50,color=(120,120,215),thickness=5)
        
cv2.namedWindow('Draw_Here')
cv2.setMouseCallback('Draw_Here',empty_rekt)

while True:
    cv2.imshow('Draw_Here',img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()