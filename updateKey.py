#!/usr/bin/python
import random
import os
from time import sleep

keylist = ['AIzaSyC3YucMwudWnj1tJbIkgcWiUBXGFLGAZRo','AIzaSyAc-iPHrBoZwi8o78lnx9A5SJmd5R-J0Zk','AIzaSyCVPjZM25JkJ6kQzBcf-HeTPwEdgF1zTWw','AIzaSyDUrwFGkihqp3m-1Eq21BYkHtmv6qm8Pj8','AIzaSyCT6kPt38CdE2fzMBfupWR7YnjSV5_yPg8','AIzaSyCG9CimHpUDYVwvs1xTmizFMeANa-RCFU0']

file = open('profile.yml','r')
fileI = open('profile.yml','r')

#FIND KEY
"""
data = fileI.readlines()

lastline = data[len(data)-1]
modifiedlast= lastline[18:-2]

print(modifiedlast)
index = keylist.index(modifiedlast)
newKeyIndex = index
newKeyIndex += 1
"""
#APPEND KEY
lines = file.readlines()
lines = lines[:-1]
lines.append("  GOOGLE_SPEECH: '"+random.choice(keylist)+"'")

#CREATE NEW FILE
newfile = open("profile.yml",'w')
for item in lines:
  print(item)
  newfile.write("%s" % item)

#CLOSE FILES
fileI.close
file.close

#restart jasper.py
os.system("pkill -f jasper.py")
sleep(2)
os.system("/usr/bin/jasperservice")
