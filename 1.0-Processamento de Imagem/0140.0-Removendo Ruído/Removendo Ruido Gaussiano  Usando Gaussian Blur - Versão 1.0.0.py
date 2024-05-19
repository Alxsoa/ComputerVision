# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
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
ImagemOriginal  = 'Caravela.jpg'
ImagemRuido  = 'CaravelaRuidoGausiano.jpg'
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoOriginal = str(Path(dirRaiz, dirBase, dirImagem, ImagemOriginal))
dirCaminhoRuido = str(Path(dirRaiz, dirBase, dirImagem, ImagemRuido))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
ImagemOriginal = cv.imread ( dirCaminhoOriginal, cv.IMREAD_COLOR)
if ImagemOriginal is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", ImagemOriginal)
   exit ()

ImagemRuido = cv.imread ( dirCaminhoRuido, cv.IMREAD_COLOR)
if ImagemRuido is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", ImagemRuido)
   exit ()

# 
########################################################################
# Removendo o Ruído  
########################################################################
#
ImagemSemRuido = cv.GaussianBlur(ImagemRuido,(3,3),0)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgCaravela = cv.cvtColor(ImagemOriginal, cv.COLOR_BGR2RGB)
imgRuido = cv.cvtColor(ImagemRuido, cv.COLOR_BGR2RGB)
imgSemRuido = cv.cvtColor(ImagemSemRuido, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure( )
  
Grafico.add_subplot(1,3,1)
plt.imshow(imgCaravela )
plt.title("Original")

Grafico.add_subplot(1,3,2)
plt.imshow(imgRuido )
plt.title("Imagem Ruído")

Grafico.add_subplot(1,3,3)
plt.imshow(imgSemRuido )
plt.title("Imagem\nsem Ruído")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
