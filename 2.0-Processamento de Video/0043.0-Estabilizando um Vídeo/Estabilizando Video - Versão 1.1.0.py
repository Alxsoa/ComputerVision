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

# 
########################################################################
# Calcula a Média Móvel de uma Curva Usando um Determinado Raio
########################################################################
#
def CalculaMovimentoMedio(curve, Raio):
    TamanhoJanela = 2 * Raio + 1
    Kernel = np.ones(TamanhoJanela) / TamanhoJanela
    CurvaPreenchida = np.lib.pad(curve, (Raio, Raio), 'edge')
    CurvaSuavizada = np.convolve(CurvaPreenchida, Kernel, mode='same')
    CurvaSuavizada = CurvaSuavizada[Raio:-Raio]
    return (CurvaSuavizada)

# 
########################################################################
# Suavize a Trajetória Usando a Média Móvel em Cada Dimensão
########################################################################
#
def SuavizandoTrajetoria(iTrajetoria):
    TrajetoriaSuave = np.copy(iTrajetoria)

    for iAux in range(3):
        TrajetoriaSuave[:, iAux] = CalculaMovimentoMedio    (
                                                                iTrajetoria[:, iAux],
                                                                Raio=RAIO_DE_SUAVIZACAO
                                                            )

    return (TrajetoriaSuave)

# 
########################################################################
# Corrije a Borda do Quadro Aplicando Rotação e Transformação da Escala
########################################################################
#
def ResolveBorda(VideoFrame):
    iDimensaoFrame = VideoFrame.shape    
    iMatriz = cv.getRotationMatrix2D    (
                                            (iDimensaoFrame[1] / 2, iDimensaoFrame[0] / 2),
                                            0,
                                            1.04
                                        )

    VideoFrame = cv.warpAffine(VideoFrame, iMatriz, (iDimensaoFrame[1], iDimensaoFrame[0]))
    return (VideoFrame)

# 
########################################################################
# Definições Gerais
########################################################################
#
Codec = cv.VideoWriter_fourcc(*'mp4v')
NomeVideoOUT = "PianistaNaoEstabilizadoOUT.mp4"
NomeVideo = "PianistaNaoEstabilizado.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirVideo = "Videos"  

dirVideoIN = str(Path(dirRaiz, dirBase, dirVideo, NomeVideo))
dirVideoOut = str(Path(dirRaiz, dirBase, dirVideo, NomeVideoOUT))

# Suavização da Trajetória
RAIO_DE_SUAVIZACAO = 50

# 
########################################################################
# Lendo o Video
########################################################################
#
CapturaVideo = cv.VideoCapture (dirVideoIN)
if (CapturaVideo.isOpened()== False): 
    LimpaTerminal ()
    print( "Não Foi Localizado o Video : ", NomeVideo)
    exit ()

# 
########################################################################
# Recuperando as Propriedades do Vídeo 
########################################################################
#
iNumeroFrames = int(CapturaVideo.get(cv.CAP_PROP_FRAME_COUNT))
iLargura = int(CapturaVideo.get(cv.CAP_PROP_FRAME_WIDTH))
iAltura = int(CapturaVideo.get(cv.CAP_PROP_FRAME_HEIGHT))
iFPS = CapturaVideo.get(cv.CAP_PROP_FPS)

# 
########################################################################
# Criando o Arquivo de Resultado e Lendo o Primeiro Frame
########################################################################
#
VideoOut = cv.VideoWriter(dirVideoOut, Codec, iFPS, (2 * iLargura, iAltura))
_, FrameAnterior = CapturaVideo.read()
FrameAnteriorCinza = cv.cvtColor(FrameAnterior, cv.COLOR_BGR2GRAY)

