
# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import os

# 
########################################################################
# Funções de Apoio
########################################################################
#
def SelecionaMonitor ( TipoMonitor ):
# 
########################################################################
# Recupera a Versão Instalado do OpenCV
########################################################################
#
    (Versao, Atualizacao, Subversao) = (cv.__version__).split('.')

# 
########################################################################
# Define o Monitor Padrão
########################################################################
#
    if int(Atualizacao) < 3:
        Monitor = cv.Tracker_create('KCF')
        Descricao = "KCF"
    else:
        if TipoMonitor == 0:
            Monitor = cv.TrackerBoosting_create()
            Descricao = "Boosting"
        elif TipoMonitor == 1:
             Monitor = cv.TrackerMIL_create()
             Descricao = "MIL"
        elif TipoMonitor == 2:
             Monitor = cv.TrackerKCF_create()
             Descricao = "KCF"
        elif TipoMonitor == 3:
             Monitor = cv.TrackerMedianFlow_create()
             Descricao = "MedianFlow"
        elif TipoMonitor == 4:
             Monitor = cv.TrackerGOTURN_create()
             Descricao = "GOTURN"
        elif TipoMonitor == 5:
             Monitor = cv.TrackerCSRT_create()  
             Descricao = "CSRT"                                                         
        else: 
            Monitor = -1
            Descricao = "Sem Descricao"

    return (Monitor, Descricao)

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeVideo = "MovimentoPessoas.mp4"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoVideo = CaminhoBase + "Videos/" 


# 
########################################################################
# Checando se o Vídeo Está Disponível
########################################################################
#
video = cv.VideoCapture( CaminhoVideo + NomeVideo )
if not video.isOpened():
    os.system ("clear")
    print( "Não Foi Localizado o Vídeo: ", NomeVideo)
    exit ()

# 
########################################################################
# Leitura do Primeiro Frame
########################################################################
#
Status, VideoFrame = video.read()
if not Status:
    os.system ("clear")
    print( "Não Foi Possível Ler o Primeiro VideoFrame do Vídeo : ", NomeVideo)
    exit ()
# 
########################################################################
# Seleciona o Tipo de Monitor
########################################################################
#
Monitor, Descricao = SelecionaMonitor ( 1 )

# 
########################################################################
# Redução do Tamanho do Primeiro Frame
########################################################################
#
VideoFrame = cv.resize(VideoFrame, (0,0), fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)

# 
########################################################################
# Seleção da Região de Interesse e Inicialização do Tracker
########################################################################
#
Seletor = cv.selectROI(VideoFrame, False,  printNotice=False)
TrackerStatus = Monitor.init(VideoFrame, Seletor)

# 
########################################################################
# Lendo o Vídeo
########################################################################
#
while (True):
    Status, VideoFrame = video.read()
    if not Status:
        break

    VideoFrame = cv.resize(VideoFrame, (0,0), fx=0.5, fy=0.5, interpolation = cv.INTER_AREA)

# 
########################################################################
# Iniciando o Timer, Atualizando o Tracker e Calculando o FPS
########################################################################
#    
    timer = cv.getTickCount()
    TrackerStatus, Seletor = Monitor.update(VideoFrame)
    fps = cv.getTickFrequency() / (cv.getTickCount() - timer);

# 
########################################################################
# Desenhando a Região de Interesse
########################################################################
#   
    if TrackerStatus:
        ptsInicial = (int(Seletor[0]), int(Seletor[1]))
        ptsFinal = (int(Seletor[0] + Seletor[2]), int(Seletor[1] + Seletor[3]))
        cv.rectangle(VideoFrame, ptsInicial, ptsFinal, (255,0,0), 2, 1)
    else :
        cv.putText(VideoFrame, "Falhou o Monitoramento de Objeto", (100,80), cv.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

# 
########################################################################
# Dados do Monitoramento do Vídeo
########################################################################
#
    cv.putText(VideoFrame, Descricao + " Tracker Selecionado", (100,20), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    cv.putText(VideoFrame, "FPS : " + str(int(fps)), (100,50), cv.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

# 
########################################################################
# Apresentando o Vídeo
########################################################################
#
    cv.imshow("Monitoracao", VideoFrame)
    k = cv.waitKey(1) & 0xff
    if k == 27 : break


########################################################################
# FIM DO PROGRAMA
########################################################################