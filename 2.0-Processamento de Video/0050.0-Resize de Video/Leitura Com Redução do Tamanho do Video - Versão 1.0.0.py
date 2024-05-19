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
NomeJanela = "Redução do Tamanho do Vídeo"
NomeVideo = "Escritorio.mp4"
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

# 
########################################################################
# Recuperando o Tamanho do Frame
########################################################################
#
LarguraFrame = Video.get(cv.CAP_PROP_FRAME_WIDTH)
AlturaFrame  = Video.get(cv.CAP_PROP_FRAME_HEIGHT)

# 
########################################################################
# Apresentando o Vídeo Com Redução
########################################################################
#
EscalaPercentual = 50 
LarguraAlterada  = int(LarguraFrame * EscalaPercentual / 100)
AlturaAlterada   = int(AlturaFrame * EscalaPercentual / 100)
NovoTamanho = (LarguraAlterada, AlturaAlterada)

while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:
 
    NovoTamanho = cv.resize(VideoFrame,(0, 0),fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)
    cv.imshow ( "JanelaBase", NovoTamanho)
    cv.setWindowTitle("JanelaBase", NomeJanela )    
 
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
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
