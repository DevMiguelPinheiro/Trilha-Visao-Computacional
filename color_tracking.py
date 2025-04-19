import cv2
import numpy as np

def detectar_cor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cor_pixel = frame_hsv[y, x]
        detectar_cor_selecionada(cor_pixel, x, y)

def detectar_cor_selecionada(cor_pixel, x, y):
    limite_inferior = np.array([cor_pixel[0] - 10, cor_pixel[1] - 40, cor_pixel[2] - 40])
    limite_superior = np.array([cor_pixel[0] + 10, cor_pixel[1] + 40, cor_pixel[2] + 40])

    mascara = cv2.inRange(frame_hsv, limite_inferior, limite_superior)

    resultado = cv2.bitwise_and(frame, frame, mask=mascara)

    cv2.imshow('Imagem Original', frame)
    cv2.imshow('Cor Selecionada', resultado)
    print(f'Coordenadas: x={x}, y={y}, Cor (HSV): {cor_pixel}')

webcam = cv2.VideoCapture(0)

if not webcam.isOpened():
    print('Erro ao abrir a webcam.')
    exit()

cv2.namedWindow('Imagem Original')
cv2.setMouseCallback('Imagem Original', detectar_cor)

while True:
    ret, frame = webcam.read()

    if not ret:
        print('Erro ao capturar o quadro.')
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('Imagem Original', frame)

    if cv2.waitKey(1) == 27:
        break

webcam.release()
cv2.destroyAllWindows()