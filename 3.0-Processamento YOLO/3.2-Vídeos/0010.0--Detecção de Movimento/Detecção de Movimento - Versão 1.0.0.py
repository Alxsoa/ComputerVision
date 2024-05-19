# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
from ultralytics import YOLO
import numpy as np
from PIL import Image
import requests
from io import BytesIO
import cv2 as cv
import os
from pathlib import Path
import pickle
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


def box_label(image, box, label='', color=(128, 128, 128), txt_color=(255, 255, 255)):
  lw = max(round(sum(image.shape) / 2 * 0.003), 2)
  p1, p2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
  cv.rectangle(image, p1, p2, color, thickness=lw, lineType=cv.LINE_AA)
  if label:
    tf = max(lw - 1, 1)  # font thickness
    w, h = cv.getTextSize(label, 0, fontScale=lw / 3, thickness=tf)[0]  # text width, height
    outside = p1[1] - h >= 3
    p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3
    cv.rectangle(image, p1, p2, color, -1, cv.LINE_AA)  # filled
    cv.putText( image,
                label, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2),
                0,
                lw / 3,
                txt_color,
                thickness=tf,
                lineType=cv.LINE_AA)
    
def plot_bboxes(image, boxes, score=True, conf=None):

  #plot each boxes
  for box in boxes:
    #add score in label if score=True
    if score :
      label = labels[int(box[-1])+1] + " " + str(round(100 * float(box[-2]),1)) + "%"
    else :
      label = labels[int(box[-1])+1]
    #filter every box under conf threshold if conf threshold setted
    if conf :
      if box[-2] > conf:
        color = colors[int(box[-1])]
        box_label(image, box, label, color)
    else:
      color = colors[int(box[-1])]
      box_label(image, box, label, color)

  #show image
  image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
  return (image) 

# 
########################################################################
# Definições Gerais
########################################################################
#
Codec = cv.VideoWriter_fourcc('m','p','4','v')
NomeVideoBase = "DetectaMovimento.mp4"
VideoOutName = "DetectaMovimentoYoloNanoOUT.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Videos"  

NomeEtiqueta = "Etiquetas.pkl"
NomeCores = "Cores.pkl"
NomeModelo  = "yolov8n.pt"
dirModelos = "Modelos"  

dirCaminhoEtiquetas = str(Path(dirRaiz, dirBase, dirModelos, NomeEtiqueta))
dirCaminhoCores = str(Path(dirRaiz, dirBase, dirModelos, NomeCores))
dirCaminhoModelo = str(Path(dirRaiz, dirBase, dirModelos, NomeModelo))
dirCaminhoBase = str(Path(dirRaiz, dirBase, dirImagem, NomeVideoBase))
dirVideoOut = str(Path(dirRaiz, dirBase, dirImagem, VideoOutName))

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
   model = YOLO(dirCaminhoModelo)

# 
########################################################################
# Lendo e Checando se o Arquivo de Etiquetas Existe
########################################################################
#
if not Path(dirCaminhoEtiquetas).is_file():
   LimpaTerminal ()
   print( "Não Foi Localizado o Arquivo : ", NomeEtiqueta)
   exit ()
else:
    with open(dirCaminhoEtiquetas, 'rb') as file:
      labels = pickle.load(file)

# 
########################################################################
# Lendo e Checando se o Arquivo de Cores Existe
########################################################################
#
if not Path(dirCaminhoCores).is_file():
   LimpaTerminal ()
   print( "Não Foi Localizado o Arquivo : ", NomeEtiqueta)
   exit ()
else:
    with open(dirCaminhoCores, 'rb') as file:
      colors = pickle.load(file)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( dirVideoOut, 
                            Codec,                            
                            25, 
                            (700, 400))

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

lstFrameVideo = []
while(Video.isOpened()):
    Status, VideoFrame = Video.read()

    if Status == True:
      TempoAtual = datetime.now() 
      HoraAtual = TempoAtual.strftime("%H:%M:%S")
      DataAtual = str(TempoAtual.day) + "-" + str(TempoAtual.month) + "-" + str(TempoAtual.year)

      cv.putText(VideoFrame, HoraAtual, (5, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
      cv.putText(VideoFrame, DataAtual, (570, 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

# 
########################################################################
# Executando o Modelo  
########################################################################
#
      iResultado = model.predict(VideoFrame)
      imgResultado = plot_bboxes(VideoFrame, iResultado[0].boxes.boxes, score=False)

      TemMovimento = iResultado [0]
      if ( len(TemMovimento.boxes) > 0):
         cv.putText(VideoFrame, "Movimento Detectado", (5, 420), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

      VideoFrameOUT = cv.resize(VideoFrame, (700, 400) ) 
      lstFrameVideo.append(VideoFrameOUT)

      cv.imshow ( "Janela Base", VideoFrame)
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
Video.release()
VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################	
