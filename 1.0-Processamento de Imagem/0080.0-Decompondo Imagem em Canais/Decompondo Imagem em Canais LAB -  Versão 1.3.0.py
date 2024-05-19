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
NomeDiagrama = "DiagramaLAB.jpg"
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
imgLAB = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2LAB)

# 
########################################################################
# Decompondo a Imagem nos Diferentes Canais
########################################################################
#
L, A, B = cv.split(imgLAB)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgL = cv.cvtColor(L, cv.COLOR_BGR2RGB)
imgA = cv.cvtColor(A, cv.COLOR_BGR2RGB)
imgB = cv.cvtColor(B, cv.COLOR_BGR2RGB)

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
plt.title("Diagrama LAB")

Grafico.add_subplot(2,3,4)
plt.imshow(imgL )
plt.title("Canal Lightness")

Grafico.add_subplot(2,3,5)
plt.imshow(imgA )
plt.title("Canal A")

Grafico.add_subplot(2,3,6)
plt.imshow(imgB )
plt.title("Canal B")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

