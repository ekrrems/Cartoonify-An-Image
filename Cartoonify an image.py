import cv2 #for image processing
import easygui #to open the filebox
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

def upload():
    image_path=easygui.fileopenbox()
    print(image_path)
    return image_path

def cartoonify():
    original_img = cv2.imread('original.png')

    if original_img is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()

    grayScaleimg = cv2.cvtColor(original_img, cv2.COLOR_RGB2GRAY)
    Resized2 = cv2.resize(grayScaleimg, (960, 540))

    cv2.imshow('grayscaled',Resized2)
    cv2.waitKey()

    smoothGrayScale = cv2.medianBlur(grayScaleimg, 5)
    ReSized3 = cv2.resize(smoothGrayScale, (960, 540))

    getEdge = cv2.adaptiveThreshold(smoothGrayScale, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)
    ReSized4 = cv2.resize(getEdge, (960, 540))

    colorImage = cv2.bilateralFilter(original_img, 9, 300, 300)
    ReSized5 = cv2.resize(colorImage, (960, 540))

    cartoonImage = cv2.bitwise_and(colorImage, colorImage, mask=getEdge)
    ReSized6 = cv2.resize(cartoonImage, (960, 540))
    cv2.imshow('cartoon',cartoonImage)
    cv2.waitKey(0)


cartoonify()