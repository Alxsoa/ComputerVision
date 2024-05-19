# Referencia
# https://github.com/GSNCodes/Image_Overlaying_Using_Perspective_Transform/blob/master/main.py

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os

# 
########################################################################
# Funções de Apoio
########################################################################
#
def CapturaEvento (event, x, y, flags, params):

    if event == cv.EVENT_LBUTTONDOWN:
        cv.circle(imgOutDoorSemPontos, (x,y), 4, (0,0,255), -1)
        lstPontos.append([x, y])
        if len(lstPontos) <= 4:
            cv.imshow("Imagem Base", imgOutDoorSemPontos)

    return ()


# 
########################################################################
# Ordena os Pontos da Superior-Esquerda, Superior-Direita, 
# Inferior-Direita, Inferior-Esquerda
########################################################################
#
def OrdenaPontos (lstPontos):
    ptsOrdenado = np.zeros((4, 2), dtype="float32")
    s = np.sum(lstPontos, axis=1)
    ptsOrdenado[0] = lstPontos[np.argmin(s)]
    ptsOrdenado[2] = lstPontos[np.argmax(s)]

    diff = np.diff(lstPontos, axis=1)
    ptsOrdenado[1] = lstPontos[np.argmin(diff)]
    ptsOrdenado[3] = lstPontos[np.argmax(diff)]

    return (ptsOrdenado)

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeImagemOutDoor = "OutDoor.jpg"
NomeVideo = "EscritorioComposto.mp4"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 
CaminhoVideo = CaminhoBase + "Videos/" 

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgOutDoor = cv.imread ( CaminhoImagem + NomeImagemOutDoor, cv.IMREAD_COLOR)
if imgOutDoor is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagemOutDoor)
    exit ()

# 
########################################################################
# Lendo o Vídeo
########################################################################
#
VideoEscritorio = cv.VideoCapture ( CaminhoVideo+NomeVideo )
if not VideoEscritorio.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", NomeVideo)
    exit ()


# 
########################################################################
# Captura os Pontos para Preencher a Imagem
########################################################################
#
lstPontos = []
imgOutDoorSemPontos = imgOutDoor.copy()
cv.imshow("Imagem Base", imgOutDoorSemPontos)
cv.setMouseCallback("Imagem Base", CapturaEvento)
cv.waitKey(0)
cv.destroyAllWindows()

# 
########################################################################
# Informacao dos Pontos da Imagem
########################################################################
#

while(VideoEscritorio.isOpened()):
    Status, VideoFrame = VideoEscritorio.read()
    if Status == True:
        lstPontosOrdenados = OrdenaPontos (lstPontos)
        AlturaOutDoor, LarguraOutDoor, CorOutdoor = imgOutDoor.shape
        AlturaVideo, LarguraVideo = VideoFrame.shape[:2]

        ptsInicial = np.float32([[0, 0], [LarguraVideo, 0], [LarguraVideo, AlturaVideo], [0, AlturaVideo]])
        ptsFinal = np.float32(lstPontosOrdenados)

        MatrizTransformacao = cv.getPerspectiveTransform(ptsInicial, ptsFinal)
        imgTransformada = cv.warpPerspective(VideoFrame, MatrizTransformacao, (LarguraOutDoor, AlturaOutDoor))

        Mascara = np.zeros(imgOutDoor.shape, dtype=np.uint8)
        RegiaoInteresse = np.int32(lstPontosOrdenados)

        imgPreenchida = Mascara.copy()
        cv.fillConvexPoly(imgPreenchida, RegiaoInteresse, (255, 255, 255))

        MascaraInvertida = cv.bitwise_not(imgPreenchida)
        imgMascara = cv.bitwise_and(imgOutDoor, MascaraInvertida)
        imgResultado = cv.bitwise_or(imgTransformada, imgMascara)

        cv.imshow( "Imagem Resultado", imgResultado)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else: 
        break

cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
