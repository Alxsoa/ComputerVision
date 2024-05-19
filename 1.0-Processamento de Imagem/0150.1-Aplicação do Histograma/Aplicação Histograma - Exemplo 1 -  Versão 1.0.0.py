# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import os
import numpy as np
from pathlib import Path

# 
########################################################################
# Funções de Apoio
########################################################################
#
def HistogramaCurva (tmpImgBase):
    CorBranca = (255, 255, 255)
    imgGrafico = np.full((300, 256, 3), CorBranca, dtype=np.uint8) 
    bins = np.arange(256).reshape(256,1)

    if len(tmpImgBase.shape) == 2:
        CorLinha = [(255,255,255)]
    elif tmpImgBase.shape[2] == 3:
        CorLinha = [ (255,0,0),(0,255,0),(0,0,255) ]
        
    for Canais, ColunaCanal in enumerate(CorLinha):
        ItemHistograma = cv.calcHist([tmpImgBase],[Canais],None,[256],[0,256])
        cv.normalize(ItemHistograma,ItemHistograma,0,255,cv.NORM_MINMAX)
        Historico = np.int32(np.around(ItemHistograma))
        Pontos = np.int32(np.column_stack((bins,Historico)))
        cv.polylines(imgGrafico,[Pontos],False,ColunaCanal)

    imgResultado = np.flipud(imgGrafico)
    return (imgResultado)

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
NomeImagem = "Montanha.png"
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
# Convertendo para o Padrão HSV
########################################################################
#
imgHSVBase = cv.cvtColor(imgBase,cv.COLOR_BGR2HSV)
imgHSVCorrigida = imgHSVBase.copy ()

# 
########################################################################
# Executando o Histograma
########################################################################
#
imgCurvaBase = HistogramaCurva (imgBase)

# 
########################################################################
# Equalizando a Imagem e Calculando o Novo Histograma
########################################################################
#
imgHSVCorrigida [:,:,2]=cv.equalizeHist(imgHSVBase[:,:,2])
imgCurvaCorrigida = HistogramaCurva (imgHSVCorrigida)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgHSVBase = cv.cvtColor(imgHSVBase, cv.COLOR_HSV2RGB)
imgCurvaBase = cv.cvtColor(imgCurvaBase, cv.COLOR_BGR2RGB)
imgHSVCorrigida = cv.cvtColor(imgHSVCorrigida, cv.COLOR_HSV2RGB)
imgCurvaCorrigida = cv.cvtColor(imgCurvaCorrigida, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,2,1)
plt.imshow(imgHSVBase )
plt.title("Imagem Original", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,2)
plt.imshow(imgCurvaBase )
plt.title("Histograma Base", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,3)
plt.imshow(imgHSVCorrigida )
plt.title("Imagem Corrigida", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,4)
plt.imshow(imgCurvaCorrigida )
plt.title("Histograma Corrigido", fontsize=11, weight='bold' )

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

