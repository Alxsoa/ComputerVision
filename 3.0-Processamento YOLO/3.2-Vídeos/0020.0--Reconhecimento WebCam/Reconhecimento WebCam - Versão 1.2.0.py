# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
from ultralytics import YOLO
import cv2 as cv
import math 
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
Codec = cv.VideoWriter_fourcc("m","p","4","v")
VideoOutName = "ReconhecimentoWebCamOUT.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Videos"  

NomeModelo  = "yolov8n.pt"
dirModelos = "Modelos"  

dirCaminhoModelo = str(Path(dirRaiz, dirBase, dirModelos, NomeModelo))
dirVideoOut = str(Path(dirRaiz, dirBase, dirImagem, VideoOutName))

Debug = False
WebCam = 2
Largura = 640
Altura = 480
FPS = 25 

corCaixa = (0, 0, 255)
larguraCaixa = 2
escalaTexto = 1
corTexto = (255, 0, 0)
larguraTexto = 2

classNames =    [
                    "person",           "bicycle",      "car",              "motorbike",     "aeroplane",    
                    "bus",              "train",        "truck",            "boat",          "traffic light", 
                    "fire hydrant",     "stop sign",    "parking meter",    "bench",         "bird", 
                    "cat",              "dog",          "horse",            "sheep",         "cow", 
                    "elephant",         "bear",         "zebra",            "giraffe",       "backpack", 
                    "umbrella",         "handbag",      "tie",              "suitcase",      "frisbee", 
                    "skis",             "snowboard",    "sports ball",      "kite",          "baseball bat",
                    "baseball glove",   "skateboard",   "surfboard",        "tennis racket", "bottle", 
                    "wine glass",       "cup",          "fork",             "knife",         "spoon", 
                    "bowl",             "banana",       "apple",            "sandwich",      "orange", 
                    "broccoli",         "carrot",       "hot dog",          "pizza",         "donut", 
                    "cake",             "chair",        "sofa",             "pottedplant",   "bed",
                    "diningtable",      "toilet",       "tvmonitor",        "laptop",        "mouse", 
                    "remote",           "keyboard",     "cell phone",       "microwave",     "oven", 
                    "toaster",          "sink",         "refrigerator",     "book",          "clock", 
                    "vase",             "scissors",     "teddy bear",       "hair drier",    "toothbrush"
              ]

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
                            FPS, 
                            (Largura, Altura))

# 
########################################################################
# Especificando as Propriedades Desejadas
########################################################################
# 
CapturaVideo.set(cv.CAP_PROP_FRAME_WIDTH, Largura)
CapturaVideo.set(cv.CAP_PROP_FRAME_HEIGHT, Altura)
CapturaVideo.set(cv.CAP_PROP_FPS, FPS)

# 
########################################################################
# Lendo e Checando se o Modelo Existe
########################################################################
#
if not Path(dirCaminhoModelo).is_file():
   LimpaTerminal ()
   print( "Não Foi Localizado o Modelo : ", NomeModelo)
   exit ()
else:
   yoloModelo = YOLO(dirCaminhoModelo)

lstFrameVideo = []
while (True):
    Status, VideoFrame = CapturaVideo.read()

    if Status == True:
        Resultado = yoloModelo ( VideoFrame, conf=0.4, verbose=False)

        for Coordenadas in Resultado:
            Caixas = Coordenadas.boxes

            for ListaCaixas in Caixas:
                x1, y1, x2, y2 = ListaCaixas.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 

                cv.rectangle (
                                VideoFrame, 
                                (x1, y1), 
                                (x2, y2), 
                                corCaixa, 
                                larguraCaixa
                             )

                IndentificaClasse = int(ListaCaixas.cls[0])
                if (Debug):
                    confidence = math.ceil((ListaCaixas.conf[0]*100))/100
                    print("Confiança Detecção ..: ", confidence)
                    print("Nome da Classe ......: ", classNames[IndentificaClasse])

                ptsOrigem = [x1, y1]
                cv.putText  (
                                VideoFrame, 
                                classNames[IndentificaClasse], 
                                ptsOrigem, 
                                cv.FONT_HERSHEY_SIMPLEX, 
                                escalaTexto, 
                                corTexto, 
                                larguraTexto
                            )

        VideoFrameOUT = cv.resize(VideoFrame, (Largura, Altura) ) 
        lstFrameVideo.append(VideoFrameOUT)
        cv.imshow("Reconhecimento Webcam", VideoFrame)
        if cv.waitKey(1) == ord("q"):
            break

    else: 
      break

# 
########################################################################
# Fechando o Arquivo de Vídeo e Desmontando o Janelamento
########################################################################
# 
CapturaVideo.release()
cv.destroyAllWindows()

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
for iAux in range (0, len(lstFrameVideo)):
    VideoOut.write(lstFrameVideo[iAux])  
VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################