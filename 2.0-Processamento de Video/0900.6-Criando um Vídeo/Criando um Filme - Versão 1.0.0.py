# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
from pathlib import Path
import time
import numpy as np

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
NomeImagem = [ 
               "VideoSlide0.png", "VideoSlide1.png", 
               "VideoSlide2.png", "VideoSlide3.png",
               "VideoSlide4.png", "VideoSlide5.png", 
               "VideoSlide6.png"
             ]

NomeVideoOUT = "MeuFilme.mp4"
NomeJanela = "Imagem Base"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirVideo = "Videos" 
dirSlides = "CriandoVideo"  
dirVideoOut = str(Path(dirRaiz, dirBase, dirVideo, NomeVideoOUT))

Largura = 800
Altura  = 450
FPS = 24
seconds = 10
Radius = 90
ptsH = int(Altura/2)

# 
########################################################################
# Cria a Introdução do Vídeo
########################################################################
#
lstFrameVideo = []
iFrame = 0
for iAux in range ( 0, len(NomeImagem)):
      dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirVideo, dirSlides, NomeImagem[iAux]))
      imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

      if imgBase is None:
         LimpaTerminal ()
         print( "Não Foi Localizada a Imagem : ", NomeImagem[iAux])
         exit ()   
      
      imgReduzida = cv.resize(imgBase, (800, 450), interpolation = cv.INTER_AREA)
      #cv.imshow ( "Janela Base", imgReduzida)
      while ( iFrame < 50):
         lstFrameVideo.append(imgReduzida)
         iFrame = iFrame + 1
      iFrame = 0
      #cv.waitKey(1)
       

for ptsX in range(-Radius, 800+Radius, 6):     
   VideoFrame = np.random.randint  ( 
                                       0, 256, 
                                       (Altura, Largura, 3), 
                                       dtype=np.uint8
                                    )
   
   cv.circle(VideoFrame, (ptsX, ptsH), Radius, (0, 255, 0), -1)
   lstFrameVideo.append(VideoFrame)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( dirVideoOut, 
                            Codec,                            
                            25, 
                            (800, 450))

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
for iAux in range (0, len(lstFrameVideo)):
    VideoOut.write(lstFrameVideo[iAux])  

# 
########################################################################
# Fechando o Arquivo de Vídeo e Desmontando o Janelamento
########################################################################
# 
VideoOut.release()
#cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
