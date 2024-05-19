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
Video = cv.VideoCapture(0)
fsize = (520, 720)
scene = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
scene = cv.resize(scene, (fsize[1], fsize[0])) # resize scene to the size of frame

while True: # loop until termination
    ret, frame = Video.read() # read frame
    frame= cv.flip(frame, 1) # flip the frame to make frame like mirror image
    frame = cv.resize(frame, (fsize[1], fsize[0]))
    
    clone = frame.copy() # make a local copy of frame

    gray = cv.cvtColor(clone, cv.COLOR_BGR2GRAY) # convert frame to grayscale
    gray = cv.medianBlur(gray, 9) # add some median blur to remove Salt and Pepper noise
    
    
    key = cv.waitKey(1) & 0xFF # listen for the key event
    
    
    if key == 27: # if hit escape key
        break # break out of the loop
        
    
    kernel = np.ones((7, 7))
    th = cv.threshold(gray, 40, 255, cv.THRESH_OTSU)[1]        
    th = cv.dilate(th, kernel, iterations=1)
    th = cv.erode(th, kernel, iterations=5)
    
    f = clone.copy()
    
    f[th!=0] = scene[th!=0]
    cv.imshow("Thresh Result", f)
    
    edges = cv.Canny(gray, 10, 50)
    kernel = np.ones((3, 3))
    edges = cv.dilate(edges, kernel, iterations=5)
#     edges = cv.erode(edges, kernel, iterations=7)
    cv.imshow("Canny", edges)
    
    (cnts, _) = cv.findContours(edges.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    dm = np.zeros_like(edges)    
    if len(cnts)>0:
        mcnt = max(cnts[:], key=cv.contourArea)
        dm=cv.fillConvexPoly(dm, mcnt, (255))
        cv.imshow("DM", dm)
    c = frame.copy()
    c[dm!=255]=scene[dm!=255]
    cv.imshow("Canny Result", c)
    
Video.release()
cv.destroyAllWindows()
