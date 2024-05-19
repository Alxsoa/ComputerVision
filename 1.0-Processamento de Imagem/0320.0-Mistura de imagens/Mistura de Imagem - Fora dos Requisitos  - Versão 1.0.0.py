# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
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
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "Janela Base", ImagemMisturada)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
