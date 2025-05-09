from machine import Pin, ADC  # 匯入控制腳位與類比輸入的模組
from time import sleep  # 匯入延遲時間的 sleep 函式
import mcu  # 匯入自訂的 mcu 模組
import network  # 匯入網路連線模組
import time  # 匯入時間相關模組


# 定義連接 WiFi 的函式，ssid: WiFi 名稱, password: WiFi 密碼
def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)  # 建立 WiFi 連線物件，設定為工作站模式
    wlan.active(True)  # 啟用 WiFi

    networks = wlan.scan()  # 掃描並顯示可用的網路
    print("Available networks:")
    for net in networks:
        # 顯示每個網路的 SSID 與訊號強度
        print(f"SSID: {net[0].decode()}, Signal strength: {net[3]}%")

    if not wlan.isconnected():  # 如果尚未連線，則嘗試連線
        print("Connecting to network...")
        wlan.connect(ssid, password)  # 連線到指定 WiFi
        while not wlan.isconnected():  # 等待連線成功
            time.sleep(1)
    print("Network configuration:", wlan.ifconfig())  # 顯示網路連線資訊


# 建立 mcu.gpio 物件，方便後續控制腳位
gpio = mcu.gpio()
# 請替換成您的 WIFI 認證資訊
WIFI_SSID = "Singular_AI"
WIFI_PASSWORD = "Singular#1234"

# 連接 WIFI
connect_wifi(WIFI_SSID, WIFI_PASSWORD)

# 主程式迴圈，目前尚未執行其他功能
while True:
    pass
