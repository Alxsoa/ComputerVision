# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
from pathlib import Path
import imutils

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
NomeImagem  = "Centroide.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Transformando em Tons de Cinza a Imagem
########################################################################
#
ImagemBase  = cv.imread(dirCaminhoImagem)
if ImagemBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Transformando em Tons de Cinza a Imagem e Aplica Blur e Limiar
########################################################################
#
imgBaseCinza = cv.cvtColor(ImagemBase, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgBaseCinza, (5, 5), 0)
imgLimiar = cv.threshold(imgBlur, 60, 255, cv.THRESH_BINARY)[1]

# 
########################################################################
# Busca os Contornos
########################################################################
#
iContornos = cv.findContours(imgLimiar.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
NumContornos = imutils.grab_contours(iContornos)

# 
########################################################################
# Calcula os Momentos e Indica o Centro
########################################################################
#
for iAux in NumContornos:
    M = cv.moments(iAux)
    if M['m00'] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv.drawContours(ImagemBase, [iAux], -1, (0, 255, 0), 2)
        cv.circle(ImagemBase, (cx, cy), 7, (255, 255, 255), -1)
        cv.putText(ImagemBase, "Centro", (cx - 20, cy - 20),cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

# 
########################################################################
# Apresenta os Resultados
########################################################################
#
cv.imshow ( "Janela Base", ImagemBase)
cv.waitKey(0)

########################################################################
# FIM DO PROGRAMA
########################################################################