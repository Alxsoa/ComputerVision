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
# Definições Gerais
########################################################################
#
NomeImagem  = "Lapis.jpg"
NomeDiagrama = "DiagramaYCbCr.png"
dirRaiz = Path.home()
dirBase = "Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoDiagrama = str(Path(dirRaiz, dirBase, dirImagem, NomeDiagrama))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
ImagemColorida = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
ImgDiagrama = cv.imread ( dirCaminhoDiagrama, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemColorida is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

if ImgDiagrama is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeDiagrama)
    exit ()

# 
########################################################################
# Transformando para o Padrào HSV
########################################################################
#
imgRGB = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgYCrCb = cv.cvtColor(imgRGB, cv.COLOR_RGB2YCrCb)

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
Y, Cr, Cb = cv.split(imgYCrCb)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgY = cv.cvtColor(Y, cv.COLOR_BGR2RGB)
imgCr = cv.cvtColor(Cr, cv.COLOR_BGR2RGB)
imgCb = cv.cvtColor(Cb, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,3,1)
plt.imshow(ImagemColorida )
plt.title("Original")

Grafico.add_subplot(2,3,2)
plt.imshow(ImgDiagrama )
plt.axis ( "off")
plt.title("Diagrama YCrCb")

Grafico.add_subplot(2,3,4)
plt.imshow(imgY )
plt.title("Canal Y")

Grafico.add_subplot(2,3,5)
plt.imshow(imgCr )
plt.title("Canal Cr")

Grafico.add_subplot(2,3,6)
plt.imshow(imgCb )
plt.title("Canal Cb")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

