# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns 

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
NomeImagem = "Adicao.png"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_GRAYSCALE)

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
imgColorida = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def my_function1(df):
    bruto = plt.imshow( imgColorida )
    plt.title("Original", fontsize=11, weight='bold' )
    return bruto

def my_function2(df):
    heatmap=sns.heatmap (  
                           imgBase, 
                           annot=True, 
                           fmt="d", 
                           linewidth=1, 
                           cbar=False, 
                           annot_kws={"size": 8},
                           #cmap="blue", 
                           square=True, 
                           linecolor="k" 
                        )
    
    plt.title("Visão Matricial da Imagem", fontsize=11, weight='bold' )
    return heatmap

df = pd.DataFrame(np.random.rand(100).reshape(10,10))

Grafico = plt.figure()

Grafico.add_subplot(1,2,1)
bruto = my_function1(df)
# bruto.set_title("Imagem 1")

Grafico.add_subplot(1,2,2)
heatmap = my_function2(df)
# heatmap.set_title("Imagem 2")

plt.show()

exit()


def Mostra (imgBase):
    bruto = plt.imshow(imgBase )
    plt.title("Original", fontsize=11, weight='bold' )
    return (bruto)

def my_function(imgBase):
   #  plt.figure()
    heatmap=sns.heatmap (  
                           imgBase, 
                           annot=True, 
                           fmt="d", 
                           linewidth=1, 
                           cbar=False, 
                           annot_kws={"size": 8},
                           #cmap="blue", 
                           square=True, 
                           linecolor="k" 
                        )
    
    plt.title("Visão Matricial da Imagem", fontsize=11, weight='bold' )
    return heatmap

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(1,2,1)
# plt.imshow(imgColorida )
# plt.title("Original", fontsize=11, weight='bold' )
plt.figure()
bruto = Mostra (imgColorida)

Grafico.add_subplot(1,2,2)
# plt.title("Visão Matricial da Imagem", fontsize=11, weight='bold' )
# sns.heatmap ( imgBase, 
#               annot=True, 
#               fmt="d", 
#               linewidth=1, 
#               cbar=False, 
#               annot_kws={"size": 8},
#               #cmap="blue", 
#               square=True, 
#               linecolor="k" )

heatmap = my_function(imgBase)
# heatmap.set_title("my_function call with df")

plt.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
