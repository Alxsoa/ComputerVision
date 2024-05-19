# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import os
import numpy as np
from skimage.exposure import cumulative_distribution
from skimage.color import rgb2gray
from skimage.exposure import histogram, cumulative_distribution
from skimage import img_as_ubyte
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
NomeImagem = "Escuridao5.jpg"
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
# Convertendo para Cinza
########################################################################
#
imgBaseCinza = cv.cvtColor(imgBase, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBaseCinza = cv.cvtColor(imgBaseCinza, cv.COLOR_GRAY2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot (2,2,1)
plt.imshow (imgBaseCinza )
plt.title ("Imagem Original", fontsize=11, weight="bold" )

Grafico.add_subplot (2,2,2)
imgBaseIntensidade = img_as_ubyte(rgb2gray(imgBase))
freq, bins = histogram (imgBaseIntensidade)
plt.step (bins, freq*1.0/freq.sum())
plt.xlabel ("Valor da Intensidade")
plt.ylabel ( "Fração de Pixels")
plt.title ("Histograma das Intesidades", fontsize=11, weight="bold" )

Grafico.add_subplot (2,2,3)
freq, bins = cumulative_distribution(imgBaseIntensidade)
target_bins = np.arange(255)
target_freq = np.linspace(0, 1, len(target_bins))
plt.step(bins, freq, c="b", label="actual cdf")
plt.plot(target_bins, target_freq, c="r", label="target cdf")
plt.legend()
plt.xlim(0, 255)
plt.ylim(0, 1)
plt.xlabel ("Valor da Intensidade")
plt.ylabel ( "Fração Cumulativa de Pixels" )
plt.title ( "Distribuição Equalizada", fontsize=11, weight="bold" )

Grafico.add_subplot (2,2,4)
new_vals = np.interp(freq, target_freq, target_bins)
dark_image_eq = img_as_ubyte(new_vals[imgBaseIntensidade].astype(np.uint8))

plt.imshow ( dark_image_eq , cmap='gray')
cv.imwrite ( "Imagem.png", dark_image_eq)
plt.title ( "Imagem Resultado", fontsize=11, weight="bold" )

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

