from machine import Pin, ADC
from time import sleep
import mcu


gpio = mcu.gpio()
light_sensor = ADC(0)  # 光敏電阻

while True:
    light_value = light_sensor.read()  # 讀取光敏電阻的值
    print(f"value={light_value}, {round(light_value * 100 / 1024)}%")
    sleep(1.0)  # 每秒讀取一次
