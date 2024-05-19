# Referencia
# https://techtutorialsx.com/2021/04/20/python-real-time-hand-tracking/
# https://learnopencv.com/introduction-to-mediapipe/
# https://mlhive.com/2022/02/hand-landmarks-detection-using-mediapipe-in-python
# https://www.geeksforgeeks.org/face-and-hand-landmarks-detection-using-python-mediapipe-opencv/
# https://www.section.io/engineering-education/creating-a-hand-tracking-module/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv 
import mediapipe as mp
import os

# 
########################################################################
# Definições Gerais
########################################################################
# 
drawingModule = mp.solutions.drawing_utils
handsModule = mp.solutions.hands
WebCam = 2
CameraLargura=800
CameraAltura=600

# 
########################################################################
# Abrindo a WebCam e Checando o Acesso
########################################################################
# 
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
# Processo de Captura de Gestos
########################################################################
# 
with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands: 
    while (True):
 
        Status, VideoFrame = CapturaVideo.read()
        VideoFrame = cv.flip(VideoFrame, 1)        
        Resultado = hands.process(cv.cvtColor(VideoFrame, cv.COLOR_BGR2RGB))
 
        if Resultado.multi_hand_landmarks != None:
            for handLandmarks in Resultado.multi_hand_landmarks:
                drawingModule.draw_landmarks(VideoFrame, handLandmarks, handsModule.HAND_CONNECTIONS)

# 
########################################################################
# Apresentando a Captura
########################################################################
#
        cv.imshow( "Caputa de Gestos", VideoFrame)
        if cv.waitKey(1) == 27:
            break

# 
########################################################################
# Fechando o Janelamento e Camera
########################################################################
# 
cv.destroyAllWindows()
CapturaVideo.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
