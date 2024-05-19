# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# 
########################################################################
# Funções de Uso Geral
########################################################################
#
def HistogramaCurva (imgBase):
    CorBranca = (255, 255, 255)
    imgGrafico = np.full((300, 256, 3), CorBranca, dtype=np.uint8) 

    if len(imgBase.shape) == 2:
        CorLinha = [(255,255,255)]
    elif imgBase.shape[2] == 3:
        CorLinha = [ (255,0,0),(0,255,0),(0,0,255) ]
        
    for Canais, ColunaCanal in enumerate(CorLinha):
        ItemHistograma = cv.calcHist([imgBase],[Canais],None,[256],[0,256])
        cv.normalize(ItemHistograma,ItemHistograma,0,255,cv.NORM_MINMAX)
        Historico = np.int32(np.around(ItemHistograma))
        Pontos = np.int32(np.column_stack((bins,Historico)))
        cv.polylines(imgGrafico,[Pontos],False,ColunaCanal)

    imgResultado = np.flipud(imgGrafico)
    return (imgResultado)

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Imagem Base"
NomeImagem  = "Baloes.jpg"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 
bins = np.arange(256).reshape(256,1)

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( CaminhoImagem + NomeImagem )
imgReduzida = cv.resize(ImagemBase, (0,0), fx=0.3, fy=0.3, interpolation = cv.INTER_AREA)

# 
########################################################################
# Executando o Histograma
########################################################################
#
imgCurva = HistogramaCurva (imgReduzida)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
imgCurva = cv.cvtColor(imgCurva, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(10,6))

Grafico.add_subplot(1,2,1)
plt.imshow(imgReduzida )
plt.title("Imagem Original", fontsize=11, weight='bold' )

Grafico.add_subplot(1,2,2)
plt.imshow(imgCurva )
plt.title("Histograma", fontsize=11, weight='bold' )

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.3,
                      hspace = 0.3 )
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
