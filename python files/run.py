from buzz import Buzz
from pynput.keyboard import Key, Controller
import time
import traceback, sys, os

buzz = Buzz()
#buzz.startBlink(15, 0.5)
buzz.setLights(1)
keyboard = Controller()

while True:
    r = buzz.readController(timeout=500)
    if r != None:
        if buzz.getButtons()[0]['red'] == True:
            keyboard.press('a')
            keyboard.release('a')
        elif buzz.getButtons()[0]['blue'] == True:
            keyboard.press('b')
            keyboard.release('b')
        elif buzz.getButtons()[0]['orange'] == True:
            keyboard.press('c')
            keyboard.release('c')
        elif buzz.getButtons()[0]['green'] == True:
            keyboard.press('d')
            keyboard.release('d')
        elif buzz.getButtons()[0]['yellow'] == True:
            keyboard.press('e')
            keyboard.release('e')
