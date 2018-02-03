# -*- coding: utf-8 -*-

import cv2

class VideoCamera(object):
    
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        success, image = self.video.read()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.3, 5)
        for (a,b,x,y) in faces:
            cv2.rectangle(image,(a,b),(a+x,b+y),(255, 0, 0), 2)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
    