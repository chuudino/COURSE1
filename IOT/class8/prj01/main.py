import time  # 匯入時間相關模組
import mcu
import ssd1306
from machine import I2C, Pin

global_msg = ""


def on_message(topic, msg):
    global global_msg
    global_msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"Received message on topic '{topic}': {global_msg}")


# 建立 mcu.gpio 物件，方便後續控制腳位
gpio = mcu.gpio()
led = mcu.led(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7, pwm=True)
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


# 請替換成您的 WIFI 認證資訊
WIFI_SSID = "Singular_AI"
WIFI_PASSWORD = "Singular#1234"
# WIFI_SSID = "Dino Chuu"
# WIFI_PASSWORD = "0937524990"

# 建立 mcu.wifi 物件
wifi = mcu.wifi(WIFI_SSID, WIFI_PASSWORD)
wifi.connect()

# 建立 MQTT 客戶端並連接到 MQTT 代理伺服器
mqtt_client = mcu.MQTT(
    client_id="dino",
    server="mqtt.singularinnovation-ai.com",
    user="singular",
    password="Singular#1234",
    keepalive=60,
)

mqtt_client.connect()  # 連接到 MQTT 代理伺服器
mqtt_client.subscribe("dino", on_message)  # 訂閱主題 "dino" 並設定回呼函式

# 主程式迴圈，目前尚未執行其他功能
while True:
    oled.fill(0)  # 清除顯示內容
    oled.text("MQTT LED Control", 0, 0)
    oled.text("Topic: dino", 0, 8)
    oled.text("Msg: " + global_msg, 0, 16)
    mqtt_client.check_msg()  # 檢查是否有收到新的 MQTT 訊息
    if global_msg == "ON":
        led.led_open(1023, 1023, 1023)  # 白光
    elif global_msg == "OFF":
        led.led_open(0, 0, 0)  # 關閉
    oled.show()
    time.sleep(0.5)
