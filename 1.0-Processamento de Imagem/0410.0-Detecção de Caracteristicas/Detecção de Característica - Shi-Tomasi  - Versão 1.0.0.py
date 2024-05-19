# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
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
NomeImagem  = "CaracteristicaCarro.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
ImagemBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR )
ImagemBase = cv.resize(ImagemBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemBase is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Convertendo para Tons de Cinza
########################################################################
#
imgCinza = cv.cvtColor(ImagemBase, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Executa a Correlação
########################################################################
#
lstPontos = cv.goodFeaturesToTrack (
                                      imgCinza, 
                                      maxCorners=50,      
                                      qualityLevel=0.02, 
                                      minDistance=20
                                   )
corners = np.float32(lstPontos)

# 
########################################################################
# Dilatação para Marcação
########################################################################
#
CorLinha = (0, 255, 0)
LarguraLinha = 1

for Elementos in lstPontos:
    x, y = Elementos [0]
    PontoCentral = ( int(x), int(y) )
    ImagemBase = cv.circle(ImagemBase, PontoCentral, 6, CorLinha , LarguraLinha)

# 
########################################################################
# Apresenta os Resultados
########################################################################
#
cv.imshow( "Deteccao de Caracteristicas", ImagemBase)
cv.waitKey()
	
########################################################################
# FIM DO PROGRAMA
########################################################################	
