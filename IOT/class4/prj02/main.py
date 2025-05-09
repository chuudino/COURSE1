from machine import Pin, ADC
from time import sleep
import mcu
import network
import time


def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    # 掃描並顯示可用的網路
    networks = wlan.scan()
    print("Available networks:")
    for net in networks:
        print(f"SSID: {net[0].decode()}, Signal strength: {net[3]}%")

    if not wlan.isconnected():
        print("Connecting to network...")
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            time.sleep(1)
    print("Network configuration:", wlan.ifconfig())


gpio = mcu.gpio()
# 請替換成您的 WIFI 認證資訊
WIFI_SSID = "Singular_AI"
WIFI_PASSWORD = "Singular#1234"

# 連接 WIFI
connect_wifi(WIFI_SSID, WIFI_PASSWORD)


while True:
    pass
