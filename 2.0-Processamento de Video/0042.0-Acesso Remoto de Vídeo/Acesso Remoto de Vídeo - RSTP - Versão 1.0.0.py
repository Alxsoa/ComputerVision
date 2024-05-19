# Referencia
# https://lindevs.com/capture-rtsp-stream-from-ip-camera-using-opencv
# https://docs.videolan.me/vlc-user/3.0/en/advanced/streaming/rtsp_session.html
# https://www.appsloveworld.com/opencv/100/46/rtsp-stream-doesnt-work-on-python-but-does-on-vlc-why
# Lado server
# vlc FogosArtificio.mp4 --sout="#rtp{sdp=rtsp://192.168.15.26:8090/stream}"
#

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv 
import os

# 
########################################################################
# Abrindo a WebCam e Checando o Acesso
########################################################################
# 
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"
CapturaVideo = cv.VideoCapture ("rtsp://192.168.15.26:8090/stream")

# 
########################################################################
# Processo de Captura de Vídeo
########################################################################
# 

while (True):

    Status, VideoFrame = CapturaVideo.read()
    if Status == True:
        VideoFrame = cv.resize(VideoFrame, (640, 480), interpolation = cv.INTER_AREA)
        cv.imshow( "Caputa de Video", VideoFrame)
        if cv.waitKey(1) == 27:
            break

# 
########################################################################
# Fechando o Janelamento e Camera
########################################################################
# 
cv.destroyAllWindows()
CapturaVideo.release()

########################################################################
# FIM DO PROGRAMA
########################################################################
