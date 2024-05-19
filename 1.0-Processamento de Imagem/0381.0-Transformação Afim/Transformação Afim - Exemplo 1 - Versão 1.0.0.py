# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
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
NomeImagem = "Caravela.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem )

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
# Definindo os Pontos Origem e Destino
########################################################################
#
ptsOrigem = np.array (  [
                        [0, 0], 
                        [imgBase.shape[1] - 1, 0], 
                        [0, imgBase.shape[0] - 1]
                        ]).astype(np.float32)

ptsDestino = np.array ( [
                        [0, imgBase.shape[1]*0.33], 
                        [imgBase.shape[1]*0.85, imgBase.shape[0]*0.25], 
                        [imgBase.shape[1]*0.15, imgBase.shape[0]*0.7]
                        ]).astype(np.float32)

# 
########################################################################
# Executando a Transformação
########################################################################
#
MatrizTransformacao = cv.getAffineTransform(ptsOrigem, ptsDestino)
TransformacaoDestino = cv.warpAffine  ( 
                                        imgBase, 
                                        MatrizTransformacao, 
                                        (imgBase.shape[1], imgBase.shape[0])
                                      )

# 
########################################################################
# Executando a Rotação
########################################################################
#
Centro = (
          TransformacaoDestino.shape[1]//2, 
          TransformacaoDestino.shape[0]//2
         )

Angulo = -50
Escala = 0.6
MatrizRotacao = cv.getRotationMatrix2D( Centro, Angulo, Escala )
DestinoRotacionado = cv.warpAffine (
                                      TransformacaoDestino, 
                                      MatrizRotacao, 
                                      (
                                          TransformacaoDestino.shape[1], 
                                          TransformacaoDestino.shape[0]
                                      )
                                    )

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)
TransformacaoDestino = cv.cvtColor(TransformacaoDestino, cv.COLOR_BGR2RGB)
DestinoRotacionado = cv.cvtColor(DestinoRotacionado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure ()
Grafico.add_subplot (1,3,1)
plt.imshow ( imgBase )
plt.title ("Imagem Original")

Grafico.add_subplot (1,3,2)
plt.imshow ( TransformacaoDestino )
plt.title ("Imagem Transformada")

Grafico.add_subplot (1,3,3)
plt.imshow ( DestinoRotacionado )
plt.title ("Imagem Rotacionada")
Grafico.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
