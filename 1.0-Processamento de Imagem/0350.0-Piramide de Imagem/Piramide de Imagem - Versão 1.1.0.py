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
NomeImagem  = "Olho.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
Imagem = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)
if Imagem is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

imgReduzida = cv.resize(Imagem, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)
while True:
    nLinhas, nColunas, _channels = map(int, imgReduzida.shape)  
    cv.imshow ( "Janela Base", imgReduzida)
 
    Tecla = cv.waitKey(0)
    if Tecla == 27:
        break
        
    elif chr(Tecla) == 'i':
        imgReduzida = cv.pyrUp(imgReduzida, dstsize=(2 * nColunas, 2 * nLinhas))
        
    elif chr(Tecla) == 'o':
        imgReduzida = cv.pyrDown(imgReduzida, dstsize=(nColunas // 2, nLinhas // 2))

# 
########################################################################
# Destrói o Janelamento
########################################################################
#        
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
