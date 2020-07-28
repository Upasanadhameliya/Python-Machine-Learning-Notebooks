import cv2
import numpy as np

drawing = False
ix,iy = -1,-1


def draw_rekt(event,x,y,flag,params):
    global drawing,ix,iy
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(255,127,99),thickness=2)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),color=(255,127,99),thickness=2)

        

cv2.namedWindow('rekt')

cv2.setMouseCallback('rekt',draw_rekt)

img = np.zeros((512,512,3),dtype='int8')
while True:
    cv2.imshow('rekt',img)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()