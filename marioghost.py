from djitellopy import Tello
import cv2
import time

"""
Tello detects a face and flies towards it when face is turned away. Tello stops when looking at him.
"""
frameWidth = 320
frameHeight = 180

me = Tello()
me.connect()
print(me.get_battery())

me.streamoff()
me.streamon()

while(True):

    # Get Tello image
    frame_read = me.get_frame_read()
    currentFrame = frame_read.frame
    img = cv2.resize(currentFrame, (frameWidth, frameHeight))

    cv2.imshow("MyResult", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break
    