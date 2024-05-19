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
# Funções de Apoio
########################################################################
#
def SeparaImagem (imgTmpImagem, Direcao):
    Altura, Largura, Cor = imgTmpImagem.shape
    
    if Direcao == 'vertical':
        imgEsquerda = imgTmpImagem[:, :Largura // 2]
        imgDireita = imgTmpImagem[:, Largura // 2:]
        return imgEsquerda, imgDireita
    
    elif Direcao == 'horizontal':
        imgSuperior    = imgTmpImagem[:Altura // 2, :]
        imgInferior = imgTmpImagem[Altura // 2:, :]
        return imgSuperior, imgInferior
   
    else:
        raise ValueError('Parametro Invalido Use "vertical" ou "horizontal".')

def CaputuraDiferenca (imgTmpPrimeira, imgTmpSegunda):
    if(imgTmpPrimeira.shape == imgTmpSegunda.shape):
      imgDiferenca = cv.absdiff(imgTmpPrimeira, imgTmpSegunda)
      Azul, Verde, Vermelho = cv.split(imgDiferenca)
      zeros = np.zeros(imgDiferenca.shape[:2], dtype=np.uint8)
      imgDiferenca = cv.merge((Azul, zeros, zeros))
      return imgDiferenca
    
    else:
      raise ValueError( "As Imagens Devem Ser do Mesmo Tamanho")

def DesenhaCirculos (imgTmpDiferenca):
    imgCinza = cv.cvtColor(imgTmpDiferenca, cv.COLOR_BGR2GRAY)
    ret, Limiar = cv.threshold(imgCinza, 10, 255, cv.THRESH_BINARY)
    Contornos, Hierarquia = cv.findContours(Limiar, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    Circulos = []
    for iAux, lstContornos in enumerate(Contornos):
        (x, y), radius = cv.minEnclosingCircle(lstContornos)

        if radius > 5:
            IntersecaoCirculo = False
            for jAux, (center, r) in enumerate(Circulos):
                Distancia = np.sqrt((x - center[0])**2 + (y - center[1])**2)
                if Distancia < r or Distancia < radius:
                    IntersecaoCirculo = True

                    if radius > r:
                        Circulos[jAux] = ((x, y), radius)
                    break

            if not IntersecaoCirculo:
                Circulos.append(((x, y), radius))
    
    return Circulos
  
# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "JogoSeteErros.jpg"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
imgJogo = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR )

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgJogo is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Separa as Imagens da Tira Original
########################################################################
#
imgEsquerda, imgDireita = SeparaImagem (imgJogo, "vertical")

# 
########################################################################
# Calcula a Diferença
########################################################################
#
imgDiferenca = CaputuraDiferenca (imgEsquerda, imgDireita)

# 
########################################################################
# Desenha os Círclos Indicativos da Diferença
########################################################################
#
imgResultado = imgEsquerda.copy()
circles = DesenhaCirculos (imgDiferenca)
for (x, y), radius in circles:
    cv.circle(imgResultado, (int(x), int(y)), int(radius), (0, 0, 255), 2)

# 
########################################################################
# Apresenta os Resultados
########################################################################
#
imgTemporaria1 = cv.hconcat([imgEsquerda, imgDireita])
imgTemporaria2 = cv.hconcat([imgDiferenca, imgResultado])
imgTodasImagens = np.hstack(( imgTemporaria1, imgTemporaria2))   

cv.imshow( "Resultado", imgTodasImagens)
cv.waitKey()
	
########################################################################
# FIM DO PROGRAMA
########################################################################	
