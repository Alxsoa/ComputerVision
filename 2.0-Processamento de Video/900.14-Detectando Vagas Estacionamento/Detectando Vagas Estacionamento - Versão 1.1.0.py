# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
from pathlib import Path

# 
########################################################################
# Funções de Apoio
########################################################################
#
def LimpaTerminal ():
    if os.name == "nt":
       _ = os.system( "cls" )
    else:
      _ = os.system( "clear ")
    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
Codec = cv.VideoWriter_fourcc('m','p','4','v')
NomeVideoBase = "Estacionamento.mp4"
VideoOutName = "EstacionamentoOUT.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Videos"  
dirCaminhoBase = str(Path(dirRaiz, dirBase, dirImagem, NomeVideoBase))
dirVideoOut = str(Path(dirRaiz, dirBase, dirImagem, VideoOutName))
Debug = False

ListaVagas = [
               [  1,  89, 108, 213, 0, 0],
               [115,  87, 152, 211, 1, 0],
               [289,  89, 138, 212, 2, 0],
               [439,  87, 135, 212, 3, 1],      
               [591,  90, 132, 206, 4, 0],
               [738,  93, 139, 204, 5, 1],
               [881,  93, 138, 201, 6, 0],
               [1027, 94, 147, 202, 7, 0]                        
             ]

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( dirVideoOut, 
                            Codec,                            
                            25, 
                            (700, 400))

# 
########################################################################
# Lendo e Checando a Disponibilidade do Vídeo 
########################################################################
#
Video = cv.VideoCapture (dirCaminhoBase)
if (Video.isOpened()== False): 
    LimpaTerminal ()
    print( "Não Foi Localizada o Vídeo : ", NomeVideoBase)
    exit ()

# 
########################################################################
# Usado para Levantar os Pontos das ListaVagas (Gimp)
########################################################################
#
#Status, VideoFrameSalvo = Video.read(0)
#cv.imwrite (dirVideoOut, VideoFrameSalvo )
#exit ()

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
lstFrameVideo = []
iListaVagasLivres = 6
iListaVagasOcupadas = 2

while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:
    imgVideoFrameCinza = cv.cvtColor ( VideoFrame, cv.COLOR_BGR2GRAY )
    imgVideoFrameLimiar = cv.adaptiveThreshold (imgVideoFrameCinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)
    imgVideoFrameBlur = cv.medianBlur (imgVideoFrameLimiar, 5)
    Kernel = np.ones ( (3,3), np.int8)
    imgVideoFrameDilatado = cv.dilate (imgVideoFrameBlur, Kernel)

    for xPos, yPos, Largura, Altura, idVaga, statusVaga in ListaVagas:
        imgPedaco = imgVideoFrameDilatado [yPos:yPos+Altura, xPos:xPos+Largura]
        iBrancos = cv.countNonZero (imgPedaco)

        if (Debug):
           cv.putText (VideoFrame, str(iBrancos), (xPos, yPos+Altura-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

        if (iBrancos > 3000):
           if (statusVaga == 0):
              ListaVagas [idVaga][statusVaga] = 1
              iListaVagasLivres = iListaVagasLivres - 1
              iListaVagasOcupadas = iListaVagasOcupadas + 1           
        else:      
           if (statusVaga == 1):
              ListaVagas [idVaga][statusVaga] = 0
              iListaVagasLivres = iListaVagasLivres + 1
              iListaVagasOcupadas = iListaVagasOcupadas - 1     

    cv.putText (VideoFrame, "Vagas Livres   = "+str(iListaVagasLivres), (15, 580), cv.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 1)
    cv.putText (VideoFrame, "Vagas Ocupadas = "+str(iListaVagasOcupadas), (15, 620), cv.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 1)

    VideoFrameOUT = cv.resize(VideoFrame, (700, 400) ) 
    lstFrameVideo.append(VideoFrameOUT)
    
    cv.imshow ( "Janela Base", VideoFrame)
    #cv.imshow ( "Janela Negativa ", imgVideoFrameLimiar)
    cv.waitKey (10)
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
for iAux in range (0, len(lstFrameVideo)):
    VideoOut.write(lstFrameVideo[iAux])  

# 
########################################################################
# Fechando o Arquivo de Vídeo  
########################################################################
# 
Video.release()
VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
