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
ClearCmd = "clear"  # Em Ambiente Windows deve ser usado cls
DirBase = "LocalCV/"
NomeJanela = "Video Base"
NomeImagem = "Pessoa.jpg"
CaminhoBase = "/home/asoares/" + DirBase
NomeJanela = "Leitura de Vídeo"
NomeVideo = "VideoPessoaCentro.mp4"
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

    VideoFrame = cv.resize(VideoFrame, (0,0), fx=0.3, fy=0.3, interpolation = cv.INTER_AREA)

    cv.imshow ( "JanelaBase", VideoFrame)
    cv.setWindowTitle("JanelaBase", NomeJanela )
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
  else: 
    break

# 
########################################################################
# Fechando o Arquivo de Vídeo e Destruindo o Janelamento
########################################################################
#  
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
