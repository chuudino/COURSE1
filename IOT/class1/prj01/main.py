from machine import Pin, PWM
from time import sleep

freq = 1000
led = PWM(Pin(2), freq=freq, duty=0)

while True:
    led.duty(0)
    sleep(2)
    led.duty(700)
    sleep(2)
    led.duty(1023)
    sleep(1)
