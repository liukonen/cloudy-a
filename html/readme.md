#Installing of HTML page
Here is my designed page for Cloudy Pie. You can install this either in a subdirectory or root of your apache server on your pi
Instructions:
+ Install Apache on your box
+ copy files to your server. On my machine, the root is located in /var/html/www while others are in var/html, so this might be different on your box
+ Configure your cloudy pie script to have WebInterfaceActive = True
+ Make sure that the WebInterfacePath is set to the path you are giving the cloudy pie html's folder
+ Restart your machine
+ After boot, navigate to your machines IP in a browser (192.168.XXX.XXX)/folder_you_gave_cloudyPie

The Python script should write out the output of the call out the door to WeatherUnderground out to the output.json file on the pi. 
It should also write out the last timestamp it was updated to LastUpdated.log
Any errors should log to error.log
The Index.html will rendor all forcasts returned and / or last update timestamp or errors recieved.
