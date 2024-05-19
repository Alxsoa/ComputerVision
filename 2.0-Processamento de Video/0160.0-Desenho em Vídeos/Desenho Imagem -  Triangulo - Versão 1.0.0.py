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
NomeJanela   = "Video com Círculo Desenhado"
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
# Desenhando o Círculo
########################################################################
#
     ImagemAlturaCentral  = int(imgChuva.shape[0]/2)
     ImagemLarguraCentral = int(imgChuva.shape[1]/2)
     Lado = 200

     LarguraLinha = 9
     CorLinha = (0, 0, 255 )
     Pontos = [(ImagemLarguraCentral-Lado, ImagemAlturaCentral), (ImagemLarguraCentral+Lado, ImagemAlturaCentral), (ImagemLarguraCentral, ImagemAlturaCentral-Lado)]
     imgChuva =  cv.polylines(imgChuva, np.array([Pontos]), True, CorLinha, 5)

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
