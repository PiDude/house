#!/bin/sh

# +3.3 is wired to the middle lead of switch.
# GPIO pin is wired to the end lead of switch

# DHT22 is GPIO24

# door #1 is GPIO4
# door #2 is GPIO17
# door #3 is GPIO_XX
# door #4 is GPIO_YY
# door #5 is GPIO_ZZ


import RPi.GPIO as GPIO     ## Import GPIO library
import time
import datetime
import Adafruit_DHT



GPIO.setmode(GPIO.BCM) ## Use chip numbering

GPIO.setup(4,  GPIO.IN, pull_up_down=GPIO.PUD_UP) ## door 1. setup GPIO pin 4 to input
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # door 2
GPIO.setup(XX, GPIO.IN, pull_up_down=GPIO.PUD_UP) # door 3
GPIO.setup(YY, GPIO.IN, pull_up_down=GPIO.PUD_UP) # door 4
GPIO.setup(ZZ, GPIO.IN, pull_up_down=GPIO.PUD_UP) # door 5


#set up temp and humidity sensor on GPIO24

sensor = Adafruit_DHT.DHT22      # use either DHT11 or DHT22
pin = 24


#print (time.strftime("%m/%d/%Y"))
#print (time.strftime("%I:%M:%S"))
print datetime.datetime.now()
print '\n'


#door is open when current is flowing.   when door is closed, 
#it is an open circuit, current will not flow so pin will be False.


if GPIO.input(4):
    print 'initial state:  door #1 is open'
else:
    print 'initial state: door #1 is closed'


if GPIO.input(17):
    print 'initial state: door #2 is open'
else:
    print 'initial state: door #2 is closed'




if GPIO.input(XX):
    print 'initial state:  door #3 is open'
else:
    print 'initial state: door #3 is closed'


if GPIO.input(YY):
    print 'initial state:  door #4 is open'
else:
    print 'initial state: door #4 is closed'


if GPIO.input(ZZ):
    print 'initial state:  door #5 is open'
else:
    print 'initial state: door #5 is closed'


print '\n'



        
def door_1(channel):
    print datetime.datetime.now()
  
    if GPIO.input(4):
        print 'door #1 is open' 
    else:
        print 'door #1 is closed'

    print '\n'



def door_2(channel):
    print datetime.datetime.now()
    
    if GPIO.input(17):             #if True, switch is closed (door open)
        print 'door #2 is open'
    else:
        print 'door #2 is closed'  #if False, switch is open (door closed)

    print '\n'



def door_3(channel):
    print datetime.datetime.now()
  
    if GPIO.input(XX):
        print 'door #3 is open' 
    else:
        print 'door #3 is closed'

    print '\n'


        
def door_4(channel):
    print datetime.datetime.now()
  
    if GPIO.input(YY):
        print 'door #4 is open' 
    else:
        print 'door #4 is closed'

    print '\n'


        
def door_5(channel):
    print datetime.datetime.now()
  
    if GPIO.input(ZZ):
        print 'door #5 is open' 
    else:
        print 'door #5 is closed'

    print '\n'




#set interrupts to check for change on door reed switches
#door closed = switch open = no current flowing = False
#door open = switch closed = current flowing = True
    
GPIO.add_event_detect(4,  GPIO.BOTH, callback=door_1, bouncetime=300)
GPIO.add_event_detect(17, GPIO.BOTH, callback=door_2, bouncetime=300)
GPIO.add_event_detect(XX, GPIO.BOTH, callback=door_3, bouncetime=300)
GPIO.add_event_detect(YY, GPIO.BOTH, callback=door_4, bouncetime=300)
GPIO.add_event_detect(ZZ, GPIO.BOTH, callback=door_5, bouncetime=300)



#loop to:
#  a) wait for door switch interrupts
#  b) occationally read temperature
#  c) button push shuts down the R.Pi

        
n=0

while n < 10:
    n=n+1
#    print n

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)  #read DHT22
    temperature = (((temperature *9.0) / 5.0) + 32.0)   #convert to Celcius

    if humidity is not None and temperature is not None:
        print 'Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity)
    else:
        print 'Failed to get reading.  Try again.'
   
    
    time.sleep(5)



GPIO.cleanup()


