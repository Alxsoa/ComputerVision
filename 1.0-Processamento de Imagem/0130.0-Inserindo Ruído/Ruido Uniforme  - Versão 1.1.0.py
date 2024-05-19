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
NomeOutput  = 'CaravelaRuidoUniforme.jpg'
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
# Reduzindo o Tamanho da Imagem
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
RuidoUniforme = np.zeros((ImagemAltura, ImagemLargura) )
cv.randu(RuidoUniforme,0,255)
RuidoUniforme=(RuidoUniforme*0.5).astype(np.uint8)
RuidoUniforme = cv.merge((RuidoUniforme,RuidoUniforme,RuidoUniforme))

# 
########################################################################
# Recuperando as Dimensões da Imagem com Ruido
########################################################################
#
RuidoAltura = RuidoUniforme.shape[0]
RuidoLargura = RuidoUniforme.shape[1]
RuidoCanais  = RuidoUniforme.shape[2]

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
ImagemResultado = cv.add ( imgCaravela,RuidoUniforme) 

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
imgCaravela = cv.cvtColor(imgCaravela, cv.COLOR_BGR2RGB)
RuidoUniforme = cv.cvtColor(RuidoUniforme, cv.COLOR_BGR2RGB)
ImagemResultado = cv.cvtColor(ImagemResultado, cv.COLOR_BGR2RGB)

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
plt.imshow(RuidoUniforme )
plt.title("Ruído Uniforme")

Grafico.add_subplot(1,3,3)
plt.imshow(ImagemResultado )
plt.title("Imagens \n Combinadas")

plt.tight_layout()
plt.show ()


########################################################################
# FIM DO PROGRAMA
########################################################################

