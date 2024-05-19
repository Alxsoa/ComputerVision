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
NomeImagem  = "Mulher.jpg"
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
# Recuperando Dados da Imagem
########################################################################
#
imgReduzida = cv.resize(imgBase, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)
Linhas, Colunas, Canais = imgReduzida.shape

# 
########################################################################
# Definindo a Translação
# np.float32([[1,0,tx],[0,1,ty]]) 
# tx e ty Definem a translação
########################################################################
#
tEsquerda = np.float32([[1,0,-50],[0,1,0]])
tDireita  = np.float32([[1,0,50],[0,1,0]])
tSuperior = np.float32([[1,0,0],[0,1,50]])
tInferior = np.float32([[1,0,0],[0,1,-50]])

# 
########################################################################
# Translação da Imagem
# (Colunas, Linhas) Define onde ficará a imagem
########################################################################
#
imgEsquerda = cv.warpAffine(imgReduzida,tEsquerda,(Colunas, Linhas))
imgDireita  = cv.warpAffine(imgReduzida,tDireita, (Colunas, Linhas))
imgSuperior = cv.warpAffine(imgReduzida,tSuperior,(Colunas, Linhas))
imgInferior = cv.warpAffine(imgReduzida,tInferior,(Colunas, Linhas))

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgEsquerda = cv.cvtColor (imgEsquerda, cv.COLOR_BGR2RGB)
imgDireita  = cv.cvtColor (imgDireita,  cv.COLOR_BGR2RGB)
imgSuperior = cv.cvtColor (imgSuperior, cv.COLOR_BGR2RGB)
imgInferior = cv.cvtColor (imgInferior, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,2,1)
plt.imshow(imgEsquerda )
plt.title("Translação Esquerda", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,2)
plt.imshow(imgDireita )
plt.title("Translação Direita", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,3)
plt.imshow(imgSuperior )
plt.title("Translação Superior", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,4)
plt.imshow(imgInferior )
plt.title("Translação Inferior", fontsize=11, weight='bold' )

Grafico.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
