
# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np 
  
# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture(0) 
if (Video.isOpened()== False): 
    print ("########################################################################")
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit ()


while(Video.isOpened()):        
    Status, VideoFrame = Video.read() 
# 
########################################################################
# Convertendo os Frames BGR para HSV
########################################################################
#
    hsvCor = cv.cvtColor(VideoFrame, cv.COLOR_BGR2HSV)
    baixoAzul = np.array([110,50,50]) # BGR = 50/50/110
    altoAzul  = np.array([130,255,255]) # BGR = 255/255/130
  
# 
########################################################################
# Investigando as Cores Baseadas nos Limites Definidos (Mask)
########################################################################
#
    Mascara = cv.inRange(hsvCor, baixoAzul, altoAzul)
  
# 
########################################################################
# Apresentando a Imagem
########################################################################
#
    imgResultado = cv.bitwise_and (VideoFrame, VideoFrame, mask = Mascara)

    cv.imshow ( "JanelaBase", VideoFrame)
    cv.setWindowTitle("JanelaBase", "Frame de Vídeo" )

    cv.imshow ( "MascaraFrame", Mascara)
    cv.setWindowTitle("MascaraFrame", "Máscara de Vídeo" )

    cv.imshow ( "FrameResultado", imgResultado)
    cv.setWindowTitle("FrameResultado", "Frame Resultado de Vídeo" )
  
    if cv.waitKey(25) & 0xFF == ord('q'):
      break

# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#   
cv.destroyAllWindows()
Video.release()
