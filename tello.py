from djitellopy import Tello
import cv2
import time

width = 320
height = 240


me = Tello()
me.connect()
print(me.get_battery())

me.takeoff()
print(me.get_current_state())
me.move("back",50)
me.land()

time.sleep(10)
me.takeoff()
me.move("left",50)
me.land()