# -*- coding: utf-8-*-
import random
import re
from datetime import datetime


WORDS = ["TIME"]
PRIORITY = 4

def weekdayConverter(weekday_integer):

    if weekday_integer is 0:
        string = "monday"
    elif weekday_integer is 1:
        string = "tuesday"
    elif weekday_integer is 2:
        string = "wednesday"
    elif weekday_integer is 3:
        string = "thursday"
    elif weekday_integer is 4:
        string = "friday"
    elif weekday_integer is 5:
        string = "saturday"
    elif weekday_integer is 6:
        string = "sunday"
            
    return string

def monthConverter(month_integer):

    if month_integer is 1:
        string = "january"
    elif month_integer is 2:
        string = "february"
    elif month_integer is 3:
        string = "march"
    elif month_integer is 4:
        string = "april"
    elif month_integer is 5:
        string = "may"
    elif month_integer is 6:
        string = "june"
    elif month_integer is 7:
        string = "july"
    elif month_integer is 8:
        string = "august"
    elif month_integer is 9:
        string = "september"
    elif month_integer is 10:
        string = "october"
    elif month_integer is 11:
        string = "november"
    elif month_integer is 12:
        string = "december"

    return string

def handle(text, mic, profile):
	
    
    hour = datetime.now().time().hour 
    minute = datetime.now().time().minute
    date = datetime.now().day
    month = monthConverter(datetime.now().month)
    weekday = weekdayConverter(datetime.now().weekday())

    if "time" in text.lower():
        message = "It's currently " + str(hour) +" " + str(minute)
    else :
        message = "Today is "+ str(month) + " " + str(date)

    mic.say(message)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b(date|time)\b', text, re.IGNORECASE))


