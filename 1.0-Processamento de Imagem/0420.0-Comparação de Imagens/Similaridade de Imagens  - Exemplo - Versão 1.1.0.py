# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
from skimage.metrics import structural_similarity
import imageio
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

def Similaridade (imgBase, imgAlvo):
    (GrauSimilaridade, imgDiff) = structural_similarity(imgBase, imgAlvo, full=True)
    return (GrauSimilaridade, imgDiff)

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagemAlvo = "ImagemAlvo.jpg"
NomeImagemBase = "ImagemBase.jpg"
NomeImagemGif  = "ImagemComparacao.gif"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoAlvo = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemAlvo))
dirCaminhoBase = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemBase))
dirCaminhoOutput = str(Path(dirRaiz, dirBase, dirImagem, NomeImagemGif))

# 
########################################################################
# Lendo as Imagens
########################################################################
#
imgBase = cv.imread ( dirCaminhoBase, cv.IMREAD_COLOR )
if imgBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagemBase)
   exit ()


imgAlvo = cv.imread ( dirCaminhoAlvo, cv.IMREAD_COLOR )
if imgAlvo is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagemAlvo)
   exit ()

# 
########################################################################
# Convertendo para Tons de Cinza
########################################################################
#
imgOriginalReserva = np.copy (imgBase)
imgBaseCinza = cv.cvtColor(imgBase, cv.COLOR_BGR2GRAY)
imgAlvoCinza = cv.cvtColor(imgAlvo, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Calculando a Similaridade
########################################################################
#
(GrauSimilaridade, imgDiferenca) = Similaridade (imgBaseCinza, imgAlvoCinza) 

# 
########################################################################
# Transforma Resultados de Reais para Inteiros
########################################################################
#
imgDiferenca = (imgDiferenca * 255).astype("uint8")
imgDiferencaBox = cv.merge([imgDiferenca, imgDiferenca, imgDiferenca])

# 
########################################################################
# Busca os Contornos para Obter as Regiões que Diferem 
########################################################################
#
Limiar = cv.threshold(imgDiferenca, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
Contornos = cv.findContours(Limiar, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
Contornos = Contornos[0] if len(Contornos) == 2 else Contornos[1]

imgMascara = np.zeros(imgBase.shape, dtype='uint8')
imgPreenchida = np.copy (imgAlvo)

# 
########################################################################
# Percorre os Contornos
########################################################################
#
for cAux in Contornos:
    iArea = cv.contourArea(cAux)
    if iArea > 40:
        x,y,w,h = cv.boundingRect(cAux)
        cv.rectangle(imgBase, (x, y), (x + w, y + h), (36,255,12), 2)
        cv.rectangle(imgAlvo, (x, y), (x + w, y + h), (36,255,12), 2)
        cv.rectangle(imgDiferencaBox, (x, y), (x + w, y + h), (36,255,12), 2)
        cv.drawContours(imgMascara, [cAux], 0, (255,255,255), -1)
        cv.drawContours(imgPreenchida, [cAux], 0, (0,255,0), -1)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
imgOriginalReserva = cv.cvtColor(imgOriginalReserva, cv.COLOR_BGR2RGB)
imgAlvo = cv.cvtColor(imgAlvo, cv.COLOR_BGR2RGB)
imgDiferenca = cv.cvtColor(imgDiferenca, cv.COLOR_BGR2RGB)
imgDiferencaBox = cv.cvtColor(imgDiferencaBox, cv.COLOR_BGR2RGB)
imgMascara = cv.cvtColor(imgMascara, cv.COLOR_BGR2RGB)
imgPreenchida = cv.cvtColor(imgPreenchida, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
Grafico = plt.figure()

Grafico.add_subplot(2,3,1)
plt.imshow(imgOriginalReserva )
plt.title("Original")

Grafico.add_subplot(2,3,2)
plt.imshow(imgAlvo )
plt.title('Grau de Similaridade\n ({:.2f})'.format(GrauSimilaridade))

Grafico.add_subplot(2,3,3)
plt.imshow(imgDiferenca )
plt.title("Diferença Imagem")

Grafico.add_subplot(2,3,4)
plt.imshow(imgDiferencaBox )
plt.title("Diferença Preenchida")

Grafico.add_subplot(2,3,5)
plt.imshow(imgMascara )
plt.title("Máscara")

Grafico.add_subplot(2,3,6)
plt.imshow(imgPreenchida )
plt.title("Preenchimento")

plt.tight_layout ()
plt.show ()

# 
########################################################################
# Loop de Criação do Gif Animado
########################################################################
#
lstFrame = []
for iAux in range (0, 100):
    if ( (iAux % 2) == 0):
       lstFrame.append(imgOriginalReserva)
    else:
       lstFrame.append(imgPreenchida)

# 
########################################################################
# Salvando o Gif Animado a Duracao é em ms (50 fps == 20 duration)
########################################################################
#
with imageio.get_writer( dirCaminhoOutput, mode="I") as EscreveGif:
    for idx, frame in enumerate(lstFrame):
        EscreveGif.append_data(frame)

########################################################################
# FIM DO PROGRAMA
########################################################################	
