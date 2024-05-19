# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import imutils
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
NomeWebsiteAlvo = "Website-ScreenShot-Alvo.png"
NomeWebsiteOriginal = "Website-ScreenShot-Original.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoWebsiteAlvo = str(Path(dirRaiz, dirBase, dirImagem, NomeWebsiteAlvo))
dirCaminhoWebsiteOriginal  = str(Path(dirRaiz, dirBase, dirImagem, NomeWebsiteOriginal))

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgWebsiteAlvo  = cv.imread (dirCaminhoWebsiteAlvo, cv.IMREAD_COLOR )
if imgWebsiteAlvo is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeWebsiteAlvo)
   exit ()


imgWebsiteOriginal = cv.imread (dirCaminhoWebsiteOriginal, cv.IMREAD_COLOR )
if imgWebsiteOriginal is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeWebsiteOriginal )
   exit ()

# 
########################################################################
# Uniformizando as Dimensões da Imagem
########################################################################
#
imgAlvo = imutils.resize(imgWebsiteAlvo, height = 450)
imgOriginal = imutils.resize(imgWebsiteOriginal, height = 450)

# 
########################################################################
# Diferença Entre as Imagens
########################################################################
#
#imgDiferenca = imgOriginal.copy()
imgDiferenca = np.copy(imgOriginal)
cv.absdiff ( imgOriginal, imgAlvo, imgDiferenca )

# 
########################################################################
# Convertendo a Diferença para Tons de Cinza
########################################################################
#
imgDiferencaCinza = cv.cvtColor(imgDiferenca, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Dilata a Imagem para Capturar as Diferenças
########################################################################
#
for iAux in range(0, 3):
    imgDilatada = cv.dilate(imgDiferencaCinza.copy(), None, iterations= iAux+ 1)

# 
########################################################################
# Aplicando o Limiar (Tudo < 3 será 0 e Tudo que for > 3 será 255
########################################################################
#
(T, thresh) = cv.threshold(imgDilatada, 3, 255, cv.THRESH_BINARY)

# 
########################################################################
# Buscando Contornos
########################################################################
#
cnts = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# 
########################################################################
# Indicando a Diferença
########################################################################
#
for c in cnts:
    (x, y, w, h) = cv.boundingRect(c)
    cv.rectangle(imgOriginal, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgWebsiteOriginal = cv.cvtColor ( imgWebsiteOriginal, cv.COLOR_BGR2RGB )
imgAlvo = cv.cvtColor ( imgAlvo, cv.COLOR_BGR2RGB )
imgOriginal = cv.cvtColor ( imgOriginal, cv.COLOR_BGR2RGB )
imgDiferenca = cv.cvtColor ( imgDiferenca, cv.COLOR_BGR2RGB )
imgDiferencaCinza = cv.cvtColor ( imgDiferencaCinza, cv.COLOR_BGR2RGB )
imgDilatada = cv.cvtColor ( imgDilatada, cv.COLOR_BGR2RGB )
thresh = cv.cvtColor ( thresh, cv.COLOR_BGR2RGB )

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,4,1)
plt.imshow(imgWebsiteOriginal )
plt.title("Imagem Original")

Grafico.add_subplot(2,4,2)
plt.imshow(imgAlvo )
plt.title( "Imagem Alvo" )

Grafico.add_subplot(2,4,3)
plt.imshow(imgDiferenca )
plt.title("Diferença")

Grafico.add_subplot(2,4,4)
plt.imshow(imgDiferencaCinza )
plt.title("Diferença Cinza")

Grafico.add_subplot(2,4,5)
plt.imshow(imgDilatada )
plt.title("Dilatada")

Grafico.add_subplot(2,4,6)
plt.imshow(thresh )
plt.title("Limiar")

Grafico.add_subplot(2,4,7)
plt.imshow(imgOriginal )
plt.title("Limiar")

plt.tight_layout ()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################	
