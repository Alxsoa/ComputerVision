# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread, imshow
from skimage import img_as_ubyte, img_as_float
from skimage.color import rgb2gray
from skimage.exposure import histogram, cumulative_distribution
from scipy.stats import norm, cauchy, logistic
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
NomeImagem = "Catedral.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
try:
  imgCatedral = imread(dirCaminhoImagem)
except:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Figura, Grafico = plt.subplots(2, 2, constrained_layout=True)
imgCatedralCinza = rgb2gray(imgCatedral)

Grafico[0, 0].imshow(imgCatedralCinza, cmap="gray")
Grafico[0, 0].set_title("Imagem Cinza Original", fontweight="bold", fontsize=9) 

Grafico1 = Grafico[0, 1]
Grafico2 = Grafico1.twinx()

frqHistograma, bnsHistograma = histogram(imgCatedralCinza)
frqCumlativa, bnsCumulativa = cumulative_distribution(imgCatedralCinza)
Grafico1.step(bnsHistograma, frqHistograma*1.0/frqHistograma.sum(), c="b", label="PDF")
Grafico2.step(bnsCumulativa, frqCumlativa, c="r",  label="CDF")
Grafico1.set_ylabel("PDF", color="b", fontweight="bold", fontsize=9) 
Grafico2.set_ylabel("CDF", color="r", fontweight="bold", fontsize=9) 
Grafico[0, 1].set_xlabel("Valor da Intensidade", fontweight="bold", fontsize=9) 
Grafico[0, 1].set_title("Histograma da Intensidade dos Pixel", fontweight="bold", fontsize=9) 

imgIntensidade = img_as_ubyte(imgCatedralCinza)
frqCumlativa, bnsCumulativa = cumulative_distribution(imgIntensidade)
target_bnsCumulativa = np.arange(255)
target_frqCumlativa = np.linspace(0, 1, len(target_bnsCumulativa))
imgCorrigida = np.interp(frqCumlativa, target_frqCumlativa, target_bnsCumulativa)
Grafico[1, 0].step(bnsCumulativa, frqCumlativa, c="b", label="Atual CDF") 
Grafico[1, 0].plot(target_bnsCumulativa, target_frqCumlativa, c="r", label="Alvo CDF") 
Grafico[1, 0].legend() 
Grafico[1, 0].set_title("CDF Atual x Objetivo", fontweight="bold", fontsize=9) 

Grafico[1, 1].imshow(imgCorrigida[imgIntensidade].astype(np.uint8), cmap="gray") 
Grafico[1, 1].set_title("Imagem Cinza Corrigida", fontweight="bold", fontsize=9) 

plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
