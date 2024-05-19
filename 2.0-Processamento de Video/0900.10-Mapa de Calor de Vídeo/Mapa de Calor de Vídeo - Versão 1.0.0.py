import numpy as np
import cv2
import copy
from progress.bar import Bar
import os
import re

# 
########################################################################
# Funções de Uso Geral
########################################################################
#
def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def CriaVideo (image_folder, video_name):
    images = [img for img in os.listdir(image_folder)]
    images.sort(key=natural_keys)

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape
    Codec = cv2.VideoWriter_fourcc('m','p','4','v')
    video = cv2.VideoWriter(video_name, Codec, 30.0, (width, height))
    bar = Bar('Criando o Vídeo', max=len(images))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        bar.next()

    video.release()

    for file in os.listdir(image_folder):
        os.remove(image_folder + file)

    return 

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Leitura de Vídeo"
NomeVideo = "Shopping.mp4"
CaminhoBase = "/home/asoares/LocalCV/"
CaminhoVideo = CaminhoBase + "Videos/"
MapaFinalCalor = "MapaFinalCalor.jpg"
DiretorioAuxiliar = "Frames/"
VideoMapaCalor = "HeatMapVideo-VideoMapaCalor.mp4"

# 
########################################################################
# Lendo o Vídeo e Subtraindo o Background
########################################################################
#
Video = cv2.VideoCapture(CaminhoVideo+NomeVideo)
SemBackGround = cv2.createBackgroundSubtractorMOG2()
TamanhoVideo = int(Video.get(cv2.CAP_PROP_FRAME_COUNT))

BarraProgresso = Bar( "Processamento dos Frames ", max=TamanhoVideo)
Interacao = 1
for iAux in range(0, TamanhoVideo):

    Status, VideoFrame = Video.read()
    if Interacao == 1:

        PrimeiroFrame = copy.deepcopy(VideoFrame)
        Altura, Largura = VideoFrame.shape[:2]
        ImagemAcumulada = np.zeros((Altura, Largura), np.uint8)
        Interacao = 0
    else:
        Filtro = SemBackGround.apply(VideoFrame)  
        cv2.imwrite(CaminhoVideo+'/HeatMapVideo-Frame.jpg', VideoFrame)
        cv2.imwrite(CaminhoVideo+'/HeatMapVideo-DifrencaBackgroudFrame.jpg', Filtro)

        threshold = 2
        maxValue = 2
        ret, th1 = cv2.threshold(Filtro, threshold, maxValue, cv2.THRESH_BINARY)

        ImagemAcumulada = cv2.add(ImagemAcumulada, th1)
        cv2.imwrite(CaminhoVideo+'/HeatMapVideo-Mascara.jpg', ImagemAcumulada)
        VideoFrameColorido = cv2.applyColorMap(ImagemAcumulada, cv2.COLORMAP_AUTUMN  ) 
        VideoFrameResultado = cv2.addWeighted(VideoFrame, 0.7, VideoFrameColorido, 0.7, 0)

        NomeCaminhoFrames = CaminhoVideo+DiretorioAuxiliar+"/Frame%d.jpg" % iAux
        cv2.imwrite(NomeCaminhoFrames, VideoFrameResultado)

    BarraProgresso.next()

BarraProgresso.finish()

# 
########################################################################
# Gerando o Vídeo e o Mapa de Calor Final
########################################################################
#
print ( CaminhoVideo+DiretorioAuxiliar )
print ( CaminhoVideo+VideoMapaCalor )

CriaVideo (CaminhoVideo+DiretorioAuxiliar, CaminhoVideo+VideoMapaCalor)
imgColorida = cv2.applyColorMap(ImagemAcumulada, cv2.COLORMAP_HOT)
imgMapaCalorFinal = cv2.addWeighted(PrimeiroFrame, 0.7, imgColorida, 0.7, 0)

# 
########################################################################
# Salvndo o Mapa de Calor Final
########################################################################
#
cv2.imwrite(CaminhoVideo+MapaFinalCalor, imgMapaCalorFinal)

# 
########################################################################
# Fechando o Vídeo 
########################################################################
#
Video.release()
print (" ")

########################################################################
# FIM DO PROGRAMA
########################################################################
