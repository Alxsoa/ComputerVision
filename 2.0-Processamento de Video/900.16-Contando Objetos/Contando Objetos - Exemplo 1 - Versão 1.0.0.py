
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
NomeVideoBase = "Trafego.mp4"
NomeVideoOUT = "TrafegoOUT.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Videos"  
dirCaminhoBase = str(Path(dirRaiz, dirBase, dirImagem, NomeVideoBase))
dirVideoOut = str(Path(dirRaiz, dirBase, dirImagem, NomeVideoOUT))
LarguraLinha = 9
CorLinha = (0, 255, 255 )

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

#Status, VideoFrameSalvo = Video.read(0)
#cv.imwrite (dirVideoOut, VideoFrameSalvo )
#exit ()

iTotalCarroVindo = 0
lstFrameVideo = []
while(Video.isOpened()):
    Status, VideoFrame = Video.read()

    if Status == True:
      cv.putText(VideoFrame, "Total Carro Vindo = "+str(iTotalCarroVindo), (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

      LarguraLinha = 2
      cv.line(VideoFrame, (427,250), (660,250), (0, 0, 255 ), thickness=LarguraLinha)
      cv.line(VideoFrame, (60,321), (350,321), (0, 255, 0 ), thickness=LarguraLinha)

      imgMascara = np.zeros(VideoFrame.shape[0:2], dtype=np.uint8)
      ptsRecorte = [
                  (427,250), 
                  (427,300), 
                  (700,300), 
                  (700,250),                   
#                  (852,480),
#                  (463,480)

              ]
      VideoFrame =  cv.polylines(VideoFrame, np.array([ptsRecorte]), True, CorLinha, 1)

# 
########################################################################
# Recorta a Imagem nos Pontos Definidos
########################################################################
#
      imgMascara = cv.drawContours(imgMascara, np.array([ptsRecorte]), -1, (255, 255, 255), -1, cv.LINE_AA)

# 
########################################################################
# Excluí o Fundo Original Recupera (x,y,w,h) e Recorta a Imagem
########################################################################
#
      imgRecortadaTamanhoOriginal = cv.bitwise_and ( VideoFrame, VideoFrame, mask = imgMascara)
      Recorte = cv.boundingRect(np.array([ptsRecorte])) 
      imgRecortada = imgRecortadaTamanhoOriginal[Recorte[1]: Recorte[1] + Recorte[3], Recorte[0]: Recorte[0] + Recorte[2]]


      bbox, label, conf = clb.detect_common_objects(imgRecortada, confidence=0.4, model="yolov5")
      print ( label.count( "car") )
      #if ( len(label) > 0):
      iTotalCarroVindo = iTotalCarroVindo + label.count( "car")

      #print ( iTotalCarroVindo )
      #VideoFrame = draw_bbox(VideoFrame, bbox, label, conf)

      #VideoFrameOUT = cv.resize(VideoFrame, (700, 400) ) 
      #lstFrameVideo.append(VideoFrame)
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
# Criando o Arquivo de Vídeo
########################################################################
#
print ( "Escrevendo ")
VideoOut = cv.VideoWriter ( dirVideoOut, 
                            Codec,                            
                            25, 
                            (700, 400))

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
#cv.imwrite (VideoFrameSalvo, VideoFrame )
Video.release()
VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################	
