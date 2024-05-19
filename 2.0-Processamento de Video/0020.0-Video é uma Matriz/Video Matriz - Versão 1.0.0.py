# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 
########################################################################
# Construindo a Matriz 
########################################################################
#
CorPreta = (0, 0, 0)
ImagemMatriz = np.full((256, 256, 3), CorPreta, dtype=np.uint8) 

#Matriz = np.zeros([256, 256, 3])
#ImagemMatriz = np.array(Matriz ,dtype=np.uint8)

ImagemMatriz[0:32, :, :3] = (0, 0, 255)     # linha superior
ImagemMatriz[:, :32, :3]  = (0, 0, 255)     # coluna esquerda
ImagemMatriz[:, 224:256, :3] = (0, 0, 255)  # coluna direita
ImagemMatriz[224:, :, :3] = (0, 0, 255)     # linha inferior

ImagemMatriz[32:64, 32:224, :3]   = (0, 128, 255)  # linha superior
ImagemMatriz[64:224, 32:64, :3]   = (0, 128, 255)  # coluna esquerda
ImagemMatriz[64:224, 192:224, :3] = (0, 128, 255)  # Coluna direita
ImagemMatriz[192:224, 32:224, :3] = (0, 128, 255)  # linha inferior

ImagemMatriz[64:96, 64:192, :3]   = (0, 255, 255)  # linha superior
ImagemMatriz[96:192, 64:96, :3]   = (0, 255, 255)  # coluna esquerda
ImagemMatriz[96:192, 160:192, :3] = (0, 255, 255)  # coluna direita
ImagemMatriz[160:192, 64:192, :3] = (0, 255, 255)  # linha inferior

ImagemMatriz[96:160, 96:160, :3]  = (0, 255, 128) 

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemMatriz = cv.cvtColor(ImagemMatriz, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
plt.title( "Imagem como Matriz", fontsize=14, weight='bold' )
plt.imshow(ImagemMatriz)
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
