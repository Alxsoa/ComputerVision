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
NomeImagem  = "Farol.jpg"
dirRaiz = Path.home()
dirBase = "Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_GRAYSCALE)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Multiplicar a Imagem por uma Constante > 1 produz imagem mais brilhante
########################################################################
#
imgOriginal = np.copy(imgBase)
for k in range(0,60):
    imgBase[:,:] = np.where(imgBase[:,:]* 1.03 < 255, (imgBase[:,:] * 1.03).astype(np.uint8) , imgBase[:,:])
    imgResultado = np.concatenate((imgOriginal, imgBase), axis=1)

    cv.imshow( "Resultado Obtido",imgResultado)
    cv.waitKey(40)

cv.waitKey()    

########################################################################
# FIM DO PROGRAMA
########################################################################
