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
BaseDir = "LocalCV/"
NomeJanela = "Imagem Reduzida"
NomeImagem  = "audi.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
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

imgReduzida = cv.resize(Imagem, (0,0), fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)
cv.imshow ( "JanelaBase", imgReduzida)
cv.setWindowTitle("JanelaBase", NomeJanela )
cv.imshow ( "Imagem Grande" , Imagem )
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
