# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeVideo = "EscritorioComposto.mp4"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo= CaminhoBase + "Videos/" 
Codec = cv.VideoWriter_fourcc('m','p','4','v')

# 
########################################################################
# Lendo o Vídeo com Diferentes Canais
########################################################################
#
VideoAzul = cv.VideoCapture ( CaminhoVideo+'EscritorioAzul.mp4' )
if not VideoAzul.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", 'EscritorioAzul.mp4')
    exit ()

VideoVerde = cv.VideoCapture ( CaminhoVideo+'EscritorioVerde.mp4')
if not VideoVerde.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", 'EscritorioVerde.mp4')
    exit ()

VideoVermelho = cv.VideoCapture ( CaminhoVideo+'EscritorioVermelho.mp4')
if not VideoVermelho.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", 'EscritorioVermelho.mp4')
    exit ()

# 
########################################################################
# Criando o Vídeo Resultado
########################################################################
#
VideoComposto = cv.VideoWriter ( CaminhoVideo+'EscritorioComposto.mp4', 
                                 Codec,                            
                                 25, 
                                 (400, 250))

# 
########################################################################
# Recuperando os Canais de Vídeo
########################################################################
#
lstAzul = []
while(VideoAzul.isOpened()):
    Status, VideoFrameAzul = VideoAzul.read()
    if Status == True:
        lstAzul.append( VideoFrameAzul )
    else: 
        break

lstVerde = []
while(VideoVerde.isOpened()):
    Status, VideoFrameVerde = VideoVerde.read()
    if Status == True:
        lstVerde.append( VideoFrameVerde )
    else: 
        break

lstVermelho = []
while(VideoAzul.isOpened()):
    Status, VideoFrameVermelho = VideoVermelho.read()
    if Status == True:
        lstVermelho.append( VideoFrameVermelho )
    else: 
        break

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
for iAux in range (0, len(lstAzul)):
    imgComposta = cv.merge((lstAzul[iAux][:, :, 2:3],lstVerde[iAux][:, :, 1:2],lstVermelho[iAux][:, :, 0:1]))
    VideoComposto.write ( imgComposta )

# 
########################################################################
# Fechando o Vídeo 
########################################################################
#  
VideoAzul.release()
VideoVerde.release()
VideoVermelho.release()
VideoComposto.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
