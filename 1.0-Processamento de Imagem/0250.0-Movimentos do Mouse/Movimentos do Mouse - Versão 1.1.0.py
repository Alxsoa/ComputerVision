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
NomeJanela = "Imagem Base"
NomeImagem  = "Girassol.png"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
Desenho = False
ModeExecucao  = True 
ix,iy = -1,-1

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
# Função de Callback para Controle do Mouse
########################################################################
#
def ExecutaTracado(Evento,x,y,flags,param):
    global ix,iy,Desenho,ModeExecucao

    if Evento == cv.EVENT_LBUTTONDOWN:
       Desenho = True
       ix,iy = x,y

    elif Evento == cv.EVENT_MOUSEMOVE:
         if Desenho == True:
            if ModeExecucao == True:
                cv.rectangle(Imagem,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(Imagem,(x,y),5,(0,0,255),-1)

    elif Evento == cv.EVENT_LBUTTONUP:
         Desenho = False
         if ModeExecucao == True:
            cv.rectangle(Imagem,(ix,iy),(x,y),(0,255,0),-1)
         else:
            cv.circle(Imagem,(x,y),5,(0,0,255),-1)

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
# Loop de Execução
########################################################################
#
while(1):
    cv.imshow ( NomeJanela, Imagem)
    k = cv.waitKey(1) & 0xFF

    if k == ord('m'):
        ModeExecucao = not ModeExecucao
    elif k == 27:
        break

cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################

