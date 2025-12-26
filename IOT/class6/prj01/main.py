from machine import Pin, ADC  # 匯入控制腳位與類比輸入的模組
from time import sleep  # 匯入延遲時間的 sleep 函式
import mcu  # 匯入自訂的 mcu 模組
import time  # 匯入時間相關模組


# 建立 mcu.gpio 物件，方便後續控制腳位
gpio = mcu.gpio()

led = mcu.led(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7, pwm=True)

# 請替換成您的 WIFI 認證資訊
WIFI_SSID = "Singular_AI"
WIFI_PASSWORD = "Singular#1234"
# WIFI_SSID = "Dino Chuu"
# WIFI_PASSWORD = "0937524990"

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
