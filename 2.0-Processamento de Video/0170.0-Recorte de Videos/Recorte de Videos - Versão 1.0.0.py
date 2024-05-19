# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela   = "Recorte de Vídeo"
NomeVideoIN  = "Chuva.mp4"
CaminhoBase  = "/home/asoares/OpenCV/"
CaminhoVideo = CaminhoBase + "Videos/" 

# 
########################################################################
# Lendo o Video
########################################################################
#
VideoIN = cv.VideoCapture (CaminhoVideo+NomeVideoIN)
if (VideoIN.isOpened()== False): 
    print ("########################################################################")
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit ()

# 
########################################################################
# Recuperando o Tamanho do Frame
########################################################################
#
while(VideoIN.isOpened()):
  Status, VideoFrame = VideoIN.read()
  if Status == True:
     imgChuva = cv.resize(VideoFrame,(0, 0),fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)    

# 
########################################################################
# Recortando o Vídeo
########################################################################
#
     imgChuva = imgChuva[0:400, 0:400]
     cv.imshow ( "JanelaBase", imgChuva)
     cv.setWindowTitle("JanelaBase", NomeJanela )     
     if cv.waitKey(25) & 0xFF == ord('q'):
        break
 
  else: 
    break

cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
