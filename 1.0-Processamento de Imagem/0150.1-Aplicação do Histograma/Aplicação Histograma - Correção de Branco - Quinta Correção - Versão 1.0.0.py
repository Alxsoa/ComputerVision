# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os
from pathlib import Path
from skimage import img_as_ubyte

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
NomeImagem = "Jantar.jpg"
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
# Convertendo para Matplotlib
########################################################################
#
imgJantar = cv.cvtColor ( imgBase, cv.COLOR_BGR2RGB )

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,2,1)
plt.imshow(imgJantar )
plt.title("Imagem Original", fontsize=11, weight='bold' )
plt.xticks(np.arange(0, 2737, 500))

Grafico.add_subplot(2,2,2)
imgJantar = ((imgJantar * (imgJantar.mean() / imgJantar.mean(axis=(0, 1)))).clip(0, 255).astype(int))
plt.imshow(imgJantar )
plt.title("Imagem Balanceada", fontsize=11, weight='bold' )
plt.xticks(np.arange(0, 2737, 500))

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
