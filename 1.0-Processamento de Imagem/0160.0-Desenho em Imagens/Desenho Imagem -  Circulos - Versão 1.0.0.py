# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
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
# Desenhando o Círculo
########################################################################
#
ImagemAltura = int(NovoTamanho.shape[0]/2)
ImagemLargura = int(NovoTamanho.shape[1]/2)

LarguraLinha = 9
CorLinha = (0, 0, 255 )
PontoCentral = (ImagemLargura,ImagemAltura )
Raio = 200

ImagemCarro = cv.circle ( 
                           NovoTamanho, 
                           PontoCentral, 
                           100, 
                           CorLinha, 
                           LarguraLinha
                        )

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( NomeJanela, ImagemCarro)
cv.setWindowTitle(NomeJanela, NomeJanela )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
