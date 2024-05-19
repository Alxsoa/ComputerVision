# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
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
NomeImagem  = "CarroFord.jpg"
NomeTemplate = "LogoFord.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoTemplate = str(Path(dirRaiz, dirBase, dirImagem, NomeTemplate))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem ) 
if imgBase is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

imgTemplate = cv.imread ( dirCaminhoTemplate, 0)
if imgBase is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeTemplate)
    exit ()

# 
########################################################################
# Convertendo para Cinza (Requerimento)
########################################################################
#
imgCinza = cv.cvtColor(imgBase, cv.COLOR_BGR2GRAY)
Largura, Altura = imgTemplate.shape[::-1]

# 
########################################################################
# Aplicando o Template e Recuperando os Maximos e Minimos da Imagem
########################################################################
#
imgResultado = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(imgResultado)

# 
########################################################################
# Acrescentando Outros Modificadores
########################################################################
#
imgCCOEFF = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_CCOEFF)
imgCCORR = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_CCORR )
imgCCORR_NORMED = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_CCORR_NORMED)
imgSQDIFF = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_SQDIFF)
imgSQDIFFNORMED = cv.matchTemplate(imgCinza, imgTemplate, cv.TM_SQDIFF_NORMED)

# 
########################################################################
# Recuperando as Coordenadas (Esquerda Superior e Direita Inferior)
########################################################################
#
xEsquerdaSuperior, yEsquerdaSuperior = max_loc
xDireitaInferior, yDireitaInferior = (xEsquerdaSuperior + Largura, yEsquerdaSuperior+ Altura)

# 
########################################################################
# Desenhando a Identificação do Logo na Imagem
########################################################################
#
cv.rectangle ( imgBase, 
                (xEsquerdaSuperior, yEsquerdaSuperior), 
                (xDireitaInferior, yDireitaInferior ), 
                (0, 0, 255), 
                2 )

# 
########################################################################
# Normalizando e Apresentando a Imagem
########################################################################
#
cv.normalize(imgResultado, imgResultado, 0, 1, cv.NORM_MINMAX, -1 )

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure( )

Grafico.add_subplot(3,3,1)
plt.imshow(imgBase)
plt.title("Imagem Identificada", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,2)
plt.imshow(imgResultado, cmap="gray")
plt.title("TM_CCOEFF_NORMED", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,3)
plt.imshow(imgCCOEFF, cmap="gray")
plt.title("TM_CCOEFF", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,4)
plt.imshow(imgCCORR, cmap="gray")
plt.title("TM_CCORR", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,5)
plt.imshow(imgCCORR_NORMED, cmap="gray")
plt.title("TM_CCORR_NORMED", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,6)
plt.imshow(imgSQDIFF, cmap="gray")
plt.title("TM_SQDIFF", fontsize=11, weight='bold' )

Grafico.add_subplot(3,3,7)
plt.imshow(imgSQDIFFNORMED, cmap="gray")
plt.title("TM_SQDIFFNORMED", fontsize=11, weight='bold' )

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
