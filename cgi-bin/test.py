#!/usr/bin/env python
import cgitb ; cgitb.enable()
from buzz import Buzz
import time
import traceback, sys, os

buzz = Buzz()
#buzz.startBlink(15, 0.5)
buzz.setLights(15)

def printResult(result):
    print ("Content-Type: text/json")
    print ("""
    %s
    """ % result)

buzz.readController(timeout=5000)
printResult(buzz.getButtons())

