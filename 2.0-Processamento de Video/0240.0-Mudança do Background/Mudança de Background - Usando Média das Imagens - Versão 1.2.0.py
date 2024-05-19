# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv

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
notify_num = 200 # up to how many frames to take background average.
frame_count=0 # a variable to count current frame

aweight = 0.5 # variable used to take average
bg = None # background image
take_bg=True # 

fsize = (520, 720)
scene = cv.imread ( CaminhoImagem + NomeImagem, cv.IMREAD_COLOR)
scene = cv.resize(scene, (fsize[1], fsize[0])) # resize scene to the size of frame

left,top,right,bottom=(400, 20, 630, 300)


while True: # loop until termination
    ret, frame = Video.read() # read frame
    frame= cv.flip(frame, 1) # flip the frame to make frame like mirror image
    frame = cv.resize(frame, (fsize[1], fsize[0]))
    
    clone = frame.copy() # make a local copy of frame

    gray = cv.cvtColor(clone, cv.COLOR_BGR2GRAY) # convert frame to grayscale
    gray = cv.medianBlur(gray, 5) # add some median blur to remove Salt and Pepper noise
    
    
    key = cv.waitKey(1) & 0xFF # listen for the key event
    
    roi = gray[top:bottom, left:right]
    
    roi = cv.resize(roi, (fsize[1], fsize[0]))
    
    if key == 27: # if hit escape key
        break # break out of the loop
        
    
    if take_bg == True and notify_num>frame_count: # condition to take a background average
        txt = f"Taking background, Hold Still: {str(notify_num-frame_count)}"
        
        cv.putText(clone, txt, (10, 50),
                                           cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv.rectangle(clone, (left, top), (right, bottom), (0, 0, 255), 1)
        bg=running_average(bg, roi, aweight) # call the running average function to get the average on each frame
    else:
        take_bg= False # don't take background average now!
        frame_count=0 # set frame count to 0
        
        diff = cv.absdiff(bg.astype("uint8"), gray) # get the absolute difference of background image and current image
        diff[diff<40]=0 # threshold it little bit
        cv.imshow("diff", diff.astype("uint8"))
        f = clone.copy() # again make a loval copy 
        f[diff==0] = scene[diff==0] # image masking !!!!!
        cv.imshow("Subtraction", f) # show the background subtracted image.
        

        
    frame_count+=1
    cv.imshow("Output", clone)
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
