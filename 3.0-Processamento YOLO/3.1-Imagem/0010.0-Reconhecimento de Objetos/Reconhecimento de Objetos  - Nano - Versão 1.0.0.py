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
NomeImagem  = "AmigosEscritorio.jpg"
NomeOutput  = "AmigosEscritorioNanoOUT.jpg"
NomeEtiqueta = "Etiquetas.pkl"
NomeCores = "Cores.pkl"
NomeModelo  = "yolov8n.pt"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirModelos = "Modelos"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoEtiquetas = str(Path(dirRaiz, dirBase, dirModelos, NomeEtiqueta))
dirCaminhoCores = str(Path(dirRaiz, dirBase, dirModelos, NomeCores))
dirCaminhoModelo = str(Path(dirRaiz, dirBase, dirModelos, NomeModelo))
dirCaminhoResultado = str(Path(dirRaiz, dirBase, dirImagem, NomeOutput))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
if imgBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()
else:
   imgReduzida = cv.resize(imgBase, (0,0), fx=0.50, fy=0.50, interpolation = cv.INTER_AREA)

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
# Convertendo para RGB
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)

# 
########################################################################
# Executando o Modelo  
########################################################################
#
iResultado = model.predict(imgReduzida)
imgResultado = plot_bboxes(imgReduzida, iResultado[0].boxes.boxes, score=False)

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
cv.imwrite(dirCaminhoResultado, imgResultado)
cv.imshow ( "Resultado Predicao", imgResultado)  
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################

