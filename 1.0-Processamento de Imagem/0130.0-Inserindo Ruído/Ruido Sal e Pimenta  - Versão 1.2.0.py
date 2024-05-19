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

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "Caravela.jpg"
NomeOutput  = 'CaravelaRuidoSalPimenta.jpg'
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoOutput = str(Path(dirRaiz, dirBase, dirImagem, NomeOutput))
EscalaPercentual = 0.80

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
# Reduzindo a Imagem
########################################################################
#
imgCaravela = cv.resize(imgBase, (0, 0),fx=EscalaPercentual, fy=EscalaPercentual, interpolation = cv.INTER_AREA)

# 
########################################################################
# Recuperando as Dimensões da Imagem 
########################################################################
#
ImagemAltura = imgCaravela.shape[0]
ImagemLargura  = imgCaravela.shape[1]
ImagemCanais = imgCaravela.shape[2]

# 
########################################################################
# Inserindo o Ruído 
########################################################################
#
RuidoSalPimenta = np.zeros((ImagemAltura, ImagemLargura), dtype=np.uint8)
cv.randu(RuidoSalPimenta,0,255)
RuidoSalPimenta = cv.merge((RuidoSalPimenta,RuidoSalPimenta,RuidoSalPimenta))
RuidoSalPimenta = cv.threshold(RuidoSalPimenta,245,255,cv.THRESH_BINARY)[1]

# 
########################################################################
# Recuperando as Dimensões da Imagem com Ruido
########################################################################
#
RuidoAltura  = RuidoSalPimenta.shape[0]
RuidoLargura = RuidoSalPimenta.shape[1]
RuidoCanais  = RuidoSalPimenta.shape[2]

# 
########################################################################
# Checando se as Imagens São do Mesmo Tamanho
########################################################################
#
LimpaTerminal ()
print ( "########################################################################")
print ( "# Avaliando as Condições para o Merge")
print ( "########################################################################")
print ( "# Altura Imagem Original .....: ", ImagemAltura)
print ( "# Largura Imagem Original ....: ", ImagemLargura)
print ( "# Canais Imagem Original .....: ", ImagemCanais)
print ( "# ")
print ( "# Altura Imagem Ruido ........: ", RuidoAltura)
print ( "# Largura Imagem Ruido .......: ", RuidoLargura)
print ( "# Canais Imagem Ruido ........: ", RuidoCanais)
print ( "########################################################################")

# 
########################################################################
# Combinando as Imagens
########################################################################
#
ImagemResultado = cv.add ( imgCaravela, RuidoSalPimenta ) 

# 
########################################################################
# Salvando o Resultado
########################################################################
#
cv.imwrite (dirCaminhoOutput, ImagemResultado)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgCaravela = cv.cvtColor ( imgCaravela, cv.COLOR_BGR2RGB )
RuidoSalPimenta = cv.cvtColor ( RuidoSalPimenta, cv.COLOR_BGR2RGB )
ImagemResultado = cv.cvtColor ( ImagemResultado, cv.COLOR_BGR2RGB )

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(1,3,1)
plt.imshow(imgCaravela )
plt.title("Original")

Grafico.add_subplot(1,3,2)
plt.imshow(RuidoSalPimenta )
plt.title("Ruído \n Sal e Pimenta")

Grafico.add_subplot(1,3,3)
plt.imshow(ImagemResultado )
plt.title("Imagens \n Combinadas")

plt.tight_layout()
plt.show ()

########################################################################
# FIM DO PROGRAMA
########################################################################

