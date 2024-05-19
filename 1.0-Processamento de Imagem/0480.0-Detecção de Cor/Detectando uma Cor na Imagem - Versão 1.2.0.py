# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv 
import glob
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

def RecuperaCorPixel (event,x,y,flags,param):
    global imgCubo, imgResultado, imgMoldura
    
    if event == cv.EVENT_MOUSEMOVE:
        if ( x > 450 ): return ()
# 
########################################################################
# Identificando a Cor do Pixel
########################################################################
#        
        Cor = imgCubo[y,x]
        corAzul= int(Cor[0])
        corVerde = int(Cor[1])
        corVermelha = int(Cor[2])
        corPixel = np.dstack((corVermelha,corVerde,corAzul))

        bgr = cv.cvtColor(np.uint8(corPixel),cv.COLOR_BGR2RGB) 
        ycb = cv.cvtColor(np.uint8(corPixel),cv.COLOR_BGR2YCrCb) 
        lab = cv.cvtColor(np.uint8(corPixel),cv.COLOR_BGR2Lab) 
        hsv = cv.cvtColor(np.uint8(corPixel),cv.COLOR_BGR2HSV) 

# 
########################################################################
# Construindo a Moldura de Resultados
########################################################################
#
        imgMoldura = np.full([imgCubo.shape[0],450,3], (160, 160, 160), dtype=np.uint8)
        cv.putText(imgMoldura, "BGR {}".format(bgr[0][0]), (20, 70), cv.FONT_HERSHEY_COMPLEX, .9, (255,255,255), 1, cv.LINE_AA)
        cv.putText(imgMoldura, "HSV {}".format(hsv[0][0]), (20, 140), cv.FONT_HERSHEY_COMPLEX, .9, (255,255,255), 1, cv.LINE_AA)
        cv.putText(imgMoldura, "YCrCb {}".format(ycb[0][0]), (20, 210), cv.FONT_HERSHEY_COMPLEX, .9, (255,255,255), 1, cv.LINE_AA)
        cv.putText(imgMoldura, "LAB {}".format(lab[0][0]), (20, 280), cv.FONT_HERSHEY_COMPLEX, .9, (255,255,255), 1, cv.LINE_AA)
        
        imgResultado = np.hstack([imgCubo,imgMoldura])        
        cv.imshow("Resultado da Captura da Cor",imgResultado)
        return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "CuboMagico.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
global imgCubo, imgResultado, imgMoldura
imgBase = cv.imread( dirCaminhoImagem )
if imgBase is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Lendo e reduzindo o Tamanho da Imagem
########################################################################
#
imgCubo = cv.resize( imgBase,(450,450) )

# 
########################################################################
# Apresentando o Frame de Resultados
########################################################################
#
imgMoldura = np.full([imgCubo.shape[0],450,3], (160, 160, 160), dtype=np.uint8)
imgResultado = np.hstack([imgCubo,imgMoldura])
cv.imshow("Resultado da Captura da Cor",imgResultado)

# 
########################################################################
# Apresenta o Resultado Até o Momento
########################################################################
#
cv.namedWindow ("Resultado da Captura da Cor")
cv.setMouseCallback("Resultado da Captura da Cor", RecuperaCorPixel)

# 
########################################################################
# Loop de Controle
########################################################################
#
while(True):
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        cv.destroyAllWindows()
        break

########################################################################
# FIM DO PROGRAMA
########################################################################
        