
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from skimage.morphology import (square, rectangle, diamond, disk, cube,
                                octahedron, ball, octagon, star)

# Generate 2D and 3D structuring elements.
struc_2d = {
    #"square(15)": square(15),
    #"rectangle(15, 10)": rectangle(15, 10),
    "diamond(7)": diamond(7) #,
    #"disk(7)": disk(7),
    #"octagon(7, 4)": octagon(7, 4),
    #"star(5)": star(5)
}

#struc_3d = {
#    "cube(11)": cube(11),
#    "octahedron(5)": octahedron(5),
#    "ball(5)": ball(5)
#}

# Visualize the elements.
fig = plt.figure(figsize=(8, 8))

idx = 1
for title, struc in struc_2d.items():
    print ( struc )
    ax = fig.add_subplot(3, 3, idx)
    ax.imshow(struc, cmap="Paired", vmin=0, vmax=12)
    for i in range(struc.shape[0]):
        for j in range(struc.shape[1]):
            ax.text(j, i, struc[i, j], ha="center", va="center", color="w")
    ax.set_axis_off()
    ax.set_title(title)
    idx += 1

#for title, struc in struc_3d.items():
#    ax = fig.add_subplot(3, 3, idx, projection=Axes3D.name)
#    ax.voxels(struc)
#    ax.set_title(title)
#    idx += 1

fig.tight_layout()
plt.show()



exit ()
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
