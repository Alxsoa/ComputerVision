# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import random
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
Codec = cv.VideoWriter_fourcc('m','p','4','v')
NomeImagem = "IngridGomes.jpg"
NomeVideo = "IngridGomes.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirVideo = "Videos"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoVideo = str(Path(dirRaiz, dirBase, dirVideo, NomeVideo))

# 
########################################################################
# Lendo e Checando a Disponibilidade da Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
if imgBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()
else:
    imgReduzida = cv.resize(imgBase, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
iLargura = imgReduzida.shape[1]
iAltura  = imgReduzida.shape[0]
VideoOut = cv.VideoWriter ( dirCaminhoVideo, 
                            Codec,                            
                            25, 
                            (iLargura, iAltura))

# 
########################################################################
# Preparação dos Frames de Vídeo
########################################################################
#
imgFrame = np.zeros((iAltura, iLargura, 3), np.uint8)
iFrame = 0
lstLinhasAleatorias = list(range(len(imgReduzida)))
random.shuffle(lstLinhasAleatorias)

# 
########################################################################
# Loop de Criaçào do Efeito
########################################################################
#
for jAux in lstLinhasAleatorias:
    for iAux in range(len(imgFrame[jAux])):
        cv.circle   (
                        imgFrame,                     
                        (iAux, jAux),                     
                        1,                          
                        (
                            int(imgReduzida[jAux][iAux][0]),       
                            int(imgReduzida[jAux][iAux][1]),      
                            int(imgReduzida[jAux][iAux][2])        
                        ), 
                        -1                         
                    )
    
    if (jAux % 10 == 0):
        iFrame += 1
        VideoOut.write(imgFrame)

# 
########################################################################
# Fechamento o Arquivo de Vídeo
########################################################################
#
VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
