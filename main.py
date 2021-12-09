import cv2 as cv
from CascadeLoader import LoadFrontalFaceCascade



# load the model to detect the face
frontal_face_cascade = LoadFrontalFaceCascade()
frontal_face_cascade.loadFaceCascade()



