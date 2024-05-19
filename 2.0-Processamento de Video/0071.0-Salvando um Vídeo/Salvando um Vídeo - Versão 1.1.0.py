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
NomeJanela = "Vídeo Transformado em Tons de Cinza"
NomeVideo  = "Escritorio.mp4"
VideoOutName = "EscritorioCinza.mp4"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo = CaminhoBase + "Videos/"  
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
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( CaminhoVideo+VideoOutName, 
                            Codec,                            
                            25, 
                            (400, 250))

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
lstFrameVideoCinza = []
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:

    ImagemCinza = cv.cvtColor(VideoFrame, cv.COLOR_BGR2GRAY)
    ImagemCinza = cv.resize(ImagemCinza, (400, 250) )     
    ImagemCinza = cv.cvtColor(ImagemCinza, cv.COLOR_GRAY2RGB )    
    VideoFrame = cv.resize(VideoFrame, (400, 250) )    
    lstFrameVideoCinza.append(ImagemCinza)

    imgTodasImagens = np.hstack(( VideoFrame, ImagemCinza )) 
    cv.imshow ( "Transformacao do Video", imgTodasImagens)
    if cv.waitKey(25) == ord('q'):
      break
 
  else: 
    break

# 
########################################################################
# Fechamento do Janelamento
########################################################################
#
cv.destroyAllWindows()

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
for iAux in range (0, len(lstFrameVideoCinza)):
    VideoOut.write(lstFrameVideoCinza[iAux])  

# 
########################################################################
# Fechamento dos Arquivos
########################################################################
#
Video.release()
VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
