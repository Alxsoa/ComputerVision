# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
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
NomeImagem = "Caravela.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem )

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
Altura, Largura = imgBase.shape[:2]

# 
########################################################################
# Definindo os Pontos Origem e Destino
########################################################################
#
ptsInicial = np.float32([[0,0], [Largura-1,0], [0,Altura-1]])
output_pts = np.float32([[Largura-1,0], [0,0], [Largura-1,Altura-1]])

# 
########################################################################
# Calculate the transformation matrix
########################################################################
#
Matriz = cv.getAffineTransform(ptsInicial , output_pts)

# 
########################################################################
# Apply the affine transformation
########################################################################
#
imgResultado = cv.warpAffine(imgBase, Matriz, (Largura,Altura))

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)
imgResultado = cv.cvtColor(imgResultado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure ()
Grafico.add_subplot (1,2,1)
plt.imshow ( imgBase )
plt.title ("Imagem Original")

Grafico.add_subplot (1,2,2)
plt.imshow ( imgResultado )
plt.title ("Imagem Transformada")

Grafico.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
