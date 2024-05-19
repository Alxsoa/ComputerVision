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
NomeVideo = "Escritorio.mp4"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo= CaminhoBase + "Videos/" 
Codec = cv.VideoWriter_fourcc('m','p','4','v')

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoAzul = cv.VideoWriter ( CaminhoVideo+'EscritorioAzul.mp4', 
                             Codec,                            
                             25, 
                             (400, 250))

VideoVerde = cv.VideoWriter ( CaminhoVideo+'EscritorioVerde.mp4', 
                              Codec,                            
                              25, 
                              (400, 250))

VideoVermelho = cv.VideoWriter ( CaminhoVideo+'EscritorioVermelho.mp4', 
                                 Codec,                            
                                 25, 
                                 (400, 250))


# 
########################################################################
# Checando se o Vídeo Está Disponível
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo+NomeVideo)
if not Video.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", NomeVideo)
    exit ()

# 
########################################################################
# Apresentando o Vídeo Com Redução
########################################################################
#
lstAzul = []
lstVerde = []
lstVermelho = []
while(Video.isOpened()):
    Status, VideoFrame = Video.read()
    if Status == True:
# 
########################################################################
# Separando a Imagem nos Canais 
########################################################################
#
        VideoFrame = cv.resize(VideoFrame, (400, 250), interpolation = cv.INTER_AREA)
        Azul, Verde, Vermelho = cv.split(VideoFrame)
       
# 
########################################################################
# Apresentando a Imagem
########################################################################
#     
        imgAzul = cv.cvtColor(Azul, cv.COLOR_RGB2BGR)
        imgVerde = cv.cvtColor(Verde, cv.COLOR_RGB2BGR)
        imgVermelho = cv.cvtColor(Vermelho, cv.COLOR_RGB2BGR)

        lstAzul.append( imgAzul)
        lstVerde.append( imgVerde)
        lstVermelho.append( imgVermelho)       
        
    else: 
        break
# 
########################################################################
# Criação do Vídeo
########################################################################
#  
for iAux in range (0, len(lstAzul)):
    VideoAzul.write(lstAzul[iAux])  
 
for iAux in range (0, len(lstVerde)):
    VideoVerde.write(lstVerde[iAux])  

for iAux in range (0, len(lstVermelho)):
    VideoVermelho.write(lstVermelho[iAux])  

# 
########################################################################
# Fechando o Vídeo 
########################################################################
#  
VideoAzul.release()
VideoVerde.release()
VideoVermelho.release()
Video.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
