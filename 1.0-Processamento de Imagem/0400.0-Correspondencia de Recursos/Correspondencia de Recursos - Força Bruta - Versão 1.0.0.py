# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2
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
NomeImagemBase = "LivroFrontalTesla.jpg"
NomeImagemComparada = "LivroInclinadoTesla.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagemBase = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemBase))
dirCaminhoImagemComparada = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemComparada))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
ImagemBase = cv2.imread ( dirCaminhoImagemBase, cv2.IMREAD_COLOR )
ImagemComparada = cv2.imread ( dirCaminhoImagemComparada, cv2.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemBase is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagemBase)
    exit ()

if ImagemComparada is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagemComparada)
    exit ()

# 
########################################################################
# Executa a Correlação
########################################################################
#
orbDetector = cv2.ORB_create(nfeatures=1500)
ptsPrincipal1, Descritor1 = orbDetector.detectAndCompute(ImagemBase, None)
ptsPrincipal2, Descritor2 = orbDetector.detectAndCompute(ImagemComparada, None)

bfDetector = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
Correspondencias = bfDetector.match(Descritor1, Descritor2)
Correspondencias = sorted(Correspondencias, key=lambda x: x.distance)

# 
########################################################################
# apresenta os 50 Primeiros Resultados
########################################################################
#
imgResultado = cv2.drawMatches  (
                                    ImagemBase, 
                                    ptsPrincipal1, 
                                    ImagemComparada, 
                                    ptsPrincipal2, 
                                    Correspondencias[:50], 
                                    None
                                )

# 
########################################################################
# Apresenta os Resultados
########################################################################
#
cv2.imshow( "Correspondencias da Imagem", imgResultado)
cv2.waitKey()
	
########################################################################
# FIM DO PROGRAMA
########################################################################	
