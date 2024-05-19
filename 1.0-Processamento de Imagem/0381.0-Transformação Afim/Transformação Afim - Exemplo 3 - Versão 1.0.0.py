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
        cv.circle(imgCartas, (x,y), 4, (0,0,255), -1)
        lstPontos.append([x, y])
        if len(lstPontos) <= 4:
            cv.imshow("Imagem Base", imgCartas)
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
NomeImagemCartas = "Cartas.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoCartas = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemCartas))

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgCartas = cv.imread ( dirCaminhoCartas, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgCartas is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagemCartas)
   exit ()

# 
########################################################################
# Captura os Pontos para Preencher a Imagem
########################################################################
#
lstPontos = []
cv.imshow("Imagem Base", imgCartas)
cv.setMouseCallback("Imagem Base", CapturaEvento)
cv.waitKey(0)

# 
########################################################################
# Informacao dos Pontos da Imagem
########################################################################
#
ptsInicial = np.float32([[781, 247], [1036, 304], [976, 705], [695, 630]])
ptsFinal = np.float32([[0,0],[300,0],[300,400],[0,400]])

# 
########################################################################
# Obtenha a matriz de transformação e Use para criar a imagem do tema
########################################################################
#
MatrizTransformacao = cv.getPerspectiveTransform(ptsInicial, ptsFinal)
imgResultado = cv.warpPerspective(imgCartas, MatrizTransformacao, (300,400))

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