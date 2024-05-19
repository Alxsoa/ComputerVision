# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os

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
WebCam = 2
CameraLargura=800
CameraAltura=600

# 
########################################################################
# Definindo o Objeto Camera para Captura
########################################################################
#
VideoCamera = cv.VideoCapture(WebCam)

# 
########################################################################
# Abrindo a WebCam e Checando o Acesso
########################################################################
# 
if not VideoCamera.isOpened():
    LimpaTerminal ()
    print( "A WebCam Não esta Disponível")
    exit ()


# 
########################################################################
# Definindo o Tamanho da Imagem Capturada pela Câmera
########################################################################
#
VideoCamera.set(cv.CAP_PROP_FRAME_WIDTH, CameraLargura)
VideoCamera.set(cv.CAP_PROP_FRAME_HEIGHT,CameraAltura)

# 
########################################################################
# Início da Captura da Camera
########################################################################
#  
while(True):
      
    Status, Frame = VideoCamera.read()
    Frame = cv.flip(Frame, 1)    
    cv.imshow( "Camera Web", Frame)     
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
  
# 
########################################################################
# Liberando a Camera e Fechando o Janelamento
########################################################################
#  
VideoCamera.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
