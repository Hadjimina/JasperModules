# JasperModules
Collection of different Jasper Modules

##Alarm Module
Basically creates a cronjob at a certain time that executes jasperAlarm.py<br />
If you want to play a music file after the alarm, you have to add the yourself at the end of the jasperAlarm.py file.<br /><br />
Usage = "Set an alarm for every monday at 8", or "Wake me up in 8 hours" (Only accepts full hours, no minutes)<br /><br />

Requires pywapi. Install it like so :<br />
```pip install pywapi```

##Hue Module
Turns all hue lights on,off or dims them. Keep in mind that you need to a "bridgeip" to your profile.yml like so:<br />
```bridgeip: 192.168.XXX.XXX```<br /><br />

Requires phue library. Install with :<br />
```pip install phue```

<br /><br />
Usage = "Turn the lights on/off","Reduce the brightness","Dim the lights"

##JasperLife Module
You are able to control jasper with saying restart, shut down, shut up and reboot followed by yourself (restart = restarts jasper, reboot = reboots computer).<br /><br /> Needs a "root_pwd" setting in profile.yml. Add it like so :<br />
```root_pwd: YOUR PASSWORD HERE```<br />
ATTENTION: YOUR PASSWORD IS SAVED IN PLAIN TEXT


##Knowledged Module
Extremely minor changes to the knowledged module from [nexhero](https://github.com/nexhero) all credit should go to him. [Visit his github page on the knowledged module for further instruction](https://github.com/nexhero/wolframalpha_jasper)<br /><br />
Requires wolframalpha library. Install with :<br />
```pip install wolframalpha```

##Movie Module
Gets the best result for your query from kickasstorrents and downloads it to a remote server. You can change it to wherever your torrent download directory is.<br />
If you also use a server, add "downloadip" to your profile.yml like so :<br />
```downloadip: 192.168.XXX.XXX```

Requires KAT library Install with :<br />

```pip install kat```<br />

Usage: "Download a movie" BEEP "Iron man"<br />
##Time Module
The default time module somehow stopped working for me, so I wrote a new one.<br />
Usage: "What time is it?", "What date is it?"

##Weather Module
Tells you what the weather is like and can also give advice for your clothing according to the current weather. Tells you if it's going to rain or not<br />
Change ``` weather_com_result = pywapi.get_weather_from_weather_com('SZXX0728')``` according to your location. <br />
Here is how:<br />
Go to [weather.com](www.weather.com), search for your location. Your URL should change to something like this : ```http://www.weather.com/weather/today/l/SZXX0728:1:```. The caractes after ```l/``` until ```:``` is your location code.

Requires pywapi. Install it like so :<br />
```pip install pywapi```<br />

Usage: "What should i wear today?", "Whats the current temperature?","Is it going to rain today?"

##Say Module
Simply repeats what you have said.<br />
Usage : "Say XXXXXXXXXXXXXXXXXX"

##System Module
Pings the ip addresses listed in the system.py file and tells you if they are online or not.<br />

Usage : "Do a systems check"

##What's all that fridge.py and LampON/OFF.py ?
Where I life the wemo switches are not available so I built my own. I am using intertechno IT-1500 switches which are just normal radio switches with a remote. I poped the remote open looked at the circuit and then hacked something together using a raspberry pi. Afterwards I have configured [nanpy](http://nanpy.github.io/). So these LampON/OFF.py are simply making a nanpy call to the arduino which then uses a relay to control the remote for the switches. You probably do not need these so if you plan on using my modules I would suggest deleting fride.py and any refrence to LampON/OFF. However if someone more intrested in how I configured my setup just email me I am always happy to help.

