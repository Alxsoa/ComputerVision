# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os
import numpy as np
from pathlib import Path
from matplotlib import pyplot as plt
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
NomeImagem  = "CataVento.jpg" # Exemplo 1
#NomeImagem  = "Ator.jpg"      # Exemplo 2
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Imagens"  
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread( dirCaminhoImagem )

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
   os.system ("clear")
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Seleção da Região de Interesse e Inicialização do Tracker
########################################################################
#
sltRegiao = cv.selectROI ("Selecione a Regiao", imgBase, True,  printNotice=False)

# 
########################################################################
# Definindo a Mascara e os Modelos de Fundo e Frente
########################################################################
#
mskBase = np.zeros(imgBase.shape[:2],np.uint8) 
fundoModel = np.zeros((1,65),np.float64) 
frenteModel = np.zeros((1,65),np.float64)

# 
########################################################################
# Aplicando o Recorte e Calcullando a Imagem 
########################################################################
#
rctRegiao = sltRegiao
mskGrab, fg, bg = cv.grabCut ( 
                                imgBase,
                                mskBase,
                                rctRegiao,
                                fundoModel,
                                frenteModel,
                                10,
                                cv.GC_INIT_WITH_RECT
                             )

# 
########################################################################
# Calculando a Mascara e Imagem Resultado
########################################################################
#
mskResultado = np.where((mskGrab==2)|(mskGrab==0),0,1).astype('uint8') 
imgResultado = imgBase*mskResultado[:,:,np.newaxis] 

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
cv.imshow ( "Imagem Resultado", imgResultado)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################