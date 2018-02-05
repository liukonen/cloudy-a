#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib2
import json
import sys
import time
import datetime
import pigpio
import random

#insert the WeatherUnderground API-key here:
wunder_api = ""

#insert the location for the forecast here. For example "Germany/Berlin"
location = ""

#this decides when it is time to display the forecast for the next day. If you want to show always the forecast for the day, set it to 24:
switch_time = 24

#time we call the API
UpdateTimeInMinutes = 60

#Valid Values are  1,2,3, and 4
Brightness = 4

#mapping the colors rather then hardcode
r1 = 17
g1 = 24
b1 = 22
r2 = 26 #Pi B 27
g2 = 13 #Pi B 23
b2 = 12 #Pi B 25

#------------DO NOT EDIT BELOW THIS LINE UNLESS YOU ARE A PROGRAMMER ------------#

#region Global Variables
NextUpdate = datetime.datetime.now() + datetime.timedelta(minutes = -1) #forces an update right away
condition = ""
conditions = {"cloudy" : "cloudy", "nt_cloudy" : "cloudy", "fog" : "cloudy", "nt_fog" : "cloudy", "hazy" : "cloudy", "nt_hazy" : "cloudy", "mostlycloudy" : "cloudy", "nt_mostlycloudy" : "cloudy", "partlycloudy" : "cloudy", "nt_partlycloudy" : "cloudy", "clear" : "sunny", "nt_clear" : "sunny", "sunny" : "sunny", "nt_sunny" : "sunny", "mostlysunny" : "sunny", "nt_mostlysunny" : "sunny", "partlysunny" : "sunny", "nt_partlysunny" : "sunny", "chanceflurries" : "snowy", "nt_chanceflurries" : "snowy", "flurries" : "snowy", "nt_flurries" : "snowy", "chancesnow" : "snowy", "nt_chancesnow" : "snowy", "snow" : "snowy", "nt_snow" : "snowy", "chancerain" : "rainy", "nt_chancerain" : "rainy", "chancesleet" : "rainy", "nt_chancesleet" : "rainy", "sleet" : "rainy", "nt_sleet" : "rainy", "rain" : "rainy", "nt_rain" : "rainy", "tstorms" : "stormy", "nt_tstorms" : "stormy", "chancetstorms" : "stormy", "nt_chancetstorms" : "stormy"}
bright=0
brightnew=0
brightnew2=0
bright2=0
fadetime=0
fadetime2=0
maxBrightness = 63 * Brightness
BrightnessMulitiplier = 5-Brightness
pi = pigpio.pi()


def WeatherNeedsUpdating():
  return NextUpdate < datetime.datetime.now()

def CheckWeather():
 global NextUpdate
 global condition

 if WeatherNeedsUpdating():
  NextUpdate = datetime.datetime.now() + datetime.timedelta(minutes = UpdateTimeInMinutes)
  try:
   myweather = json.load(urllib2.urlopen('http://api.wunderground.com/api/' + wunder_api + '/forecast/q/' + location + '.json'))
   myweather_sum = myweather['forecast']['simpleforecast']['forecastday']
   if int(time.strftime("%H")) < int(switch_time):
	ampm = 1
   else:
	ampm = 2

   for period in myweather_sum:
    if period['period'] == ampm:
     orig_conditions = period['icon']
    condition = conditions[orig_conditions]
  except:
   NextUpdate = datetime.datetime.now() + datetime.timedelta(seconds = 30)
   condition = "Error"



#These are the different animations for the LED-strips:
def rain():

 blueishness1=maxBrightness
 blueishness2=0
 fadetimeblue=random.uniform(0.02,0.06) * BrightnessMulitiplier
 pi.set_PWM_dutycycle(r1,0)
 pi.set_PWM_dutycycle(g1,0)
 pi.set_PWM_dutycycle(r2,0)
 pi.set_PWM_dutycycle(g2,0)

 while blueishness1 !=0 and blueishness2 !=maxBrightness:
  blueishness1=blueishness1-1
  blueishness2=blueishness2+1
  time.sleep(fadetimeblue)
  pi.set_PWM_dutycycle(b1,blueishness1)
  pi.set_PWM_dutycycle(b2,blueishness2)
 time.sleep(random.uniform(0.1,2))
 while blueishness1 !=maxBrightness and blueishness2 !=0:
  blueishness1=blueishness1+1
  blueishness2=blueishness2-1
  time.sleep(fadetimeblue)
  pi.set_PWM_dutycycle(b1,blueishness1)
  pi.set_PWM_dutycycle(b2,blueishness2)
 time.sleep(random.uniform(0.1,2))

def cloud():
 whiteness1=maxBrightness
 whiteness2=0
 fadetimewhite=random.uniform(0.02,0.04) * BrightnessMulitiplier

 while whiteness1 != 0 and whiteness2 != maxBrightness:
  whiteness1=whiteness1-1
  whiteness2=whiteness2+1
  time.sleep(fadetimewhite)
  pi.set_PWM_dutycycle(g2,whiteness1)
  pi.set_PWM_dutycycle(r2,whiteness1)
  pi.set_PWM_dutycycle(b2,whiteness1)
  pi.set_PWM_dutycycle(r1,whiteness2)
  pi.set_PWM_dutycycle(g1,whiteness2)
  pi.set_PWM_dutycycle(b1,whiteness2)
 time.sleep(random.uniform(0.5,1))
 while whiteness1 != maxBrightness and whiteness2 != 0:
  whiteness1=whiteness1+1
  whiteness2=whiteness2-1
  time.sleep(fadetimewhite)
  pi.set_PWM_dutycycle(g2,whiteness1)
  pi.set_PWM_dutycycle(r2,whiteness1)
  pi.set_PWM_dutycycle(b2,whiteness1)
  pi.set_PWM_dutycycle(r1,whiteness2)
  pi.set_PWM_dutycycle(g1,whiteness2)
  pi.set_PWM_dutycycle(b1,whiteness2)
 time.sleep(random.uniform(0.5,1))

