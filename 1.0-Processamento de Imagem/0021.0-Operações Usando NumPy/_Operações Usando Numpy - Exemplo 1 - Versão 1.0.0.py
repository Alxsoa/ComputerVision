import numpy as np
from skimage import data
import matplotlib.pyplot as plt
import cv2 as cv

# 
########################################################################
# Recupera a Imagem da Base de Dados
########################################################################
#
imgCamera = data.camera()
imgOriginal = imgCamera.copy()

# 
########################################################################
# Preenche de Branco o Que Estiver Fora da Regra
########################################################################
#
Mascara = imgCamera < 87
imgCamera[Mascara] = 255
imgMascara = imgCamera.copy ()

# 
########################################################################
# Inserindo Linhas
########################################################################
#
IndiceX = np.arange(len(imgCamera))
IndiceY = (4 * IndiceX) % len(imgCamera)
imgCamera[IndiceX, IndiceY] = 0
imgLinhas = imgCamera.copy ()

# 
########################################################################
# Desenha o Círculo e Preenche de Preto o Externo
########################################################################
#
TamanhoX = imgCamera.shape[0] 
TamanhoY = imgCamera.shape[1]
X, Y = np.ogrid[:TamanhoX, :TamanhoY]
outer_disk_Mascara = (X - TamanhoX / 2)**2 + (Y - TamanhoY / 2)**2 > (TamanhoX / 2)**2
imgCamera[outer_disk_Mascara] = 0

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgOriginal = cv.cvtColor(imgOriginal, cv.COLOR_BGR2RGB)
imgMascara = cv.cvtColor(imgMascara, cv.COLOR_BGR2RGB)
imgLinhas = cv.cvtColor(imgLinhas, cv.COLOR_BGR2RGB)
imgCamera = cv.cvtColor(imgCamera, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(11,10))

Grafico.add_subplot(2,2,1)
plt.imshow( imgOriginal )
plt.title("Imagem Original", fontweight="bold", fontsize=10) 

Grafico.add_subplot(2,2,2)
plt.imshow(imgMascara )
plt.title("Imagem Baseada na Regra", fontweight="bold", fontsize=10) 

Grafico.add_subplot(2,2,3)
plt.imshow(imgLinhas )
plt.title("Imagem com Linhas", fontweight="bold", fontsize=10) 

Grafico.add_subplot(2,2,4)
plt.imshow(imgCamera )
plt.title("Imagem Resultado", fontweight="bold", fontsize=10) 

plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
