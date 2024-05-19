# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import mediapipe as mp


# 
########################################################################
# Definições Gerais
########################################################################
#
ClearCmd = "clear"  # Em Ambiente Windows deve ser usado cls
DirBase = "LocalCV/"
NomeJanela = "Video Base"
NomeImagem = "Cena.jpg"
CaminhoBase = "/home/asoares/" + DirBase
NomeJanela = "Leitura de Vídeo"
NomeVideo = "PessoaSentada.mp4"
CaminhoVideo= CaminhoBase + "Videos/"
CaminhoImagem = CaminhoBase + "Imagens/" 

mp_selfie_segmentation = mp.solutions.selfie_segmentation
cam = cv.VideoCapture(0)

fsize = (520, 720)
scene = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
scene = cv.resize(scene, (fsize[1], fsize[0])) # resize scene to the size of frame


# begin with selfie segmentation model
with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_seg:
    bg_image = scene
    
    while cam.isOpened():
        ret, frame = cam.read()
        if not ret:
            print("Error reading frame...")
            continue
        frame = cv.resize(frame, (fsize[1], fsize[0]))
        
        # flip it to look like selfie camera
        frame = cv.flip(frame, 1)
        
        
        # get rgb image to pass that on selfie segmentation
        rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        
        # process it!
        results = selfie_seg.process(rgb) 
        
        # get the condition from result's segmentation mask
        condition = np.stack((results.segmentation_mask, ) * 3, axis=-1) > 0.1
        
        # apply background change if condition matches
        output_image = np.where(condition, frame, bg_image)

        # show the output
        cv.imshow('Background Change with MP', output_image)
        if cv.waitKey(5) & 0xFF == 27:
            break
cam.release()
cv.destroyAllWindows()