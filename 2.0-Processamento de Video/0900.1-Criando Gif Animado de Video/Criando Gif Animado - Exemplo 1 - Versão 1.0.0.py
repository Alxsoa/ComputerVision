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
# Salvando o Gif Animado a Duracao é em ms (50 fps == 20 duration)
########################################################################
#
imageio.mimsave( CaminhoVideo + NomeSaida, lstFrameVideo, duration=100)

########################################################################
# FIM DO PROGRAMA
########################################################################