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
def LimpaTerminal ( ):

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
# Convertendo de SkImage para OpenCV
########################################################################
#
imgBaseCV = img_as_ubyte(imgBase)
imgBaseCV = cv.cvtColor(imgBaseCV, cv.COLOR_RGB2BGR)

# 
########################################################################
# Apresentando a Imagem (OpenCV)
########################################################################
#
cv.imshow ( "Janela Base", imgBaseCV)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
