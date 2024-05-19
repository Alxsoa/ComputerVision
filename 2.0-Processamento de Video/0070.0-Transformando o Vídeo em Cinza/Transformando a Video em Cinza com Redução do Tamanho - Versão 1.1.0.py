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
BaseDir = "LocalCV/"
NomeJanela = "Vídeo Transformado em Tons de Cinza"
NomeVideo  = "Escritorio.mp4"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo = CaminhoBase + "Videos/"  

# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo+NomeVideo)
if (Video.isOpened()== False): 
    print ("########################################################################")
    print ("# Mensagem de Erro ")
    print ("########################################################################")
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit ()

# 
########################################################################
# Recuperando o Tamanho do Frame
########################################################################
#
LarguraFrame = Video.get(cv.CAP_PROP_FRAME_WIDTH)
AlturaFrame  = Video.get(cv.CAP_PROP_FRAME_HEIGHT)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
EscalaPercentual = 0.3 
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:

    ImagemCinza = cv.cvtColor(VideoFrame, cv.COLOR_BGR2GRAY)
    ImagemCinza = cv.resize(ImagemCinza, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual)
    VideoFrame  = cv.resize(VideoFrame, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual)
    ImagemCinza = cv.cvtColor(ImagemCinza,cv.COLOR_GRAY2RGB)   

    imgTodasImagens = np.hstack(( VideoFrame, ImagemCinza )) 
    cv.imshow ( "Transformacao do Video", imgTodasImagens)
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break

# 
########################################################################
# Fechamento dos Arquivos
########################################################################
#
cv.waitKey(0)
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
