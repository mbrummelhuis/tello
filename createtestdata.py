from djitellopy import Tello
import cv2
import time
import os

"""
Tello detects a face and tracks it at a fixed distance
"""
frameWidth = 320
frameHeight = 180

path = os.path.abspath(__file__)
path = path.removesuffix('createtestdata.py') + "imgs"
counter = 0
print(path)
me = Tello()
me.connect()
print(me.get_battery())

me.streamoff()
me.streamon()

while(True):
    filename = path + '\img_tello_' + str(counter) + '.png'

    print(filename)

    # Get Tello image
    frame_read = me.get_frame_read()
    currentFrame = frame_read.frame
    img = cv2.resize(currentFrame, (frameWidth, frameHeight))

    cv2.imshow("MyResult", img)
    cv2.imwrite(filename, img)
    counter +=1
    time.sleep(0.04)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break 
    