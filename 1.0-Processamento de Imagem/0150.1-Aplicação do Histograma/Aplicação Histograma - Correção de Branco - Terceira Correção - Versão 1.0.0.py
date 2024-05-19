# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import os
from pathlib import Path
from skimage import img_as_ubyte

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

def percentile_whitebalance(image, percentile_value):
    Grafico = plt.figure()

    Grafico.add_subplot(2,2,1)
    for channel, color in enumerate('rgb'):
        channel_values = image[:,:,channel]
        value = np.percentile(channel_values, percentile_value)
        plt.step(np.arange(256), np.bincount(channel_values.flatten(), minlength=256)*1.0 / channel_values.size, c=color)
        plt.xlim(0, 255)
        plt.axvline(value, ls='--', c=color)
        plt.text(value-70, .01+.012*channel, "{} Valor Max = {}".format(color, value), weight='bold', fontsize=10)

    Grafico.add_subplot(2,2,2)
    plt.xlabel('Pixel')
    plt.ylabel('Fração de Pixel');
    plt.title('Histograma de Cores (Canal RGB)')    


    whitebalanced = img_as_ubyte((image*1.0 / np.percentile(image, percentile_value, axis=(0, 1))).clip(0, 1))
    plt.imshow(whitebalanced)
    plt.title('Imagem Balanceada pelo Branco')

    plt.tight_layout()
    plt.show ()
    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem = "Jantar.jpg"
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
# Convertendo para Matplotlib
########################################################################
#
imgJantar = cv.cvtColor ( imgBase, cv.COLOR_BGR2RGB )

# 
########################################################################
# Acertando o Branco pelo Percentil 
########################################################################
#
percentile_whitebalance(imgJantar, 99)

########################################################################
# FIM DO PROGRAMA
########################################################################
