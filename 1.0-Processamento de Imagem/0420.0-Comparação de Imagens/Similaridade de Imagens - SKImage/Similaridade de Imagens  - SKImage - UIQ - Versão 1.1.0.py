# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
from skimage.metrics import structural_similarity as compare_uiq
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

def Similaridade (imgBase, imgAlvo):
    GrauSimilaridade = compare_uiq( imgBase,  imgAlvo, channel_axis=2)
    return (GrauSimilaridade)

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem = [ 
               "Violao1.jpg", 
               "Violao2.jpg", 
               "Violao3.jpg", 
               "Violao4.jpg", 
               "Violao5.jpg", 
               "Violao6.jpg"  
            ]

dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem[0]))
dirCaminhoOpcao1 = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem[1]))
dirCaminhoOpcao2 = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem[2]))
dirCaminhoOpcao3 = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem[3]))
dirCaminhoOpcao4 = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem[4]))
dirCaminhoOpcao5 = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem[5]))

dirCaminhoOutputImagem = str(Path(dirRaiz, dirBase, dirImagem, "Violao1Output.jpg"))
dirCaminhoOutputOpcao1 = str(Path(dirRaiz, dirBase, dirImagem, "Violao2Output.jpg"))

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgViolaoOriginal = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR )
if imgViolaoOriginal is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem[0])
   exit ()


imgViolaoOpcao1 = cv.imread ( dirCaminhoOpcao1, cv.IMREAD_COLOR )
if imgViolaoOpcao1 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem[1])
   exit ()

imgViolaoOpcao2 = cv.imread ( dirCaminhoOpcao2, cv.IMREAD_COLOR )
if imgViolaoOpcao1 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem[2])
   exit ()

imgViolaoOpcao3 = cv.imread ( dirCaminhoOpcao3, cv.IMREAD_COLOR )
if imgViolaoOpcao1 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem[3])
   exit ()

imgViolaoOpcao4 = cv.imread ( dirCaminhoOpcao4, cv.IMREAD_COLOR )
if imgViolaoOpcao4 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem[4])
   exit ()

imgViolaoOpcao5 = cv.imread ( dirCaminhoOpcao5, cv.IMREAD_COLOR )
if imgViolaoOpcao5 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem[5])
   exit ()

# 
########################################################################
# Uniformizando o Tamanho das Imagens
########################################################################
#
imgViolaoOriginal = cv.resize(imgViolaoOriginal, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao1 = cv.resize(imgViolaoOpcao1, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao2 = cv.resize(imgViolaoOpcao2, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao3 = cv.resize(imgViolaoOpcao3, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao4 = cv.resize(imgViolaoOpcao4, (160, 400), interpolation = cv.INTER_AREA)
imgViolaoOpcao5 = cv.resize(imgViolaoOpcao5, (160, 400), interpolation = cv.INTER_AREA)

# 
########################################################################
# Calculo da Diferença
########################################################################
#
DiferencaOriginalImagem1 = Similaridade ( imgViolaoOriginal, imgViolaoOpcao1 )
DiferencaOriginalImagem2 = Similaridade ( imgViolaoOriginal, imgViolaoOpcao2 )
DiferencaOriginalImagem3 = Similaridade ( imgViolaoOriginal, imgViolaoOpcao3 )
DiferencaOriginalImagem4 = Similaridade ( imgViolaoOriginal, imgViolaoOpcao4 )
DiferencaOriginalImagem5 = Similaridade ( imgViolaoOriginal, imgViolaoOpcao5 )

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgViolaoOriginal = cv.cvtColor(imgViolaoOriginal, cv.COLOR_BGR2RGB)
imgViolaoOpcao1 = cv.cvtColor(imgViolaoOpcao1, cv.COLOR_BGR2RGB)
imgViolaoOpcao2 = cv.cvtColor(imgViolaoOpcao2, cv.COLOR_BGR2RGB)
imgViolaoOpcao3 = cv.cvtColor(imgViolaoOpcao3, cv.COLOR_BGR2RGB)
imgViolaoOpcao4 = cv.cvtColor(imgViolaoOpcao4, cv.COLOR_BGR2RGB)
imgViolaoOpcao5 = cv.cvtColor(imgViolaoOpcao5, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,3,1)
plt.imshow(imgViolaoOriginal )
plt.title("Original")

Grafico.add_subplot(2,3,2)
plt.imshow(imgViolaoOpcao1 )
plt.title('Grau de Similaridade\n ({:.2f})'.format(DiferencaOriginalImagem1))

Grafico.add_subplot(2,3,3)
plt.imshow(imgViolaoOpcao2 )
plt.title('Grau de Similaridade\n ({:.2f})'.format(DiferencaOriginalImagem2))

Grafico.add_subplot(2,3,4)
plt.imshow(imgViolaoOpcao3 )
plt.title('Grau de Similaridade\n ({:.2f})'.format(DiferencaOriginalImagem3))

Grafico.add_subplot(2,3,5)
plt.imshow(imgViolaoOpcao4 )
plt.title('Grau de Similaridade\n ({:.2f})'.format(DiferencaOriginalImagem4))

Grafico.add_subplot(2,3,6)
plt.imshow(imgViolaoOpcao5 )
plt.title('Grau de Similaridade\n  ({:.2f})'.format(DiferencaOriginalImagem5))

plt.tight_layout ()
plt.show ()
	
########################################################################
# FIM DO PROGRAMA
########################################################################	
