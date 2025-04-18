from machine import Pin, PWM
from time import sleep
import mcu

gpio = mcu.gpio()
freq = 1000  # 頻率
duty = 0  # 工作週期
RED = PWM(Pin(gpio.D5), freq=freq, duty=duty)  # 紅燈
GREEN = PWM(Pin(gpio.D6), freq=freq, duty=duty)  # 綠燈
BLUE = PWM(Pin(gpio.D7), freq=freq, duty=duty)  # 藍燈
delay = 0.002  # 延遲時間

while True:
    for duty in range(0, 1024, 1):
        RED.duty(duty)
        GREEN.duty(1023 - duty)
        sleep(delay)

    for duty in range(0, 1024, 1):
        GREEN.duty(duty)
        BLUE.duty(1023 - duty)
        sleep(delay)

    for duty in range(0, 1024, 1):
        BLUE.duty(duty)
        RED.duty(1023 - duty)
        sleep(delay)
