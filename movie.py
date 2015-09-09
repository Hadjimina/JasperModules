# -*- coding: utf-8-*-
import random
import re
from datetime import datetime, time
import kat
import subprocess

WORDS = ["DOWNLOAD", "MOVIE", "TORRENT","ADD TO"]


def handle(text, mic, profile):
    
    messages1 = ["Naturally Sir ","Of course Sir "]
    messages2 = ["which Movie did you have in mind","which Movie shall it be"]

    message = random.choice(messages1)
    message += random.choice(messages2)
    mic.say(message)
    global command 
    global finished

    test = mic.activeListen()
    query = kat.search(test, category=kat.Categories.MOVIES,sort=kat.Sorting.SEED, order=kat.Sorting.Order.DESC)

    finishedmessages1 =  ["I have downloaded the torrent file for "+ test+ "successfully", test + " has been added to your download directory", "The download of "+test+"has started"]
    finished =random.choice(finishedmessages1)
    
    if 'downloadip' in profile:    
        ip = profile['downloadip']
    else:
        ip = '127.0.0.1'
	
    command = "ssh philipp@"+ ip + " cd /home/philipp/MediaHD/Torrents/torrents && wget --trust-server-names "+query[0].download
    print(command)
    #subprocess.call(["ssh pi@"+ ip +" wget --trust-server-names "+query[0].download], shell=True)

    try:
        subprocess.check_call(command,shell=True)
    except subprocess.CalledProcessError:
        finishedmessages2 = ["It seems that there was an Error, Sir", "I ran into a Problem while downloading your torrent file"]
        finished = random.choice(finishedmessages2)
    
    mic.say(finished)
    
    

def isValid(text):
    """
        Returns True if the input is related to the meaning of life.

        Arguments:
        text -- user-input, typically transcribed speech
    """
    return bool(re.search(r'\b((download|add) a (movie|torrent))\b', text, re.IGNORECASE))




