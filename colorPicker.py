# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 16:26:03 2018

@author: Sarthak
"""

import cv2
import numpy as np

def func():
    pass

def main():
    img=np.zeros((512,512,3),np.uint8)
    windowName='Color Picker'
    cv2.namedWindow(windowName)
    
    cv2.createTrackbar('Blue',windowName,0,255,func)
    cv2.createTrackbar('Green',windowName,0,255,func)
    cv2.createTrackbar('Red',windowName,0,255,func)
    
    while(True):
        cv2.imshow(windowName,img)
        
        if cv2.waitKey(1)==27:  #Escape key will close the window
            break
        
        blue=cv2.getTrackbarPos('Blue',windowName)
        green=cv2.getTrackbarPos('Red',windowName)
        red=cv2.getTrackbarPos('Green',windowName)
        
        img[:]=[blue,green,red]
    
        print(blue,green,red)
        
    cv2.destroyAllWindows()
        

if __name__=="__main__":
    main()