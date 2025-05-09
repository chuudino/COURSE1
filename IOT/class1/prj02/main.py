from machine import Pin, PWM
from time import sleep

freq = 1000
led = PWM(Pin(2), freq=freq, duty=0)

while True:
    for duty in range(0, 1024, 10):
        led.duty(duty)
        sleep(0.025
    for duty in range(1023, -1, -10):
        led.duty(duty)
        sleep(0.025)
