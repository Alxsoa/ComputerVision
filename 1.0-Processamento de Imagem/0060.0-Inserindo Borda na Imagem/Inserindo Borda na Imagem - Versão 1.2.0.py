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
NomeImagem  = "Cafeteria.png"
dirRaiz = Path.home()
dirBase = "Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Reduzindo as Dimensões da Imagem
########################################################################
#
imgReduzida = cv.resize(imgBase, (640, 480), interpolation = cv.INTER_AREA)

# 
########################################################################
# Inserindo a Borda
########################################################################
#
imgBorda = cv.copyMakeBorder (
                                src=imgReduzida, 
                                top=15, 
                                bottom=15, 
                                left=15, 
                                right=15, 
                                borderType=cv.BORDER_CONSTANT, 
                                value=(255,255,255)
                             ) 

# 
########################################################################
# Apresentando a Imagem 
########################################################################
#
cv.imshow ( "Cafeteria Original", imgReduzida)
cv.imshow ( "Cafeteria com Borda", imgBorda)

# 
########################################################################
# Destruindo o Janelamento
########################################################################
#
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
