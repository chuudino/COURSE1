from umqtt.simple import MQTTClient
import sys
import time  # 匯入時間相關模組
import mcu

global_msg = ""


def on_message(topic, msg):
    global global_msg
    global_msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"Received message on topic '{topic}': {global_msg}")


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

# 建立 MQTT 客戶端並連接到 MQTT 代理伺服器
mqtt_client = MQTTClient(
    client_id="dino",
    server="mqtt.singularinnovation-ai.com",
    user="singular",
    password="Singular#1234",
    keepalive=60,
)

try:
    mqtt_client.connect()  # 連接到 MQTT 代理伺服器
except:
    sys.exit()
finally:
    print("Connected to MQTT broker")

mqtt_client.set_callback(on_message)  # 一定要寫在subscribe前面
mqtt_client.subscribe("dino")  # 訂閱主題

# 主程式迴圈，目前尚未執行其他功能
while True:
    mqtt_client.check_msg()  # 檢查是否有收到訊息
    mqtt_client.ping()  # 發送心跳包以保持連線
    if global_msg == "ON":
        led.led_open(1023, 1023, 1023)  # 白光
    elif global_msg == "OFF":
        led.led_open(0, 0, 0)  # 關閉
    time.sleep(0.5)
