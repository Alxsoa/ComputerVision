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
NomeJanela   = "Video Base"
NomeVideoIN  = "BaloesRuidoGaussiano.mp4"
NomeVideoOUT = "BaloesSemRuidoGaussiano.mp4"
CaminhoBase  = "/home/asoares/LocalCV/"
CaminhoVideo = CaminhoBase + "Videos/" 
Codec = cv.VideoWriter_fourcc('m','p','4','v')

# 
########################################################################
# Checando se o Vídeo Está Disponível
########################################################################
#
VideoIN = cv.VideoCapture (CaminhoVideo+NomeVideoIN)
if not VideoIN.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", NomeVideoIN)
    exit ()

# 
########################################################################
# Recuperando o Tamanho do Frame
########################################################################
#
LarguraFrame = int(VideoIN.get(3)/2)
AlturaFrame  = int(VideoIN.get(4)/2)
size = (LarguraFrame, AlturaFrame)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOUT = cv.VideoWriter(CaminhoVideo+NomeVideoOUT,
                         Codec,
                         24, size)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
VideoArray = []
print ("########################################################################")
print ("# Geração do Vídeo sem Ruído")
print ("########################################################################")
print ("# Início do Processamento de Remoção do Ruído do Vídeo ")
while(VideoIN.isOpened()):
  Status, VideoFrame = VideoIN.read()
  if Status == True:
    imgBaloes = cv.resize(VideoFrame,(0, 0),fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)    
    ImagemSemRuido = cv.fastNlMeansDenoisingColored (imgBaloes,None, 3, 3, 7, 21)
    VideoArray.append(ImagemSemRuido)
 
  else: 
    break

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
print ("# Fim do Processamento de Remoção do Ruído do Vídeo ")
print ("# Início da Geração do Vídeo ")

for iAux in range (0, len(VideoArray)):
    VideoOUT.write(VideoArray[iAux])

# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#  
VideoIN.release()
VideoOUT.release()

print ("# Fim da Geração do Vídeo ")
print ("########################################################################")

########################################################################
# FIM DO PROGRAMA
########################################################################
