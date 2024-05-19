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
NomeImagem = "QRCode.png"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgQRCode = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgQRCode is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()
# 
########################################################################
# Inicializando o Detector
########################################################################
#
qrCodeDetector = cv.QRCodeDetector()
qrDados, qrBox, _  = qrCodeDetector.detectAndDecode(imgQRCode)

# 
########################################################################
# Detectando e Decodificando o QRCode
########################################################################
#
if qrBox is not None:
    print ( "Dados Decodificados : ", qrDados )
else:
    print ( "Não foi detectado Nenhuma Informação \n")

# 
########################################################################
# Apresentando a Imagem
########################################################################
#
cv.imshow ( "QRCode Capturado", imgQRCode)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
