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
imgJantarMax = (imgJantar*1.0 / imgJantar.mean(axis=(0,1)))
imgJantarMax = np.clip(imgJantarMax, 0, 1)

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
plt.imshow(imgJantarMax )
plt.title("Imagem Balanceada", fontsize=11, weight='bold' )
plt.xticks(np.arange(0, 2737, 500))

plt.tight_layout()
plt.show ()


########################################################################
# FIM DO PROGRAMA
########################################################################
