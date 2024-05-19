# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import cv2 as cv
import extcolors
from colormap import rgb2hex
from pathlib import Path
import os

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

def TamanhoImagemPadrao ( pilImgTmpBase,  iTamanho ):
    iLargura = iTamanho
    if pilImgTmpBase.size[0] >= iTamanho:
        TamanhoPercentual = (iLargura/float(pilImgTmpBase.size[0]))
        TamanhoAltura = int((float(pilImgTmpBase.size[1])*float(TamanhoPercentual)))
        pilImgTmpBase = pilImgTmpBase.resize((iLargura,TamanhoAltura), Image.ANTIALIAS)
    return (pilImgTmpBase)

def ConverteCorDF (imgTmpBase, iTolerancia, iLimite):
    imgBase = extcolors.extract_from_image(imgTmpBase, tolerance = iTolerancia, limit = iLimite)

    PreListaCor = str(imgBase).replace('([(','').split(', (')[0:-1]
    dfRgb = [i.split('), ')[0] + ')' for i in PreListaCor]
    dfPercentual = [i.split('), ')[1].replace(')','') for i in PreListaCor]
    
    dfResutadoCor = [rgb2hex(int(i.split(", ")[0].replace("(","")),int(i.split(", ")[1]),int(i.split(", ")[2].replace(")",""))) for i in dfRgb]    
    dfResultado = pd.DataFrame(zip(dfResutadoCor, dfPercentual), columns = [ "Codigo", "Percentual"])
    return (dfResultado)

def CriaLista (dfCor):
    lstCor = list(dfCor["Codigo"])
    lstPercentual = [int(i) for i in list(dfCor["Percentual"])]
    TextoCor = [Cor for Cor in list(lstCor)]
    return (TextoCor, lstCor, lstPercentual)

def MostraResultado (imgEntrada, iTamanho, iTolerancia, iZoom, iTamanhoLista):
   
    imgBase = TamanhoImagemPadrao ( imgEntrada, iTamanho )
    dfCor = ConverteCorDF(imgBase, iTolerancia, iTamanhoLista)
    TextoCor, lstCor, lstPercentual = CriaLista (dfCor)

    Grafico, pltArte = plt.subplots(1, 1, figsize=(160,120), dpi = 10) 
    Separador, Texto = pltArte.pie (lstPercentual,labels= TextoCor,labeldistance= 1.05,colors = lstCor,textprops={'fontsize': 110, 'color':'black'})
    plt.setp(Separador, width=0.3)

    imgCentroPie = OffsetImage(imgBase, zoom=iZoom)
    adicionaFigura = AnnotationBbox(imgCentroPie, (0, 0))
    pltArte.add_artist(adicionaFigura)
        
    plt.tight_layout()
    return (plt.show())

# 
########################################################################
# Definições Gerais
########################################################################
#
NomeImagem  = "IdentificaCor.jpg"
NomeOutput  = "Resultado.html"
dirRaiz = Path.home()
dirBase = "/home/asoares/Insync/alexandre.asoares@gmail.com/OneDrive/Atividades/LocalCV"
dirImagem = "Imagens"  
dirOutput = "Output"
dirCaminhoImagem = str(Path(dirRaiz, dirBase, dirImagem, NomeImagem))
dirCaminhoResultado = str(Path(dirRaiz, dirBase, dirOutput, NomeOutput))

# 
########################################################################
# Lendo a Imagem
########################################################################
#
imgBase = cv.imread ( dirCaminhoImagem, cv.IMREAD_COLOR)

# 
########################################################################
# Checando se a Imagem Foi Lida com Sucesso
########################################################################
#
if imgBase is None:
   LimpaTerminal ()
   print( "Não Foi Localizada a Imagem : ", NomeImagem)
   exit ()

# 
########################################################################
# Convertendo de openCV to Image PIL
########################################################################
#
imgTmpBase = cv.cvtColor(imgBase, cv.COLOR_BGR2RGB)
pilImgBase = Image.fromarray(imgTmpBase)

# 
########################################################################
# Apresentando o Resultado
########################################################################
#
MostraResultado ( pilImgBase, 900, 12, 2.5, 13)

# 
########################################################################
# Criando a Tabela com Todas as Cores
########################################################################
#
imgBase = TamanhoImagemPadrao ( pilImgBase, 900 )
dfCor = ConverteCorDF(imgBase, 12, 200)
TextoCor, lstCor, lstPercentual = CriaLista (dfCor)

fleOut = open(dirCaminhoResultado, 'w')
iTotal = dfCor["Percentual"].astype('int').sum()

print ( "<!DOCTYPE html> \n" +
"        <html lang=\"pt\"> \n" +
"        <head> \n" +
"           <meta charset=\"iso-8859-1\"> \n" +
"           <title>Tabela de Cores</title> \n" +
"        </head> \n" +
"       <body> \n" +
"           <table border=\"1\" width=\"500\" > \n" +
"           <thead> \n" +
"               <tr> \n" +
"                   <th>Cor</th> \n" +
"                   <th>C&oacute;digo</th> \n" +
"                   <th>Quantidade</th>	 \n" +  
"                   <th>Percentual</th> \n" +
"               </tr> \n" +
"           </thead> \n" +
"       <tbody> \n" +
"           <tr> \n" ,  file=fleOut)

for iAux in range (0, len(lstCor)):
    print ( "<tr> \n" ,  file=fleOut)
    print ( "<td style=\"text-align: center\">\n" ,  file=fleOut)
    print ( "<svg width=\"100\" height=\"20\">\n" ,  file=fleOut)
    print ( "<rect width=\"100\" height=\"20\" style=\"fill:" + TextoCor[iAux] + "\"\/> \n" ,  file=fleOut)
    print ( "</svg>",  file=fleOut)
    print ( "</td>",  file=fleOut)
    print ( "<td width=\"auto\" style=\"text-align: center\">"+ str(lstCor[iAux]) + "</td> \n",  file=fleOut)
    print ( "<td width=\"auto\" style=\"text-align: center\">"+ str(lstPercentual[iAux] )+ "</td> \n",  file=fleOut)
    print ( "<td width=\"auto\" style=\"text-align: center\">"+ str(round((lstPercentual[iAux]/iTotal)*100,2)) + "</td> \n",  file=fleOut)
    print ( "</tr> \n" ,  file=fleOut)
    print (  TextoCor[iAux]  )

print ( "         </tr> \n" +
        "    </tbody> \n" +
        " </table> \n" +
        " </body> \n" +
        "</html>" ,  file=fleOut)

########################################################################
# FIM DO PROGRAMA
########################################################################
