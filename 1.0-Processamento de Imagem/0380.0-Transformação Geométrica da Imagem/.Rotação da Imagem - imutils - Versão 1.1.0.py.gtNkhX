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
import imutils

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
NomeImagem  = "Gato.jpg"
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
# Rotacionando a Imagem
########################################################################
#
ImagemRotacionada = imutils.rotate(imgBase, angle=45)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)
ImagemRotacionada = cv.cvtColor(ImagemRotacionada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure ()
Grafico.add_subplot(1,2,1)
plt.imshow ( imgBase )
plt.title ("Imagem Original")

Grafico.add_subplot(1,2,2)
plt.imshow ( ImagemRotacionada )
plt.title ("Imagem Resultado")

Grafico.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
