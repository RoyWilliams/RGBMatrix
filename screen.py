#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
import cv2
import sys

def init():
    return None

def show(a, matrix):
    scale = 10
    scalea = cv2.resize(a, None, fx=scale, fy=scale, 
        interpolation= cv2.INTER_NEAREST)
    cv2.imshow('image', scalea)
    cv2.waitKey(1)
