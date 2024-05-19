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
NomeImagem  = "IngridGomes.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
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
# Reduzindo a Imagem e Criando a Máscara
########################################################################
#
imgReduzida = cv.resize(imgBase, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)
imgMascara  = np.zeros_like(imgReduzida)

iPosX = 10
iPosY = 40
iLargura = 40
iAltura = 40
for iAux in range (0,17):
    cv.rectangle(imgMascara, ( iPosX, 50), (iPosY, 800), (255, 255, 255), thickness=-1)
    iPosX = iPosX + iLargura
    iPosY = iPosY + iAltura

# 
########################################################################
# Aplicando a Máscara
########################################################################
#
imgResultado = bitwiseAnd = cv.bitwise_and(imgReduzida, imgMascara)

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
cv.imshow ( "Janela Resultado", imgResultado)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
