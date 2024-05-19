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
imgRetangulo = np.full((300, 300, 3), CorPreta, dtype=np.uint8) 
imgCirculo = np.full((300, 300, 3 ), CorPreta, dtype=np.uint8) 

# 
########################################################################
# Desenhando as Figuras nas Imagens
########################################################################
#
imgRetangulo = cv.rectangle (imgRetangulo, (25, 25), (275, 275), (255,255,255), -1)
imgCirculo = cv.circle (imgCirculo, (150, 150), 150, (255,255,255), -1)

# 
########################################################################
# Executando a Operação AND Entre as Imagens
########################################################################
#
bitwiseAnd = cv.bitwise_and(imgRetangulo, imgCirculo)

# 
########################################################################
# Executando a Operação OR Entre as Imagens
########################################################################
#
bitwiseOr = cv.bitwise_or(imgRetangulo, imgCirculo)

# 
########################################################################
# Executando a Operação XOR Entre as Imagens
########################################################################
#
bitwiseXor = cv.bitwise_xor(imgRetangulo, imgCirculo)

# 
########################################################################
# Executando a Operação NOT na Imagem Círculo
########################################################################
#
bitwiseNotCirculo = cv.bitwise_not (imgCirculo)

# 
########################################################################
# Executando a Operação NOT na Imagem Retangulo
########################################################################
#
bitwiseNotRetangulo = cv.bitwise_not (imgRetangulo)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(3,3,1)
plt.imshow(imgRetangulo )
plt.title("Retangulo")

Grafico.add_subplot(3,3,2)
plt.imshow(imgCirculo )
plt.title("Circulo")

Grafico.add_subplot(3,3,4)
plt.imshow(bitwiseAnd )
plt.title("Bitwise AND")

Grafico.add_subplot(3,3,5)
plt.imshow(bitwiseOr )
plt.title("Bitwise OR")

Grafico.add_subplot(3,3,6)
plt.imshow(bitwiseXor )
plt.title("Bitwise XOR")

Grafico.add_subplot(3,3,7)
plt.imshow(bitwiseNotCirculo )
plt.title("Bitwise NOT Circulo")

Grafico.add_subplot(3,3,8)
plt.imshow(bitwiseNotRetangulo )
plt.title("Bitwise NOT Retangulo")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################