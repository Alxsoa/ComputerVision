
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
NomeImagem = "Estacionamento.png"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
LarguraLinha = 9
CorLinha = (0, 255, 255 )

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
if imgBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgReduzida = cv.resize(imgBase, (0,0), fx=0.4, fy=0.4, interpolation = cv.INTER_AREA)
  
# 
########################################################################
# Selecionando a Região de Interesse
########################################################################
#
datRegiao = cv.selectROI("select the area", imgReduzida)
  
# 
########################################################################
# Recortando a Região
########################################################################
#
imgRecorte = imgReduzida   [
                              int(datRegiao[1]):int(datRegiao[1]+datRegiao[3]), 
                              int(datRegiao[0]):int(datRegiao[0]+datRegiao[2])
                           ]

# 
########################################################################
# Recortando a Região
########################################################################
#
LimpaTerminal ()
print ( "########################################################################" )
print ( "# Dados da Região " )
print ( "########################################################################" )
print ( "# Ponto X Inicial ...: ",  datRegiao[0])
print ( "# Ponto Y Inicial ...: ",  datRegiao[1])
print ( "# Largura ...........: ",  datRegiao[2])
print ( "# Altura ............: ",  datRegiao[3])
print ( "########################################################################" )

# 
########################################################################
# Definindo os Pontos de Referenca da Imagem
########################################################################
#
ptsXInicial = int(datRegiao[0])
ptsYInicial = int(datRegiao[1])

iLargura = datRegiao[3]
iAltura  = datRegiao[2]

ptsXFinal = ptsXInicial + iAltura
ptsYFinal = ptsYInicial + iLargura

# 
########################################################################
# Indicando a Região na Imagem Selecionada
########################################################################
#
LarguraLinha = 9
CorLinha = (0, 0, 255 )
PontoInicial = (ptsXInicial,ptsYInicial)
PontoFinal = (ptsXFinal,ptsYFinal)
cv.rectangle (imgReduzida, PontoInicial, PontoFinal, CorLinha, LarguraLinha)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "Imagem Recortada", imgRecorte)
cv.imshow ( "Imagem Resultado", imgReduzida)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################	
