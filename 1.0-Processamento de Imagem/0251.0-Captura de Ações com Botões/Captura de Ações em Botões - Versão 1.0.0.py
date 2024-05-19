# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
from pathlib import Path
import numpy as np

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
NomeImagem = "Lapis.jpg"
NomeJanela = "Imagem Base"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Reduzindo a Imagem
########################################################################
#
imgReduzida = cv.resize(imgBase, (0,0), fx=0.4, fy=0.4, interpolation = cv.INTER_AREA)
imgOriginal = np.copy(imgReduzida) 

# 
########################################################################
# Função de Callback para Controle do Mouse
########################################################################
#
def ExecutaTracado(Evento,x,y,flags,param):
    global imgReduzida

    if Evento == cv.EVENT_LBUTTONDOWN:
       if ( (x > 15 and x < 180) and (y > 460 and y < 500)):
          imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2GRAY)
       else:
         if ( (x > 200 and x < 400) and (y > 460 and y < 500)):
            imgReduzida = np.copy(imgOriginal)    

            cv.rectangle(imgReduzida, (15,460), (180,500), (255,255,255), -1)
            cv.putText(imgReduzida, "[MUDA PARA CINZA]", (19, 485), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))

            cv.rectangle(imgReduzida, (200,460), (400,500), (255,255,255), -1)
            cv.putText(imgReduzida, "[MUDA PARA COLORIDA]", (206, 485), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))

    return ()

# 
########################################################################
# Janelamento e Instancia de Função
########################################################################
#
cv.namedWindow (NomeJanela)
cv.setMouseCallback (NomeJanela, ExecutaTracado)

# 
########################################################################
# Desenhando o Botão e Escrevendo o Texto
########################################################################
#
cv.rectangle(imgReduzida, (15,460), (180,500), (255,255,255), -1)
cv.putText(imgReduzida, "[MUDA PARA CINZA]", (19, 485), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))

cv.rectangle(imgReduzida, (200,460), (400,500), (255,255,255), -1)
cv.putText(imgReduzida, "[MUDA PARA COLORIDA]", (206, 485), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0))

# 
########################################################################
# Janelamento e Instancia de Função
########################################################################
#
cv.namedWindow (NomeJanela)
cv.setMouseCallback (NomeJanela, ExecutaTracado)

# 
########################################################################
# Loop de Execução
########################################################################
#
while(1):
    cv.imshow ( NomeJanela, imgReduzida)
    k = cv.waitKey(1) & 0xFF

    if k == 27:
        break

cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
