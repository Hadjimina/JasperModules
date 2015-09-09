# -*- coding: utf-8-*-
import random
import re
import os

from datetime import datetime, time
from phue import Bridge

WORDS = ["TURN", "LIGHTS", "ON","OFF"]


def handle(text, mic, profile):
	
    bridgeip = profile['bridgeip']
    b = Bridge(bridgeip)
    b.connect()
    global message
    message = ""    

    if "on" in text.lower():
        os.system("ssh pi@192.168.1.41 python /home/pi/james/sockets/lampON.py")

	for l in lights:
		l.on = True
		l.brightness = 254
	message = "All Lights have been turned on"
	
    elif "dim" in text.lower() or "reduce" in text.lower():
        os.system("ssh pi@192.168.1.41 python /home/pi/james/sockets/lampOFF.py")

	for l in lights:
		l.on = True
		l.brightness = 127

        message = "The Brightness has been reduced."

    elif "off" in text.lower():
        os.system("ssh pi@192.168.1.41 python /home/pi/james/sockets/lampOFF.py")

	for l in lights:
		l.on = True
		l.brightness = 254

    	message = "All Lights have been turned off."
	
    	now = datetime.now()
    	now_time = now.time()
    
    	if now_time > time(21,30) or now_time < time(02,00):
        	message += " Good Night"



    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b((turn|dim|reduce) (all|the) (brightness|lights))\b', text, re.IGNORECASE))

