
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
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
LarguraLinha = 3
CorLinhaLivre = (0, 255, 0 )
CorLinhaOcupada = (0, 0, 255 )
Debug = False
ListaVagas = [
               [ 31,  74, 101, 193],
               [141,  74, 101, 193],
               [255,  74, 101, 193],
               [363,  74, 101, 193],      
               [470,  74, 101, 193],
               [ 33, 341, 101, 193],
               [143, 341, 101, 193],
               [256, 341, 101, 193],
               [363, 341, 101, 193],
               [472, 341, 101, 193]                        
             ]

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
imgResultado = np.copy (imgReduzida)
for xPos, yPos, Largura, Altura in ListaVagas:   
      PontoInicial = (xPos,yPos)
      PontoFinal = (xPos+Largura,yPos+Altura)

      imgResultadoCinza = cv.cvtColor ( imgResultado, cv.COLOR_BGR2GRAY )
      imgResultadoLimiar = cv.adaptiveThreshold (imgResultadoCinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)
      imgResultadoBlur = cv.medianBlur (imgResultadoLimiar, 5)
      Kernel = np.ones ( (3,3), np.int8)
      imgResultadoDilatado = cv.dilate (imgResultadoBlur, Kernel)

      imgPedaco = imgResultadoDilatado [yPos:yPos+Altura, xPos:xPos+Largura]
      iBrancos = cv.countNonZero (imgPedaco)

      if (Debug):
         cv.putText (imgResultado, str(iBrancos), (xPos, yPos+Altura-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
           
      if (iBrancos > 1500):
         imgResultado = cv.rectangle (imgResultado, PontoInicial, PontoFinal, CorLinhaOcupada, LarguraLinha)         
      else:      
         imgResultado = cv.rectangle (imgResultado, PontoInicial, PontoFinal, CorLinhaLivre, LarguraLinha)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "Imagem Base", imgReduzida)
cv.imshow ( "Imagem Desenhada", imgResultado)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################	
