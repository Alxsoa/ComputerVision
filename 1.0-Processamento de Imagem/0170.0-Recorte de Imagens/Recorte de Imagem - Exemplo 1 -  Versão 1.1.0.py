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
NomeImagem  = "Mesa.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
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
# Reduzindo o Tamanho
########################################################################
#
EscalaPercentual = 10
LarguraAlterada = int(imgBase.shape[1] * EscalaPercentual / 100)
AlturaAlterada  = int(imgBase.shape[0] * EscalaPercentual / 100)
NovoTamanho = (LarguraAlterada, AlturaAlterada)
ImagemReduzida = cv.resize(imgBase, NovoTamanho, interpolation = cv.INTER_AREA)
ImagemOriginal = ImagemReduzida.copy ()

# 
########################################################################
# Desenhando o Retangulo
########################################################################
#
LarguraLinha = 9
CorLinha = (0, 0, 255 )
PontoInicial = (0,175)
PontoFinal = (344, 516 )
NovaImagem = cv.rectangle(ImagemReduzida, PontoInicial, PontoFinal, CorLinha, LarguraLinha)

# 
########################################################################
# Recortando a Imagem
########################################################################
#
RecorteImagem = ImagemReduzida[175:516, 0:344]

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemOriginal = cv.cvtColor(ImagemOriginal, cv.COLOR_BGR2RGB)
NovaImagem = cv.cvtColor(ImagemReduzida, cv.COLOR_BGR2RGB)
RecorteImagem = cv.cvtColor(RecorteImagem, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(1,3,1)
plt.imshow( ImagemOriginal )
plt.title("Imagem\nOriginal")

Grafico.add_subplot(1,3,2)
plt.imshow(NovaImagem )
plt.title("Recorte\nProjetado")

Grafico.add_subplot(1,3,3)
plt.imshow(RecorteImagem )
plt.title("Imagem\nResultado")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
