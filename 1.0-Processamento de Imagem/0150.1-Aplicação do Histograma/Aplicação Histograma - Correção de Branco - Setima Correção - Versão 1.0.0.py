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
from matplotlib.patches import Rectangle

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

def BalanceandoBrancoRegiao (imgBase, Linha, Coluna, LinhaLargura, LinhaColuna):

    fig, ax = plt.subplots(1,2)
    ax[0].imshow(imgBase)
    ax[0].add_patch(Rectangle((Coluna, Linha), LinhaColuna, LinhaLargura, linewidth=3, edgecolor='r', facecolor='none'))
    ax[0].set_title("Imagem Original", fontsize=11, weight='bold' )

    imgRegiao = imgBase[Linha:Linha+LinhaLargura, Coluna:Coluna+LinhaColuna]
    imgRegiaoMax = (imgBase*1.0 / imgRegiao.max(axis=(0, 1))).clip(0, 1)

    ax[1].imshow(imgRegiaoMax)
    ax[1].set_title("Imagem Balanceada", fontsize=11, weight='bold' )
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
BalanceandoBrancoRegiao (imgJantar, 1900, 200, 120, 120)

########################################################################
# FIM DO PROGRAMA
########################################################################
