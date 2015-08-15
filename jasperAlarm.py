#!/usr/bin/python2.7
import pyvona
import time
import  pywapi
import string
from datetime import datetime
import os




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

def temperatureSuggestion(temp):
	
	global string 
	string = ""
	if 0 > temp :
		string = "It's freezing cold so I'd suggest warm clothes as well as a winter coat. "
	elif (0<=temp) and (temp<5):
		string = "It's rather cold so I'd suggest warm clothes.One might consider a winter coat. "
	elif (5<=temp) and (temp< 16):
		string = "It's rather cold today so I'd suggest moderatly long trousers and a pullover . As for a coat, a spring jacket should suffice. "
	elif (16<=temp)and (temp<20):
		string = "It's rather fresh today so I'd suggest long trouses and a t-shirt. Maybe a jacket is needed. "
	elif (20<=temp)and (temp<25):
		string = "It's hot today. I'd suggest shorts and a t-shirt. "
	elif (25<=temp)and (temp<30):
		string = "It's very hot today. I'd suggest wearing the least amount of clothes you can. "
	elif 30 <= temp:
		string = "It's blazing today. I'd go naked if I were you. "

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
		string += "It should not rain, so don't bother taking an umbrella."
	elif (30 < likelyhood) and (likelyhood<= 50):
		string += "Keep in mind though that there is a slight chance of rain, so maybe take an umbrella with you, when you leave."
	elif(50< likelyhood) and (likelyhood <65):
		string += "Keep in mind though that it's probably going to rain, so taking an umbrella would be a smart idea."
	else:
		string += "Keep in mind though that it's definitly going to rain, so do take an umbrella."

	return string



v = pyvona.create_voice("GDNAJLZKU4RZDT2IO7IQ", "/otzbhhTp5AlPWO1d64RWruDxA6s2Zqc7MoY9qsi")
v.voice_name ="Brian"
v.sentence_break = 400

#TIME
hour = datetime.now().time().hour 
minute = datetime.now().time().minute
month = monthConverter(datetime.now().month)
weekday = weekdayConverter(datetime.now().weekday())


if hour > 12:
	am_pm = "pm"
	greetings = "Good Afternoon Sir. "
else:
	am_pm = "am"
	greetings = "Good Morning Sir. "
	
today = "It's "+str(hour)+" "+str(minute)+" "+ am_pm
today += ". "


weather_com_result = pywapi.get_weather_from_weather_com('SZXX0728')
weather_status = weather_com_result['current_conditions']['text'] 
weather_felttemp = weather_com_result['current_conditions']['feels_like']
weather = "The weather conditions are "+weather_status+" with a felt temperature of "+ weather_felttemp+ " degrees Celsius. "
chance_rain = rain(weather_com_result['forecasts'])


felttemp_int = int(weather_felttemp)
weather_suggestion = temperatureSuggestion(felttemp_int)

v.speak(greetings+today+weather+weather_suggestion+" "+ chance_rain+"Let me play some music for you to get you started")

"""
PLAY YOUR MUSIC FILE HERE
"""
