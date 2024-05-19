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
NomeImagem = "Baloes.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirOutput = "Output"
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
EscalaPercentual = 0.5

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( dirCaminhoImagem )

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
# Calculando o Histograma
########################################################################
#
HistogramaAzul  = cv.calcHist([ImagemBase], [0],None,[256],[0,256])
HistogramaVerde = cv.calcHist([ImagemBase], [1],None,[256],[0,256])
HistogramaVermelho = cv.calcHist([ImagemBase], [2],None,[256],[0,256])

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
Grafico = plt.figure(figsize=(10,8))

Grafico.add_subplot(1,2,1)
plt.plot(HistogramaAzul, color = "b", label= "Azul" )
plt.plot(HistogramaVerde, color = "g", label= "Verde" )
plt.plot(HistogramaVermelho, color = "r", label= "Vermelho" )
plt.xlim([0,256])
plt.xlabel("Intensidade", fontweight='bold', fontsize=11)
plt.ylabel("# de Pixels", fontweight='bold', fontsize=11)
plt.legend ()
plt.title("Histograma", fontweight='bold', fontsize=11)

ImagemBase = cv.cvtColor(ImagemBase, cv.COLOR_BGR2RGB)
Grafico.add_subplot(1,2,2)
plt.imshow(ImagemBase )
plt.title("Imagem\nOriginal", fontweight='bold', fontsize=11)

plt.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
