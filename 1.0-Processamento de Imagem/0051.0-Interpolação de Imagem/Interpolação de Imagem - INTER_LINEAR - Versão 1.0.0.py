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

def CenarioInterpolacaoImagem ( imgOriginal, imgDobro, imgMetade, strTituloDobro, strTituloMetade ):
    Grafico = plt.figure( )

    Grafico.add_subplot(1,3,1)
    plt.imshow(imgOriginal )
    plt.title("Original")

    Grafico.add_subplot(1,3,2)
    plt.imshow(imgDobro )
    plt.title(strTituloDobro)

    Grafico.add_subplot(1,3,3)
    plt.imshow(imgMetade )
    plt.title(strTituloMetade)
      
    plt.tight_layout()
    plt.show ()
    return ()
      
def EscalaImagemProporcao (imgOriginal, EscalaX, EscalaY, MetodoInterpolacao ):   
    return (cv.resize ( imgOriginal,
                        None,
                        fx=EscalaX, 
                        fy=EscalaY, 
                        interpolation = MetodoInterpolacao ))

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Olho.png"
dirRaiz = Path.home()
dirBase = "Atividades/LocalCV"
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
# Convertendo para Matplotlib
########################################################################
#
imgBase = cv.cvtColor ( imgBase, cv.COLOR_BGR2RGB )

# 
########################################################################
# Executa o Aumento e Redução da Imagem
########################################################################
#
CenarioInterpolacaoImagem ( imgBase,
                            EscalaImagemProporcao(imgBase,2,2,cv.INTER_LINEAR),
                            EscalaImagemProporcao(imgBase,.5,.5,cv.INTER_NEAREST),
                            "2 x Original",
                            "1/2 x Original")

########################################################################
# FIM DO PROGRAMA
########################################################################
# 						  