# Referencia
# https://pyimagesearch.com/2021/01/23/splitting-and-merging-channels-with-opencv/

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
# Definições Gerais
########################################################################
#
NomeImagem  = "Lapis.jpg"
NomeDiagrama = "DiagramaRGB.png"
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
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
Azul, Verde, Vermelho = cv.split(ImagemColorida)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure( )

Grafico.add_subplot(2,3,1)
plt.imshow(ImagemColorida )
plt.title("Original")

Grafico.add_subplot(2,3,2)
plt.imshow(ImgDiagrama )
plt.axis ( "off")
plt.title("Diagrama RGB")

Grafico.add_subplot(2,3,4)
plt.imshow(Azul, cmap="Blues" )
plt.title("Canal Azul")

Grafico.add_subplot(2,3,5)
plt.imshow(Verde, cmap="Greens" )
plt.title("Canal Verde")

Grafico.add_subplot(2,3,6)
plt.imshow(Vermelho, cmap="Reds" )
plt.title("Canal Vermelho")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

