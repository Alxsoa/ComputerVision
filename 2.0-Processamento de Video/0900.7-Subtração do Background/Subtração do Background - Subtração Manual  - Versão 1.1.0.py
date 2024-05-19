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
DirBase = "LocalCV/"
NomeVideo = "PeixeNadando.mp4"
CaminhoBase = "/home/asoares/" + DirBase
CaminhoVideo = CaminhoBase + "Videos/" 

# 
########################################################################
# Abrindo o Arquivo de Vídeo
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo + NomeVideo)
if (Video.isOpened()== False): 
  print ("########################################################################")
  print ("# Video Não Encontrado ")
  print ("########################################################################")
  exit ()

# 
########################################################################
# Conhecendo o Primeiro Frame
########################################################################
#
_, imgPeixeFrameInicial = Video.read()
imgPeixeFrameInicial = cv.resize(imgPeixeFrameInicial, (640, 480))
imgPeixeFrameInicialCinza = cv.cvtColor(imgPeixeFrameInicial, cv.COLOR_BGR2GRAY)
imgPeixeFrameInicialCinza = cv.GaussianBlur(imgPeixeFrameInicialCinza, (9, 9), 0)

# 
########################################################################
# Lendo o Video
########################################################################
#
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:

# 
########################################################################
# Reduzindo o Tamanho da Imagem
########################################################################
#
    imgPeixe = cv.resize(VideoFrame, (640, 480))

# 
########################################################################
# Removendo Possíveis Ruídos
########################################################################
#
    imgPeixeCinza = cv.cvtColor(imgPeixe, cv.COLOR_BGR2GRAY)
    imgPeixeCinza = cv.GaussianBlur(imgPeixeCinza, (9, 9), 0)

# 
########################################################################
# Diferença entre Frames
########################################################################
#
    imgDiferenca = cv.absdiff(imgPeixeFrameInicialCinza, imgPeixeCinza)
    _, imgDiferenca = cv.threshold(imgDiferenca, 25, 255, cv.THRESH_OTSU)

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
    imgTmpDiferenca = cv.cvtColor(imgDiferenca,cv.COLOR_GRAY2RGB)    
    imgTmpPeixeCinza = cv.cvtColor(imgPeixeCinza,cv.COLOR_GRAY2RGB)        
    imgTodasImagens = np.hstack(( imgPeixe, imgTmpPeixeCinza, imgTmpDiferenca ))   
    
    cv.imshow ( "Video Peixe", imgTodasImagens)  
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
# 
########################################################################
# Atualiza o Frame Inicial
########################################################################
#
    imgPeixeFrameInicialCinza = imgPeixeCinza

  else: 
    break
  
# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#  
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
