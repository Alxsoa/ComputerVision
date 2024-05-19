# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cvlib as clb
from cvlib.object_detection import draw_bbox
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
from pathlib import Path
from datetime import datetime

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
NomeVideoBase = "DetectaMovimento.mp4"
VideoOutName = "DetectaMovimentoOUT.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Videos"  
dirCaminhoBase = str(Path(dirRaiz, dirBase, dirImagem, NomeVideoBase))
dirVideoOut = str(Path(dirRaiz, dirBase, dirImagem, VideoOutName))

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( dirVideoOut, 
                            Codec,                            
                            25, 
                            (700, 400))

# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture (dirCaminhoBase)
if (Video.isOpened()== False): 
    LimpaTerminal ()
    print( "Não Foi Localizada o Vídeo : ", NomeVideoBase)
    exit ()

lstFrameVideo = []
while(Video.isOpened()):
    Status, VideoFrame = Video.read()

    if Status == True:
      TempoAtual = datetime.now() 
      HoraAtual = TempoAtual.strftime("%H:%M:%S")
      DataAtual = str(TempoAtual.day) + "-" + str(TempoAtual.month) + "-" + str(TempoAtual.year)

      cv.putText(VideoFrame, HoraAtual, (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
      cv.putText(VideoFrame, DataAtual, (570, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

      bbox, label, conf = clb.detect_common_objects(VideoFrame, confidence=0.4, model="yolov5")
      VideoFrame = draw_bbox(VideoFrame, bbox, label, conf)

      if ( len(label) > 0):
         cv.putText(VideoFrame, "Movimento Detectado", (5, 420), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

      VideoFrameOUT = cv.resize(VideoFrame, (700, 400) ) 
      lstFrameVideo.append(VideoFrameOUT)
      cv.imshow ( "JanelaBase", VideoFrame)
      if cv.waitKey(1) & 0xFF == ord('q'):
        break
  
    else: 
      break

# 
########################################################################
# Fechamento do Janelamento
########################################################################
#
cv.destroyAllWindows()

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
Video.release()
VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################	
