# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 
########################################################################
# Funções de Apoio
########################################################################
#
def ImagensExposicao ():
  
  Exposicao = np.array([ 1/30.0, 0.25, 2.5, 15.0 ], dtype=np.float32)
  NomeArquivos = [
                  "/home/asoares/LocalCV/Imagens/img_0.033.jpg", 
                  "/home/asoares/LocalCV/Imagens/img_0.25.jpg", 
                  "/home/asoares/LocalCV/Imagens/img_2.5.jpg", 
                  "/home/asoares/LocalCV/Imagens/img_15.jpg"
                 ]

  imgImagens = []
  for Nome in NomeArquivos:
      imgTmp = cv.imread(Nome)
      imgImagens.append(imgTmp)
  
  return (imgImagens, Exposicao)

# 
########################################################################
# Leitura das Imagens e Exposições
########################################################################
#
lstImagens, Exposicao = ImagensExposicao()

# 
########################################################################
# Alinhando as Imagens
########################################################################
#
alignMTB = cv.createAlignMTB()
alignMTB.process(lstImagens, lstImagens)

# 
########################################################################
# Obtendo Camera Response Function (CRF)
########################################################################
#
calibrateDebevec = cv.createCalibrateDebevec()
responseDebevec = calibrateDebevec.process(lstImagens, Exposicao)

# 
########################################################################
# Juntando as Imgens de Maneira Linear
########################################################################
#
mergeDebevec = cv.createMergeDebevec()
hdrDebevec = mergeDebevec.process(lstImagens, Exposicao, responseDebevec)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
lstImagens[0]  = cv.cvtColor(lstImagens[0] , cv.COLOR_BGR2RGB)
lstImagens[1]  = cv.cvtColor(lstImagens[1] , cv.COLOR_BGR2RGB)
lstImagens[2]  = cv.cvtColor(lstImagens[2] , cv.COLOR_BGR2RGB)
lstImagens[3]  = cv.cvtColor(lstImagens[3] , cv.COLOR_BGR2RGB)
hdrDebevec = cv.cvtColor(hdrDebevec , cv.COLOR_BGR2RGB)

# 
########################################################################
# Preparação para Apresentação dos Resultados
########################################################################
#
lstImagens[0] = cv.resize(lstImagens[0], (450, 300), interpolation = cv.INTER_AREA)
lstImagens[0] = cv.copyMakeBorder (
                                      src=lstImagens[0], 
                                      top=5, 
                                      bottom=5, 
                                      left=5, 
                                      right=5, 
                                      borderType=cv.BORDER_CONSTANT, 
                                      value=(255,255,255)
                                    ) 

lstImagens[1] = cv.resize(lstImagens[1], (450, 300), interpolation = cv.INTER_AREA)
lstImagens[1] = cv.copyMakeBorder (
                                      src=lstImagens[1], 
                                      top=5, 
                                      bottom=5, 
                                      left=5, 
                                      right=5, 
                                      borderType=cv.BORDER_CONSTANT, 
                                      value=(255,255,255)
                                    ) 

lstImagens[2] = cv.resize(lstImagens[2], (450, 300), interpolation = cv.INTER_AREA)
lstImagens[2] = cv.copyMakeBorder (
                                      src=lstImagens[2], 
                                      top=5, 
                                      bottom=5, 
                                      left=5, 
                                      right=5, 
                                      borderType=cv.BORDER_CONSTANT, 
                                      value=(255,255,255)
                                    ) 

lstImagens[3] = cv.resize(lstImagens[3], (450, 300), interpolation = cv.INTER_AREA)
lstImagens[3] = cv.copyMakeBorder (
                                      src=lstImagens[3], 
                                      top=5, 
                                      bottom=5, 
                                      left=5, 
                                      right=5, 
                                      borderType=cv.BORDER_CONSTANT, 
                                      value=(255,255,255)
                                    ) 

hdrDebevec = cv.resize(hdrDebevec, (450, 300), interpolation = cv.INTER_AREA)
hdrDebevec = cv.copyMakeBorder (
                                src=hdrDebevec, 
                                top=5, 
                                bottom=5, 
                                left=5, 
                                right=5, 
                                borderType=cv.BORDER_CONSTANT, 
                                value=(255,255,255)
                             ) 

# 
########################################################################
# Apresentação dos Resultados
########################################################################
#
imgResultado = np.hstack ( [lstImagens[0], lstImagens[1], lstImagens [2], lstImagens [3]])
cv.imshow ( "Imagens com Diferentes Exposicoes", imgResultado)
cv.imshow ( "Efeito Final", hdrDebevec)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
