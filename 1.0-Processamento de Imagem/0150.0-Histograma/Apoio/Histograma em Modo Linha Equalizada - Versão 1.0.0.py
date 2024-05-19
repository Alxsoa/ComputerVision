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
def HistogramaLinha(imgBase):
    CorBranca = (255, 255, 255)
    imgGrafico = np.full((300, 256, 3), CorBranca, dtype=np.uint8) 

    ItemHistograma = cv.calcHist([imgBase],[0],None,[256],[0,256])
    cv.normalize(ItemHistograma,ItemHistograma,0,255,cv.NORM_MINMAX)
    Historico = np.int32(np.around(ItemHistograma))
    for xPts,yPts in enumerate(Historico):
        cv.line(imgGrafico,(xPts,0),(xPts,yPts[0]),(0,0,0))

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
ImagemBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_GRAYSCALE)
imgReduzida = cv.resize(ImagemBase, (0,0), fx=0.3, fy=0.3, interpolation = cv.INTER_AREA)

# 
########################################################################
# Executando o Histograma
########################################################################
#
Equalizada = cv.equalizeHist(imgReduzida)
imgCurva = HistogramaLinha (Equalizada)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)

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
