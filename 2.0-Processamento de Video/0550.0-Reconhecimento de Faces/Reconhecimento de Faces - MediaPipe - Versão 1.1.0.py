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

# 
########################################################################
# Definições Gerais
########################################################################
#
mpDetecacaoFaces = mp.solutions.face_detection
NomeVideo = "PessoaCorrendo.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirVideo= "Videos"  
dirCaminhoVideo = str(Path(dirRaiz, dirBase, dirVideo, NomeVideo))

# 
########################################################################
# Lendo o Video
########################################################################
#
CapturaVideo = cv.VideoCapture (dirCaminhoVideo)
if (CapturaVideo.isOpened()== False): 
    os.system ("clear")
    print( "Não Foi Localizada o Video : ", NomeVideo)
    exit ()

# 
########################################################################
# Processo de Captura de Faces
########################################################################
# 
with mpDetecacaoFaces.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detector:

    while (True):
        Status, VideoFrame = CapturaVideo.read()
        if Status is False:
           break

        imgReduzida = cv.resize(VideoFrame, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)
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

# 
########################################################################
# Apresentando a Captura
########################################################################
#        
        cv.imshow("Caputa de Video", imgReduzida)
        key = cv.waitKey(1)
        if key == ord("q"):
            break

# 
########################################################################
# Fechando o Vídeo e Desmontando o Janelamento
########################################################################
# 
    CapturaVideo.release()
    cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
