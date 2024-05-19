import cv2 as cv
import time
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
Codec = cv.VideoWriter_fourcc('m','p','4','v')
NomeImagemGato1  = "FotoGato2.jpg"
NomeImagemGato2  = "FotoGato3.jpg"
VideoOutName = "EfeitoFadeInFadeOut.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens" 
dirVideo = "Videos"  
dirCaminhoImagemGato1 = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemGato1))
dirCaminhoImagemGato2 = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemGato2))
dirVideoOut = str(Path(dirRaiz, dirBase, dirVideo, VideoOutName))
TempoTransicao = 1
PesoImagemGato1 = 0
DirecaoFade = False 
FPS = 25

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
imgGato1 = cv.imread ( dirCaminhoImagemGato1, cv.IMREAD_COLOR)
if imgGato1 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagemGato1)
   exit ()

imgGato2 = cv.imread ( dirCaminhoImagemGato2, cv.IMREAD_COLOR)
if imgGato2 is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagemGato2)
   exit ()

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
VideoOut = cv.VideoWriter ( dirVideoOut, 
                            Codec,                            
                            FPS, 
                            (600, 400))   

# 
########################################################################
# Padronizando o Tamanho das Imagens
########################################################################
#
imgGato1 = cv.resize(imgGato1, (600, 400))   
imgGato2 = cv.resize(imgGato2, (600, 400))   
 
PesoImagemGato1 = 0
DirecaoFade = False 

lstFrameVideo = [] 
while (True):
     
    if DirecaoFade:
        PesoImagemGato1 -= 0.1
    else:
        PesoImagemGato1 += 0.1
         
    PesoImagemGato2 = 1 - PesoImagemGato1       
    imgResultado = cv.addWeighted(imgGato1, PesoImagemGato1 , imgGato2, PesoImagemGato2 , 0)
     
    time.sleep(TempoTransicao)     
    cv.imshow ( "Efeito Fade In Fade Out", imgResultado)

    #VideoFrameOUT = cv.resize(imgResultado, (600, 400))  
    lstFrameVideo.append(imgResultado)
         
    if PesoImagemGato1 > 1: 
       time.sleep(1)     
       DirecaoFade =True
    elif PesoImagemGato1 < 0:          
        time.sleep(1)
        DirecaoFade =False
    
    if cv.waitKey(1)  & 0xFF == ord('q'):  
          break

# 
########################################################################
# Fechando o Janelamento
########################################################################
#              
#cv.destroyAllWindows()

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
for iAux in range (0, len(lstFrameVideo)):
    VideoOut.write(lstFrameVideo[iAux])  

# 
########################################################################
# Fechando o Arquivo de Vídeo e Desmontando o Janelamento
########################################################################
# 
VideoOut.release()
cv.destroyAllWindows()

exit ()

########################################################################
# FIM DO PROGRAMA
########################################################################





# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
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
NomeImagem  = "Mesa.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if Imagem is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Construindo a Matriz (Kernel)
########################################################################
#
imgReduzida = cv.resize(Imagem, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)
matKernel = np.array([
                        [0, 0, 0],
                        [0, 1, 0],
                        [0, 0, 0]
                     ]) 

########################################################################
# Aplicando o Filtro (Sobel)
########################################################################
#
imgResultado = cv.filter2D(imgReduzida, -1, matKernel)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
imgResultado = cv.cvtColor(imgResultado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#

Grafico = plt.figure()

Grafico.add_subplot(1,2,1)
plt.imshow ( imgReduzida )
plt.title ( "Imagem Original", fontsize=11, weight="bold" )

Grafico.add_subplot(1,2,2)
plt.imshow ( imgResultado )
plt.title ( "Imagem Filtrada", fontsize=11, weight="bold" )

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
