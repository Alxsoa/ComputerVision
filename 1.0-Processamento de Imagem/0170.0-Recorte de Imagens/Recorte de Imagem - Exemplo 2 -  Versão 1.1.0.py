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
# Funções de Apoio
########################################################################
#
def AproximaImagem ( imgTmpImagem, iFator ):
    return (cv.resize(imgTmpImagem, None, fx=iFator, fy=iFator))

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
LarguraLinha = 3
CorLinha = (0, 0, 255 )
PontoInicial = (160, 230)
PontoFinal = (257, 332)
NovaImagem = cv.rectangle(ImagemReduzida, PontoInicial, PontoFinal, CorLinha, LarguraLinha)

# 
########################################################################
# Recortando a Imagem
########################################################################
#
RecorteImagem = NovaImagem[230:332, 160:257]

# 
########################################################################
# Aumentando a Imagem
########################################################################
#
imgAumentada = AproximaImagem (RecorteImagem, 3)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemOriginal = cv.cvtColor(ImagemOriginal, cv.COLOR_BGR2RGB)
NovaImagem = cv.cvtColor(ImagemReduzida, cv.COLOR_BGR2RGB)
imgAumentada = cv.cvtColor(imgAumentada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
Grafico = plt.figure( )

Grafico.add_subplot(1,3,1)
plt.imshow( ImagemOriginal )
plt.title("Imagem\nOriginal")

Grafico.add_subplot(1,3,2)
plt.imshow(NovaImagem )
plt.title("Recorte\nProjetado")

Grafico.add_subplot(1,3,3)
plt.imshow(imgAumentada )
plt.title("Imagem\nResultado")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################
