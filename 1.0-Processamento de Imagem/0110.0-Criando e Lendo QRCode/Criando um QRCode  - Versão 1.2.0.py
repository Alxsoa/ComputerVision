# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import os
import qrcode
import sys
from pathlib import Path

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem = "QRCode.png"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
qrData = "www.opencv.org"
dirCaminhoOutput = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
print ( dirCaminhoOutput )
# 
########################################################################
# Gerando o QRCode
########################################################################
#
imgQRCode = qrcode.make ( qrData )

# 
########################################################################
# Salvando a Imagem do QRCode
########################################################################
#
imgQRCode.save ( dirCaminhoOutput )

########################################################################
# FIM DO PROGRAMA
########################################################################
