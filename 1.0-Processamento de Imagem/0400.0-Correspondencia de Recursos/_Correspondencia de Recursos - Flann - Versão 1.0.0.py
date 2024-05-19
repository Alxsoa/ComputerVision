# Referencia
# https://blog.francium.tech/feature-detection-and-matching-with-opencv-5fd2394a590

# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

# 
########################################################################
# Funções de Apoio
########################################################################
#
def IdentificaCorrelacao (img1, img2):
    MIN_MATCHES = 50

    orb = cv.ORB_create(nfeatures=500)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    index_params = dict (
                            algorithm=6,
                            table_number=6,
                            key_size=12,
                            multi_probe_level=2
                        )
    
    search_params = {}
    flann = cv.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # As per Lowe's ratio test to filter good matches
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    if len(good_matches) > MIN_MATCHES:
        src_points = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_points = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        m, mask = cv.findHomography(src_points, dst_points, cv.RANSAC, 5.0)
        corrected_img = cv.warpPerspective(img1, m, (img2.shape[1], img2.shape[0]))

        return corrected_img
    return img2

# 
########################################################################
# Definições Gerais
########################################################################
#
BaseDir = "LocalCV/"
NomeImagemBase = "LivroFrontalTesla.jpg"
NomeImagemComparada = "LivroInclinadoTesla.jpg"
CaminhoBase = "/home/asoares/" + BaseDir
CaminhoImagem = CaminhoBase + "Imagens/" 

# 
########################################################################
# Lendo e Reduzindo a Imagem
########################################################################
#
ImagemBase = cv.imread ( CaminhoImagem + NomeImagemBase, cv.IMREAD_COLOR )
ImagemComparada = cv.imread ( CaminhoImagem + NomeImagemComparada, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if ImagemBase is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagemBase)
    exit ()

if ImagemComparada is None:
    os.system ("clear")
    print( "Não Foi Localizada a Imagem : ", NomeImagemComparada)
    exit ()

# 
########################################################################
# Executa a Correlação
########################################################################
#
imgResultado = IdentificaCorrelacao (ImagemComparada, ImagemBase)

# 
########################################################################
# Convertendo para Matplotlib
########################################################################
#
ImagemBase = cv.cvtColor(ImagemBase, cv.COLOR_BGR2RGB)
imgResultado = cv.cvtColor(imgResultado, cv.COLOR_BGR2RGB)

# 
########################################################################
# Apresenta os Resultados
########################################################################
#

Grafico = plt.figure(figsize=(10,8))

Grafico.add_subplot(1,2,1)
plt.imshow (ImagemBase )
plt.title ("Imagem Original", fontsize=11, weight='bold' )

Grafico.add_subplot(1,2,2)
plt.imshow (imgResultado )
plt.title ("Imagem Resultado", fontsize=11, weight='bold' )

plt.subplots_adjust ( left   = 0.1,
                      bottom = 0.1,
                      right  = 0.9,
                      top    = 0.9,
                      wspace = 0.1,
                      hspace = 0.1 )
plt.show ()
	
########################################################################
# FIM DO PROGRAMA
########################################################################	
