# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
Area = "Cor Resultante"

# 
########################################################################
# Instancia de Evento
########################################################################
#
def SemExecucao(x):
    pass

# 
########################################################################
# Criação do Retangulo Inicialmente Cor Preta
########################################################################
#
Imagem = np.zeros((300,512,3), np.uint8)
cv.namedWindow(Area)

# 
########################################################################
# Controle das Cores
########################################################################
#
cv.createTrackbar('R',Area,0,255,SemExecucao)
cv.createTrackbar('G',Area,0,255,SemExecucao)
cv.createTrackbar('B',Area,0,255,SemExecucao)

# 
########################################################################
# Switch para Execução
########################################################################
#
Switch = '0 : OFF \n1 : ON'
cv.createTrackbar (Switch, Area,0,1,SemExecucao)

# 
########################################################################
# Loop de Captura
########################################################################
#
while(1):
    cv.imshow( Area, Imagem)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    CorVermelha = cv.getTrackbarPos ('R', Area)
    CorVerde  = cv.getTrackbarPos ('G', Area)
    CorAzul = cv.getTrackbarPos ('B', Area)
    Mudanca = cv.getTrackbarPos (Switch, Area)

    if Mudanca == 0:
        Imagem[:] = 0
    else:
        Imagem[:] = [CorAzul,CorVerde,CorVermelha]
        
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
