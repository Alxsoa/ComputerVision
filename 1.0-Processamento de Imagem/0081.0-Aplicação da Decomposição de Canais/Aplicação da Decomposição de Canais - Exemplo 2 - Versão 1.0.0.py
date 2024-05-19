# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from skimage.io import imshow, imread
from skimage.util import img_as_ubyte
from pathlib import Path
import os

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

def EstatisticaCanal (imgImagem):
    dfCor = []
    for iAux in range(0, 3):
        CorMaxima =np.max(imgImagem[:,:,iAux])
        CorMedia = np.mean(imgImagem[:,:,iAux])
        CorMediana = np.median(imgImagem[:,:,iAux])
        Percentil90 = np.percentile(imgImagem[:,:,iAux], 90, axis=(0,1))
        Percentil95 = np.percentile(imgImagem[:,:,iAux], 95, axis=(0,1))
        Percentil99 = np.percentile(imgImagem[:,:,iAux], 99, axis=(0,1))
        
        Linha = (CorMaxima, CorMedia, CorMediana, Percentil90, Percentil95, Percentil99)        
        dfCor.append(Linha)
    
    dfResultado = pd.DataFrame (
                                dfCor, 
                                index = ["Vermelho", "Verde", "Azul"],
                                columns = ["Maximo", "Media", "Mediana", "Percentil_90","Percentil_95", "Percentil_99"]
                               )
    return (dfResultado)


def AjustePercentil (imgImagem):
    Figura, Grafico = plt.subplots(2, 3) 
    AzulPercentil = 99.75 
    Parametros =    [
                    [99] + [99] + [AzulPercentil] + [99] ,
                    [95] + [95] + [AzulPercentil] + [95] ,
                    [90] + [90] + [AzulPercentil] + [90] ,
                    [85] + [85] + [AzulPercentil] + [85] ,
                    [80] + [80] + [AzulPercentil] + [80]
                    ]

    Grafico[0][0].imshow(imgImagem)
    Grafico[0][0].set_title("Original", fontsize = 11)
    Grafico[0][1].imshow    (  
                                img_as_ubyte 
                                (
                                    (
                                        imgImagem / 
                                        [
                                            np.percentile(imgImagem[:,:,iAux], Parametros[0][iAux], axis=(0, 1)) for iAux in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )
        
    Grafico[0][1].set_title("Azul : {}, Outros : {}".format(AzulPercentil, Parametros[0][1], fontsize = 11))
    Grafico[0][2].imshow    (
                                img_as_ubyte
                                (
                                    (
                                        imgImagem / 
                                        [
                                            np.percentile(imgImagem[:,:,iAux], Parametros[1][iAux], axis=(0, 1)) for iAux in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )
    
    Grafico[0][2].set_title("Azul : {}, Outros : {}".format(AzulPercentil, Parametros[1][1], fontsize = 11))
    Grafico[1][0].imshow    (
                                img_as_ubyte
                                (
                                    (
                                        imgImagem / 
                                        [
                                            np.percentile(imgImagem[:,:,iAux], Parametros[2][iAux], axis=(0, 1)) for iAux in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )
    
    Grafico[1][0].set_title("Azul : {}, Outros : {}".format(AzulPercentil,Parametros[2][1], fontsize = 11))
    Grafico[1][1].imshow    (
                                img_as_ubyte
                                (
                                    (
                                        imgImagem /
                                        [
                                            np.percentile(imgImagem[:,:,iAux], Parametros[3][iAux], axis=(0, 1)) for iAux in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )
    
    Grafico[1][1].set_title("Azul : {}, Outros : {}".format(AzulPercentil,Parametros[3][1], fontsize = 11))
    Grafico[1][2].imshow    ( 
                                img_as_ubyte 
                                (
                                    ( 
                                        imgImagem /
                                        [
                                            np.percentile(imgImagem[:,:,iAux], Parametros[4][iAux], axis=(0, 1)) for iAux in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )
    
    Grafico[1][2].set_title("Azul : {}, Outros : {}".format(AzulPercentil,Parametros[4][1], fontsize = 11))
    plt.tight_layout() 
    plt.show ()
    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Praia.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
try:
  imgBase = imread(dirCaminhoImagem)
except:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Mostrando a Imagem nos Diferentes Canais
########################################################################
#
rgbLista = ["Reds","Greens","Blues"]
rgbTitulo = ["Canal Vermelho", "Canal Verde", "Canal Azul"]
Figura, Grafico = plt.subplots (1, 3) 

for iAux in range(3):
    Grafico[iAux].imshow(imgBase[:,:,iAux], cmap = rgbLista[iAux])
    Grafico[iAux].set_title(rgbTitulo[iAux], fontsize = 11)

plt.tight_layout() 
plt.show ()

# 
########################################################################
# Identifica Qual o Canal Predominante
########################################################################
#
dfResultado = EstatisticaCanal (imgBase)
LimpaTerminal ()
print (dfResultado)

# 
########################################################################
# Aplica a Correção
########################################################################
#
AjustePercentil (imgBase)

# 
########################################################################
# Melhorando a Correção em Partes
########################################################################
#
Parametros =    [
                [99.9] + [97.75]*3,
                [99.75] + [92]*3
                ]  

Figura, Grafico = plt.subplots(2, 2)
Grafico[0][0].imshow(imgBase[0:320])
Grafico[0][0].set_title("Céu Original", fontsize = 11)

Grafico[1][0].imshow(imgBase[320:])
Grafico[1][0].set_title("Oceano Original", fontsize = 11)

imgCeuAjustado = img_as_ubyte(((imgBase[0:320]/ [np.percentile(imgBase[:,:,i], Parametros[0][i], axis=(0, 1)) for i in range(3)]).clip(0,1)))
Grafico[0][1].imshow(  imgCeuAjustado )
Grafico[0][1].set_title("Céu Ajustado", fontsize = 11)

imgOceanoAjustado = img_as_ubyte(((imgBase[320:]/ [np.percentile(imgBase[:,:,i], Parametros[1][i], axis=(0, 1)) for i in range(3)]).clip(0,1)))
Grafico[1][1].imshow(imgOceanoAjustado)
Grafico[1][1].set_title("Oceano Ajustado", fontsize = 11)

Figura.tight_layout()
plt.show ()

# 
########################################################################
# Resultado Final
########################################################################
#
Figura, Grafico = plt.subplots(1, 1)
Grafico.imshow(np.concatenate((imgCeuAjustado, imgOceanoAjustado), axis=0))
Grafico.set_title("Resultado Final", fontsize = 11)
Figura.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

