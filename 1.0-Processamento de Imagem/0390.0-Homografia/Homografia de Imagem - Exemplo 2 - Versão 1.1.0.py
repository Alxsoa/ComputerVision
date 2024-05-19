# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
from pathlib import Path

# 
########################################################################
# Funções de Apoio
########################################################################
#
def LimpaTerminal ():
    if os.name == "nt":
       _ = os.system( "cls" )
    else:
      _ = os.system( "clear ")
    return ()

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
NomeImagemOutDoor = "OutDoor.jpg"
NomeImagemPikachu = "Pikachu.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoOutDoor = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemOutDoor))
dirCaminhoPikachu = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemPikachu))

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgOutDoor = cv.imread ( dirCaminhoOutDoor, cv.IMREAD_COLOR)
imgPikachu = cv.imread ( dirCaminhoPikachu, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgOutDoor is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagemOutDoor)
   exit ()

if imgPikachu is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagemPikachu)
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
lstPontosOrdenados = OrdenaPontos (lstPontos)
AlturaOutDoor, LarguraOutDoor, c_base = imgOutDoor.shape
AlturaPikachu, LarguraPikachu = imgPikachu.shape[:2]

ptsInicial = np.float32([[0, 0], [LarguraPikachu, 0], [LarguraPikachu, AlturaPikachu], [0, AlturaPikachu]])
ptsFinal = np.float32(lstPontosOrdenados)

# 
########################################################################
# Obtenha a matriz de transformação e Use para criar a imagem do tema
########################################################################
#
MatrizTransformacao = cv.getPerspectiveTransform(ptsInicial, ptsFinal)
imgTransformada = cv.warpPerspective(imgPikachu, MatrizTransformacao, (LarguraOutDoor, AlturaOutDoor))

# 
########################################################################
# Cria a Máscara
########################################################################
#
Mascara = np.zeros(imgOutDoor.shape, dtype=np.uint8)
RegiaoInteresse = np.int32(lstPontosOrdenados)

# 
########################################################################
# Preenche a Região Selecionada com a Cor Branca
########################################################################
#
imgPreenchida = Mascara.copy()
cv.fillConvexPoly(imgPreenchida, RegiaoInteresse, (255, 255, 255))

# 
########################################################################
# Inverte a Máscara 
########################################################################
#
MascaraInvertida = cv.bitwise_not(imgPreenchida)

# 
########################################################################
# Bitwise AND Aplicada a Máscara na Imagem Base
########################################################################
#
imgMascara = cv.bitwise_and(imgOutDoor, MascaraInvertida)

# 
########################################################################
# Bitwise OR para juntar as Duas Imagens
########################################################################
#
imgResultado = cv.bitwise_or(imgTransformada, imgMascara)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow( "Imagem Resultado", imgResultado)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
