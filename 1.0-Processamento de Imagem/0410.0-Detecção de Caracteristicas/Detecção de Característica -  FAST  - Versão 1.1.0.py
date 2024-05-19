# Referencia
# https://blog.francium.tech/feature-detection-and-matching-with-opencv-5fd2394a590

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
fastDetector = cv.FastFeatureDetector_create()
fastDetector.setNonmaxSuppression(False)

# 
########################################################################
# Dilatação para Marcação
########################################################################
#
kp = fastDetector.detect(imgCinza, None)
imgResultado = cv.drawKeypoints(ImagemBase, kp, None, color=(0, 255, 0))

# 
########################################################################
# Apresenta os Resultados
########################################################################
#
cv.imshow( "Deteccao de Caracteristicas", imgResultado)
cv.waitKey()
	
########################################################################
# FIM DO PROGRAMA
########################################################################	
