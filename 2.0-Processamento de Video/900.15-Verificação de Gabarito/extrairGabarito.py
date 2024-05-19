import cv2
import numpy as np

def extrairMaiorCtn(img):
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTh = cv2.adaptiveThreshold(imgGray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)
    kernel = np.ones((2,2), np.uint8)
    imgDil = cv2.dilate(imgTh,kernel)
    contours,hi = cv2.findContours(imgDil,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    maiorCtn = max(contours, key = cv2.contourArea)
    x,y,w,h = cv2.boundingRect(maiorCtn)
    bbox = [x,y,w,h]
    recorte = img[y:y+h,x:x+w]
    recorte = cv2.resize(recorte,(400,500))

    return recorte,bbox