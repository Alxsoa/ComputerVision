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
NomeDiagrama = "DiagramaHSV.png"
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
imgHSV = cv.cvtColor(imgRGB, cv.COLOR_RGB2HSV)

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
Matiz, Saturacao, Valor = cv.split(imgHSV)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgMatiz = cv.cvtColor(Matiz, cv.COLOR_BGR2RGB)
imgSaturacao = cv.cvtColor(Saturacao, cv.COLOR_BGR2RGB)
imgValor = cv.cvtColor(Valor, cv.COLOR_BGR2RGB)

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
plt.title("Diagrama HSV")

Grafico.add_subplot(2,3,4)
plt.imshow(imgMatiz )
plt.title("Canal Matiz")

Grafico.add_subplot(2,3,5)
plt.imshow(imgSaturacao )
plt.title("Canal Saturacao")

Grafico.add_subplot(2,3,6)
plt.imshow(imgValor )
plt.title("Canal Intensidade")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

