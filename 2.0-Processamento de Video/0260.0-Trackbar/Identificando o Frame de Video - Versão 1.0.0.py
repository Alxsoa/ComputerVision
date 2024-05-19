# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Funções Necessárias
########################################################################
#
def getFrame(VideoFrame_nr):
    global Video
    Video.set(cv.CAP_PROP_POS_FRAMES, VideoFrame_nr)
    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Contraste e Brilho em Vídeo"
NomeVideo = "Baloes.mp4"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoVideo= CaminhoBase + "Videos/"

# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo + NomeVideo)
if (Video.isOpened()== False): 
    print ("########################################################################")
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit ()


NFrames = int(Video.get(cv.CAP_PROP_FRAME_COUNT))
cv.namedWindow("Video")
VelocidadeVideo = 1
cv.createTrackbar("Frame", "Video", 0,NFrames,getFrame)

while (True):
    Status, VideoFrame = Video.read()

    if Status:
        VideoFrame = cv.resize(VideoFrame,(0, 0),fx=0.3, fy=0.3, interpolation = cv.INTER_AREA)         
        cv.imshow ( "Video", VideoFrame)
        cv.setWindowTitle("Video", NomeJanela )     
        cv.setTrackbarPos("Frame","Video", int(Video.get(cv.CAP_PROP_POS_FRAMES)))
    else:
        break

    key = cv.waitKey(VelocidadeVideo)
    if key == ord('q'):
        break

# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#  
Video.release()
cv.destroyAllWindows()
exit ()

########################################################################
# FIM DO PROGRAMA
########################################################################
