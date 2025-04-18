from machine import Pin, ADC
from time import sleep
import mcu

gpio = mcu.gpio()
light_sensor = ADC(0)  # 光敏電阻

while True:
    light_value = light_sensor.read()  # 讀取光敏電阻的值
    print(f"Light Value: {light_value}")  # 打印光敏電阻的值
    sleep(0.5)  # 每秒讀取一次
