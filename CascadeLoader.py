import cv2 as cv
import Config


class LoadFrontalFaceCascade:
    def __init__(self):
        self.haar_face_cascade = Config.HAAR_FACE_CASCADE_PATH
        self.faceCascade = cv.CascadeClassifier()


    def loadFaceCascade(self):
        if not self.faceCascade.load(cv.samples.findFile(self.haar_face_cascade)):
            print(f"Loading the Cascade failed")
            exit(0)
        else:
            return True

    def getFaceCascade(self):
        return self.faceCascade







