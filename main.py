import cv2 as cv
from CascadeLoader import LoadFrontalFaceCascade
from DetectFace import PersonFace



# load the model to detect the face
frontal_face_cascade = LoadFrontalFaceCascade()
frontal_face_cascade.loadFaceCascade()


#Detect faces in the live stream
cap = cv.VideoCapture(0)
if not cap.isOpened:
    print('--(!)Error opening video capture')
    exit(0)

person_face = PersonFace()

while True:
    ret, frame = cap.read()

    if frame is None:
        print(f"Capture Failed")
        break

    # detect the face and display in the captured frame
    person_face.detect()








