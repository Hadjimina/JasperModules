#-*- coding: utf-8-*-
import random
import re
import os

WORDS = []


def handle(text, mic, profile):
    messages = ["Naturally Sir,","Of course Sir,","Right away Sir,"]
    global output

    message = random.choice(messages)
    mic.say(message)

    if ("on" in text.lower()):
        os.system("ssh pi@192.168.1.41 python /home/pi/james/sockets/fridgeON.py")
        output ="I have turned the fridge on."
    elif ("off" in text.lower()):
        os.system("ssh pi@192.168.1.41 python /home/pi/james/sockets/fridgeOFF.py")
        output ="I have turned the fridge off."

    mic.say(output)


def isValid(text):
    return bool(re.search(r'\bfridge|refrigerator\b', text, re.IGNORECASE))




