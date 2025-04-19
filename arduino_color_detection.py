import serial 
import time 
import cv2 as cv
conexao = serial.Serial('COM3', baudrate=9600)
time.sleep(2)
webcam = cv.VideoCapture(0,cv.CAP_DSHOW)

while True :
    data = conexao.read_all().decode('ascii')
    print(data)

    if"foto"in data:
        _,frame = webcam.read()
        _,frame = webcam.read()
        media = cv.mean(frame)
        b,g,r,alpha = media
        msg ="vermelho"
        if b>g and b>r :
            msg ="azul"
        if g>b and g>r:
            msg ="verde"
        if r>g and r>b:
            msg ="vermelho"
        conexao.write(msg.encode("ascii"))
        cv.imshow('Imagem real',frame)
    tecla = cv.waitKey(1)
    if tecla==ord('q'):
        break

conexao.close()