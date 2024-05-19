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
    Vermelho = 99.75  
    parameter_matrix =  [
                            [Vermelho] + [99]*3,
                            [Vermelho] + [95]*3,
                            [Vermelho] + [90]*3,
                            [Vermelho] + [85]*3,
                            [Vermelho] + [80]*3
                        ]
    
    Grafico[0][0].imshow(imgImagem)
    Grafico[0][0].set_title("Original", fontsize = 11)

    Grafico[0][1].set_title(f"Vermelho : {Vermelho}, Outros : {parameter_matrix[0][1]}", fontsize = 11)
    Grafico[0][1].imshow    (
                                img_as_ubyte
                                (
                                    (
                                        imgImagem / 
                                        [
                                            np.percentile(imgImagem[:,:,i], parameter_matrix[0][i], axis=(0, 1)) for i in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )

    Grafico[0][2].set_title(f"Vermelho : {Vermelho}, Outros : {parameter_matrix[1][1]}", fontsize = 11)
    Grafico[0][2].imshow    (
                                img_as_ubyte
                                (
                                    (
                                        imgImagem / 
                                        [
                                            np.percentile(imgImagem[:,:,i], parameter_matrix[1][i], axis=(0, 1)) for i in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )  
    
    Grafico[1][0].set_title(f"Vermelho : {Vermelho}, Outros : {parameter_matrix[2][1]}", fontsize = 11)
    Grafico[1][0].imshow    (
                                img_as_ubyte
                                (
                                    (
                                        imgImagem / 
                                        [
                                            np.percentile(imgImagem[:,:,i],parameter_matrix[2][i], axis=(0, 1)) for i in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )

    Grafico[1][1].set_title(f"Vermelho : {Vermelho}, Outros : {parameter_matrix[3][1]}", fontsize = 11)
    Grafico[1][1].imshow    (
                                img_as_ubyte
                                (
                                    (
                                        imgImagem /
                                        [
                                            np.percentile(imgImagem[:,:,i],parameter_matrix[3][i], axis=(0, 1)) for i in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )

    Grafico[1][2].set_title(f"Vermelho : {Vermelho}, Outros : {parameter_matrix[4][1]}", fontsize = 11)
    Grafico[1][2].imshow    (
                                img_as_ubyte
                                (
                                    (
                                        imgImagem / 
                                        [
                                            np.percentile(imgImagem[:,:,i],parameter_matrix[4][i], axis=(0, 1)) for i in range(0, 3)
                                        ]
                                    ).clip(0,1)
                                )
                            )    
    
    Figura.tight_layout() 
    plt.show ()
    return ()

def AjusteMediaMediana (imgImagem):
    Figura, Grafico = plt.subplots(2, 2)

    Grafico[0][0].imshow(imgImagem )
    Grafico[0][0].set_title("Imagem Original", fontsize = 11)

    Grafico[0][1].imshow(img_as_ubyte((imgImagem / np.mean(imgImagem)).clip(0,1)))
    Grafico[0][1].set_title("Ajustada pela Média", fontsize = 11)
    
    Grafico[1][0].imshow(img_as_ubyte((imgImagem/ np.median(imgImagem)).clip(0,1)))
    Grafico[1][0].set_title("Ajustada pela Mediana", fontsize = 11)

    Grafico[1][1].imshow(img_as_ubyte((imgImagem/ np.max(imgImagem)).clip(0, 1)))
    Grafico[1][1].set_title("Ajustada pelo Máximo", fontsize = 11)
    
    Figura.tight_layout()
    plt.show ()
    return ()

def ReduzindoVermelho (imgImagem):

    Figura, Grafico = plt.subplots(1, 3) 
    Grafico[0].imshow(imgImagem)
    Grafico[0].set_title("Original", fontsize = 11)

    Grafico[1].set_title("Vermelho : Max, Outros : Média", fontsize = 11)
    Grafico[1].imshow   (
                            img_as_ubyte
                            (
                                (
                                    imgImagem / 
                                    [
                                        np.max(imgImagem[:,:,0]),
                                        np.mean(imgImagem[:,:,1]),
                                        np.mean(imgImagem[:,:,2])
                                    ]
                                ).clip(0, 1)
                            )
                        )

    Grafico[2].set_title("Vermelho : Max, Outros : Mediana", fontsize = 11)
    Grafico[2].imshow   (
                            img_as_ubyte
                            (
                                (
                                    imgImagem / 
                                    [
                                        np.max(imgImagem[:,:,0]),
                                        np.median(imgImagem[:,:,1]),
                                        np.median(imgImagem[:,:,2])
                                    ]
                                ).clip(0, 1)
                            )
                        )

    Figura.tight_layout()
    plt.show ()
    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Predio.jpg"
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
# Ajusta os Pontos pela Média e Mediana
########################################################################
#
AjusteMediaMediana (imgBase)

# 
########################################################################
# Reduzindo Vermelho
########################################################################
#
ReduzindoVermelho (imgBase)

# 
########################################################################
# Aplica a Correção
########################################################################
#
AjustePercentil (imgBase)

########################################################################
# FIM DO PROGRAMA
########################################################################

