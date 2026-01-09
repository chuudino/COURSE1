import sys

# 這份程式是給 ESP8266/ESP32 的 MicroPython 使用
if sys.implementation.name != "micropython":
    raise SystemExit(
        "這是 MicroPython 程式，請用開發板上的 MicroPython 執行。\n"
        "你目前用的是 Windows Python（CPython），所以會出現找不到 'machine' 的錯誤。\n"
        "建議：用 Thonny 選 MicroPython(ESP32/ESP8266) 或用 mpremote 上傳/執行。"
    )

from machine import Pin, PWM
from time import sleep

freq = 1000
led = PWM(Pin(2), freq=freq, duty=0)

while True:
    for duty in range(0, 1024, 10):
        led.duty(duty)
        sleep(0.025)
    for duty in range(1023, -1, -10):
        led.duty(duty)
        sleep(0.025)
