import os
import cv2
from djitellopy import Tello
import numpy as np

class VisionController:
    def __init__(self, scaleFactor = 1.1, minNeighbors = 5, minSize = (40, 40)):
        self.cascPathface = os.path.dirname(cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
        self.cascPatheyes = os.path.dirname(cv2.__file__) + "/data/haarcascade_eye_tree_eyeglasses.xml"
        self.faceCascade = cv2.CascadeClassifier(self.cascPathface)
        self.eyeCascade = cv2.CascadeClassifier(self.cascPatheyes)

        self.scaleFactor = scaleFactor
        self.minNeighbors = minNeighbors
        self.minSize = minSize

        self.me = Tello()

        self.faces = None
        self.img = None
        self.targets = []

        self.me.connect()
        print(self.me.get_battery())

        self.state = "searching"

    def searchFace(self):
        """
        Yaw until a face is detected, then set state to 
        """
        if np.random.rand() < 0.5:
            self.me.rotate_clockwise()
        else:
            self.me.rotate_counter_clockwise()


    def detectFace(self,img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.faceCascade.detectMultiScale(gray, scaleFactor=self.scaleFactor, minNeighbors=self.minNeighbors, 
                                                    minSize=self.minSize, flags=cv2.CASCADE_SCALE_IMAGE)
        self.faces = faces
        self.img = img

        if faces == ():
            return self.img
        else:                                                
            for (x,y,w,h) in faces:
                cv2.rectangle(self.img, (x, y), (x + w, y + h),(0,255,0), 2)
                
            return self.img
    
    def generateControl(self):


if __name__ == "__main__":
    visor = VisionController()
    video_capture = cv2.VideoCapture(0)

    while(True):
        ret, frame = video_capture.read()
        frame = visor.detectFace(frame)
        
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()