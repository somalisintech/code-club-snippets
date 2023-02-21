from machine import Pin
from time import sleep

leds = [
    Pin(21, Pin.OUT), 
    Pin(20, Pin.OUT), 
    Pin(19, Pin.OUT), 
    Pin(18, Pin.OUT)
    ]

for led in leds:
    led.off()


while True:
    # ----------->>>>
    for led in leds:
        led.toggle()
        sleep(0.1)
        led.toggle()
    # <<<<-----------
    for led in reversed(leds):
        led.toggle()
        sleep(0.1)
        led.toggle()