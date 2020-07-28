import cv2
import numpy as np
from matplotlib import cm


road = cv2.imread("../DATA/tom-and-jerry.jpg")
# road = cv2.imread("../DATA/road_image.jpg")
set2 = cm.Set2

def ret_rgb(colortup):
    x = np.array(colortup)*255
    x = [int(i) for i in x]
    return tuple(x)

colors = []

for color in set2.colors:
    colors.append(ret_rgb(color))
    
markers = np.zeros(road.shape[:2],'int32')
segments = np.zeros(road.shape,'uint8')

roadcpy = road.copy()

ncol = len(colors)
marker_changed = False
col_indx = 1

def clickFun(event,x,y,flag,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global marker_changed, col_indx
#         print(str(colindex))
#         print(str(marker_changed))
        cv2.circle(markers,(x,y),10,(col_indx),-1)
        cv2.circle(roadcpy,(x,y),10,colors[col_indx],-1)
        marker_changed = True
    
cv2.namedWindow("Road Image")
cv2.setMouseCallback("Road Image",clickFun)

while True:
    cv2.imshow("Road Image",roadcpy)
    cv2.imshow("Road Segments",segments)
    
    k = cv2.waitKey(1)
    
    if k == 27:
        break
    
    if k == ord('c'):
        roadcpy = road.copy()
        markers = np.zeros(road.shape[:2],'int32')
        segments = np.zeros(road.shape,'uint8')
        
    if k > 0:
        if chr(k).isdigit():
            num = int(chr(k))
            if num < ncol:
#                 print("Colind Changed!")
                col_indx = num
            
    if marker_changed:
        markercpy = markers.copy()
        markercpy = cv2.watershed(road,markercpy)
        
        for i in range(len(colors)):
            segments[markercpy == i] = colors[i]
        marker_changed = False
        
        
cv2.destroyAllWindows()