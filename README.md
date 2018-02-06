# cloudy-Pie (a remake of DJAkbar's cloudy-a project)
A  script for light animations for two LED strips according to the weather forecast. For an example see [Youtube](https://www.youtube.com/watch?v=DNXssI4LuMc)  

![](https://lh3.googleusercontent.com/OWZv2fEOazNtOKzn04vIXL1WkjLKEBS2XjN8mAmALI3k3eyp2ftHteBgxuCBxdeUuTZcjzoTVvUROQToHgtBTr1X2pJ8PGiK-xiI1HSHDtBNMo6fXunyQ7nH6e0Ys-16SorFYjvX7jpDHuD8UuIjoVGQZk261v0onbipPugYrq-x7VZ7ay5YZPJAYq9jODe376Kq8IojVbeS4ZZT1dJwElg_BWsMrHbzh2VnIoZ5UHZ1Oye5_sQvuAKnR21LrvYnW-XRMIKu_bpW9Us9iV3FsfCOpthBFlUnuWf7-59jd-LRr-t_ajMmEnAIhjaIq6_zPyAVa1YSsnSjYcVxFlzjYd7HIJ1YKGE3EvvzPx6BT2NTs3JIllOzp6rIiVAhAwnUC_aE7cdRHlR6we18gC4D096QcLvOSn30XIX6bMm2p-_eL8SaEUAntnPyrWB_w19irEm0ayfgI5bPT7LQoFTIxUntLxeo8DytMpm56dgS1rr2Uwf8FQeaHhrDKOZefsvOdK_RwvDFbBFFD2YYu1VMbejPlUhEWtKMRr79-jZih597zZvV-QKJo6y-ahQGNWiOFigeCNt4buLBmW7eXhuNXVl_73y6S8GUpNEeHnS6rFy9DF9GePVDfIzbyWJcmWL96Pi0o2isNgxn-QuSgj2no6SrwUJLSov64w=w869-h989-no | width=100)

Instructions for use: 
Here is a short write-up of some instructions to make your own DIY weather forecast cloud lamp.  
The creator of this project built his using this with a Raspberry Pi 3. I am currently using a Rasberry Pi B.Some things should be set-up already:  
+ Python and pigpio installed on the Raspberry Pi  
+ An internet connection (if you’re not using WIFI make sure to have a cable that’s long enough)  
+ A WeatherUnderground API key and your location to append the link for the request. For more information see [here](https://github.com/InitialState/wunderground-sensehat/wiki/Part-1.-How-to-Use-the-Wunderground-API)
+ - Optional: the Apache Server for the future project of having a local webpage / maintenance 

So what do you need:  
+ Raspberry Pi 
+ Internet connectivity 
+ RGB LED-strip with 3 Pins for RGB and 1 Strip for power (I have used a length of 3m but shorter is also fine depending of how much of the strip you want to use) (I used the following [strips](https://www.amazon.com/gp/product/B073NXF8B7/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1), and split the power line between 2 of these off a single USB port. I used the MOSFETS below as regulators,  
+ A breadboard or perfboard (for the second option you’ll of course need a soldering iron too, I recommend this since it’s a bit more permanent and also saves space)
+ Some jumper wires (male to male, male to female)  
+ Six MOSFETs (IRLZ34N)  
+ A power jack and / or USB Power Supply  
+ - optional - Multiple socket strip (with at least two sockets, I used one with three sockets because they are more common). I have chosen a lenght of 5 meters, just keep in mind it has to run up to the ceiling, along the ceiling and then to the power outlet. (depends on how you are getting power to the device.  
For the lamp itself I recommend the following:  
+ A 5 liter (or 1 gallon) plastic bottle (or a similarly big container of see-through material. Some people are using these IKEA paper lanterns but I do not recommend them since they could theoretically burn)  
+ Cotton batting. For the 5 liter bottle I needed about 100g, i have SO much left over now! I have used [this](https://www.idee-shop.com/shop/de/dieprodukte/Basteln/Bastelmaterial/FuellmaterialFell/Fuellwatteweiss250g.html)  
+ A "cool" glue gun or similar to attach the batting to the bottle  

If Making a true "Lamp" like I did
+ A light socket to power adapter


If Hanging
+ Some fishing line (clear string might work too but keep in mind that it will be a bit heavy in the end)  
+ A hook for your ceiling  
This seems to be a lot of stuff at first glance. But I didn’t have any of this just lying around and still managed to stay well under 150 € with this project (including the Raspberry Pi 3). If you’re using a Raspberry Pi Zero or do have a Pi lying around you will not spend more than 100 €).  

Ok, so what do you need to do? This:  
+ optional, inital designer started by cutting the LED strip to lengh. I used one strip of two segments (with 3 LEDs each) and one of three segments. But I recommend to use a bit more. 4 and 5 segments should be fine I think. I think having a longer and a shorter segment helps the effect since it gives it a bit of “imbalance”.... I left my strips alone and just balled them up in the container.
+ Set up two circuits according to this [Tutorial](http://popoklopsi.github.io/RaspberryPi-LedStrip/#!/)
+ To tweak the above tutorial for two strips you should keep two things in mind: first you will need a common ground for all the MOSFETs. But the 12 V should run directly from the end of the first strip to the beginning of the second. I have used jumper cables soldered to the strips and the perfboard, but any kind of cable should work.  
+ Ideally, the GPIO-pins should be connected as follows (one half follows the above tutorial; I will call them Strip A and Strip B here):  
+ Red A: GPIO 17, Blue A: GPIO 22, Green A: 24  
+ Red B: GPIO 26, Blue B: GPIO 12, Green B: 13
+ Since the Pi B does not have the Second strips pin layout. I went with Red B 27, Blue 23, Green 25. You'll also have to adjust the source code for the new pin layout (look for sites for the Pi B pin layout on the internet to make sure you got it right)
+ Now is a good moment to plug in the Raspberry Pi and its power supply. Use the multiple socket strip because they should run on the same power cord (since mine is on USB... they are on different USB ports). Keep the cables as short as possible. I just rolled them up and bound them together. Some people say you should not do this, I guess with such low Voltages there is no risk but be aware that I can not be held responsible if anything goes wrong with your electronics)  
+ To test the LEDs you should open a terminal and type the following “sudo pigpiod”, press enter and then “pigs p 26 255 p 13 255 p 12 255 p 17 255 p 22 255 p 24 255” (or adjust for the pins listed above if programing on the old model). When you press enter again, both LED strips should be completely white. If it doesn’t work please check if you connected everything correctly. You can try out other colours by changin the value 255 to something else. Experiment a bit, expecially how to get a good yellow. I suspect that the correct values for yellow change from strip to strip.  
+ Now we’ll have a look at the code. In the beginning you will have to insert the API key you got earlier from WeatherUndergound and the location for appending the link of the request. You can also decide at which time the lamp should display the forecast for the next day by changing the number of the variable switch_time (if you always want to display the weather for the moment just set it to 24).  
+ If you fill in all the variables correctly we are already done here. To see if you have the correct data for it, insert it in the according places here and check this [link](http://api.wunderground.com/api/ API-KEY /forecast/q/ LOCATION .json)  
+ I recommend trying this first because if something is not working, the problem lies probably in the weather forecast request.  
+ It’s all working and you can see a text forecast for your location? Good, then we will install the code on the Pi now. For this you just have to copy it into the home/pi (or whatever is your username) folder of your Pi and safe it as cloudy-a.py (do this by the method you prefer, either by ssh or directly with a USB stick for example) and run “sudo chmod +x cloudy-a.py” while being in that folder.  
+ Now is probably a good time to see if we can get some lights, eh? Run the code with “sudo pigpiod” followed by “python cloudy-a.py”. When you have been sufficiently blinded by the LEDs, press CTRL-C to stop.  
+ If you are happy with starting the script every time manually, you can skip the next few steps and start building the actual lamp.But who wants to do that, right? So on we go:  
+ Create a new file in the home/pi (again: or whatever is your username) directory: navigate to the folder in the terminal and type “sudo nano launcher.sh” You will have created a new file where you should write the following:  
    #!/bin/sh  
    launcher.sh  
	    cd /  
	    cd home/pi  
	    sudo python cloudy-a.py  
	    cd /  
+ We now have to set up rules that this file is executed on every startup. For that you type in the terminal “sudo crontab -e”. At the end of the file insert the following two lines:  
	    @reboot /usr/bin/pigpiod  
	    @reboot /home/pi/launcher.sh    
+ Close the file with CTRL-X and restart with “sudo reboot”. Now the LED strips should light up according to the weather forecast already. We are finally ready to build the lamp!  

Just some notes: When you finished the lamp, put the Raspberry Pi, the breadboard or perfboard and the LED-strips all in and have everything attached to the socket strip adapter.  I used a rectangular 1 gallon watter bottle. I cut the bottom open for easy access, and kept the cutout as a lid I could tape shut. I also added some air holes on the top for ventalation and kept the opening of the jug open for even more air flow. On the bottom I cut a hole perfect for the lamp to hold the jug, and since the lamp had a threaded piece to it, I was able to secure it down.

The designer bought a cheap timeclock because they didn’t want the lamp to be switched on all the time, but obviusly this is up to you. The program is set up so that it will finish the cycle of animation about every hour (and can be adjusted in code). It will then check for the forecast again and start the according animation. 

Anyway, now everything should be finished and you have a working weather forecast cloud lamp. I want to stress again that I can not be held responsible for any damages of injuries that might occur in the making or running of this project. Of course I can also not guarantee that it will work for you even if you follow all the steps correctly. If you have suggestions I would be happy to hear them. I will try to answer questions but don’t count on it. Now I would be very happy to see your creations!  


Photos of my project can be found [here!](https://photos.app.goo.gl/HpOL2VZhOtbpGhuh1)