def sun():
 yellowness1=maxBrightness
 yellowness2=0
 fadetimeyellow=random.uniform(0.05,0.06) * BrightnessMulitiplier
 pi.set_PWM_dutycycle(b1,0)
 pi.set_PWM_dutycycle(b2,0)

 while yellowness1 != 0 and yellowness2 != maxBrightness:
  yellowness1=yellowness1-1
  yellowness2=yellowness2+1
  time.sleep(fadetimeyellow)
  pi.set_PWM_dutycycle(g2,(yellowness1/5))
  pi.set_PWM_dutycycle(r2,yellowness1)
  pi.set_PWM_dutycycle(r1,yellowness2)
  pi.set_PWM_dutycycle(g1,(yellowness2/5))
 time.sleep(random.uniform(0.1,0.5))
 while yellowness1 != maxBrightness and yellowness2 != 0:
  yellowness1=yellowness1+1
  yellowness2=yellowness2-1
  time.sleep(fadetimeyellow)
  pi.set_PWM_dutycycle(g2,(yellowness1/5))
  pi.set_PWM_dutycycle(r2,yellowness1)
  pi.set_PWM_dutycycle(r1,yellowness2)
  pi.set_PWM_dutycycle(g1,(yellowness2/5))
 time.sleep(random.uniform(0.1,0.5))


def snow():
 global bright
 global brightnew
 global brightnew2
 global bright2
 global fadetime
 global fadetime2
 SnowBright = 61 * Brightness

 start=random.randint(1,100)
 if start==1 and bright==0:
  brightnew= 50*Brightness #200
  if bright==0:
    fadetime=random.uniform(0.002,0.0025) * BrightnessMulitiplier
  else:
   pass
 elif start==2 and bright2==0:
  brightnew2=50 * Brightness
  if bright2==0:
   fadetime2=random.uniform(0.002,0.0025) * BrightnessMulitiplier
  else:
   pass
 else:
  pass


 if brightnew > bright and bright < SnowBright:
  bright=bright+1
 elif brightnew == bright:
  brightnew=0
 elif brightnew < bright and bright !=0:
  bright=bright-1
 else:
  pass

 if brightnew2 > bright2 and bright2 < SnowBright:
  bright2=bright2+1
 elif brightnew2 == bright2:
  brightnew2=0
 elif brightnew2 < bright2 and bright2 !=0:
  bright2=bright2-1
 else:
  pass
 pi.set_PWM_dutycycle(r1, bright+55)
 pi.set_PWM_dutycycle(b1, bright+55)
 pi.set_PWM_dutycycle(g1, bright+55)
 time.sleep(fadetime)
 pi.set_PWM_dutycycle(r2, bright2+55)
 pi.set_PWM_dutycycle(b2, bright2+55)
 pi.set_PWM_dutycycle(g2, bright2+55)
 time.sleep(fadetime2)

def flash():
 global bright
 global brightnew
 global brightnew2
 global bright2
 global fadetime
 global fadetime2
 MinBrightness = 13*maxBrightness

 start=random.randint(1,210)
 if start==1:
  brightnew=random.randint(MinBrightness,maxBrightness)
  if bright==0:
   fadetime=random.uniform(0.002,0.006) * BrightnessMulitiplier
  else:
   pass
 elif start==2:
  brightnew2=random.randint(MinBrightness,maxBrightness)
  if bright2==0:
   fadetime2=random.uniform(0.002,0.006) * BrightnessMulitiplier
  else:
   pass
 else:
  pass

 if bright+brightnew<maxBrightness:
  bright=bright+brightnew
  brightnew=0
 else:
  pass	

 if bright2+brightnew2<maxBrightness:
  bright2=bright2+brightnew2
  brightnew2=0
 else:
  pass	
 
 pi.set_PWM_dutycycle(r1, bright)
 if bright>50:
  pi.set_PWM_dutycycle(b1, bright)
 else:
  pi.set_PWM_dutycycle(b1, 50)
  pi.set_PWM_dutycycle(g1, bright)
 time.sleep(fadetime)
 if bright !=0:
  bright=bright-1
 else:
  pass

 pi.set_PWM_dutycycle(r2, bright2)
 if bright2>50:
  pi.set_PWM_dutycycle(b2, bright2)
 else:
  pi.set_PWM_dutycycle(b2, 50)
  pi.set_PWM_dutycycle(g2, bright2)
 time.sleep(fadetime2)

 if bright2 !=0:
  bright2=bright2-1
 else:
  pass

def error_value():
 pi.set_PWM_dutycycle(r2, 100)
 time.sleep(1)
 pi.set_PWM_dutycycle(r1, 100)
 time.sleep(1)

#this executes the main loop. E.g. it is looking for the conditions and decides for the animation that should be displayed:
def main_loop():
 while 1:
  CheckWeather()

  if  condition=="rainy":
   rain()
  elif condition=="cloudy":
   cloud()
  elif condition=="sunny":
   sun()
  elif condition=="snowy":
   snow()
  elif condition=="stormy":
   flash()
  else:
   error_value()


#Start
if __name__ == '__main__':
 try:
  main_loop()
 except KeyboardInterrupt:
  print >> sys.stderr, '\nExiting by user request.\n'
  sys.exit(0)
