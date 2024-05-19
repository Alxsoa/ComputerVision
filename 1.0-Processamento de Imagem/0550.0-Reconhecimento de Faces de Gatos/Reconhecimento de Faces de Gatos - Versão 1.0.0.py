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
NomeImagem  = "FotoGato1.jpg"
#NomeImagem  = "FotoGato2.jpg"
#NomeImagem  = "FotoGato3.jpg"
NomePadrao  = "haarcascade_frontalcatface.xml"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirPadroes = "Padroes"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoPadrao = str(Path(dirRaiz, dirBase, dirPadroes, NomePadrao))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
if ImagemBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Lendo o Padrão de Reconhecimento
########################################################################
#
CascataFaces = cv.CascadeClassifier(dirCaminhoPadrao)
if not CascataFaces.load(dirCaminhoPadrao):
   LimpaTerminal ()
   print( "Não Foi Localizada o Padrão : ", dirCaminhoPadrao)
   exit ()

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
