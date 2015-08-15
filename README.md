# JasperModules
Collection of different Jasper Modules

##Hue Module
Turns all hue lights on or off. Keep in mind that you need to a "bridgeip" to your profile.yml like so:<br />
```bridgeip: 192.168.XXX.XXX```<br /><br />

Requires phue library. Install with :<br />
```pip install phue```

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

```pip install kat```

##Time Module
The default time module somehow stopped working for me, so I wrote a new one.<br />

##Weather Module
Tells you what the weather is like and can also give advice for your clothing according to the current weather.<br />
Change ``` weather_com_result = pywapi.get_weather_from_weather_com('SZXX0728')``` according to your location. <br />
Here is how:<br />
Go to [weather.com](www.weather.com), search for your location. Your URL should change to something like this : ```http://www.weather.com/weather/today/l/SZXX0728:1:```. The caractes after ```l/``` until ```:``` is your location code.

Requires pywapi. Install it like so :<br />
```pip install pywapi```
