# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import numpy as np
import cv2
from matplotlib import pyplot as plt
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
NomeImagem  = "FormasGeometricas.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Convertendo para Cinza a Imagem
########################################################################
#
imgBase  = cv2.imread(dirCaminhoImagem)

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
# Convertendo para Tons de Cinza
########################################################################
#
imgCinza = cv2.cvtColor(imgBase, cv2.COLOR_BGR2GRAY)

# 
########################################################################
# Detectando os Cornes 
########################################################################
#  
Corners = cv2.goodFeaturesToTrack(imgCinza, 29, 0.01, 10)
Corners = np.intp(Corners)
  
# 
########################################################################
# Desenhando o Indicativo do Corner
########################################################################
#
for iAux in Corners:
    xPosicao, yPosicao = iAux.ravel()
    cv2.circle(imgBase, (xPosicao, yPosicao), 5, 255, -1)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv2.cvtColor(imgBase, cv2.COLOR_BGR2RGB)  

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure( )

plt.imshow(imgBase)

plt.tight_layout ()
plt.show()
