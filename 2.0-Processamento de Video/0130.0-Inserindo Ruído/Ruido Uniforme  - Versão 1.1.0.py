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
NomeJanela = "Video Base"
NomeVideo = "Baloes.mp4"
CaminhoBase = "/home/asoares/LocalCV/"
CaminhoVideo= CaminhoBase + "Videos/" 
Codec = cv.VideoWriter_fourcc('m','p','4','v')

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
# Recuperando o Tamanho do Frame
########################################################################
#
LarguraFrame = int(Video.get(3)/2)
AlturaFrame  = int(Video.get(4)/2)
size = (LarguraFrame, AlturaFrame)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter(CaminhoVideo+'BaloesRuidoUniforme.mp4', 
                         Codec,
                         24, size)

# 
########################################################################
# Apresentando o Vídeo Com Redução
########################################################################
#
VideoArray = []

print ("########################################################################")
print ("# Geração do Vídeo com Ruído")
print ("########################################################################")
print ("# Início da Geração do Vídeo ")

while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:
 
    imgBaloes = cv.resize(VideoFrame,(0, 0),fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)
# 
########################################################################
# Recuperando as Dimensões da Imagem 
########################################################################
#
    ImagemAltura  = imgBaloes.shape[0]
    ImagemLargura = imgBaloes.shape[1]
    ImagemCanais  = imgBaloes.shape[2]

# 
########################################################################
# Inserindo o Ruído 
########################################################################
#
    RuidoUniforme = np.zeros((ImagemAltura, ImagemLargura) )
    cv.randu(RuidoUniforme,0,255)
    RuidoUniforme=(RuidoUniforme*0.5).astype(np.uint8)
    RuidoUniforme = cv.merge((RuidoUniforme,RuidoUniforme,RuidoUniforme))

# 
########################################################################
# Combinando as Imagens
########################################################################
#
    ImagemResultado = cv.add ( imgBaloes, RuidoUniforme ) 
    VideoArray.append(ImagemResultado)

  else: 
    break

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
for iAux in range (0, len(VideoArray)):
    VideoOut.write(VideoArray[iAux])

# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#  
Video.release()
print ("# Fim da Geração do Vídeo ")
print ("########################################################################")

########################################################################
# FIM DO PROGRAMA
########################################################################
