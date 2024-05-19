
# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
from pathlib import Path
from vehicle_detector import VehicleDetector

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

exit ()

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
# 
########################################################################
# Apresentação das Marcações
########################################################################
#
      LarguraLinha = 2
      cv.line(VideoFrame, (732,330), (423,330), (0, 0, 255 ), thickness=LarguraLinha)
      #cv.line(VideoFrame, (60,321), (350,321), (0, 255, 0 ), thickness=LarguraLinha)

      ptsRecorte = [
                    (425,250), 
                    (590,250), 
                    (732,330), 
                    (423,330)
                   ]
      cv.polylines(VideoFrame, np.array([ptsRecorte]), True, CorLinha, 1)  

# 
########################################################################
# Transformando em Tons de Cinza a Imagem e Aplica Blur e Limiar
########################################################################
#
      imgMascara = np.zeros(VideoFrame.shape[0:2], dtype=np.uint8)
      imgBaseCinza = cv.cvtColor(VideoFrame, cv.COLOR_BGR2GRAY)
      imgBlur = cv.GaussianBlur(imgBaseCinza, (5, 5), 0)
      imgLimiar = cv.threshold(imgBlur, 60, 255, cv.THRESH_BINARY)[1]

# 
########################################################################
# Busca os Contornos
########################################################################
#
      #iContornos = cv.findContours(imgLimiar.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
      #NumContornos = imutils.grab_contours(iContornos)

# 
########################################################################
# Calcula os Momentos e Indica o Centro
########################################################################
#
      #for iAux in NumContornos:
          #M = cv.moments(iAux)
          #if M['m00'] != 0:
          #    cx = int(M['m10']/M['m00'])
          #    cy = int(M['m01']/M['m00'])
          #    cv.drawContours(VideoFrame, [iAux], -1, (0, 255, 0), 2)
          #    cv.circle(VideoFrame, (cx, cy), 7, (255, 255, 255), -1)
          #    cv.putText(VideoFrame, "Centro", (cx - 20, cy - 20),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

#      cv.putText(VideoFrame, "Total Carro Vindo = "+str(iTotalCarroVindo), (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

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
      if ( len(bbox) > 0):
          for iAux in range (0, len(bbox)):
              #cv.circle(imgRecortada, (bbox[0][0], bbox[0][1]), 7, (255, 255, 255), -1)
              #cv.circle(imgRecortada, (bbox[0][2], bbox[0][3]), 7, (255, 0, 255), -1)          
              bbox[iAux][0] = 425 + bbox[iAux][0]
              bbox[iAux][1] = 250 + bbox[iAux][1] 
              bbox[iAux][2] = 425 + bbox[iAux][2] 
              bbox[iAux][3] = 250 + bbox[iAux][3] 

              LarguraLinha = 2
              CorLinha = (0, 0, 255 )
              PontoInicial = (bbox[iAux][0], bbox[iAux][1])
              PontoFinal = (bbox[iAux][2],bbox[iAux][3] )
              VideoFrame = cv.rectangle(VideoFrame, PontoInicial, PontoFinal, CorLinha, LarguraLinha)

          #print ( bbox[0][0])
#      bbox, label, conf = clb.detect_common_objects(VideoFrame, confidence=0.4, model="yolov5")      
#      print ( label.count( "car") )
      #if ( len(label) > 0):
#      iTotalCarroVindo = iTotalCarroVindo + label.count( "car")

      #print ( iTotalCarroVindo )
      #VideoFrame = draw_bbox(VideoFrame, bbox, label, conf)

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
