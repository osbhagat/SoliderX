from machine import Pin
from time import sleep
led = Pin(25,Pin.OUT)  # BuitIn led connected to 25 Pin
while(1):
    led.on()
    sleep(1)
    led.off()
    sleep(1)