# 
########################################################################
# Inicializa o Vetor de Transformacao e Calcula a Trans, para Cada Frame
########################################################################
#
Transformacao = np.zeros((iNumeroFrames - 1, 3), np.float32)
for iAux in range(iNumeroFrames - 2):
    # Calcula o optical flow Entre os Frames Consecutivos
    ptsAnterior = cv.goodFeaturesToTrack    (
                                                FrameAnteriorCinza,
                                                maxCorners=200,
                                                qualityLevel=0.01,
                                                minDistance=30,
                                                blockSize=3
                                            )

    Status, VideoFrameAtual = CapturaVideo.read()
    if (not Status):
        break

    FrameAtualCinza = cv.cvtColor(VideoFrameAtual, cv.COLOR_BGR2GRAY) 
    ptsAtual, status, err = cv.calcOpticalFlowPyrLK     (
                                                            FrameAnteriorCinza,
                                                            FrameAtualCinza,
                                                            ptsAnterior,
                                                            None
                                                        )
    
    assert ptsAnterior.shape == ptsAtual.shape
    iIndice = np.where(status == 1)[0]
    ptsAnterior = ptsAnterior[iIndice]
    ptsAtual = ptsAtual[iIndice]

    # Estimo a Transformacao affine Entre os Pontos 
    iMatriz, _ = cv.estimateAffine2D(ptsAnterior, ptsAtual)
    iTranslacaoX = iMatriz[0, 2]
    iTranslacaoY = iMatriz[1, 2]
    AnguloRotacao = np.arctan2(iMatriz[1, 0], iMatriz[0, 0])
    Transformacao[iAux] = [iTranslacaoX, iTranslacaoY, AnguloRotacao]
    FrameAnteriorCinza = FrameAtualCinza

# Calculo a Trajetoria Pela Acumulação das Transformações 
iTrajetoria = np.cumsum(Transformacao, axis=0)

# Suaviza a Trajetória Pela Média do Movimento 
TrajetoriaSuave = SuavizandoTrajetoria(iTrajetoria)

# Calcula a Diferença entre o Original e o Suavizado 
iDiferenca = TrajetoriaSuave - iTrajetoria

# Adiciona a Diferença às Transformações Originais para Obter Transformações Suaves
TransformacaoSuave = Transformacao + iDiferenca

# 
########################################################################
# Volta ao Frame Inicial e Processa cada Frame e Estabiliza o Vídeo
########################################################################
#
CapturaVideo.set(cv.CAP_PROP_POS_FRAMES, 0)
for iAux in range(iNumeroFrames - 2):
    Status, VideoFrame = CapturaVideo.read()
    if not Status:
        break

    iTranslacaoX = TransformacaoSuave[iAux, 0]
    iTranslacaoY = TransformacaoSuave[iAux, 1]
    AnguloRotacao = TransformacaoSuave[iAux, 2]

    # Crie a Matriz de Transformação para Estabilização 
    MatrizTransformacao = np.zeros((2, 3), np.float32)
    MatrizTransformacao[0, 0] = np.cos(AnguloRotacao)
    MatrizTransformacao[0, 1] = -np.sin(AnguloRotacao)
    MatrizTransformacao[1, 0] = np.sin(AnguloRotacao)
    MatrizTransformacao[1, 1] = np.cos(AnguloRotacao)
    MatrizTransformacao[0, 2] = iTranslacaoX
    MatrizTransformacao[1, 2] = iTranslacaoY

    # Aplica a Transformação para Estabilizar o Quadro 
    FrameEstabilizado = cv.warpAffine   (
                                            VideoFrame,
                                            MatrizTransformacao,
                                            (iLargura, iAltura)
                                        )

    # Resolve a Borda do Quadro Estabilizado
    FrameEstabilizado = ResolveBorda(FrameEstabilizado)

    # Concatenate the original and stabilized frames side by side
    FrameResultado = cv.hconcat([VideoFrame, FrameEstabilizado])

    # Redefine o Tamanho do Quadro Caso Maior de 1920 pixels 
    if FrameResultado.shape[1] > 1920:
        FrameResultado = cv.resize  (
                                        FrameResultado,
                                        (FrameResultado.shape[1] // 2, FrameResultado.shape[0] // 2)
                                    )

# 
########################################################################
# Apresenta o Resultado e Grava o Arquivo de Saída
########################################################################
# 
    cv.imshow("Transformacao do Video", FrameResultado)
    cv.waitKey(10)
    VideoOut.write(FrameResultado)

# 
########################################################################
# Fechando o Arquivo de Vídeo e Desmontando o Janelamento
########################################################################
# 
CapturaVideo.release()
VideoOut.release()
cv.destroyAllWindows()

########################################################################
# FIM DO PROGRAMA
########################################################################
