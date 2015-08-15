# -*- coding: utf-8-*-
import random
import re
import os

WORDS = []


def handle(text, mic, profile):
	

   greetings = ["For you sir, always.","Naturally sir.","Running a systems check immediately."]
   greeting = random.choice(greetings)
   mic.say(greeting)
  
   responseAudio = os.system("ping -c 1  192.168.1.41")
   responseMedia = os.system("ping -c 1  192.168.1.107")
   global message
   message = ""

   if responseAudio == 0 and responseMedia == 0:
	output = ["All systems are ready.", "All systems are online.","You have programmed me, of course all the systems are fine."]
	message = random.choice(output)

   elif responseAudio == 1:
	message = "I was unable to contact the audio server."

   elif responseMedia == 1:
	message = "I was unable to contact the media server."

   elif responseAudio == 1 and responseMedia == 1:
        output = ["All system are down.", "All system are offline.","I have run into a critical error, all system are down."]
        message = random.choice(output)
   mic.say(message)


def isValid(text):
    return bool(re.search(r'\b(system|check|systems)\b', text, re.IGNORECASE))

