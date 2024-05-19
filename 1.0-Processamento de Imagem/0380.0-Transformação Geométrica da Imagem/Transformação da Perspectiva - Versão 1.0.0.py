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
LarguraLinha = 1
CorLinha = (0, 0, 255 )
Raio = 4

NomeImagem  = "Mapa.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
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
#pts1 = np.float32([[104,524],[315,476],[101,139], [318,126]])
pts1 = np.float32([[101,139], [318,126], [104,524],[315,476]])
pts2 = np.float32([[0,0],[400,0],[0,400],[400,400]])

# 
########################################################################
# Desenhando os Pontos Virtuais na Imagem
########################################################################
#
ImagemVirtual = imgReduzida.copy()
ImagemVirtual = cv.circle(ImagemVirtual, (104,524), Raio, CorLinha, cv.FILLED)
ImagemVirtual = cv.circle(ImagemVirtual, (315,476), Raio, CorLinha, cv.FILLED)
ImagemVirtual = cv.circle(ImagemVirtual, (101,139), Raio, CorLinha, cv.FILLED)
ImagemVirtual = cv.circle(ImagemVirtual, (318,126), Raio, CorLinha, cv.FILLED)

# 
########################################################################
# Executando a Rotação Guiada
########################################################################
#
Matriz = cv.getPerspectiveTransform(pts1,pts2)
ImagemGuiada = cv.warpPerspective(ImagemVirtual,Matriz,(400,400))

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
plt.title("Imagen \nResultado")

Grafico.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
