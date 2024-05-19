# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
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
NomeImagem = "Baloes.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
bins = np.arange(256).reshape(256,1)

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemBase = cv.imread ( dirCaminhoImagem)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Reduzindo a Imagem Base
########################################################################
#
imgReduzida = cv.resize ( ImagemBase, 
                          (0,0), 
                          fx=0.3, 
                          fy=0.3, 
                          interpolation = cv.INTER_AREA )
imgHistogramaOriginal = HistogramaCurva (imgReduzida)

# 
########################################################################
# Recuperando os Dados da Imagem
########################################################################
#
ImagemAltura = imgReduzida.shape[0]
ImagemLargura  = imgReduzida.shape[1]
ImagemNumCanais = imgReduzida.shape[2]

# 
########################################################################
# Executando o Histograma
########################################################################
#
imgNormal = np.zeros ((ImagemLargura, ImagemAltura))
imgNormalizada = cv.normalize ( imgReduzida, 
                                imgNormal, 
                                alpha = 0,
                                beta = 255,
                                norm_type = cv.NORM_MINMAX )
imgHistogramaNormalizado = HistogramaCurva (imgNormalizada)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
imgHistogramaOriginal = cv.cvtColor(imgHistogramaOriginal, cv.COLOR_BGR2RGB)
imgNormalizada = cv.cvtColor(imgNormalizada, cv.COLOR_BGR2RGB)
imgHistogramaNormalizado = cv.cvtColor(imgHistogramaNormalizado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,2,1)
plt.imshow(imgReduzida )
plt.title("Imagem Original", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,2)
plt.imshow(imgHistogramaOriginal )
plt.title("Histograma Original", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,3)
plt.imshow(imgNormalizada )
plt.title("Imagem Normalizada", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,4)
plt.imshow(imgHistogramaNormalizado )
plt.title("Histograma Normalizdo", fontsize=11, weight='bold' )

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
