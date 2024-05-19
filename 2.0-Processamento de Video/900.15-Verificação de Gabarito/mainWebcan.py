import cv2
import pickle
import extrairGabarito as exG

campos = []
with open('campos.pkl', 'rb') as arquivo:
    campos = pickle.load(arquivo)

resp = []
with open('resp.pkl', 'rb') as arquivo:
    resp = pickle.load(arquivo)

respostasCorretas = ["1-A","2-C","3-B","4-D","5-A"]

video = cv2.VideoCapture(1)

while True:
    _,imagem = video.read()
    imagem = cv2.resize(imagem,(600,700))
    gabarito,bbox = exG.extrairMaiorCtn(imagem)
    imgGray = cv2.cvtColor(gabarito, cv2.COLOR_BGR2GRAY)
    ret,imgTh = cv2.threshold(imgGray,70,255,cv2.THRESH_BINARY_INV)
    cv2.rectangle(imagem, (bbox[0], bbox[1]), (bbox[0] + bbox[2], bbox[1] + bbox[3]), (0, 255,0), 3)
    respostas = []
    for id,vg in enumerate(campos):
        x = int(vg[0])
        y = int(vg[1])
        w = int(vg[2])
        h = int(vg[3])
        cv2.rectangle(gabarito, (x, y), (x + w, y + h),(0,0,255),2)
        cv2.rectangle(imgTh, (x, y), (x + w, y + h), (255, 255, 255), 1)
        campo = imgTh[y:y + h, x:x + w]
        height, width = campo.shape[:2]
        tamanho = height * width
        pretos = cv2.countNonZero(campo)
        percentual = round((pretos / tamanho) * 100, 2)
        if percentual >=15:
            cv2.rectangle(gabarito, (x, y), (x + w, y + h), (255, 0, 0), 2)
            respostas.append(resp[id])

    #print(respostas)
    erros = 0
    acertos = 0
    if len(respostas)==len(respostasCorretas):
        for num,res in enumerate(respostas):
            if res == respostasCorretas[num]:
                #print(f'{res} Verdadeiro, correto: {respostasCorretas[num]}')
                acertos +=1
            else:
                #print(f'{res} Falso, correto: {respostasCorretas[num]}')
                erros +=1

        pontuacao = int(acertos *6)
        cv2.putText(imagem,f'ACERTOS: {acertos}, PONTOS: {pontuacao}',(30,140),cv2.FONT_HERSHEY_SIMPLEX,1.2,(0,0,255),3)

    cv2.imshow('img',imagem)
    cv2.imshow('Gabarito', gabarito)
    cv2.imshow('IMG TH', imgTh)
    cv2.waitKey(1)