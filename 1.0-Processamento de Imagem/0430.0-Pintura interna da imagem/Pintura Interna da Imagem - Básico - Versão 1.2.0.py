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
ImagemMascara = "PikachuMascara.png"
ImagemRiscada = "PikachuRiscado.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagemMascara = str(Path(dirRaiz, dirBase, dirImagem, ImagemMascara))
dirCaminhoImagemRiscada = str(Path(dirRaiz, dirBase, dirImagem, ImagemRiscada))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgMascara = cv.imread ( dirCaminhoImagemMascara, cv.IMREAD_GRAYSCALE)
imgRiscada = cv.imread ( dirCaminhoImagemRiscada, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgMascara is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", ImagemMascara)
    exit ()

if imgRiscada is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", ImagemRiscada)
    exit ()

# 
########################################################################
# Aplicando a Técnica Inpaint (Preenchimento por semelhança dos vizinhos)
########################################################################
#
imgRestaurada = cv.inpaint(imgRiscada, imgMascara, 3, cv.INPAINT_TELEA)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgRiscada = cv.cvtColor(imgRiscada, cv.COLOR_BGR2RGB)
imgMascara = cv.cvtColor(imgMascara, cv.COLOR_BGR2RGB)
imgRestaurada = cv.cvtColor(imgRestaurada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure( )

Grafico.add_subplot(1,3,1)
plt.imshow(imgRiscada )
plt.title("Original")

Grafico.add_subplot(1,3,2)
plt.imshow(imgMascara )
plt.title("Máscara")

Grafico.add_subplot(1,3,3)
plt.imshow(imgRestaurada )
plt.title("Imagem\nRestaurada")

plt.tight_layout ()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
