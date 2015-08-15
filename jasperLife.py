# -*- coding: utf-8-*-
import random
import re
import os
import sys

WORDS = ["RESTART", "REBOOT", "SHUT DOWN","SHUT UP"]


def handle(text, mic, profile):
    


    #HANDLE REBOOT
    if "reboot" in text.lower():

        if 'root_pwd' in profile:    
            root_pwd = profile['root_pwd']
        else:
            mic.say("Sir it seems that I lack the necessary permission to execute this module")
            sys.exit(1) 

        messages = ["Are you sure that you want me to reboot and not simply restart my jasper interface ?","Am I correct in assuming that you want me to reboot the entire jasper server ?"]
        mic.say(random.choice(messages))
        rebootresponse = mic.activeListen()
        if ("yes" in rebootresponse.lower()) or ("i am sure" in rebootresponse.lower()) or ("of course" in rebootresponse.lower()):
	    rebootMessages1 = ["As you wish. ","As you command. ","Of course sir. "]
	    rebootMessages2 = ["Rebooting process initiated.","See you soon", "Lets hope this works"]
	    rebootfinal = random.choice(rebootMessages1)
	    rebootfinal += random.choice(rebootMessages2)
	    mic.say(rebootfinal)
            rebootString= 'echo "'+root_pwd+'" | sudo -S -k reboot'
            os.system(rebootString)

    
    #HANDLE RESTART 
    if "restart" in text.lower():
        messages1 = ["As you wish. ","As you command. ","Of course sir. ","Ok then. "]
        messages2 = ["I will be back soon.","Give me a second to restart.","restarting process initiated. Loading."]
        final = random.choice(messages1)
        final += random.choice(messages2)

        mic.say(final)
	os.execv("/usr/share/jasper-voice-control/jasper.py", sys.argv)

        #HANDLE SHUTDOWN 
    if ( ("shut" in text.lower()) and ("down" in text.lower())) or (("shut" in text.lower()) and ("down" in text.lower())):
        messages1 = ["As you wish. ","As you command. ","Of course sir. "]
        messages2 = ["Good Bye","I know you will miss me","Don't do anything I wouldn't do","Shut dow sequence initiated","Shutting down"]
        final = random.choice(messages1)
        final += random.choice(messages2)

        mic.say(final)
	os.system("pkill -f jasper.py")

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b((restart|reboot|shut) (yourself|up))\b', text, re.IGNORECASE))


