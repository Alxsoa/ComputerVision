# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Funções de Apoio
########################################################################
#
def running_average(bg_img, image, aweight):
    if bg_img is None:
        bg_img = image.copy().astype("float")
    else:
        cv.accumulateWeighted(image, bg_img, aweight)    
    return bg_img

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

# read camera feed
cam = cv.VideoCapture(0)
mog = cv.createBackgroundSubtractorMOG2()

fsize = (520, 720)
scene = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
scene = cv.resize(scene, (fsize[1], fsize[0])) # resize scene to the size of frame


while True:
    ret, frame = cam.read()
    if ret:
        frame = cv.flip(frame, 1)
        frame = cv.resize(frame, (fsize[1], fsize[0]))
        fmask = mog.apply(frame, 0.5)
        
        
        kernel = np.ones((3, 3))  
        fmask = cv.dilate(fmask, kernel, iterations=1)
#         fmask = cv2.erode(fmask, kernel, iterations=1)
        
        cv.imshow("mog", fmask)
        
        key = cv.waitKey(1) & 0xFF 
    
    
        if key == 27: # if hit escape key
            break # break out of the loop
            
        frame[fmask==0] = scene[fmask==0]
        
        cv.imshow("Frame", frame)
    
cam.release()
cv.destroyAllWindows()
