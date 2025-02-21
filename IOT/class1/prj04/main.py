from machine import Pin, PWM
from time import sleep

RED = Pin(14, Pin.OUT)
GREEN = Pin(12, Pin.OUT)
BLUE = Pin(13, Pin.OUT)
RED.value(0)
GREEN.value(0)
BLUE.value(0)

while True:
    RED.value(1)  # 紅燈
    sleep(1)
    RED.value(0)  # 紅燈熄滅
    GREEN.value(1)  # 綠燈
    sleep(1)
    GREEN.value(1)  # 綠燈
    RED.value(1)  # 紅燈
    # 這樣可以變成黃燈
    sleep(1)
    GREEN.value(0)  # 綠燈熄滅
