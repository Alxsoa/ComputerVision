# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
import numpy as np
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
NomeImagem  = "PessoaPulando.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

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
# Reduzindo a Imagem
########################################################################
#
imgReduzida = cv.resize(imgBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)

# 
########################################################################
# Criando o Kernel
########################################################################
#
TamanhoKernel = 30
KernelVertical = np.zeros((TamanhoKernel, TamanhoKernel))

# 
########################################################################
# Fill the middle row with ones.
########################################################################
#  
KernelVertical[:, int((TamanhoKernel - 1)/2)] = np.ones(TamanhoKernel)

# 
########################################################################
# Normalizando
########################################################################
#    
KernelVertical = KernelVertical / TamanhoKernel
  
# 
########################################################################
# Aplicando o Kernel
########################################################################
#  
imgResultado = cv.filter2D(imgReduzida, -1, KernelVertical)

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
