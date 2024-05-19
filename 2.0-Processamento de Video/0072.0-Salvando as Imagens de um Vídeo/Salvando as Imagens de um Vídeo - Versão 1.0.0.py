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
NomeVideo = "Bicicleta.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirVideo = "Videos"  
dirImagem = "Slides"
dirVideoIN = str(Path(dirRaiz, dirBase, dirVideo, NomeVideo))

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
# Recuperando as Propriedades do Vídeo 
########################################################################
#
iFPS = CapturaVideo.get(cv.CAP_PROP_FPS)

# 
########################################################################
# Lendo o Tempo Restante do Vído
########################################################################
#
iFrame = 0
iFrameGeral = 1
while(CapturaVideo.isOpened()):
  Status, VideoFrame = CapturaVideo.read()
  if Status == True:
    if ( iFrame == iFPS ):
        NomeImagem = "Slide-"+str(iFrameGeral)+".jpg"
        dirImagemOUT = str(Path(dirRaiz, dirBase, dirVideo, dirImagem, NomeImagem))
        print ( dirImagemOUT )
        cv.imwrite ( dirImagemOUT, VideoFrame)
        iFrame = 0
        iFrameGeral = iFrameGeral + 1
    else:
       iFrame = iFrame + 1

  else: 
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
