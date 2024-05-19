# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import cv2 as cv
import numpy as np

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeJanela = "Exemplos de Fontes"
Escala = 1.0
Cor = (0, 0, 0)

# 
########################################################################
# Criando a Imagem
########################################################################
#
Imagem = np.zeros((640, 720, 3), np.uint8)
Imagem.fill(255)

# 
########################################################################
# Inserindo o Texto em Diferentes Fontes
########################################################################
#
FonteSelecionada = cv.FONT_HERSHEY_COMPLEX
cv.putText(Imagem, "FONT_HERSHEY_COMPLEX", (25, 40), FonteSelecionada, Escala, Cor)

FonteSelecionada = cv.FONT_HERSHEY_COMPLEX_SMALL
cv.putText(Imagem, "FONT_HERSHEY_COMPLEX_SMALL", (25, 80), FonteSelecionada, Escala, Cor)

FonteSelecionada = cv.FONT_HERSHEY_DUPLEX
cv.putText(Imagem, "FONT_HERSHEY_DUPLEX", (25, 120), FonteSelecionada, Escala, Cor)

FonteSelecionada = cv.FONT_HERSHEY_PLAIN
cv.putText(Imagem, "FONT_HERSHEY_PLAIN", (25, 160), FonteSelecionada, Escala, Cor)
FonteSelecionada = cv.FONT_HERSHEY_SCRIPT_COMPLEX

cv.putText(Imagem, "FONT_HERSHEY_SCRIPT_COMPLEX", (25, 200), FonteSelecionada, Escala, Cor)

FonteSelecionada = cv.FONT_HERSHEY_SCRIPT_SIMPLEX
cv.putText(Imagem, "FONT_HERSHEY_SCRIPT_SIMPLEX", (25, 240), FonteSelecionada, Escala, Cor)

FonteSelecionada = cv.FONT_HERSHEY_SIMPLEX
cv.putText(Imagem, "FONT_HERSHEY_SIMPLEX", (25, 280), FonteSelecionada, Escala, Cor)

FonteSelecionada = cv.FONT_HERSHEY_TRIPLEX
cv.putText(Imagem, "FONT_HERSHEY_TRIPLEX", (25, 320), FonteSelecionada, Escala, Cor)

FonteSelecionada = cv.FONT_ITALIC
cv.putText(Imagem, "FONT_ITALIC", (25, 360), FonteSelecionada, Escala, Cor)

# 
########################################################################
# Apresentação de Resultados
########################################################################
#
cv.imshow ( "Janela Base", Imagem)
cv.waitKey (0)
cv.destroyAllWindows ()

########################################################################
# FIM DO PROGRAMA
########################################################################
