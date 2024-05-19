# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
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

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Bicicleta.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem ) 

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()
    
# 
########################################################################
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgBase = cv.resize(imgBase,(0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)

# 
########################################################################
# Convertendo para Cinza (Requerimento)
########################################################################
#
imgCinza = cv.cvtColor(imgBase, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Buscando a Existencia de Círculos
########################################################################
#
Circulos = cv.HoughCircles (
                            imgCinza,
                            cv.HOUGH_GRADIENT,
                            dp = 0.9,
                            minDist = 300,
                            param1 = 200,
                            param2 = 40,
                            minRadius = 50, 
                            maxRadius = 400)
#print(Circulos)

# 
########################################################################
# Mostrando o Círculo
########################################################################
#
circles = np.uint16(np.around(Circulos))
imgCirculos = imgBase.copy()

for i in circles[0,:]:
#   Desenhando o círculo externo (Verde)
    cv.circle(imgCirculos,(i[0],i[1]),i[2],(0, 255, 128) ,5)

#   Desenhando o círculo interno (Vermelho)
    cv.circle(imgCirculos,(i[0],i[1]),2,(0,0,255),5)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "JanelaBase", imgCirculos )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
