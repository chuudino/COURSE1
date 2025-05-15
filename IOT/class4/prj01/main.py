import mcu
from machine import Pin, PWM, ADC  # 替換 machine 模組
from time import sleep

gpio = mcu.gpio()
freq = 1000  # 頻率
duty = 0  # 工作週期
light_sensor = ADC(0)  # 光敏電阻
RED = PWM(Pin(gpio.D5), freq=freq, duty=duty)  # 紅燈
GREEN = PWM(Pin(gpio.D6), freq=freq, duty=duty)  # 綠燈
BLUE = PWM(Pin(gpio.D7), freq=freq, duty=duty)  # 藍燈

while True:
    light_value = light_sensor.read()  # 讀取光敏電阻的值
    print(f"value={light_value}, {round(light_value * 100 / 1024)}%")
    RED.duty(light_value)
    GREEN.duty(light_value)
    BLUE.duty(light_value)
    sleep(1.0)
