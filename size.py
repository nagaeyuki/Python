# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 08:47:09 2018

@author: nagae
"""

# -*- coding: utf-8 -*

import cv2

try:
    capture = cv2.VideoCapture(0)
    width = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    
    print('frame size = ' + str(width) + ' x ' + str(height))
except:
    import sys
    print("Error:", sys.exc_info()[0])
    print(sys.exc_info()[1])
    import traceback
    print(traceback.format_tb(sys.exc_info()[2]))