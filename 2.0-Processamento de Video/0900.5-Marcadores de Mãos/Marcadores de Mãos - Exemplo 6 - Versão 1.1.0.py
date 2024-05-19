# Referencia
# https://techtutorialsx.com/2021/04/20/python-real-time-hand-tracking/
# https://learnopencv.com/introduction-to-mediapipe/
# https://mlhive.com/2022/02/hand-landmarks-detection-using-mediapipe-in-python
# https://www.geeksforgeeks.org/face-and-hand-landmarks-detection-using-python-mediapipe-opencv/
# https://www.section.io/engineering-education/creating-a-hand-tracking-module/
# https://techtutorialsx.com/2021/04/24/python-mediapipe-finger-roi/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv 
import mediapipe as mp
import os
import math
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
VideoOutName = "MarcadoresMaosExemplo6OUT.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Videos"  
dirVideoOut = str(Path(dirRaiz, dirBase, dirImagem, VideoOutName))

drawingModule = mp.solutions.drawing_utils
handsModule = mp.solutions.hands
WebCam = 2
CameraLargura=800
CameraAltura=600

# 
########################################################################
# Funções de Apoio
########################################################################
# 
def CalculaDistanciaEuclidiana ( ptsPixel, ptsCirculo):
    tmpDistancia = 0
    if ( ptsPixel is not None):
        ptsPixelX = ptsPixel[0]
        ptsPixelY = ptsPixel[1]
        ptsCirculoX = ptsCirculo [0]
        ptsCirculoY = ptsCirculo [1]
        tmpDistancia = math.sqrt ( (ptsPixelX-ptsCirculoX)**2 + (ptsPixelY-ptsCirculoY)**2 )
    return (tmpDistancia)
# 
########################################################################
# Abrindo a WebCam e Checando o Acesso
########################################################################
# 
CapturaVideo = cv.VideoCapture(WebCam)
if not CapturaVideo.isOpened():
    LimpaTerminal ()
    print( "A WebCam Não esta Disponível")
    exit ()

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( dirVideoOut, 
                            Codec,                            
                            25, 
                            (CameraLargura, CameraAltura))

# 
########################################################################
# Definindo o Tamanho da Imagem Capturada pela Câmera
########################################################################
#
CapturaVideo.set(cv.CAP_PROP_FRAME_WIDTH, CameraLargura)
CapturaVideo.set(cv.CAP_PROP_FRAME_HEIGHT,CameraAltura)

# 
########################################################################
# Recuperando as Dimensões da Janela e Desenha o Círculo de Controle
########################################################################
# 
LarguraFrame = CapturaVideo.get(cv.CAP_PROP_FRAME_WIDTH)
AlturaFrame = CapturaVideo.get(cv.CAP_PROP_FRAME_HEIGHT)
 
CentroCirculo = (round(LarguraFrame/2), round(AlturaFrame/2))
TamanhoCirculo = 40

# 
########################################################################
# Processo de Captura de Gestos
########################################################################
# 
lstFrameVideo = []
with handsModule.Hands (
                        static_image_mode=False, 
                        min_detection_confidence=0.7, 
                        min_tracking_confidence=0.7, 
                        max_num_hands=2
                       ) as hands: 
    while (True):
 
        Status, VideoFrame = CapturaVideo.read()
        VideoFrame = cv.flip(VideoFrame, 1)
        Resultado = hands.process(cv.cvtColor(VideoFrame, cv.COLOR_BGR2RGB))
        CorCirculo = (0, 0, 0)

        if Resultado.multi_hand_landmarks != None:
            ptsNormalizado = Resultado.multi_hand_landmarks[0].landmark[handsModule.HandLandmark.INDEX_FINGER_TIP]
            ptsCoordenada = drawingModule._normalized_to_pixel_coordinates ( ptsNormalizado.x,
                                                                             ptsNormalizado.y,
                                                                             LarguraFrame,
                                                                             AlturaFrame) 
            
            cv.circle(VideoFrame, ptsCoordenada, 4, (255,0,0), -1) 
            DistanciaDedoCentro = CalculaDistanciaEuclidiana (ptsCoordenada, CentroCirculo)                    
            if DistanciaDedoCentro < TamanhoCirculo:
                CorCirculo = (0,255,0)
            else:
                CorCirculo = (0,0,255)
                                       
# 
########################################################################
# Apresentando a Captura
########################################################################
#
        cv.circle(VideoFrame, CentroCirculo, TamanhoCirculo, CorCirculo, -1) 
        lstFrameVideo.append(VideoFrame)
        cv.imshow( "Marcadores de Maos", VideoFrame)
        if cv.waitKey(1) == 27:
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
CapturaVideo.release()
VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
