# -*- coding: utf-8-*-
import random
import re
from datetime import datetime
import  pywapi


WORDS = ["SUGGESTION"]

PRIORITY = 4


def temperatureSuggestion(temp):
    
    global string 
    string = ""
    if 0 > temp :
        string = "It's freezing cold so I'd suggest warm clothes as well as a winter coat."
    elif (0<=temp) and (temp<5):
        string = "It's rather cold so I'd suggest warm clothes.One might consider a winter coat."
    elif (5<=temp) and (temp< 16):
        string = "It's rather cold today so I'd suggest moderatly long trousers and a pullover . As for a coat, a spring jacket should suffice."
    elif (16<=temp)and (temp<20):
        string = "It's rather fresh today so I'd suggest long trouses and a t-shirt. Maybe a jacket is needed."
    elif (20<=temp)and (temp<25):
        string = "It's hot today. I'd suggest shorts and a t-shirt."
    elif (25<=temp)and (temp<30):
        string = "It's very hot today. I'd suggest wearing the least amount of clothes you can."
    elif 30 <= temp:
        string = "It's blazing today. I'd go naked if I were you."

    string +=". "
    return string

def rain(list):
    
    date = datetime.now().day
    integer = 0
    loc = 0
    string = ""

    for day in list:
        if str(date) in day["date"].lower():
            loc = integer

        integer +=1

    likelyhood_string = list[loc]["day"]["chance_precip"]
    likelyhood = int(likelyhood_string)

    if (0 <= likelyhood) and (likelyhood<= 30):
        string += "It should not rain today, so don't bother taking an umbrella with you."
    elif (30 < likelyhood) and (likelyhood<= 50):
        string += "Keep in mind though that there is a slight chance of rain today, so maybe take an umbrella with you, when you leave."
    elif(50< likelyhood) and (likelyhood <65):
        string += "Keep in mind though that it's probably going to rain today, so taking an umbrella would be a smart idea."
    else:
        string += "Keep in mind though that it's definitly going to rain today, so do take an umbrella."

    return string

def handle(text, mic, profile):
	
    
    weather_com_result = pywapi.get_weather_from_weather_com('SZXX0728')
    weather_status = weather_com_result['current_conditions']['text'] 
    weather_felttemp = weather_com_result['current_conditions']['feels_like']
    weather = "The weather conditions are "+weather_status+" with a felt temperature of "+ weather_felttemp+ " degrees Celsius. "
    


    if ("clothes" in text.lower()) or ("wear" in text.lower()):

        chance_rain = rain(weather_com_result['forecasts'])
        felttemp_int = int(weather_felttemp)
        weather_suggestion = temperatureSuggestion(felttemp_int)

        weather_suggestion += chance_rain
        
        mic.say(weather_suggestion)

    else :
    	mic.say(weather)


def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b((weather|wear|clothes))\b', text, re.IGNORECASE))



