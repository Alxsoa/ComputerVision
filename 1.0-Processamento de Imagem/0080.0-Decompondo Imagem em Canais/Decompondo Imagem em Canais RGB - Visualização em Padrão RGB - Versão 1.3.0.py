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
zeros = np.zeros(ImagemColorida.shape[:2], dtype="uint8")
Vermelho = cv.merge([zeros, zeros, Vermelho])
Verde = cv.merge([zeros, Verde, zeros])
Azul = cv.merge([Azul, zeros, zeros])

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgAzul = cv.cvtColor(Azul, cv.COLOR_BGR2RGB)
imgVerde = cv.cvtColor(Verde, cv.COLOR_BGR2RGB)
imgVermelho = cv.cvtColor(Vermelho, cv.COLOR_BGR2RGB)

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
plt.title("Diagrama RGB")

Grafico.add_subplot(2,3,4)
plt.imshow(imgAzul )
plt.title("Canal Azul")

Grafico.add_subplot(2,3,5)
plt.imshow(imgVerde )
plt.title("Canal Verde")

Grafico.add_subplot(2,3,6)
plt.imshow(imgVermelho )
plt.title("Canal Vermelho")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

