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
DirBase = "LocalCV/"
NomeVideo = "PeixeNadando.mp4"
CaminhoBase = "/home/asoares/" + DirBase
CaminhoVideo = CaminhoBase + "Videos/" 

# 
########################################################################
# Abrindo o Arquivo de Vídeo
########################################################################
#
Video = cv.VideoCapture (CaminhoVideo + NomeVideo)
if (Video.isOpened()== False): 
  print ("########################################################################")
  print ("# Video Não Encontrado ")
  print ("########################################################################")
  exit ()

# 
########################################################################
# Criando o Subtrador 
########################################################################
#
subPeixe = cv.bgsegm.createBackgroundSubtractorMOG (  history = 10,  # Length of the history.
                                                      nmixtures = 3,  # Number of Gaussian mixtures.
                                                      backgroundRatio = 0.6, # Background ratio.
                                                      noiseSigma = 20 ) # standard deviation of the brightness or each color channel (0 é autmoático)

# 
########################################################################
# Lendo o Video
########################################################################
#
while(Video.isOpened()):
  Status, VideoFrame = Video.read()
  if Status == True:

# 
########################################################################
# Reduzindo o Tamanho da Imagem
########################################################################
#
    imgPeixe = cv.resize(VideoFrame, (640, 480))

# 
########################################################################
# Removendo Possíveis Ruídos
########################################################################
#
    imgPeixeCinza = cv.cvtColor(imgPeixe, cv.COLOR_BGR2GRAY)
    imgPeixeCinza = cv.GaussianBlur(imgPeixeCinza, (9, 9), 0)

# 
########################################################################
# Aplicando o Subtrador 
########################################################################
#
    imgPeixeMascara = subPeixe.apply(imgPeixeCinza) 

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
    imgTmpMascara = cv.cvtColor(imgPeixeMascara,cv.COLOR_GRAY2RGB)    
    imgTmpPeixeCinza = cv.cvtColor(imgPeixeCinza,cv.COLOR_GRAY2RGB)        
    imgTodasImagens = np.hstack(( imgPeixe, imgTmpPeixeCinza, imgTmpMascara ))   
    
    cv.imshow ( "Video Peixe", imgTodasImagens)  
    if cv.waitKey(25) & 0xFF == ord('q'):
      break
 
  else: 
    break
  
# 
########################################################################
# Fechando o Vídeo e Janelamento
########################################################################
#  
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################

exit()

# 
########################################################################
# Compatibilizando o Tamanho das Imagens
########################################################################
#
imgPeixe = cv.resize(imgFrente, (640, 480))
imgFundo  = cv.resize(imgFundo, (640, 480))

# 
########################################################################
# Apresentando o Resultado Parcial
########################################################################
#
cv.imshow ( "Imagem Frente", imgFrente)
cv.imshow ( "Imagem Fundo", imgFundo)

# 
########################################################################
# Segmentando a Imagem
########################################################################
#
imgSegmentada = mp.solutions.selfie_segmentation
imgSegmento = imgSegmentada.SelfieSegmentation(model_selection = 1)

# 
########################################################################
# Criando a Máscara
########################################################################
#
imgFrente = cv.cvtColor(imgFrente, cv.COLOR_BGR2RGB)
imgResultado = imgSegmento.process(imgFrente)
imgFrente = cv.cvtColor(imgFrente, cv.COLOR_RGB2BGR)
imgSegmentoMascara = imgResultado.segmentation_mask

# 
########################################################################
# Executando a União das Imagens
########################################################################
#
Limiar = 0.6
imgMascaraBinaria = imgSegmentoMascara > Limiar
imgMascara3d = np.dstack((imgMascaraBinaria, imgMascaraBinaria, imgMascaraBinaria))
imgResultadoFinal = np.where(imgMascara3d, imgFrente, imgFundo)

# 
########################################################################
# Apresentando o Resultado Final
########################################################################
#
cv.imshow ( "Resultado Final", imgResultadoFinal)
cv.waitKey(0)
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
