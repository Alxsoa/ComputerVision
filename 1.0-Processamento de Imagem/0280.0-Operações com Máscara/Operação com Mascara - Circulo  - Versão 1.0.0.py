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
NomeImagem  = "Mulher.jpg"
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
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if Imagem is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()


# 
########################################################################
# Reduzindo a Imagem
########################################################################
#
imgReduzida = cv.resize(Imagem, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)

# 
########################################################################
# Construindo a Matriz 
########################################################################
#
Largura = imgReduzida.shape[0]
Altura  = imgReduzida.shape[1]
imgRecorte = np.zeros( (Largura, Altura), dtype="uint8")
imgAuxiliar = imgRecorte.copy()

# 
########################################################################
# Criando a Máscara
########################################################################
#
Mascara = cv.circle(imgRecorte, (300, 160), 150, 255, -1)

# 
########################################################################
# Aplicando a Máscara
########################################################################
#
imgResultado = cv.bitwise_and (imgReduzida, imgReduzida, mask= Mascara)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgReduzida = cv.cvtColor(imgReduzida, cv.COLOR_BGR2RGB)
imgAuxiliar = cv.cvtColor(imgAuxiliar, cv.COLOR_BGR2RGB)
Mascara = cv.cvtColor(Mascara, cv.COLOR_BGR2RGB)
imgResultado = cv.cvtColor(imgResultado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,2,1)
plt.imshow(imgReduzida )
plt.title("Imagem Original", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,2)
plt.imshow(imgAuxiliar )
plt.title("Imagem Recorte", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,3)
plt.imshow(Mascara )
plt.title("Imagem Máscara", fontsize=11, weight='bold' )

Grafico.add_subplot(2,2,4)
plt.imshow(imgResultado )
plt.title("Imagem Resultado", fontsize=11, weight='bold' )

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
