# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import imageio
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
NomeFoto1 = "GifAnimadoFoto1.png"
NomeFoto2 = "GifAnimadoFoto2.png"
NomeGif = "GifAnimado.gif"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoFoto1 = str(Path(dirRaiz, dirBase, dirImagem, NomeFoto1))
dirCaminhoFoto2 = str(Path(dirRaiz, dirBase, dirImagem, NomeFoto2))
dirCaminhoGif = str(Path(dirRaiz, dirBase, dirImagem, NomeGif))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
imgFoto1 = cv.imread ( dirCaminhoFoto1, cv.IMREAD_UNCHANGED)
if imgFoto1 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeFoto1)
   exit ()

imgFoto2 = cv.imread ( dirCaminhoFoto2, cv.IMREAD_UNCHANGED)
if imgFoto2 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeFoto2)
   exit ()

imgFoto1 = cv.resize(imgFoto1, (400, 400), interpolation = cv.INTER_AREA)
imgFoto2 = cv.resize(imgFoto2, (400, 400), interpolation = cv.INTER_AREA)

# 
########################################################################
# Loop de Criação do Gif Animado
########################################################################
#
lstFrame = []
for iAux in range (0, 100):
    if ( (iAux % 2) == 0):
       lstFrame.append(imgFoto1)
    else:
       lstFrame.append(imgFoto2)

# 
########################################################################
# Salvando o Gif Animado a Duracao é em ms (50 fps == 20 duration)
########################################################################
#

with imageio.get_writer( dirCaminhoGif, mode="I") as EscreveGif:
    for idx, frame in enumerate(lstFrame):
        EscreveGif.append_data(frame)

########################################################################
# FIM DO PROGRAMA
########################################################################