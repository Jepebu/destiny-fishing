from pyautogui import *
import pyautogui as pg
import time
import keyboard
import os
from PIL import ImageGrab
from PIL import Image
import PIL
import cv2 as cv

def screenGrab():
    image = ImageGrab.grab(bbox = (880, 720, 910, 756))
    time.sleep(.02)
    image.save(os.getcwd() + '\\bbox' +'.png', 'PNG')
    #image.save('bbox' +'.png', 'PNG')

def loop():
    hook = cv.imread("msg.png", cv.IMREAD_COLOR)
    while keyboard.is_pressed("backspace") == False:
            screenGrab()
            bbox = cv.imread("bbox.png", cv.IMREAD_COLOR)
            check = cv.matchTemplate(bbox, hook, cv.TM_CCOEFF_NORMED)
            minval, maxval, minloc, maxloc = cv.minMaxLoc(check)
            #print(minval, minval)
            if (maxval > .23):
                print ("msg found " + str(maxval))
                pg.keyDown("f")
                time.sleep(.2)
                pg.keyUp("f")
                print("fish reeled")
                time.sleep(3)
                print("re-fishing")
                pg.keyDown("f")
                time.sleep(1)
                pg.keyUp("f")
                time.sleep(2)
time.sleep(4)
screenGrab()
loop()
