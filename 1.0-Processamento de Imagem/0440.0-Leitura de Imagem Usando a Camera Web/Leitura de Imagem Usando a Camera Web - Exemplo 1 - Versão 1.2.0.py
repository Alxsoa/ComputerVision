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
NumeroCamera = 2

# 
########################################################################
# Definindo o Objeto Camera para Captura
########################################################################
#
VideoCamera = cv.VideoCapture(NumeroCamera)

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
# Apresentando os Dados da Imagem
########################################################################
#
# Brilho: Esta propriedade não é para arquivos de vídeo. Só funciona 
# com uma câmera ou webcam. Usado para descobrir o brilho.
#
# Contraste: Esta propriedade também funciona apenas com a câmera ou 
# webcam. Usado para descobrir o contraste nas imagens capturadas.
#
# Valor de Saturação: É usado para obter a saturação dos quadros ao 
# vivo capturados pelas câmeras. Isso também não funciona no arquivo de vídeo.
#
# Valor HUE: Serve para saber o valor HUE da imagem. Somente para câmeras.
#
# GAIN: Esta propriedade é usada para obter o ganho da imagem. Não 
# funcionaria com o arquivo de vídeo, basta retornar “0” se aplicado em um arquivo de vídeo.
#

print ("")
print ("#######################################################################")
print ("# Dados da Câmera WEB" )
print ("#######################################################################")
print ("CAP_PROP_FRAME_COUNT ....: '{}'".format(VideoCamera.get(cv.CAP_PROP_FRAME_COUNT)))
print ("CAP_PROP_BRIGHTNESS .....: '{}'".format(VideoCamera.get(cv.CAP_PROP_BRIGHTNESS)))
print ("CAP_PROP_CONTRAST .......: '{}'".format(VideoCamera.get(cv.CAP_PROP_CONTRAST)))
print ("CAP_PROP_SATURATION .....: '{}'".format(VideoCamera.get(cv.CAP_PROP_SATURATION)))
print ("CAP_PROP_HUE ............: '{}'".format(VideoCamera.get(cv.CAP_PROP_HUE)))
print ("CAP_PROP_GAIN  ..........: '{}'".format(VideoCamera.get(cv.CAP_PROP_GAIN)))
print ("#######################################################################")
print ("")

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
