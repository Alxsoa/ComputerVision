# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import numpy as np
from PIL import ImageFont, ImageDraw, Image
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
NomeImagem  = "Girassol.png"
NomeFonte   = "Oswald-SemiBold.ttf"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirFontes = "FontesTT" 
dirOswald = "Oswald" 
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoFonte  = str(Path(dirRaiz, dirBase, dirFontes, dirOswald, NomeFonte ))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
Imagem = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
if Imagem is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Selecionando o Fonte de Texto
########################################################################
#
font = ImageFont.truetype(dirCaminhoFonte, 32)
ImagemArray = Image.fromarray(Imagem)
draw = ImageDraw.Draw(ImagemArray)

# 
########################################################################
# Escrevendo o Texto
########################################################################
#
draw.text((5, 5),  "Alinhamento\nEsquerda", font = font , align ="left", fill ="yellow") 
draw.text((450, 5),  "Alinhamento\nEsquerda", font = font , align ="right", fill ="blue") 
draw.text((250, 230),  "Alinhamento\nao Centro", font = font , align ="center", fill ="green") 
ImagemEscrita = np.array(ImagemArray)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
cv.imshow ( "Janela Base", ImagemEscrita)
cv.waitKey ()
cv.destroyAllWindows ()

########################################################################
# FIM DO PROGRAMA
########################################################################

