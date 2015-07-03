
# pin 1 to +3.3V
# pin 2 to GPIO pin
# pin 3 no connection
# pin 4 ground
# 10K Ohm resistor between pin 1 and pin 2



import RPi.GPIO as GPIO     ## Import GPIO library
import time
import datetime
import Adafruit_DHT
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



GPIO.setmode(GPIO.BCM) ## Use chip numbering


def sendit():
    mail = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    mail.set_debuglevel(1)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login('dxjones00', 'GOOGpwd1')
    mail.sendmail('dxjones00@gmail.com', 'dxjones00@yahoo.com', message.as_string())
    mail.quit()



#set up temp and humidity sensor
sensor = Adafruit_DHT.DHT22      # use either DHT11 or DHT22
pin = 24   #GPIO24


print datetime.datetime.now()
print '\n'
print time.time()
print '\n'

 #loop to kill time.
        
n=0

while n < 10:
    n=n+1
    print n

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temperature = ((temperature *9.0) / 5.0) +32.0  #convert Celcius to Farenheit

    if humidity is not None and temperature is not None:
        print 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity)

        inttemp = "{0:0.2f}".format(temperature)
        inthumidity = "{0:0.2f}".format(humidity)

        message = MIMEMultipart('alternative')
        message['Subject'] = "temp and humidity"
        text = 'temperature =  ' + inttemp + '    humidity =  ' + inthumidity
        part1 = MIMEText(text, 'plain')
        message.attach(part1)
        

        sendit()



    else:
        print 'Failed to get reading.  Try again.'
    
    time.sleep(10)



# GPIO.cleanup()




