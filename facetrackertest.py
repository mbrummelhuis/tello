from djitellopy import Tello
import cv2
import time
import os
from visor import VisionController

"""
Tello detects a face and tracks it at a fixed distance
"""

# frameWidth = 320
# frameHeight = 180

counter = 0
path = os.path.abspath(__file__)
path = path.removesuffix("facetrackertest.py") + "\imgs"

visor = VisionController(scaleFactor=1.05, minNeighbors=4, minSize=(30, 30))

for n in range (403):
    filename = '\img_tello_' + str(counter) + '.png'
    filename = path + filename

    img = cv2.imread(filename, cv2.COLOR_BGR2GRAY)
    img = visor.detectFace(img)

    

    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break



    counter +=1
    time.sleep(0)
    
    