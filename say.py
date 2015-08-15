# -*- coding: utf-8-*-
import random
import re
import os

WORDS = []

PRIORITY = 6
def handle(text, mic, profile):
	output = text.replace("SAY","")
	mic.say(output)


def isValid(text):
    return bool(re.search(r'\b(say)\b', text, re.IGNORECASE))

