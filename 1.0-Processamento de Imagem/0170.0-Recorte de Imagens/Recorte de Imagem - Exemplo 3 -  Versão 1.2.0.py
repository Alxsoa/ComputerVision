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

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Mesa.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
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
# Redefinindo o Tamanho da Imagem
########################################################################
#
imgBase = cv.resize ( 
                        imgBase, 
                        (0,0), 
                        fx=0.1, 
                        fy=0.1, 
                        interpolation = cv.INTER_AREA
                    )

# 
########################################################################
# Definindo a Máscara e Pontos de Recorte da Imagem
########################################################################
#
imgMascara = np.zeros(imgBase.shape[0:2], dtype=np.uint8)
ptsRecorte = np.array( [
                        [
                           [100,350],
                           [120,400],
                           [310,350],
                           [360,200],
                           [350,20],
                           [25,120]
                        ]
                       ] )


# 
########################################################################
# Recorta a Imagem nos Pontos Definidos
########################################################################
#
cv.drawContours(imgMascara, [ptsRecorte], -1, (255, 255, 255), -1, cv.LINE_AA)

# 
########################################################################
# Excluí o Fundo Original Recupera (x,y,w,h) e Recorta a Imagem
########################################################################
#
imgRecortadaTamanhoOriginal = cv.bitwise_and ( imgBase, imgBase, mask = imgMascara)
Recorte = cv.boundingRect(ptsRecorte) 
imgRecortada = imgRecortadaTamanhoOriginal[Recorte[1]: Recorte[1] + Recorte[3], Recorte[0]: Recorte[0] + Recorte[2]]

# 
########################################################################
# Criando o Background Branco
########################################################################
#
imgBackBranco = np.ones_like(imgBase, np.uint8)*255
cv.bitwise_not(imgBackBranco, imgBackBranco, mask=imgMascara)

# 
########################################################################
# Jutando as Imagens para Resultado com Fundo Branco
########################################################################
#
imgFundoBranco = imgBackBranco + imgRecortadaTamanhoOriginal

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor ( imgBase, cv.COLOR_BGR2RGB )
imgMascara = cv.cvtColor ( imgMascara, cv.COLOR_BGR2RGB )
imgRecortada = cv.cvtColor ( imgRecortada, cv.COLOR_BGR2RGB )
imgRecortadaTamanhoOriginal = cv.cvtColor ( imgRecortadaTamanhoOriginal, cv.COLOR_BGR2RGB )
imgFundoBranco = cv.cvtColor ( imgFundoBranco, cv.COLOR_BGR2RGB )

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure( )

Grafico.add_subplot(2,3,1)
plt.imshow( imgBase )
plt.title("Imagem Original")

Grafico.add_subplot(2,3,2)
plt.imshow(imgMascara )
plt.title("Imagem Máscara")

Grafico.add_subplot(2,3,3)
plt.imshow(imgRecortadaTamanhoOriginal )
plt.title("Imagem Cortada \nTamanho Original")

Grafico.add_subplot(2,3,4)
plt.imshow(imgFundoBranco )
plt.title("Imagem Cortada \nFundo Branco")

Grafico.add_subplot(2,3,5)
plt.imshow(imgRecortada )
plt.title("Imagem Cortada")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
