# -*- coding: utf-8-*-
import random
import re
from datetime import datetime, time,timedelta
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

    if "pm" in word.lower() or "p.m." in word.lower():
        valueInt = int(value)
        valueInt += 12
        value = str(valueInt)
        

    return value

def handle(text, mic, profile):
    messages1 = ["Naturally Sir ","Of course Sir "]

    final = random.choice(messages1)
    mic.say(final)

    cronString = 'echo "'

    text.replace("at  ","",1)
    global weekdayString
    global hour
    global hourString

    if "every" in text.lower():

        if "monday" in text.lower():
            text.replace("monday","",1)
            hour = wordToInt(text)
            cronString += "0 "+hour+" * * 1"
	    weekdayString = "Monday"


        elif "tuesday" in text.lower():
            text.replace("tuesday","",1)
            hour = wordToInt(text)
            cronString += "0 "+hour+" * * 2"
	    weekdayString = "Tuesday"

        elif "wednesday" in text.lower():
            text.replace("wednesday","",1)
            hour = wordToInt(text)
            cronString += "0 "+hour+" * * 3"
            weekdayString = "Wednesday"

        elif "thursday" in text.lower():
            text.replace("thursday","",1)
            hour = wordToInt(text)
            cronString += "0 "+hour+" * * 4"
            weekdayString = "Thursday"

        elif "friday" in text.lower():
            text.replace("friday","",1)
            hour = wordToInt(text)
            cronString += "0 "+hour+" * * 5"
            weekdayString = "Friday"

        elif "saturday" in text.lower():  
            text.replace("saturday","",1)
            hour = wordToInt(text)
            cronString += "0 "+hour+" * * 6"
            weekdayString = "Saturday"

        elif "sunday" in text.lower():
            text.replace("sunday","",1)
            hour = wordToInt(text)
            cronString += "0 "+hour+" * * 0"
            weekdayString = "Sunday"

	else :
	    sys.exit(1)

    	cronString += ' /home/philipp/.jasper/alarmScript.sh" | tee -a /var/spool/cron/philipp'
	print("cd /home/philipp &&"+cronString)

    	if hour > 12:
            hourInt = int(hour)
            hourInt = hourInt-12
            hourString += str(hourInt)+" pm"
    	else:
            hourString +=str(hour)+ " am"

    	mic.say("Setting alarm for " + weekdayString +" at "+ hourString)

    	os.system("cd /home/philipp &&"+cronString)


    elif "in" in text.lower() and ("hours" in text.lower() or "hour" in text.lower()):
	hour = wordToInt(text)
	command ='echo "/home/philipp/.jasper/jamesAlarm.py" |at now + ' 
	command += hour
	command += " hours"
	print(command)
	os.system(command)
	
	xHoursFromNow = datetime.now() + timedelta(hours=int(hour))
	mic.say("I set your alarm for "+ str(xHoursFromNow.hour)+" "+ str(xHoursFromNow.minute)+". ")
	





def isValid(text):
    return bool(re.search(r'\b(((add|set) (a|another|an) (alarm|clock)|wake me))\b', text, re.IGNORECASE))

