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
NomeJanela   = "Vídeo com Retângulo Desenhado"
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
     ImagemAltura = imgChuva.shape[0]
     ImagemLargura = imgChuva.shape[1]
     LarguraLinha = 9
     CorLinha = (0, 0, 255 )
     PontoInicial = (100,100)
     PontoFinal = (ImagemLargura-100,ImagemAltura-100 )
     NovaImagem = cv.rectangle(imgChuva, PontoInicial, PontoFinal, CorLinha, LarguraLinha)

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
