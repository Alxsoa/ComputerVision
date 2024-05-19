# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2 as cv

# 
########################################################################
# Funções Gerais
########################################################################
#
def midpoint(ptA, ptB):
	return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela  = "Deteccao de Objetos"
NomeImagem  = "MedindoObjeto-3.png"
CaminhoBase = "/home/asoares/OpenCV/"
CaminhoImagem = CaminhoBase + "Imagens/" 
Tamanho = 3.5

# 
########################################################################
# Lendo a Imagem e Transformando para Cinza e Executando o Blur
########################################################################
#
image = cv.imread(CaminhoImagem+NomeImagem)
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (7, 7), 0)

# 
########################################################################
# Executa a Detecção de Borda e Executa uma dilatação + erosão 
# para Fechar as Lacunas Entre as Bordas do Objeto
########################################################################
#
edged = cv.Canny(gray, 50, 100)
edged = cv.dilate(edged, None, iterations=1)
edged = cv.erode(edged, None, iterations=1)

# 
########################################################################
# Busca os Contornos
########################################################################
#
cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

# 
########################################################################
# Classifica os Contornos da Esquerda para a Direita e Inicializa a 
# Variável de Calibração 'pixels por métrica'
########################################################################
#
(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None

# 
########################################################################
# Loop para Identificar Individualmente os Contornos
########################################################################
#
for c in cnts:
# 
########################################################################
# Caso o Contorno não for Suficientemente Grande, ignora
########################################################################
#	
	if cv.contourArea(c) < 100:
		continue

# 
########################################################################
# Calcula a Caixa Delimitadora Girada do Contorno
########################################################################
#	
	orig = image.copy()
	box = cv.minAreaRect(c)
	box = cv.cv.BoxPoints(box) if imutils.is_cv2() else cv.boxPoints(box)
	box = np.array(box, dtype="int")

# 
########################################################################
# Ordenação dos Pontos no Contorno de Modo que Apareçam na Ordem 
# Superior Esquerda, Superior Direita, Inferior Direita e 
# Inferior Esquerda e, em Seguida, Desenha o Contorno da 
# Caixa Delimitadora Girada
########################################################################
#	
	box = perspective.order_points(box)
	cv.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

# 
########################################################################
# Loop sobre os Pontos Originais para Desenho
########################################################################
#
	for (x, y) in box:
		cv.circle(orig, (int(x), int(y)), 5, (0, 0, 255), -1)

# 
########################################################################
# Descompacte a Caixa Delimitadora Ordenada e Calcule o Ponto Médio 
# Entre as Coordenadas Superior Esquerda e Superior Direita, Seguido 
# pelo Ponto Médio entre as Coordenadas Inferior Esquerda e 
# Inferior Direita
########################################################################
#
	(tl, tr, br, bl) = box
	(tltrX, tltrY) = midpoint(tl, tr)
	(blbrX, blbrY) = midpoint(bl, br)

# 
########################################################################
# Calcula o Ponto Médio Entre os Pontos Superior Esquerdo e 
# Superior Direito
########################################################################
#
	(tlblX, tlblY) = midpoint(tl, bl)
	(trbrX, trbrY) = midpoint(tr, br)

# 
########################################################################
# Desenha um Círculos nos Pontos Médios
########################################################################
#
	cv.circle(orig, (int(tltrX), int(tltrY)), 5, (255, 0, 0), -1)
	cv.circle(orig, (int(blbrX), int(blbrY)), 5, (255, 0, 0), -1)
	cv.circle(orig, (int(tlblX), int(tlblY)), 5, (255, 0, 0), -1)
	cv.circle(orig, (int(trbrX), int(trbrY)), 5, (255, 0, 0), -1)

# 
########################################################################
# Desenha uma Linha entre os Pontos Médios
########################################################################
#
	cv.line(orig, (int(tltrX), int(tltrY)), (int(blbrX), int(blbrY)), (255, 0, 255), 2)
	cv.line(orig, (int(tlblX), int(tlblY)), (int(trbrX), int(trbrY)), (255, 0, 255), 2)

# 
########################################################################
# Calcula a Distancia Euclidiana entre os Pontos Médios
########################################################################
#
	dA = dist.euclidean((tltrX, tltrY), (blbrX, blbrY))
	dB = dist.euclidean((tlblX, tlblY), (trbrX, trbrY))

# 
########################################################################
# Se os Pixels por Métrica não Tiverem sido Inicializados, 
# calcule-os como a Proporção de Pixels para a Métrica Fornecida 
# (neste caso, polegadas)
########################################################################
#
	if pixelsPerMetric is None:
		pixelsPerMetric = dB / Tamanho

# 
########################################################################
# Calcula o Tamanho do Objeto
########################################################################
#
	dimA = dA / pixelsPerMetric
	dimB = dB / pixelsPerMetric

# 
########################################################################
# Desenha os Tamanhos dos Objetos Presentes na Imagem
########################################################################
#
	cv.putText(orig, "{:.1f}in".format(dimA), (int(tltrX - 15), int(tltrY - 10)), cv.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
	cv.putText(orig, "{:.1f}in".format(dimB), (int(trbrX + 10), int(trbrY)), cv.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)

# 
########################################################################
# Apresenta os Resultados
########################################################################
#
	cv.imshow ( "JanelaBase", orig)
	cv.setWindowTitle("JanelaBase", NomeJanela )	
	cv.waitKey(0)

########################################################################
# FIM DO PROGRAMA
########################################################################