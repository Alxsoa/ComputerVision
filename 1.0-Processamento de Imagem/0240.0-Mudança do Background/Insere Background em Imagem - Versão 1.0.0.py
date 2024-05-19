# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import mediapipe as mp
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
NomeImagemFront = "Mulher.jpg"
NomeImagemBackground = "Cena.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoFront = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemFront))
dirCaminhoBackground = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemBackground))

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgFrente = cv.imread ( dirCaminhoFront, cv.IMREAD_COLOR)
if imgFrente is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagemFront)
    exit ()

imgFundo = cv.imread ( dirCaminhoBackground, cv.IMREAD_COLOR)
if imgFundo is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagemBackground)
    exit ()

# 
########################################################################
# Compatibilizando o Tamanho das Imagens
########################################################################
#
imgFrente = cv.resize(imgFrente, (640, 480))
imgFundo  = cv.resize(imgFundo, (640, 480))

# 
########################################################################
# Apresentando o Resultado Parcial
########################################################################
#
cv.imshow ( "Imagem Frente", imgFrente)
cv.imshow ( "Imagem Fundo", imgFundo)

# 
########################################################################
# Segmentando a Imagem
########################################################################
#
imgSegmentada = mp.solutions.selfie_segmentation
imgSegmento = imgSegmentada.SelfieSegmentation(model_selection = 1)

# 
########################################################################
# Criando a Máscara
########################################################################
#
imgFrente = cv.cvtColor(imgFrente, cv.COLOR_BGR2RGB)
imgResultado = imgSegmento.process(imgFrente)
imgFrente = cv.cvtColor(imgFrente, cv.COLOR_RGB2BGR)
imgSegmentoMascara = imgResultado.segmentation_mask

# 
########################################################################
# Executando a União das Imagens
########################################################################
#
Limiar = 0.6
imgMascaraBinaria = imgSegmentoMascara > Limiar
imgMascara3d = np.dstack((imgMascaraBinaria, imgMascaraBinaria, imgMascaraBinaria))
imgResultadoFinal = np.where(imgMascara3d, imgFrente, imgFundo)

# 
########################################################################
# Apresentando o Resultado Final
########################################################################
#
cv.imshow ( "Resultado Final", imgResultadoFinal)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
