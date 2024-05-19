# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns
import pandas as pd
import numpy as np

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
NomeImagem = "Adicao.png"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
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
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Recuperando as Dimensões da Imagem
########################################################################
#
iLinhas = imgBase.shape[0]
iColunas = imgBase.shape[1]

# 
########################################################################
# Apresentando a Matriz
########################################################################
#
Figura = plt.figure()

Grafico = Figura.add_subplot(1, 1, 1)
Grafico.imshow(imgBase, cmap='gray')
for iAux in range(iLinhas):
    for jAux in range(iColunas):
        Grafico.text(jAux, iAux, str(imgBase[iAux, jAux]).zfill(4), color='b', ha="center", va="center" )

# Grafico.set_axis_off()
Figura.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
