# Referencia
# https://blog.francium.tech/feature-detection-and-matching-with-opencv-5fd2394a590

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeImagemBase = "CaracteristicaCarro.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
ImagemBase = cv.imread ( CaminhoImagem + NomeImagemBase, cv.IMREAD_COLOR )
ImagemBase = cv.resize(ImagemBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemBase is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagemBase)
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
sift = cv.SIFT_create()
kp = sift.detect (imgCinza, None)

# 
########################################################################
# Dilatação para Marcação
########################################################################
#
CorLinha = (0, 255, 0)
LarguraLinha = 1
imgResultado = cv.drawKeypoints ( 
                                    ImagemBase,
                                    kp,
                                    imgCinza
                                )

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
