# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
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
NomeImagem  = "Mesa.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Construindo a Matriz (Kernel)
########################################################################
#
imgReduzida = cv.resize(Imagem, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)
matKernel = np.array ([
                        [ 0, -1,  0],
                        [-1,  5, -1],
                        [ 0, -1,  0]
                      ])
# 
########################################################################
# Aplicando o Filtro (Aumentando a nitidez de uma imagem)
########################################################################
#
imgResultado = cv.filter2D(imgReduzida, -1, matKernel)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
imgResultado = cv.cvtColor(imgResultado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(1,2,1)
plt.imshow ( imgReduzida )
plt.title ( "Imagem Original", fontsize=11, weight="bold" )

Grafico.add_subplot(1,2,2)
plt.imshow ( imgResultado )
plt.title ( "Imagem Filtrada", fontsize=11, weight="bold" )

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
