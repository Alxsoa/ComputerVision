# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Exemplo de Animação"
NomePadrao  = "haarcascade_frontalcatface.xml"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoPadrao= CaminhoBase + "Padroes/" 

# 
########################################################################
# Lendo o Padrão de Reconhecimento
########################################################################
#
face_cascade = cv.CascadeClassifier(CaminhoPadrao+NomePadrao)

# 
########################################################################
# Inicia a Web Camera
########################################################################
#
Video = cv.VideoCapture(0)
if (Video.isOpened()== False): 
    print ("########################################################################")
    print ("# Video Não Encontrado ")
    print ("########################################################################")
    exit ()

# 
########################################################################
# Loop de Busca do Padrão
########################################################################
#
while True:

	Status, VideoFrame = Video.read()
	VideoCinza = cv.cvtColor(VideoFrame, cv.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(VideoCinza, 1.3, 5)

	for (x,y,w,h) in faces:
		cv.rectangle(VideoFrame,(x,y),(x+w,y+h),(255,255,0),2)
		roi_gray = VideoCinza[y:y+h, x:x+w]
		roi_color = VideoFrame[y:y+h, x:x+w]

	cv.imshow('Reconhecimento Padrao',VideoFrame)
	k = cv.waitKey(30) & 0xff
	if k == 27:
		break

# 
########################################################################
# Fecha a Camera Web e Destroi o Janelamento
########################################################################
#
Video.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
