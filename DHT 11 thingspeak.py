from grovepi import *
import sys
import os
import time
import urllib
from urllib import urlopen

myAPI = "DG7LRDI8SI1RP7BI"  # API Key from thingSpeak.com channel
myDelay = 15 #how many seconds between posting data

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND

sensor = 7 
blue = 0


baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

while True:
    try:
        [temp,humidity] = dht(sensor,blue)
        print("temp = {:.2f}C\thumidity = {:.2f}%".format(temp, humidity))             
        #tsp = baseURL + "&field1={:.2f}&          
        f = urllib.urlopen(baseURL + "&field1={:.2f}&field2={:.2f}".format(temp,humidity))
        f.close()
        time.sleep(int(myDelay))

        

    except TypeError:
        print("Error")
    except IOError:
        print("Error")


