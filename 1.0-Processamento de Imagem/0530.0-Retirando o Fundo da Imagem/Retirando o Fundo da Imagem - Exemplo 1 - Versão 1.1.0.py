import numpy as np
import cv2
from matplotlib import pyplot as plt
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
NomeImagem  = "Pilulas.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
img = cv2.imread ( dirCaminhoImagem, cv2.IMREAD_COLOR)
if img is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Definindo Limites Superiores e Inferiores
########################################################################
#
hh, ww = img.shape[:2]
lower = np.array([200, 200, 200])
upper = np.array([255, 255, 255])

# 
########################################################################
# Criando a Máscara
########################################################################
#
thresh = cv2.inRange(img, lower, upper)

# 
########################################################################
# Aplicando a Morfologia
########################################################################
#
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20,20))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# 
########################################################################
# Invertendo a Morfologia da Imagem
########################################################################
#
mask = 255 - morph

# 
########################################################################
# Aplicando a Máscara na Imagem
########################################################################
#
result = cv2.bitwise_and(img, img, mask=mask)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2RGB)
morph = cv2.cvtColor(morph, cv2.COLOR_BGR2RGB)
mask  = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure( )

Grafico.add_subplot(1,5,1)
plt.imshow(img )
plt.title("Original")

Grafico.add_subplot(1,5,2)
plt.imshow(thresh )
plt.title("Imagem Limite")

Grafico.add_subplot(1,5,3)
plt.imshow(morph )
plt.title("Imagem Mofológica")

Grafico.add_subplot(1,5,4)
plt.imshow(mask )
plt.title("Imagem Máscara")

Grafico.add_subplot(1,5,5)
plt.imshow(result )
plt.title("Imagem Resultado")

plt.tight_layout ()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
