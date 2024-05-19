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
NomeImagem  = "Casa.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
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
# Calculando a Erosão
########################################################################
#
Kernel = np.ones((3,3), np.uint8)
imgErosao = cv.dilate(imgBase, Kernel, iterations=3)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)
imgErosao = cv.cvtColor(imgErosao, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure( )

Grafico.add_subplot(1,2,1)
plt.imshow(imgBase )
plt.title("Original")

Grafico.add_subplot(1,2,2)
plt.imshow ( imgErosao )
plt.title("Resultado\nDilatação")

plt.tight_layout ()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
