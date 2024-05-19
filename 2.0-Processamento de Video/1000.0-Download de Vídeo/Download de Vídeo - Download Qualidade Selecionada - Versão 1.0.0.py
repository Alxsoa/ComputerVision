# 
########################################################################
# Importação das Bibliotecas Necessárias
########################################################################
#
from pytube import YouTube
import os
from pathlib import Path

# 
########################################################################
# Funções de Uso Geral
########################################################################
#
def ProgressoDownload (stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    pct_completed = bytes_downloaded / total_size * 100  
    print(f"Status .........: {round(pct_completed, 2)} %")
    return ()

def DownloadTerminado (stream, file_path):
    print ("itag ...........: ", stream.itag)    
    print ("mime_tape ......: ", stream.mime_type)       
    print ("res ............: ", stream.resolution)                 
    print ("########################################################################")
    return ()

def ListaQualidade (ytTmpListaQualidade):
    #ytListaQualidade = yt.streams
    print ("########################################################################")
    print ("# Dados de Qualidade Disponível")
    print ("########################################################################")
    for iAux in range (0, len(ytTmpListaQualidade)):
        print ( "itag ...............: ", ytTmpListaQualidade[iAux].itag)
        print ( "mime_type ..........: ", ytTmpListaQualidade[iAux].mime_type)
        print ( "res ................: ", ytTmpListaQualidade[iAux].resolution)
        if ( ytTmpListaQualidade[iAux].type == "video"):
            print ( "fps ................: ", ytTmpListaQualidade[iAux].fps)
        else:
            print ( "fps ................:  None")
        print ( "type ...............: ", ytTmpListaQualidade[iAux].type)
        print ("------------------------------------------------------------------------")
    return ()

# 
########################################################################
# Definições Gerais
########################################################################
#
urlEndereco = "https://www.youtube.com/watch?v=K8NRuZ2dtYk" 
NomeVideo  = "VideoDownload.mp4"
dirRaiz = Path.home()
dirBase = "LocalCV"
dirVideo = "Videos"  
dirSaida = str(Path(dirRaiz, dirBase, dirVideo))
fileVideo = str(Path(dirRaiz, dirBase, dirVideo, NomeVideo))

# 
########################################################################
# Checando se o Arquivo Existe
########################################################################
#
isExiste = os.path.exists(fileVideo)
if ( isExiste ):
   os.remove (fileVideo)

# 
########################################################################
# Instanciando o Vídeo Desejado
########################################################################
#
try: 
    yt = YouTube(urlEndereco) 
except Exception as e:
       print ("ERRO : %s" % format(e))
       exit(1)

# 
########################################################################
# Recuperando Dados do Vídeo
########################################################################
#
os.system ("clear")
print ("########################################################################")
print ("# Informações Sobre o Vídeo")
print ("########################################################################")
print ("Titulo .............: ", yt.title )
print ("URL ................: ", yt.channel_url)
print ("Autor ..............: ", yt.author)
print ("ID do Canal ........: ", yt.channel_id)
print ("ID do Vídeo ........: ", yt.video_id)
print ("Descrição ..........: ", yt.description)
print ("Palavras-Chave .....: ", yt.keywords)
print ("Data de Publicação .: ", yt.publish_date)
print ("Avaliação ..........: ", yt.rating)
print ("Número de Views ....: ", yt.views)
print ("Duração (s) ........: ", yt.length)
    
# 
########################################################################
# Realizando o Download do Vídeo
########################################################################
#
print ("########################################################################")
print ("# Dados do Vídeo Baixado")
print ("########################################################################")
yt = YouTube (
                urlEndereco,
                on_progress_callback = ProgressoDownload,
                on_complete_callback = DownloadTerminado,
                #proxies=my_proxies,
                use_oauth=False,
                allow_oauth_cache=False
             )

# 
########################################################################
# Definindo a Qualidade Específica e Padrão de Vídeo para o Download
########################################################################
#
VideoStream = yt.streams.filter (
                                    only_video = True,
                                    only_audio = False
                                )


# 
########################################################################
# Recuperando a Lista de Qualidade Disponível para o Vídeo
########################################################################
#
ListaQualidade (VideoStream)

# 
########################################################################
# Baseado na Lista Seleciona a Qualidade Desejada
########################################################################
#
VideoStream = yt.streams.get_by_itag(136)

# 
########################################################################
# Definindo o Diretório e Nome do Arquivo de Vídeo
########################################################################
#
try: 
    VideoStream.download (
                            output_path = dirSaida,
                            filename = NomeVideo
                         )
except Exception as e:
       print ("ERRO : %s" % format(e))
       exit(1)

########################################################################
# FIM DO PROGRAMA
########################################################################

