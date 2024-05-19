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

def MostraCdfLinear(image, channel, name, ax):
    image_intensity = img_as_ubyte(image[:,:,channel])
    freq, bins = cumulative_distribution(image_intensity)
    target_bins = np.arange(255)
    target_freq = np.linspace(0, 1, len(target_bins))
    ax.step(bins, freq, c="b", label="Actual CDF")
    ax.plot(target_bins, target_freq, c="r", label="Target CDF")
    ax.legend()
    ax.set_title("CDF Atual x Objetivo - Canal {}".format(name), fontweight="bold", fontsize=9) 
    
def DistribuicaoLinear(image, channel):
    image_intensity = img_as_ubyte(image[:,:,channel])
    freq, bins = cumulative_distribution(image_intensity)
    target_bins = np.arange(255)
    target_freq = np.linspace(0, 1, len(target_bins))
    new_vals = np.interp(freq, target_freq, target_bins)
    return new_vals[image_intensity].astype(np.uint8)

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
# Apresentação dos Resultados nos Diferentes Canais
########################################################################
#
fig, ax = plt.subplots(3,2)

CanalVermelho = DistribuicaoLinear(imgCatedral, 0)
CanalVerde = DistribuicaoLinear(imgCatedral, 1)
CanalAzul = DistribuicaoLinear(imgCatedral, 2)

MostraCdfLinear(imgCatedral, 0, "Red", ax[0,0])
ax[0,1].imshow(CanalVermelho, cmap="Reds")
ax[0,1].set_title("Imagem Corrigida (Canal Vermelho)", fontweight="bold", fontsize=9) 

MostraCdfLinear(imgCatedral, 1, "Green", ax[1,0])
ax[1,1].imshow(CanalVerde, cmap="Greens")
ax[1,1].set_title("Imagem Corrigida (Canal Verde)", fontweight="bold", fontsize=9) 

MostraCdfLinear(imgCatedral, 2, "Blue", ax[2,0])
ax[2,1].imshow(CanalAzul, cmap="Blues")
ax[2,1].set_title("Imagem Corrigida (Canal Azul)", fontweight="bold", fontsize=9) 

plt.tight_layout()
plt.show ()

# 
########################################################################
# Apresentação dos Resultados de Ajuste
########################################################################
#
fig, ax = plt.subplots(1,2 )
ax[0].imshow(imgCatedral)
ax[0].set_title('Original Image')
ax[1].imshow(np.dstack([CanalVermelho, CanalVerde, CanalAzul]))
ax[1].set_title('Transformed Image')
plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
