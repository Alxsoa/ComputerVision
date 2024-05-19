# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
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
NomeImagem  = "Moda.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

LarguraLinha = 1
CorLinha = (0, 0, 255 )
Raio = 4

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
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgReduzida = cv.resize(imgBase, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)
nLinhas, nColunas, nCanais = imgReduzida.shape

# 
########################################################################
# Definindo os Pontos Virtuais na Imagem
########################################################################
#
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])

# 
########################################################################
# Desenhando os Pontos Virtuais na Imagem
########################################################################
#
ImagemVirtual = imgReduzida.copy()
ImagemVirtual = cv.circle(ImagemVirtual, (50, 50), Raio, CorLinha, cv.FILLED)
ImagemVirtual = cv.circle(ImagemVirtual, (200,50), Raio, CorLinha, cv.FILLED)
ImagemVirtual = cv.circle(ImagemVirtual, (50,200), Raio, CorLinha, cv.FILLED)

# 
########################################################################
# Executando a Rotação Guiada
########################################################################
#
Matriz = cv.getAffineTransform(pts1,pts2)
ImagemGuiada = cv.warpAffine(imgReduzida,Matriz,(nColunas,nLinhas))

# 
########################################################################
# Desenhando os Pontos Virtuais na Imagem Guiada
########################################################################
#
ImagemGuiada = cv.circle(ImagemGuiada, (10, 100), Raio, CorLinha, cv.FILLED)
ImagemGuiada = cv.circle(ImagemGuiada, (200,50), Raio, CorLinha, cv.FILLED)
ImagemGuiada = cv.circle(ImagemGuiada, (100,250), Raio, CorLinha, cv.FILLED)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
ImagemVirtual = cv.cvtColor(ImagemVirtual, cv.COLOR_BGR2RGB)
ImagemGuiada = cv.cvtColor(ImagemGuiada, cv.COLOR_BGR2RGB)
# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(1,3,1)
plt.imshow(imgReduzida )
plt.title("Imagem\nOriginal")

Grafico.add_subplot(1,3,2)
plt.imshow(ImagemVirtual )
plt.title("Imagem\nVirtual")

Grafico.add_subplot(1,3,3)
plt.imshow(ImagemGuiada )
plt.title("Imagem\nResutado")

Grafico.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
