# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
import matplotlib.pyplot as plt
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
NomeImagem = "Adicao.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_GRAYSCALE)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Recuperando as Dimensões da Imagem
########################################################################
#
iLinhas = imgBase.shape[0]
iColunas = imgBase.shape[1]

# 
########################################################################
# Apresentando a Matriz
########################################################################
#
fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.imshow(imgBase, cmap="Oranges" )
for i in range(imgBase.shape[0]):
    for j in range(imgBase.shape[1]):
        ax.text(j, i, str(imgBase[i, j]).zfill(3), ha="center", va="center" )
ax.set_axis_off()

fig.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################
