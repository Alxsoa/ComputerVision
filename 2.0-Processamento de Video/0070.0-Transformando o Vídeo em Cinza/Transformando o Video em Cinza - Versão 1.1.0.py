# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv

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
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit ()

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:

    ImagemCinza = cv.cvtColor(VideoFrame, cv.COLOR_BGR2GRAY)
    cv.imshow ( "JanelaBase", ImagemCinza)
    cv.setWindowTitle("JanelaBase", NomeJanela )    
 
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break

# 
########################################################################
# Apresentando a Imagem Cinza
########################################################################
#
cv.waitKey(0)
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
