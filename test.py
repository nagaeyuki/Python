# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 10:15:35 2018

@author: nagae
"""


import sys
import cv2, os
import numpy as np
from PIL import Image
import base64
from StringIO import StringIO

import scipy.misc

# Haar-like特徴分類器
cascadePath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

def readb64(base64_string):
    sbuf = StringIO()
    sbuf.write(base64.b64decode(base64_string))
    pimg = Image.open(sbuf)
    return pimg
    #cv2.cvtColor(np.array(pimg), cv2.COLOR_RGB2BGR)

def detect():
    # グレースケールでbase64を読み込む
    image_pil = readb64(sys.argv[1].replace("\\", "\\\\")).convert('L')
    # NumPyの配列に格納
    image = np.array(image_pil, 'uint8')
    # Haar-like特徴分類器で顔を検知 (パラメータは適当)
    faces = faceCascade.detectMultiScale(image,1.1,9,0)
    
    scipy.misc.imsave('outfile.jpg', image)

    # 検出した顔画像の座標を表示
    for (x, y, w, h) in faces:
        print (x,y,w,h)

detect()