# Referencia


# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv 
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
WebCam = 2
Largura = 1280
Altura = 720
FPS = 30 

# 
########################################################################
# Abrindo a WebCam e Checando o Acesso
########################################################################
# 
CapturaVideo = cv.VideoCapture(WebCam)
if not CapturaVideo.isOpened():
    os.system ("clear")
    print( "A WebCam Não esta Disponível")
    exit ()

# 
########################################################################
# Especificando as Propriedades Desejadas
########################################################################
# 
CapturaVideo.set(cv.CAP_PROP_FRAME_WIDTH, Largura)
CapturaVideo.set(cv.CAP_PROP_FRAME_HEIGHT, Altura)
CapturaVideo.set(cv.CAP_PROP_FPS, FPS)

# 
########################################################################
# Processo de Captura de Vídeo
########################################################################
# 
while (True):

    Status, VideoFrame = CapturaVideo.read()
    if Status == True:
        cv.imshow( "Caputa de Video", VideoFrame)
        if cv.waitKey(1) == 27:
            break

# 
########################################################################
# Fechando o Janelamento e Camera
########################################################################
# 
cv.destroyAllWindows()
CapturaVideo.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
