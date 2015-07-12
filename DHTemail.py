
# pin 1 to +3.3V
# pin 2 to GPIO pin
# pin 3 no connection
# pin 4 ground
# 10K Ohm resistor between pin 1 and pin 2


#/bin/sh

import RPi.GPIO as GPIO
import os
import time
import datetime
import Adafruit_DHT
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ISStreamer.Streamer import Streamer



GPIO.setmode(GPIO.BCM) ## Use GPIO pin numbering


# define shutdown button.  one side to GPIO, the other to GROUND
GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_UP)


# define shutdown routine
def Shutdown(channel):
    GPIO.cleanup()
    os.system("sudo shutdown -h now")

GPIO.add_event_detect(4, GPIO.FALLING, callback = Shutdown, bouncetime = 2000)


#define opening email connection
def sendit():
    mail = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    mail.set_debuglevel(0)                # 0 is off.   1 has detail.
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login('dxjones00', 'GOOGpwd1')
    mail.sendmail('dxjones00@gmail.com', 'dxjones00@yahoo.com', message.as_string())
    mail.quit()



#set up temp and humidity sensor
sensor = Adafruit_DHT.DHT22      # use either DHT11 or DHT22
pin = 24   #GPIO24

streamer = Streamer(bucket_name="House Example", access_key="nO6joCK4pkzDDj7whCAJGJEHmhevYF73")
streamer.log("notes", "stream starting")





print datetime.datetime.now()
print '\n'


#loop to kill time.
        
# n=0   setting up an infinite loop.  only way to kill it is with GPIO shutdown buttone

while True:


    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = ((temperature *9.0) / 5.0) +32.0  #convert Celcius to Farenheit

    if humidity is not None and temperature is not None:
        print 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity)

        inttemp = "{0:0.2f}".format(temperature)
        inthumidity = "{0:0.2f}".format(humidity)

        streamer.log("temperature", inttemp)
        streamer.log("humidity", inthumidity)

        #message = MIMEMultipart('alternative')
        #message['Subject'] = "temp and humidity"
        #text = 'temperature =  ' + inttemp + '    humidity =  ' + inthumidity
        #part1 = MIMEText(text, 'plain')
        #message.attach(part1)
        
        #sendit()

        time.sleep(300)   #300 is every 5 minutes



    else:
        print 'Failed to get reading.  Try again.'
        streamer.log("notes", "missed sample")
    


streamer.log("notes", "stream done")

GPIO.cleanup()




