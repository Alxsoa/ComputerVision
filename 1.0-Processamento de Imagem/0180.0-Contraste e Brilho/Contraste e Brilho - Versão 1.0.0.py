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
NomeImagem  = "Girassol.png"
NomeJanela = "Imagem Base"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Funções de Uso Geral
########################################################################
#
def Controlador (tmpImagem, Brilho=255, Contraste=127):
    
    Brilho = int((Brilho - 0) * (255 - (-255)) / (510 - 0) + (-255))
    Contraste = int((Contraste - 0) * (127 - (-127)) / (254 - 0) + (-127))
  
    if Brilho != 0:
        if Brilho > 0:
            Sombra = Brilho
            Maximo = 255
        else:
            Sombra = 0
            Maximo = 255 + Brilho
  
        al_pha = (Maximo - Sombra) / 255
        ga_mma = Sombra
        ImagemResultado = cv.addWeighted(tmpImagem, al_pha, tmpImagem, 0, ga_mma)
  
    else:
        ImagemResultado = tmpImagem
  
    if Contraste != 0:
        Alpha = float(131 * (Contraste + 127)) / (127 * (131 - Contraste))
        Gamma = 127 * (1 - Alpha)
        ImagemResultado = cv.addWeighted(ImagemResultado, Alpha, ImagemResultado, 0, Gamma)
  
    return ImagemResultado

def EfeitoContrasteBrilho (Brilho=0):
    Brilho = cv.getTrackbarPos("Brilho", "Processamento de Imagem")
    Contraste = cv.getTrackbarPos("Contraste", "Processamento de Imagem")
    EfeitoResultado = Controlador (Imagem, Brilho, Contraste)
    cv.imshow("Efeito Resultante", EfeitoResultado)
    return ()

# 
########################################################################
# Lendo a Imagem
########################################################################
#
Imagem = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if Imagem is None:
    LimpaTerminal ()
    print( "Não Foi Localizada a Imagem : ", NomeImagem)
    exit ()

cv.namedWindow("Processamento de Imagem")
cv.imshow("Processamento de Imagem", Imagem)

cv.createTrackbar("Brilho", "Processamento de Imagem", 255, 2 * 255, EfeitoContrasteBrilho) 
cv.createTrackbar("Contraste", "Processamento de Imagem", 127, 2 * 127, EfeitoContrasteBrilho)  
    
EfeitoContrasteBrilho (0)
cv.waitKey(0)

########################################################################
# FIM DO PROGRAMA
########################################################################
