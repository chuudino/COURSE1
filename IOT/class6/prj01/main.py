import sys

# 這份程式是給 ESP8266/ESP32 的 MicroPython 使用；在 Windows 的 CPython 會缺少 machine/network 等模組。
if sys.implementation.name != "micropython":
    raise SystemExit(
        "這是 MicroPython 程式，請用開發板上的 MicroPython 執行。\n"
        "你目前用的是 Windows Python（CPython），所以會出現找不到 'machine' 的錯誤。\n"
        "建議：用 Thonny 選 MicroPython(ESP32/ESP8266) 或用 mpremote 上傳/執行。"
    )

import time  # 匯入時間相關模組
import mcu  # 匯入自訂的 mcu 模組


# 建立 mcu.gpio 物件，方便後續控制腳位
gpio = mcu.gpio()

led = mcu.led(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7, pwm=True)

# 請替換成您的 WIFI 認證資訊
# WIFI_SSID = "Singular_AI"
# WIFI_PASSWORD = "Singular#1234"
WIFI_SSID = "Dino Chuu"
WIFI_PASSWORD = "0937524990"

# 建立 mcu.wifi 物件
wifi = mcu.wifi(WIFI_SSID, WIFI_PASSWORD)
wifi.connect()

# 主程式迴圈，目前尚未執行其他功能
while True:
    led.led_open(1023, 1023, 1023)  # 白光
    time.sleep(1)
    led.led_open(512, 512, 512)  # 淡白光
    time.sleep(1)
    led.led_open(0, 0, 0)  # 關閉
    time.sleep(1)
