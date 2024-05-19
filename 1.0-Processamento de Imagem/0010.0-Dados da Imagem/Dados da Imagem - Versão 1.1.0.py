# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import sys
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
NomeImagem  = "Girassol.png"
dirRaiz = Path.home()
dirBase = "Atividades/LocalCV"
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
# Recuperando os Dados da Imagem
########################################################################
#
ImagemAltura = imgBase.shape[0]
ImagemLargura  = imgBase.shape[1]
ImagemNumCanais = imgBase.shape[2]

# 
########################################################################
# Apresentando os Dados da Imagem
########################################################################
#
LimpaTerminal ()
print ("")
print ("#######################################################################")
print ("# Dados da Imagem : " + NomeImagem)
print ("#######################################################################")
print ("# Largura da Imagem (pixel) ..: ", ImagemLargura )
print ("# Altura da Imagem (pixel) ...: ", ImagemAltura )
print ("# Número de Canais ...........: ", ImagemNumCanais )
print ("#######################################################################")
print ("")

########################################################################
# FIM DO PROGRAMA
########################################################################
