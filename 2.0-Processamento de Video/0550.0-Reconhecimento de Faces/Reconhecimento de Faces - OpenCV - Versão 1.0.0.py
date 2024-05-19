# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
from pathlib import Path

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeVideo = "PessoaCorrendo.mp4"
NomePadrao = "haarcascade_frontalface_default.xml"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirVideo= "Videos"  
dirPadrao = "Padroes"
dirCaminhoVideo = str(Path(dirRaiz, dirBase, dirVideo, NomeVideo))
dirCaminhoPadrao = str(Path(dirRaiz, dirBase, dirPadrao, NomePadrao))

# 
########################################################################
# Lendo o Padrão de Reconhecimento
########################################################################
#
CascataFaces = cv.CascadeClassifier(dirCaminhoPadrao)

# 
########################################################################
# Lendo o Video
########################################################################
#
Video = cv.VideoCapture (dirCaminhoVideo)
if (Video.isOpened()== False): 
    os.system ("clear")
    print( "Não Foi Localizado o Video : ", NomeVideo)
    exit ()

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:
     imgReduzida = cv.resize(VideoFrame, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)
     ImagemCinza = cv.cvtColor(imgReduzida, cv.COLOR_BGR2GRAY)

     Faces = CascataFaces.detectMultiScale(ImagemCinza, 1.2, 1)
     if len(Faces) > 0:
         for (x,y,w,h) in Faces:
            RegiaoFace = imgReduzida[y:y+h, x:x+w]
            cv.rectangle(imgReduzida,(x,y),(x+w,y+h),(0,255,255),2)

     cv.imshow ( "JanelaBase", imgReduzida)
     if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break

# 
########################################################################
# Fechando o Vídeo e Desmontando o Janelamento
########################################################################
#  
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################

exit()
# 
########################################################################
# Lendo o Padrão de Reconhecimento
########################################################################
#
CascataFaces = cv.CascadeClassifier(CaminhoPadrao+NomePadrao)

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Loop de Busca do Padrão
########################################################################
#
ImagemCinza = cv.cvtColor(ImagemBase, cv.COLOR_BGR2GRAY)
Faces = CascataFaces.detectMultiScale(ImagemCinza, 1.1, 3)
print( "Número de Faces Detectadas = ", len(Faces))

if len(Faces) > 0:
   for (x,y,w,h) in Faces:

      cv.rectangle(ImagemBase,(x,y),(x+w,y+h),(0,255,255),2)
      cv.putText(ImagemBase, "Face Felina", (x, y-3), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)

# 
########################################################################
# Apresentando a Imagem Cinza
########################################################################
#
cv.imshow('Reconhecimento Padrao',ImagemBase)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
