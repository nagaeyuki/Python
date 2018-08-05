# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 08:38:41 2018

@author: nagae
"""

# -*- coding: utf-8 -*

import cv2

try:
    capture = cv2.VideoCapture(0)
    w=960
    h = 480
    while(True):
        ret, frame = capture.read()
       
        img2 = cv2.resize(frame,(w, h))
        if ret == False:
            print('カメラから映像を取得できませんでした。')
            break
        
        cv2.imshow('f', img2)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    capture.release()
    cv2.destroyAllWindows()
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))