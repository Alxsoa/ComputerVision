# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeVideo = "Reporter1.mp4"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo = CaminhoBase + "Videos/" 

# 
########################################################################
# Checando se o Vídeo Está Disponível
########################################################################
#
video = cv.VideoCapture( CaminhoVideo + NomeVideo )
if not video.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", NomeVideo)
    exit ()

# 
########################################################################
# Leitura do Primeiro Frame
########################################################################
#
Status, VideoFrame = video.read()
if not Status:
    os.system ("clear")
    print( "Não Foi Possível Ler o Primeiro VideoFrame do Vídeo : ", NomeVideo)
    exit ()

# 
########################################################################
# Lendo o Vídeo
########################################################################
#
while (True):
    Status, VideoFrame = video.read()
    if not Status:
        break

    VideoFrame = cv.resize(VideoFrame, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)
# 
########################################################################
# Inserindo a Borda
########################################################################
#
    VideoFrameBorda = cv.copyMakeBorder (
                                            src=VideoFrame, 
                                            top=15, 
                                            bottom=15, 
                                            left=15, 
                                            right=15, 
                                            borderType=cv.BORDER_CONSTANT, 
                                            value=(255,255,255)
                                        ) 

# 
########################################################################
# Apresentando a Imagem 
########################################################################
#
    cv.imshow("Reportagem Sem Borda", VideoFrame)
    cv.imshow("Reportagem Com Borda", VideoFrameBorda)

    k = cv.waitKey(1) & 0xff
    if k == 27 : break

# 
########################################################################
# Destruindo o Janelamento
########################################################################
#
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
