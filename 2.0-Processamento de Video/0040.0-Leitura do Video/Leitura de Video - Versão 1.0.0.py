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
NomeJanela = "Leitura de Vídeo"
NomeVideo = "Escritorio.mp4"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoVideo= CaminhoBase + "Videos/"


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
    exit()

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:
    cv.imshow ( "JanelaBase", VideoFrame)
    cv.setWindowTitle("JanelaBase", NomeJanela )

    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break
  
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
