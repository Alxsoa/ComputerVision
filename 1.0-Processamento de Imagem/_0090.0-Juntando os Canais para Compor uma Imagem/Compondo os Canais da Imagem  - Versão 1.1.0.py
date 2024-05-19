# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeJanela = "Imagem Base"
NomeImagem  = "Girassol.png"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/"  

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgGirassolAzul = cv.imread ( CaminhoImagem + "GirassolAzul.png", cv.IMREAD_UNCHANGED)
imgGirassolVerde = cv.imread ( CaminhoImagem + "GirassolVerde.png", cv.IMREAD_UNCHANGED)
imgGirassolVermelho = cv.imread ( CaminhoImagem + "GirassolVermelho.png", cv.IMREAD_UNCHANGED)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgGirassolAzul is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", "GirassolAzul.png" )
    exit ()

if imgGirassolVerde is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", "imgGirassolVerde" )
    exit ()

if imgGirassolVermelho is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", "GirassolVermelho.png" )
    exit ()

# 
########################################################################
# Montando a Imagem a Partir dos Canais
########################################################################
#
ImagemColorida = cv.merge ([imgGirassolVermelho, imgGirassolVerde, imgGirassolAzul])

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
#ImagemColorida = cv.cvtColor(ImagemColorida, cv.COLOR_BGR2RGB)
imgAzul = cv.cvtColor(imgGirassolAzul, cv.COLOR_BGR2RGB)
imgVerde = cv.cvtColor(imgGirassolVerde, cv.COLOR_BGR2RGB)
imgVermelho = cv.cvtColor(imgGirassolVermelho, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure(figsize=(15,8))

Grafico.add_subplot(1,4,1)
plt.imshow(ImagemColorida )
plt.title("Imagem\nReconstruída")

Grafico.add_subplot(1,4,2)
plt.imshow(imgAzul )
plt.title("Canal Azul")

Grafico.add_subplot(1,4,3)
plt.imshow(imgVerde )
plt.title("Canal Verde")

Grafico.add_subplot(1,4,4)
plt.imshow(imgVermelho )
plt.title("Canal Vermelho")

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.1,
                      hspace = 0.1 )

plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

