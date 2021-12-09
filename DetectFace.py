import cv2 as cv
from CascadeLoader import LoadFrontalFaceCascade

class PersonFace:
    def __init__(self, frame):
        self.frame = frame
        self.faceCascade = LoadFrontalFaceCascade.getFaceCascade()
        self.x = 0
        self.y = 0
        self.w = 0
        self.h = 0

    def detect(self):
        gray_frame = cv.cvtColor(self.frame, cv.COLOR_BGR2GRAY)
        gray_frame = cv.equalizeHist(gray_frame)

        faces = self.faceCascade.detectMultiScale3(gray_frame)

        for (x, y, w, h) in faces:
            center = (x + w // 2, y + h // 2)
            self.frame = cv.ellipse(self.frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
            cv.imshow('Capture - Face detection', self.frame)









