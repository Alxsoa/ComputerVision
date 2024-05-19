# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
from progress.bar import Bar
import os
import platform

# 
########################################################################
# Documentação
########################################################################
#
strDoc = "\
########################################################################\n\
# Documentação do Módulo\n\
########################################################################\n\
# \n\
# Objetivo\n\
# --------\n\
# Apresentar a criação de um vídeo sintético, com fundo estático.\n\
# \n\
# Referencia\n\
# ----------\n\
# Não Aplicado.\n\
# \n\
# Versão das Bibliotecas Utilizadas\n\
# ---------------------------------\n\
# OpenCV ...: {0} \n\
# Numpy ....: {1} \n\
# \n\
# Versão do Ambiente\n\
# ------------------\n\
# Python ...: {2} \n\
# SO .......: {3} \n\
# \n\
########################################################################\n\
"

# 
########################################################################
# Definições Gerais
########################################################################
#
ClearCmd = "clear"  # Em Ambiente Windows deve ser usado cls
DirBase = "LocalCV/"
NomeJanela = "Video Base"
NomeVideo  = "Baloes.mp4"
VideoOutName = "VideoSinteticoFundoEstatico.avi"
CaminhoBase = "/home/asoares/" + DirBase
CaminhoVideo = CaminhoBase + "Videos/" 
CorFundo = (204, 255, 255)

Largura = 1280
Altura  = 720
FPS = 24
seconds = 10
Radius = 90
ptsH = int(Altura/2)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( CaminhoVideo+VideoOutName, 
                            cv.VideoWriter_fourcc(*'MJPG'),
                            float(FPS), 
                            (Largura, Altura))
# 
########################################################################
# Loop de Criação do Vídeo
########################################################################
#
os.system (ClearCmd) 
print ( strDoc.format (
                        cv.__version__, 
                        np.__version__, 
                        platform.python_version(), 
                        platform.system()
                      ) )

Tamanho = list(range(-Radius, Largura+Radius, 6))
with Bar('Geração do Vídeo ...', max=len(Tamanho)) as bar:
    for ptsX in range(-Radius, Largura+Radius, 6):     
#        VideoFrame = np.random.randint  ( 
#                                            0, 256, 
#                                            (Altura, Largura, 3), 
#                                            dtype=np.uint8
#                                        )
        VideoFrame = np.full((Altura, Largura, 3), CorFundo, dtype=np.uint8) 
        
        cv.circle(VideoFrame, (ptsX, ptsH), Radius, (0, 255, 0), -1)
        VideoOut.write(VideoFrame)
        bar.next()

VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
