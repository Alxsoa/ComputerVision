# Referencia
# https://www.blog.pythonlibrary.org/2021/06/23/creating-an-animated-gif-with-python/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2
import imageio
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeVideo = "Chaplin.mp4"
NomeSaida = "Chaplin.gif"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo = CaminhoBase + "Videos/"
    
# 
########################################################################
# Checando se o Vídeo Está Disponível
########################################################################
#
Video = cv2.VideoCapture( CaminhoVideo + NomeVideo )
if not Video.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", NomeVideo)
    exit ()

# 
########################################################################
# Loop de Criação do Gif Animado
########################################################################
#
lstFrameVideo = []
while True:
    Status, VideoFrame = Video.read()

    if Status == True:
        lstFrameVideo.append(VideoFrame)
    else:
        break

# 
########################################################################
# Fechando o Video
########################################################################
#        
Video.release()

# 
########################################################################
# Salvando o Gif Animado 
########################################################################
#
with imageio.get_writer( CaminhoVideo + NomeSaida, mode="I") as EscreveGif:
    for idx, frame in enumerate(lstFrameVideo):
        EscreveGif.append_data(frame)

########################################################################
# FIM DO PROGRAMA
########################################################################