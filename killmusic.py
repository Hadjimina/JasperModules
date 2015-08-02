# -*- coding: utf-8-*-
import random
import re
from datetime import datetime, time
from phue import Bridge
import os
import glob

WORDS = []


def handle(text, mic, profile):
  

	messages1 = ["Naturally Sir ","Of course Sir ","I'll get right at it"]
	final = random.choice(messages1)
	mic.say(final)
	command = "ssh pi@"
	ip = profile['downloadip']
	command += ip
	command += " pkill omxplayer"
	os.system(command)
	os.system("pkill ssh")
	mic.say("The music process has successfully been killed")



def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b((kill|stop) the (alarm|clock|music))\b', text, re.IGNORECASE))


