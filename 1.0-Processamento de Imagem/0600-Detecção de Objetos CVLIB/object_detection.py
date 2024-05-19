# Referencia
# website: https://www.arunponnusamy.com
# https://github.com/arunponnusamy/cvlib/tree/master/examples

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cvlib as clb
from cvlib.object_detection import draw_bbox
import sys
import cv2 as cv
import os

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeJanela = "Imagem Base"
#NomeImagem  = "HomemMulher.jpg"
NomeImagem  = "PessoaAnimais.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)

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
# Reduzindo o Tamanho da Imagem
########################################################################
#
#imgBase = cv.resize(imgBase, (0,0), fx=0.2, fy=0.2, interpolation = cv.INTER_AREA)

# 
########################################################################
# Executando a Identificação dos Objetos
########################################################################
#
bbox, label, conf = clb.detect_common_objects(imgBase)
os.system ("clear")
print ("########################################################################")
print ("# Resumo da Detecção ")
print ("########################################################################")
print ( "Posição dos Objetos ......: ", bbox )
print ( "Descrição do Objeto ......: ", label )
print ( "Confiança de detecção ....: ", conf)
print ("########################################################################")
imgResultado = draw_bbox(imgBase, bbox, label, conf)

# 
########################################################################
# Apresentando a Imagem
########################################################################
#     
cv.imshow("Reconhecendo Objetos", imgResultado)
cv.waitKey()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
