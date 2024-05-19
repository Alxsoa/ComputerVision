# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
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
NomeImagem = "Audi.jpg"
NomeJanela = "Imagem Base"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
plgFechado = True
plgEspessura = 8
plgCor = (255, 0, 0)

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
# Reduzindo o Tamanho
########################################################################
#
EscalaPercentual = 70
LarguraAlterada = int(imgBase.shape[1] * EscalaPercentual / 100)
AlturaAlterada  = int(imgBase.shape[0] * EscalaPercentual / 100)
NovoTamanho = (LarguraAlterada, AlturaAlterada)
NovoTamanho = cv.resize(imgBase, NovoTamanho, interpolation = cv.INTER_AREA)

# 
########################################################################
# Definindo os Pontos do Polígono
########################################################################
#
ptsPontos = np.array([[25, 70], [25, 160],
                [110, 200], [200, 160],
                [200, 70], [110, 20]],
               np.int32 )

# 
########################################################################
# Desenhando o Triangulo
########################################################################
#
image = cv.polylines(NovoTamanho, [ptsPontos], plgFechado, plgCor, plgEspessura)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow (NomeJanela, image)
cv.setWindowTitle(NomeJanela, NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################

