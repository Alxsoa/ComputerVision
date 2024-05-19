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
gray_img = cv.cvtColor(ImagemBase, cv.COLOR_BGR2GRAY)
gray_img = np.float32(gray_img)

# 
########################################################################
# Executa a Correlação
########################################################################
#
imgMarcacao = cv.cornerHarris (
                                gray_img, 
                                blockSize=2, 
                                ksize=3, 
                                k=0.04
                              )

# 
########################################################################
# Dilatação para Marcação
########################################################################
#
imgMarcacao = cv.dilate(imgMarcacao, None)
ImagemBase[imgMarcacao > 0.01 * imgMarcacao.max()] = [0, 255, 0]

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
