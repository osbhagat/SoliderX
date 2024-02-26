from machine import Pin
from time import sleep
led = Pin(25,Pin.OUT)  # BuitIn led connected to 25 Pin
while(1):
    led.on()
    sleep(5)  #Giving 5 Sec delay
    led.off()
    sleep(5)  #Giving 5 Sec delay