# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
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

def extrairMaiorCtn(imgBase):
    imgBaseCinza = cv.cvtColor(imgBase, cv.COLOR_BGR2GRAY)
    imgLimiar = cv.adaptiveThreshold(imgBaseCinza, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 12)

    Kernel = np.ones((2,2), np.uint8)
    imgDilatada = cv.dilate(imgLimiar,Kernel)
    iContornos, iHierarquia = cv.findContours(imgDilatada,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

    iMariorContorno = max(iContornos, key = cv.contourArea)

    xPos,yPos,iLargura,iAltura = cv.boundingRect(iMariorContorno)
    matBox = [xPos,yPos,iLargura,iAltura]

    imgRecorte = imgBase[yPos:yPos+iAltura,xPos:xPos+iLargura]
    imgRecorte = cv.resize(imgRecorte,(400,500))

    return (imgRecorte,xPos,yPos,iLargura,iAltura)

# 
########################################################################
# Definições Gerais
########################################################################
#
Codec = cv.VideoWriter_fourcc('m','p','4','v')
VideoOutName = "VerificacaoGabaritoOUT.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirImagem = "Videos"  
dirVideoOut = str(Path(dirRaiz, dirBase, dirImagem, VideoOutName))
WebCam = 2

campos = [
            ( 12,   2, 92, 85), 
            (105,   2, 92, 85), 
            (196,   2, 92, 85), 
            (289,   2, 92, 85), 
            ( 12,  95, 92, 85), 
            (105,  95, 92, 85), 
            (196,  95, 92, 85), 
            (289,  95, 92, 85), 
            ( 12, 187, 92, 85), 
            (105, 187, 92, 85), 
            (196, 187, 92, 85), 
            (289, 187, 92, 85), 
            ( 12, 285, 92, 85), 
            (105, 285, 92, 85), 
            (196, 285, 92, 85), 
            (289, 285, 92, 85), 
            ( 12, 382, 92, 85), 
            (105, 382, 92, 85), 
            (196, 382, 92, 85), 
            (289, 382, 92, 85)
         ]

resp =   [
            '1-A', '1-B', '1-C', '1-D', 
            '2-A', '2-B', '2-C', '2-D', 
            '3-A', '3-B', '3-C', '3-D', 
            '4-A', '4-B', '4-C', '4-D', 
            '5-A', '5-B', '5-C', '5-D'
         ]

respostasCorretas = ["1-A","2-C","3-B","4-D","5-A"]

# 
########################################################################
# Lendo e Checando a Disponibilidade do Vídeo 
########################################################################
#
Video = cv.VideoCapture(WebCam)
if (Video.isOpened()== False): 
    LimpaTerminal ()
    print( "Não Foi Localizado a Camera Designada ")
    exit ()

# 
########################################################################
# Processando o Frame de Vídeo
########################################################################
#
lstFrameVideo = []
while (Video.isOpened()):
   Status, VideoFrame = Video.read()
   if Status == True:
      gabarito, xPos, yPos, iLargura, iAltura = extrairMaiorCtn(VideoFrame)
      imgVideoFrameCinza = cv.cvtColor(gabarito, cv.COLOR_BGR2GRAY)
      ret,imgLimiar = cv.threshold (imgVideoFrameCinza,70,255,cv.THRESH_BINARY_INV)

      cv.rectangle(VideoFrame, (xPos, yPos), (xPos + iLargura, yPos+iAltura), (0, 255,0), 3)
      respostas = []
      for id,vg in enumerate(campos):
         x = int(vg[0])
         y = int(vg[1])
         w = int(vg[2])
         h = int(vg[3])
         cv.rectangle(gabarito, (x, y), (x + w, y + h),(0,0,255),2)
         cv.rectangle(imgLimiar, (x, y), (x + w, y + h), (255, 255, 255), 1)
         campo = imgLimiar[y:y + h, x:x + w]
         height, width = campo.shape[:2]
         tamanho = height * width

         pretos = cv.countNonZero(campo)
         percentual = round((pretos / tamanho) * 100, 2)
         if percentual >=15:
               cv.rectangle(gabarito, (x, y), (x + w, y + h), (255, 0, 0), 2)
               respostas.append(resp[id])

      #print(respostas)
      erros = 0
      acertos = 0
      if len(respostas)==len(respostasCorretas):
         for num,res in enumerate(respostas):
               if res == respostasCorretas[num]:
                  #print(f'{res} Verdadeiro, correto: {respostasCorretas[num]}')
                  acertos +=1
               else:
                  #print(f'{res} Falso, correto: {respostasCorretas[num]}')
                  erros +=1

         pontuacao = int(acertos *6)
         cv.putText(VideoFrame,f'ACERTOS: {acertos}, PONTOS: {pontuacao}',(30,140),cv.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),3)

      #VideoFrameOUT = cv.resize(VideoFrame, (700, 400) ) 
      #lstFrameVideo.append(VideoFrameOUT)
   
      cv.imshow('img',VideoFrame)
      cv.imshow('Gabarito', gabarito)
      cv.imshow('IMG TH', imgLimiar)
      cv.waitKey(1)

# 
########################################################################
# Criando o Arquivo de Vídeo
########################################################################
#
#VideoOut = cv.VideoWriter ( dirVideoOut, 
#                            Codec,                            
#                            25, 
#                            (700, 400))

# 
########################################################################
# Criação do Vídeo
########################################################################
#  
#for iAux in range (0, len(lstFrameVideo)):
#    VideoOut.write(lstFrameVideo[iAux])  

# 
########################################################################
# Fechando o Arquivo de Vídeo  
########################################################################
# 
Video.release()
#VideoOut.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
