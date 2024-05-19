# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

# 
########################################################################
# Funções de Apoio
########################################################################
#
def EfeitoCartoon ( imgTemporario ):
    imgBorda = cv.bitwise_not(cv.Canny(imgTemporario, 100, 200)) 
    imgCinza = cv.cvtColor(imgTemporario, cv.COLOR_BGR2GRAY)
    imgCinza = cv.medianBlur(imgCinza, 5) 
    imgDestino = cv.edgePreservingFilter(imgTemporario, flags=2, sigma_s=64, sigma_r=0.25) 
    imgResultado = cv.bitwise_and(imgDestino, imgDestino, mask=imgBorda) 
    return (imgResultado)

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
NomeImagem = "Padaria.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

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
# Aplicando o Efeito
########################################################################
#
imgReduzida = cv.resize(imgBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)
imgCartoon = EfeitoCartoon ( imgReduzida )

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
imgTodasImagens = np.hstack(( imgReduzida, imgCartoon))   

cv.imshow ( "Resultado Efeitos", imgTodasImagens)  
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
