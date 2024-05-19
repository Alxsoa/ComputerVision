# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
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
NomeImagem  = "LinhasEstacionamento2.jpg"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem ) 

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
# Reduzindo o tamanh da Imagem
########################################################################
#
imgBase = cv.resize(imgBase, (0,0), fx=0.15, fy=0.15, interpolation = cv.INTER_AREA)

# 
########################################################################
# Convertendo para Cinza (Requerimento)
########################################################################
#
imgCinza = cv.cvtColor ( imgBase, cv.COLOR_BGR2GRAY )

# 
########################################################################
# Reduzindo o Ruído
########################################################################
#
TamanhoKernel = 5
imgSemRuido = cv.GaussianBlur(imgCinza,(TamanhoKernel, TamanhoKernel),0)

# 
########################################################################
# Destacando Contornos
########################################################################
#
LimiteBaixo = 50
LimiteAlto  = 150
imgContornos = cv.Canny(imgSemRuido, LimiteBaixo, LimiteAlto)

# 
########################################################################
# Parametros da Busca de Linhas
########################################################################
#
Rho = 1 # resolução de distância em pixels da grade Hough
Theta = np.pi / 180 # resolução angular em radianos da grade Hough
Threshold = 15 # número mínimo de votos (interseções na célula da grade Hough)
MinLineLength = 50 # número mínimo de pixels que compõem uma linha
MaxLineGap = 20 # intervalo máximo em pixels entre segmentos de linha conectáveis
line_image = np.copy(imgBase) * 0 # criando um espaço em branco para desenhar linhas

# 
########################################################################
# Buscando as Linhas
########################################################################
#
lines = cv.HoughLinesP (
                            imgContornos, 
                            Rho, 
                            Theta, 
                            Threshold, 
                            np.array([]),
                            MinLineLength, 
                            MaxLineGap
                        )

# 
########################################################################
# Construindo as Linhas
########################################################################
#
for line in lines:
    for x1,y1,x2,y2 in line:
        cv.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)

# 
########################################################################
# Desenhando as Linhas
########################################################################
#
lines_edges = cv.addWeighted ( 
                                imgBase, 
                                0.8, 
                                line_image, 
                                1, 
                                0
                             )

# 
########################################################################
# Apresentando os Resultados
########################################################################
#
cv.imshow("Resultado",lines_edges)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
