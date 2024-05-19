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
NomeJanela = "Imagem Base"
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
# Convertendo de SkImage para OpenCV
########################################################################
#
imgBaseCV = img_as_ubyte(imgBase)
imgBaseCV = cv.cvtColor(imgBaseCV, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem (Skimage)
########################################################################
#
io.imshow(imgBaseCV)
io.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
