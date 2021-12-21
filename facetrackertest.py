from djitellopy import Tello
import cv2
import time
import os

"""
Tello detects a face and tracks it at a fixed distance
"""

def analyseImage(img):
    

    return img, control

# frameWidth = 320
# frameHeight = 180

counter = 0
path = os.path.abspath(__file__)
path = path.removesuffix("facetrackertest.py") + "\imgs"

for n in range (403):
    filename = '\img_tello_' + str(counter) + '.png'
    filename = path + filename

    img = cv2.imread(filename)

    # ALGO


    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break



    counter +=1
    time.sleep(0)
    
    