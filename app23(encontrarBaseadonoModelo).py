import cv2

def encontrar_padrao(imagem, template):
    imagem_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    resultado = cv2.matchTemplate(imagem_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    _, _, _, max_loc = cv2.minMaxLoc(resultado)

    h, w = template_gray.shape
    cv2.rectangle(imagem, max_loc, (max_loc[0] + w, max_loc[1] + h), (255, 0, 0), 2)

    return imagem

imagem_principal = cv2.imread('imagens\wally\encontrar1.jpg')
template = cv2.imread('\imagens\wally\wally1.jpg')

imagem_resultado = encontrar_padrao(imagem_principal, template)

cv2.imshow('Resultado', imagem_resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()