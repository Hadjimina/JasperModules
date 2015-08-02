# -*- coding: utf-8-*-
import random
import re
from datetime import datetime, time
from phue import Bridge
import os
import glob
import sys

WORDS = []

def wordToInt(word):

    value = ""

    if "one" in word.lower():
        value = "1"
    elif "two" in word.lower():
        value = "2"
    elif "three" in word.lower():
        value = "3"
    elif "four" in word.lower():
        value = "4"
    elif "five" in word.lower():
        value = "5"
    elif "six" in word.lower():
        value = "6"
    elif "seven" in word.lower():
        value = "7"
    elif "eight" in word.lower():
        value = "8"
    elif "nine" in word.lower():
        value = "9"
    elif "ten" in word.lower():
        value = "10"
    elif "eleven" in word.lower():
        value = "11"
    elif "twelve" in word.lower():
        value = "12"
    else :
	int_val = int(re.search(r'\d+', word).group())      
	value = str(int_val)

    if "pm" in word.lower():
        valueInt = int(value)
        valueInt += 12
        value = str(valueInt)
        

    return value

def handle(text, mic, profile):
    """
        meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
        mic -- used to interact with the user (for both input and output)
        profile -- contains information related to the user (e.g., phone
                   number)
    """
    messages1 = ["Naturally Sir ","Of course Sir "]
    messages2 = ["when whould you like to wake up","when would you like to be awakend","for what time shall i set the alarm","when do you want the alarm to go off"]

    final = random.choice(messages1)
    final += random.choice(messages2)
    mic.say(final)

    cronString = 'echo "'
    response = mic.activeListen()

    response.replace("at  ","",1)


    if "every" in response.lower():

        if "monday" in response.lower():
            response.replace("monday","",1)
            hour = wordToInt(response)
            cronString += "0 "+hour+" * * 1"


        elif "tuesday" in response.lower():
            response.replace("tuesday","",1)
            hour = wordToInt(response)
            cronString += "0 "+hour+" * * 2"

        elif "wednesday" in response.lower():
            response.replace("wednesday","",1)
            hour = wordToInt(response)
            cronString += "0 "+hour+" * * 3"

        elif "thursday" in response.lower():
            response.replace("thursday","",1)
            hour = wordToInt(response)
            cronString += "0 "+hour+" * * 4"

        elif "friday" in response.lower():
            response.replace("friday","",1)
            hour = wordToInt(response)
            cronString += "0 "+hour+" * * 5"

        elif "saturday" in response.lower():  
            response.replace("saturday","",1)
            hour = wordToInt(response)
            cronString += "0 "+hour+" * * 6"

        elif "sunday" in response.lower():
            response.replace("sunday","",1)
            hour = wordToInt(response)
            cronString += "0 "+hour+" * * 0"
	else :
	    sys.exit(1)

    cronString += ' gnome-terminal /home/philipp/.jasper/tester.sh" | tee -a /var/spool/cron/philipp'
    print("cd /home/philipp &&"+cronString)

    mic.say("Setting alarm " + response)

    os.system("cd /home/philipp &&"+cronString)




def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b((add|set) (a|another|an) (alarm|clock))\b', text, re.IGNORECASE))

