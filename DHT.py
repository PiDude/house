
# pin 1 to +3.3V
# pin 2 to GPIO pin
# pin 3 no connection
# pin 4 ground
# 10K Ohm resistor between pin 1 and pin 2



import RPi.GPIO as GPIO     ## Import GPIO library
import time
import datetime
import Adafruit_DHT



GPIO.setmode(GPIO.BCM) ## Use chip numbering



#set up temp and humidity sensor
sensor = Adafruit_DHT.DHT22      # use either DHT11 or DHT22
pin = 24   #GPIO24


print datetime.datetime.now()
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
    else:
        print 'Failed to get reading.  Try again.'
    
    time.sleep(5)



# GPIO.cleanup()




