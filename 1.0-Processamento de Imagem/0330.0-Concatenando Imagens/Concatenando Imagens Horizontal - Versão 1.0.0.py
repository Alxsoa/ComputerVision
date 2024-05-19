# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
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
ImagemCarro1 = "Audi.jpg"
ImagemCarro2 = "Carro.jpeg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoCarro1 = str(Path(dirRaiz, dirBase, dirImagem, ImagemCarro1))
dirCaminhoCarro2 = str(Path(dirRaiz, dirBase, dirImagem, ImagemCarro2))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
imgCarro1 = cv.imread ( dirCaminhoCarro1, cv.IMREAD_COLOR)
if imgCarro1 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", ImagemCarro1)
   exit ()

imgCarro2 = cv.imread ( dirCaminhoCarro2, cv.IMREAD_COLOR)
if imgCarro2 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", ImagemCarro2)
   exit ()

# 
########################################################################
# Padronizando o Tamanho das Imagens
########################################################################
#
imgPadraoCarro1 = cv.resize(imgCarro1, (500, 500) , interpolation = cv.INTER_AREA) 
imgPadraoCarro2 = cv.resize(imgCarro2, (500, 500) , interpolation = cv.INTER_AREA) 

# 
########################################################################
# Concatenando Verticalmente as Imagens
########################################################################
#
imgConcatenada = cv.hconcat([imgPadraoCarro1, imgPadraoCarro2])
imgConcatenada = cv.cvtColor(imgConcatenada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure()
Grafico.add_subplot(1,1,1)
plt.imshow(imgConcatenada)
plt.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
