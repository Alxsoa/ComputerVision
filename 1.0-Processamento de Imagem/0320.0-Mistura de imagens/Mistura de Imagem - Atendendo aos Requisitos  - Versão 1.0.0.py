# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
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
NomeFundo = "Oceano.jpg"
NomeFrente  = "Peixes.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoFrente = str(Path(dirRaiz, dirBase, dirImagem, NomeFrente))
dirCaminhoFundo = str(Path(dirRaiz, dirBase, dirImagem, NomeFundo))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
ImagemFundo = cv.imread ( dirCaminhoFundo, cv.IMREAD_COLOR)
if ImagemFundo is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeFundo)
   exit ()

ImagemFrente = cv.imread ( dirCaminhoFrente, cv.IMREAD_COLOR)
if ImagemFrente is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeFrente)
   exit ()

# 
########################################################################
# Padrnizando os Tamanhos das Imagens
########################################################################
#
ImagemFrente = cv.resize( ImagemFrente, (500, 500) , interpolation = cv.INTER_AREA)
ImagemFundo = cv.resize ( ImagemFundo, (500, 500) , interpolation = cv.INTER_AREA)

# 
########################################################################
# Checa se Tem o Mesmo Tamanho
########################################################################
#
AlturaFrente, LarguraFrente, CanaisFrente = ImagemFrente.shape
AlturaFundo, LarguraFundo, CanaisFundo = ImagemFundo.shape

if ( (AlturaFrente==AlturaFundo) & (LarguraFrente==LarguraFundo) & (CanaisFrente==CanaisFundo)):
    print ( "########################################################################" )
    print ( "# Imagens Atendem aos Requisitos ")
    print ( "########################################################################" )    
else:
    print ( "########################################################################" )
    print ( "# Imagens NÃO Atendem aos Requisitos ")
    print ( "########################################################################" )    
    exit ()

# 
########################################################################
# Misturando a Imagem
########################################################################
#
ImagemMisturada = cv.addWeighted(ImagemFrente,0.7,ImagemFundo,0.3,0)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemFundo = cv.cvtColor(ImagemFundo, cv.COLOR_BGR2RGB)
ImagemFrente = cv.cvtColor(ImagemFrente, cv.COLOR_BGR2RGB)
ImagemMisturada = cv.cvtColor(ImagemMisturada, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure( )
  
Grafico.add_subplot(1,3,1)
plt.imshow(ImagemFundo )
plt.title("Oceano")

Grafico.add_subplot(1,3,2)
plt.imshow(ImagemFrente )
plt.title("Peixes")

Grafico.add_subplot(1,3,3)
plt.imshow(ImagemMisturada )
plt.title("Imagens\nCombinadas")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

