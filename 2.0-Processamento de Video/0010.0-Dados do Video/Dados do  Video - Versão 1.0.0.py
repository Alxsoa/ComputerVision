# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import datetime
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Dados do Vídeo"
NomeVideo  = "Escritorio.mp4"
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
  print ("# Mensagem de Erro ")
  print ("########################################################################")
  print ("# Vídeo Não Encontrado ")
  print ("########################################################################")
  exit()

# 
########################################################################
# Recuperando os Dados do Video
########################################################################
#
LarguraFrame = Video.get(cv.CAP_PROP_FRAME_WIDTH)
AlturaFrame  = Video.get(cv.CAP_PROP_FRAME_HEIGHT)
FramePorSegundo  = Video.get(cv.CAP_PROP_FPS)
QuantidadeFrames = Video.get(cv.CAP_PROP_FRAME_COUNT)
PlaybackTime = QuantidadeFrames / FramePorSegundo

print ("########################################################################")
print ("# Propriedades do Vídeo ")
print ("########################################################################")
print ("# Largura do Frame .......: ", LarguraFrame) 
print ("# Altura do Frame ........: ", AlturaFrame )
print ("# Frame por Segundo ......: ", FramePorSegundo )
print ("# Quantidade de Frames ...: ", QuantidadeFrames )
print ("# Tempo de Exibição (s) ..: ", PlaybackTime )
print ("########################################################################")

def TempoExibicao (TempoMiliSegundos):
    TempoMiliSegundos = int(TempoMiliSegundos)
    seconds=(TempoMiliSegundos/1000)%60
    seconds = int(seconds)
    minutes=(TempoMiliSegundos/(1000*60))%60
    minutes = int(minutes)
    hours=(TempoMiliSegundos/(1000*60*60))%24

    return(print ("%d:%d:%d" % (hours, minutes, seconds)))

# 
########################################################################
# Lendo o Tempo Restante do Vído
########################################################################
#
iFrame = 0
while(Video.isOpened()):
  ret, frame = Video.read()
  if ret == True:
    cv.imshow ( "JanelaBase", frame)
    cv.setWindowTitle("JanelaBase", NomeJanela )    
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
    if ( iFrame == FramePorSegundo ):
       TempoExibicao (Video.get(cv.CAP_PROP_POS_MSEC) )
       iFrame = 0
    else:
       iFrame = iFrame + 1
  else: 
    break
  
Video.release()
cv.destroyAllWindows()


########################################################################
# FIM DO PROGRAMA
########################################################################
