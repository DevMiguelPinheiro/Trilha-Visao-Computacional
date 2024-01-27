import cv2 as cv

webcam = cv.VideoCapture(0, cv.CAP_DSHOW)

detectorRostos = cv.CascadeClassifier('imagens/haarcascade_frontalface_alt.xml')

while True:
    _,frame = webcam.read()
    imgCinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    rostos = detectorRostos.detectMultiScale(imgCinza)

    for x, y, w, h in rostos:
        cv.rectangle(frame ,(x,y), (x+w,y+h), (0,255,0), 2)

    cv.imshow("img",frame)
    cv.waitKey(1)