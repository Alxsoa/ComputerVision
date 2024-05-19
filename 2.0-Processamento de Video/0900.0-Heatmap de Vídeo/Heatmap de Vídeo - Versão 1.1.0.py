
# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import numpy as np
import cv2
import copy
from progress.bar import Bar
import os
import re

# 
########################################################################
# Funções de Apoio
########################################################################
#
def atoi(text):
    # A helper function to return digits inside text
    return int(text) if text.isdigit() else text

def natural_keys(text):
    # A helper function to generate keys for sorting frames AKA natural sorting
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def CriaVideo (image_folder, video_name):
    images = [img for img in os.listdir(image_folder)]
    images.sort(key=natural_keys)

    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc('m','p','4','v')

    video = cv2.VideoWriter(video_name, fourcc, 30.0, (width, height))
    bar = Bar( "Criando o Video .........: ", max=len(images))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))
        bar.next()

    cv2.destroyAllWindows()
    video.release()

    for file in os.listdir(image_folder):
        os.remove(image_folder + file)

    print (" ")
# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeVideo = "MovimentoPessoas.mp4"
TmpDir = "Frames/"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo = CaminhoBase + "Videos/" 
CaminhoTmp = CaminhoBase + "Videos/" + TmpDir
NomeVideoSaida = "HeatmapMovimento.mp4"

# 
########################################################################
# Checando se o Vídeo Está Disponível
########################################################################
#
capture = cv2.VideoCapture( CaminhoVideo + NomeVideo )
if not capture.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", NomeVideo)
    exit ()

os.system ("clear")
background_subtractor = cv2.bgsegm.createBackgroundSubtractorMOG()
length = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))

bar = Bar( "Processando os Frames ...: ", max=length)

first_iteration_indicator = 1
for i in range(0, length):
    ret, frame = capture.read()

    # If first frame
    if first_iteration_indicator == 1:
        first_frame = copy.deepcopy(frame)
        height, width = frame.shape[:2]
        accum_image = np.zeros((height, width), np.uint8)
        first_iteration_indicator = 0
    else:
        filter = background_subtractor.apply(frame)  # remove the background
        cv2.imwrite( CaminhoVideo + "HeatMapVideo-Frame.jpg", frame)
        cv2.imwrite( CaminhoVideo + "HeatMapVideo-diff-bkgnd-frame.jpg", filter)

        threshold = 2
        maxValue = 2
        ret, th1 = cv2.threshold(filter, threshold, maxValue, cv2.THRESH_OTSU)

        # add to the accumulated image
        accum_image = cv2.add(accum_image, th1)
        cv2.imwrite( CaminhoVideo + "HeatMapVideo-Mascara.jpg", accum_image)

        color_image_video = cv2.applyColorMap(accum_image, cv2.COLORMAP_HOT)
        video_frame = cv2.addWeighted(frame, 0.7, color_image_video, 0.7, 0)

        name = "Frame%d.jpg" % i
        cv2.imwrite( CaminhoTmp + name, video_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    bar.next()
bar.finish()

CriaVideo (CaminhoTmp,  CaminhoVideo + NomeVideoSaida)

color_image = cv2.applyColorMap(accum_image, cv2.COLORMAP_HOT)
result_overlay = cv2.addWeighted(first_frame, 0.7, color_image, 0.7, 0)

# save the final heatmap
cv2.imwrite( CaminhoVideo + "HeatMapVideo-diff-overlay.jpg", result_overlay)

# 
########################################################################
# Apresentando o Vídeo
########################################################################
#
capture.release()
cv2.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
