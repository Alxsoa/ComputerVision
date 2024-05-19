# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# 
########################################################################
# Construindo a Matriz 
########################################################################
#
Matriz = np.zeros([256, 256])
MatrizBase = Matriz.copy ()

Matriz[0:32, :] = 40 # linha superior
MatrizLinhaSuperior1 = Matriz.copy()

Matriz[:, :32] = 40 # coluna esquerda
MatrizColunaEsquerda1 = Matriz.copy()

Matriz[:, 224:256] = 40 # coluna direita
MatrizColunaDireita1 = Matriz.copy()

Matriz[224:, :] = 40 # linha inferior
MatrizLinhaInferior1 = Matriz.copy()

Matriz[32:64, 32:224] = 80 # linha superior
MatrizLinhaSuperior2 = Matriz.copy()

Matriz[64:224, 32:64] = 80 # coluna esquerda
MatrizColunaEsquerda2 = Matriz.copy()

Matriz[64:224, 192:224] = 80 # Coluna direita
MatrizColunaDireita2 = Matriz.copy()

Matriz[192:224, 32:224] = 80 # linha inferior
MatrizLinhaInferior2 = Matriz.copy()

Matriz[64:96, 64:192]   = 160 # linha superior
MatrizLinhaSuperior3 = Matriz.copy()

Matriz[96:192, 64:96]   = 160 # coluna esquerda
MatrizColunaEsquerda3 = Matriz.copy()

Matriz[96:192, 160:192] = 160 # coluna direita
MatrizColunaDireita3 = Matriz.copy()

Matriz[160:192, 64:192] = 160 # linha inferior
MatrizLinhaInferior3 = Matriz.copy()

Matriz[96:160, 96:160]  = 220
MatrizCentro = Matriz.copy()

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(1,4,1)
plt.imshow(MatrizLinhaSuperior1)
plt.title ("Linha Superior\nMatriz[0:32, :]")

Grafico.add_subplot(1,4,2)
plt.imshow(MatrizColunaEsquerda1)
plt.title ("Coluna Esquerda\nMatriz[:, :32]")

Grafico.add_subplot(1,4,3)
plt.imshow(MatrizColunaDireita1)
plt.title ("Coluna Direita\nMatriz[:, 224:256]")

Grafico.add_subplot(1,4,4)
plt.imshow(MatrizLinhaInferior1)
plt.title ("Linha Inferior\nMatriz[224:, :]")
plt.tight_layout()
plt.show ()

Grafico = plt.figure()
Grafico.add_subplot(1,4,1)
plt.imshow(MatrizLinhaSuperior2)
plt.title ("Linha Superior\nMatriz[32:64, 32:224]")

Grafico.add_subplot(1,4,2)
plt.imshow(MatrizColunaEsquerda2)
plt.title ("Coluna Esquerda\nMatriz[64:224, 32:64]")

Grafico.add_subplot(1,4,3)
plt.imshow(MatrizColunaDireita2)
plt.title ("Coluna Direita\nMatriz[64:224, 192:224]")

Grafico.add_subplot(1,4,4)
plt.imshow(MatrizLinhaInferior2)
plt.title ("Linha Inferior\nMatriz[192:224, 32:224]")
plt.tight_layout()
plt.show ()

Grafico = plt.figure( )

Grafico.add_subplot(1,4,1)
plt.imshow(MatrizLinhaSuperior3)
plt.title ("Linha Superior\nMatriz[32:64, 32:224]")

Grafico.add_subplot(1,4,2)
plt.imshow(MatrizColunaEsquerda3)
plt.title ("Coluna Esquerda\nMatriz[64:224, 32:64]")

Grafico.add_subplot(1,4,3)
plt.imshow(MatrizColunaDireita3)
plt.title ("Coluna Direita\nMatriz[64:224, 192:224]")

Grafico.add_subplot(1,4,4)
plt.imshow(MatrizLinhaInferior3)
plt.title ("Linha Inferior\nMatriz[192:224, 32:224]")
plt.tight_layout()
plt.show ()

Grafico = plt.figure( )
Grafico.add_subplot(1,4,1)
plt.imshow(MatrizCentro)
plt.title ("Linha Superior\nMatriz[96:160, 96:160]")
plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
