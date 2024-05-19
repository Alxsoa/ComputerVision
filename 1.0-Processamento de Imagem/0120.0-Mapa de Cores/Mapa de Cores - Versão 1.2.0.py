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
# Funções de Uso Geral
########################################################################
#
def NomeMapaCor (id) :
    switcher = {
                    0 : "COLORMAP_AUTUMN",
                    1 : "COLORMAP_BONE",
                    2 : "COLORMAP_JET",
                    3 : "COLORMAP_WINTER",
                    4 : "COLORMAP_RAINBOW",
                    5 : "COLORMAP_OCEAN",
                    6 : "COLORMAP_SUMMER",
                    7 : "COLORMAP_SPRING",
                    8 : "COLORMAP_COOL",
                    9 : "COLORMAP_HSV",
                    10: "COLORMAP_PINK",
                    11: "COLORMAP_HOT",
                    12: "COLORMAP_PARULA",
                    13: "COLORMAP_MAGMA",
                    14: "COLORMAP_INFERNO",
                    15: "COLORMAP_PLASMA",
                    16: "COLORMAP_VIRIDIS",
                    17: "COLORMAP_CIVIDIS",
                    18: "COLORMAP_TWILIGHT",
                    19: "COLORMAP_TWILIGHT_SHIFTED",
                    20: "COLORMAP_TURBO",
                    21: "COLORMAP_DEEPGREEN"
                }
    return switcher.get(id, "NONE")

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Monalisa.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
ListaMonaliza = [ "Monaliza1.jpg", "Monaliza2.jpg", "Monaliza3.jpg", "Monaliza4.jpg", "Monaliza5.jpg", "Monaliza6.jpg", "Monaliza7.jpg"]

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
# Reduz o Tamanho da Imagem e Cria a Matriz
########################################################################
#
imgReduzida = cv.resize(imgBase, (250, 350), interpolation = cv.INTER_AREA)
imgTemporaria = np.zeros((250, 350, 3), np.uint8)

# 
########################################################################
# Processa e Apresenta o Resultado
########################################################################
#
iColuna = 1
iGrafico = 0
for iLinha in range (0,7):
    Grafico = plt.figure()  
    for iColuna in range (0,3):
        imgTemporaria = cv.applyColorMap(imgReduzida, iGrafico+iColuna)
        imgTemporaria = cv.cvtColor(imgTemporaria, cv.COLOR_BGR2RGB)        
        Grafico.add_subplot(1,3,iColuna+1)
        plt.imshow ( imgTemporaria )
        plt.title ( NomeMapaCor (iGrafico+iColuna) , fontsize=9 )     

    plt.tight_layout()
    plt.show ()
    iGrafico = iGrafico + 3



########################################################################
# FIM DO PROGRAMA
########################################################################
