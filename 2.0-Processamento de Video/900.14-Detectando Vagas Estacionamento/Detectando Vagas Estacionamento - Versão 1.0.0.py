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
VideoOutName = "EstacionamentoOUT.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Videos"  
dirCaminhoBase = str(Path(dirRaiz, dirBase, dirImagem, NomeVideoBase))
dirVideoOut = str(Path(dirRaiz, dirBase, dirImagem, VideoOutName))
Debug = True

vaga1 = [1, 89, 108, 213]
vaga2 = [115, 87, 152, 211]
vaga3 = [289, 89, 138, 212]
vaga4 = [439, 87, 135, 212]
vaga5 = [591, 90, 132, 206]
vaga6 = [738, 93, 139, 204]
vaga7 = [881, 93, 138, 201]
vaga8 = [1027, 94, 147, 202]
vagas = [vaga1, vaga2, vaga3, vaga4, vaga5, vaga6, vaga7, vaga8 ]

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

#Status, VideoFrameSalvo = Video.read(0)
#cv.imwrite (dirVideoOut, VideoFrameSalvo )
#exit ()

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
lstFrameVideo = []
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:
    imgVideoFrameCinza = cv.cvtColor ( VideoFrame, cv.COLOR_BGR2GRAY )
    imgVideoFrameLimiar = cv.adaptiveThreshold (imgVideoFrameCinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 25, 16)
    imgVideoFrameBlur = cv.medianBlur (imgVideoFrameLimiar, 5)
    Kernel = np.ones ( (3,3), np.int8)
    imgVideoFrameDilatado = cv.dilate (imgVideoFrameBlur, Kernel)

    for xPos, yPos, Largura, Altura in vagas:
        imgPedaco = imgVideoFrameDilatado [yPos:yPos+Altura, xPos:xPos+Largura]
        iBrancos = cv.countNonZero (imgPedaco)

        if (Debug):
           cv.putText (VideoFrame, str(iBrancos), (xPos, yPos+Altura-10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

        if (iBrancos > 3000):
           cv.rectangle ( VideoFrame, (xPos, yPos), (xPos+Largura, yPos+Altura), (0,0,255), 4)
        else:
           cv.rectangle ( VideoFrame, (xPos, yPos), (xPos+Largura, yPos+Altura), (0,255,0), 4)

  cv.imshow ( "Janela Base", VideoFrame)
  #cv.imshow ( "Janela Negativa ", imgVideoFrameLimiar)
  cv.waitKey (10)

Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
