# -*- coding: utf-8 -*

import cv2

try:
    capture = cv2.VideoCapture(0)    
    cascade = cv2.CascadeClassifier(
            'haarcascade_frontalface_alt.xml')
    
    while(True):
        ret, frame = capture.read()
        if ret == False:
            print('カメラから映像を取得できませんでした.')
            continue
        facerect = cascade.detectMultiScale(frame)
        if len(facerect) > 0:
            for rect in facerect:
                cv2.rectangle(frame, tuple(rect[0:2]),
                              tuple(rect[0:2]+rect[2:4]), (0, 0,255), thickness=2)
        cv2.imshow('f', frame)
        
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
    
    
    