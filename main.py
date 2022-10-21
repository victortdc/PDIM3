import cv2
import random
import numpy as np
from matplotlib import pyplot as plt

def salt_and_paper(imagem, intensidade=1000):
    imagem_ruidosa = imagem.copy() #copia da imagem original

    #dimensoes da imagem
    col, row = imagem_ruidosa.shape

    #espalha pixels brancos
    numero_de_pixels = random.randint(0, intensidade)
    for i in range(numero_de_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)

        imagem_ruidosa[y_coord][x_coord] = 255

    #espalha pixels pretos
    numero_de_pixels = random.randint(0, intensidade)
    for i in range(numero_de_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)

        imagem_ruidosa[y_coord][x_coord] = 0

    return imagem_ruidosa


if __name__ == '__main__':
    img = cv2.imread("BrainOriginal.png", 0) #abre a imagem
    plt.hist(img.ravel(), bins=25, range=[0, 256], label="original", alpha=.8)
    plt.title('Histogram for gray scale image')
    plt.legend()
    plt.show()
    cv2.imshow('ImgOriginal', img)

    noise = salt_and_paper(img, 5000) #faz o ruido
    plt.hist(noise.ravel(), bins=25, range=[0, 256], label="SaltyPaper", alpha=.8)
    plt.title('Histogram for gray scale image')
    plt.legend()
    plt.show()
    cv2.imshow('ImgNoise', noise)

    img_median = cv2.medianBlur(noise, 5) #aplica o filtro
    plt.hist(img_median.ravel(), bins=25, range=[0, 256], label="original", alpha=.8)
    plt.title('Histogram for gray scale image')
    plt.legend()
    plt.show()
    cv2.imshow('ImgMediana', img_median)
    cv2.waitKey(0)

