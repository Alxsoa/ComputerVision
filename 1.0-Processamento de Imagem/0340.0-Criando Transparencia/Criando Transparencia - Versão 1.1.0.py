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
NomeImagemIN  = "SolFundoBranco.jpg"
NomeImagemOUT  = "SolFundoTransparente.png"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagemIN = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemIN))
dirCaminhoImagemOUT = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemOUT))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
ImagemBase = cv.imread(dirCaminhoImagemIN, 1)
if ImagemBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagemIN)
   exit ()

# 
########################################################################
# Transformando Branco por Preto
########################################################################
#
ImagemBase[np.where((ImagemBase==[255,255,255]).all(axis=2))] = [0,0,0]


# 
########################################################################
# Converte a Imagem para Cinza
########################################################################
#
tmp = cv.cvtColor(ImagemBase, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Aplica a Técnica de Threshold 
########################################################################
#
_, alpha = cv.threshold(tmp, 0, 255, cv.THRESH_BINARY)

# 
########################################################################
# Decompõe em Canais a Imagem
########################################################################
#
b, g, r = cv.split(ImagemBase)

# 
########################################################################
# Compõe a Imagem RGB Inserindo a Transparencia (alpha)
########################################################################
#
rgba = [b, g, r, alpha]

# 
########################################################################
# Reúne Todos os Canais
########################################################################
#
dst = cv.merge(rgba, 4)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imwrite ( dirCaminhoImagemOUT, dst )

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
#dst = cv.cvtColor(dst, cv.COLOR_BGR2RGB)
Grafico = plt.figure()
Grafico.add_subplot(1,1,1)
plt.imshow(dst)
plt.tight_layout()
plt.show()

########################################################################
# FIM DO PROGRAMA
########################################################################