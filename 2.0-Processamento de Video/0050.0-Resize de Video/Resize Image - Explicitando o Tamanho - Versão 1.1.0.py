# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
DirBase = "LocalCV/"
CaminhoBase = "/home/asoares/" + DirBase
NomeJanela = "Imagem Reduzida"
NomeImagem  = "audi.jpg"
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if Imagem is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

# 
########################################################################
# Apresentando a Imagem
########################################################################
#

imgReduzida = cv.resize(Imagem, (450, 300), interpolation = cv.INTER_AREA)
cv.imshow ( "JanelaBase", imgReduzida)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.imshow ( "Imagem Grande" , Imagem )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
