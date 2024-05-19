# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
from pathlib import Path
from skimage import io
from skimage import img_as_ubyte
import matplotlib.pyplot as plt

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
NomeImagem = "Girassol.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
try:
   imgBase = io.imread ( dirCaminhoImagem )
except:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Apresentando a Imagem (Skimage)
########################################################################
#
io.imshow(imgBase)
io.show()

# 
########################################################################
# Apresentação dos Resultados (Matplotlib)
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot (1,1,1)
plt.imshow ( imgBase )
plt.title ("Imagem Original (SkImage)")

Grafico.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
