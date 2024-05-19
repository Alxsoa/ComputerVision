# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import time
import cv2 as cv
import mediapipe as mp
import numpy as np
from pathlib import Path
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
Codec = cv.VideoWriter_fourcc('m','p','4','v')
mp_drawing = mp.solutions.drawing_utils
mpDetecacaoFaces = mp.solutions.face_detection
NomeVideoOUT = "PessoaCorrendoOUT.mp4"
NomeVideo = "PessoaCorrendo.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirVideo = "Videos"  

dirVideoIN = str(Path(dirRaiz, dirBase, dirVideo, NomeVideo))
dirVideoOut = str(Path(dirRaiz, dirBase, dirVideo, NomeVideoOUT))

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
# Processo de Captura de Faces
########################################################################
# 
lstFrameVideo = []
with mpDetecacaoFaces.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detector:

    while (True):
        Status, VideoFrame = CapturaVideo.read()
        if Status is False:
           break

        imgReduzida = cv.resize(VideoFrame, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_CUBIC)
        #imgReduzida = cv.resize(VideoFrame, (640, 640), interpolation = cv.INTER_AREA)
        rgbVideoFrame = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
        faceResultado = face_detector.process(rgbVideoFrame)
        frmAltura, frmLargura, _ = imgReduzida.shape

        if faceResultado.detections:     
            for detection in faceResultado.detections:
                bbox = detection.location_data.relative_bounding_box
                xmin = int(bbox.xmin * frmLargura)
                ymin = int(bbox.ymin * frmAltura)
                xmax = int(bbox.width * frmLargura + bbox.xmin * frmLargura)
                ymax = int(bbox.height * frmAltura + bbox.ymin * frmAltura)                
                cv.rectangle(imgReduzida,  (xmin,ymin), (xmax,ymax), color=(255, 255, 255), thickness=4)           

                if ( xmin > 0  and  ymin > 0 and xmax > 0  and ymax > 0 ):          
                    RegiaoFace = imgReduzida[ymin:ymax, xmin:xmax]
                    FaceBorrada = cv.GaussianBlur(RegiaoFace, (99, 99), 30)
                    imgReduzida[ymin:ymax, xmin:xmax] = FaceBorrada
                    #cv.imshow("Caputa de Video", imgReduzida)

# 
########################################################################
# Apresentando a Captura
########################################################################
#
        cv.imshow("Caputa de Video", imgReduzida)
        lstFrameVideo.append(imgReduzida)
        if cv.waitKey(10) == 27:
            break

# 
########################################################################
# Fechando o Vídeo e Desmontando o Janelamento
########################################################################
# 
    #cv.destroyAllWindows()

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( dirVideoOut, 
                            Codec,                            
                            25, 
                            (frmLargura,frmAltura))

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
CapturaVideo.release()
VideoOut.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
