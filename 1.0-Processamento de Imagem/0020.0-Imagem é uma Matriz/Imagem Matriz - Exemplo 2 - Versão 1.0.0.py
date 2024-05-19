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
NomeOutput = "AdicaoOut.txt"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirOutput = "Output"
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoOutput = str(Path(dirRaiz, dirBase, dirOutput, NomeOutput))

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
# Apresentando a Matriz
########################################################################
#
LimpaTerminal ()
fleOut = open(dirCaminhoOutput, 'w')
for row in imgBase:
    print('|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|{:03}|'.format(*row),  file=fleOut)

########################################################################
# FIM DO PROGRAMA
########################################################################
