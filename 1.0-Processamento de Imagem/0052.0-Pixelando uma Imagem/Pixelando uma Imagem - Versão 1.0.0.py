# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
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

def CenarioInterpolacaoImagem ( imgOriginal, imgDobro, imgMetade, strTituloDobro, strTituloMetade ):
    Grafico = plt.figure( )

    Grafico.add_subplot(1,3,1)
    plt.imshow(imgOriginal )
    plt.title("Original")

    Grafico.add_subplot(1,3,2)
    plt.imshow(imgDobro )
    plt.title(strTituloDobro)

    Grafico.add_subplot(1,3,3)
    plt.imshow(imgMetade )
    plt.title(strTituloMetade)
    
    plt.tight_layout()
    plt.show ()
    return ()


# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Homem.jpg"
dirRaiz = Path.home()
dirBase = "Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
pixelLargura = 16
pixelAltura = 16

# 
########################################################################
# Lendo e Reduzindo a Imagem
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
# Pixelando a Imagem
########################################################################
#
iAltura, iLargura = imgBase.shape[:2]
imgTemporaria = cv.resize(imgBase, (pixelLargura, pixelAltura), interpolation=cv.INTER_LINEAR)
imgResultado = cv.resize(imgTemporaria, (iLargura, iAltura ), interpolation=cv.INTER_NEAREST)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor ( imgBase, cv.COLOR_BGR2RGB )
imgResultado = cv.cvtColor ( imgResultado, cv.COLOR_BGR2RGB )

# 
########################################################################
# Apresentação do Resultado
########################################################################
#
Grafico = plt.figure( )

Grafico.add_subplot(1,2,1)
plt.imshow(imgBase )
plt.title("Imagem Original")

Grafico.add_subplot(1,2,2)
plt.imshow(imgResultado )
plt.title( "Imagem Pixelada")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
				  