# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
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
NomeImagem  = "Pessoa.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
if Imagem is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Reduzindo o Tamanho da Imagem
########################################################################
#
imgReduzida = cv.resize(Imagem, (0,0), fx=0.1, fy=0.1, interpolation = cv.INTER_AREA)
Altura, Largura, Canais = imgReduzida.shape
iAux = 0
  
while True:
    iAux += 1

# 
########################################################################
# Dividimos a imagem em partes esquerda e direita    
########################################################################
#      
    MatrizEsquerda = imgReduzida[:, :(iAux % Largura)]
    MatrizDireita  = imgReduzida[:, (iAux % Largura):]

# 
########################################################################
# Concatenação da Matriz Direita e Esquerda       
########################################################################
#    
    imgResultado = np.hstack((MatrizDireita, MatrizEsquerda))
      
# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
    cv.imshow ( "JanelaBase", imgResultado)
    if cv.waitKey(1) == ord('q'):
       cv.destroyAllWindows()
       break

########################################################################
# FIM DO PROGRAMA
########################################################################
