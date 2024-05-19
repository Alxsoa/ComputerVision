# Referencia
# https://www.geeksforgeeks.org/connect-your-android-phone-camera-to-opencv-python/

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv 
import requests
import numpy as np
import imutils

# 
########################################################################
# Abrindo a WebCam e Checando o Acesso
########################################################################
# 
urlEndereco = "http://192.168.15.4:8080/shot.jpg"

# 
########################################################################
# Processo de Captura de Vídeo
########################################################################
# 

while (True):

    urlResposta = requests.get(urlEndereco)
    imgArray = np.array(bytearray(urlResposta.content), dtype=np.uint8)
    imgServidor = cv.imdecode(imgArray, -1)
    imgServidor = imutils.resize(imgServidor, width=640, height=480)
    cv.imshow("Imagem HTTP", imgServidor)

    if cv.waitKey(1) == 27:
        break

# 
########################################################################
# Fechando o Janelamento e Camera
########################################################################
# 
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
