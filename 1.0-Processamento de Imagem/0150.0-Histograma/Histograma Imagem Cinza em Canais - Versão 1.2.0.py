# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from pathlib import Path
import os

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
NomeImagem = "Farol.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( dirCaminhoImagem, 0 ) 

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
# Gerando o Histograma
########################################################################
#
ImagemHistograma = cv.calcHist([ImagemBase], [0], None, [256], [0, 256])
ImagemBase = cv.cvtColor(ImagemBase, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(1,2,1)
plt.plot(ImagemHistograma)
plt.title("Histograma")
plt.xlabel("Intensidade", fontweight='bold', fontsize=11)
plt.ylabel("# de Pixels", fontweight='bold', fontsize=11)
plt.title("Histograma", fontweight='bold', fontsize=11)

Grafico.add_subplot(1,2,2)
plt.imshow(ImagemBase )
plt.title("Imagem Original", fontweight='bold', fontsize=11)

plt.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
