# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import time
import cv2 as cv
import mediapipe as mp
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
WebCam = 2
mpDetecacaoFaces = mp.solutions.face_detection
CameraLargura = 800
CameraAltura = 600

# 
########################################################################
# Abrindo a WebCam e Checando o Acesso
########################################################################
# 
#cap = cv.VideoCapture(WebCam)
CapturaVideo = cv.VideoCapture(WebCam)
if not CapturaVideo.isOpened():
    os.system ("clear")
    print( "A WebCam Não esta Disponível")
    exit ()

# 
########################################################################
# Definindo o Tamanho da Imagem Capturada pela Câmera
########################################################################
#
CapturaVideo.set(cv.CAP_PROP_FRAME_WIDTH, CameraLargura)
CapturaVideo.set(cv.CAP_PROP_FRAME_HEIGHT,CameraAltura)

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

        rgbVideoFrame = cv.cvtColor(VideoFrame, cv.COLOR_BGR2RGB)
        faceResultado = face_detector.process(rgbVideoFrame)
        frmAltura, frmLargura, _ = VideoFrame.shape
        if faceResultado.detections:
            for iFace in faceResultado.detections:
                ptsRetangulo = np.multiply (
                                            [
                                                iFace.location_data.relative_bounding_box.xmin,
                                                iFace.location_data.relative_bounding_box.ymin,
                                                iFace.location_data.relative_bounding_box.width,
                                                iFace.location_data.relative_bounding_box.height,
                                            ],
                                            [
                                                frmLargura, 
                                                frmAltura, 
                                                frmLargura, 
                                                frmAltura
                                            ]
                                          ).astype(int)
                
                cv.rectangle(VideoFrame, ptsRetangulo, color=(255, 255, 255), thickness=4)

# 
########################################################################
# Apresentando a Captura
########################################################################
#        
        cv.imshow("Caputa de Video", VideoFrame)
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
