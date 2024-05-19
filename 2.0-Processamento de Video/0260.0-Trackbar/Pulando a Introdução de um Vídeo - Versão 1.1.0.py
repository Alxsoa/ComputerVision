# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import time
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

def ExecutaTracado(Evento,x,y,flags,param):
    global VideoFrame, Introducao

    if Evento == cv.EVENT_LBUTTONDOWN:
       if ( (x > 6 and x < 200) and (y > 414 and y < 440)):
          CapturaVideo.set(cv.CAP_PROP_POS_FRAMES, 350)
          Introducao = False

    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Base"
NomeVideo = "MeuFilme.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirVideo = "Videos"  
dirVideoIN = str(Path(dirRaiz, dirBase, dirVideo, NomeVideo))
Introducao = True

# 
########################################################################
# Lendo o Video
########################################################################
#
CapturaVideo = cv.VideoCapture (dirVideoIN)
if (CapturaVideo.isOpened()== False): 
    LimpaTerminal ()
    print( "Não Foi Localizado o Video : ", NomeVideo)
    exit ()

# 
########################################################################
# Janelamento e Instancia de Função
########################################################################
#
cv.namedWindow (NomeJanela)
cv.setMouseCallback (NomeJanela, ExecutaTracado)

# 
########################################################################
# Processo de Captura de Faces
########################################################################
# 
while (CapturaVideo.isOpened()):
    Status, VideoFrame = CapturaVideo.read()
    if Status is False:
        break

    if (Introducao):
        cv.rectangle(VideoFrame, (6,414), (200,440), (255,255,255), -1)
        cv.putText(VideoFrame, "[PULAR A INTRODUCAO]", (6, 431), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))

    cv.imshow(NomeJanela, VideoFrame)
    if cv.waitKey(25) == 27:
        break

# 
########################################################################
# Fechando o Arquivo de Vídeo e Desmontando o Janelamento
########################################################################
# 
CapturaVideo.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
