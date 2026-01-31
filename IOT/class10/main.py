import time  # 匯入時間相關模組
import mcu
import ssd1306
from machine import I2C, Pin, ADC
import dht
import json

global_msg = ""


def on_message(topic, msg):
    global global_msg
    global_msg = msg.decode("utf-8")
    topic = topic.decode("utf-8")
    print(f"Received message on topic '{topic}': {global_msg}")


def display_message(init_y, msg):
    max_chars_per_line = 16
    for i in range(0, len(msg), max_chars_per_line):
        oled.text(msg[i : i + max_chars_per_line], 0, init_y)
        init_y += 8


# 建立 mcu.gpio 物件，方便後續控制腳位
gpio = mcu.gpio()
led = mcu.led(r_pin=gpio.D5, g_pin=gpio.D6, b_pin=gpio.D7, pwm=True)
i2c = I2C(scl=Pin(gpio.D1), sda=Pin(gpio.D2))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)
light_sensor = ADC(0)  # 光敏電阻
dht_sensor = dht.DHT11(Pin(gpio.D0, Pin.IN))  # DHT11 溫濕度感測器
mp3 = mcu.MP3()


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

pub_counter = 0
home_sensor = {}
# 主程式迴圈，目前尚未執行其他功能
while True:
    dht_sensor.measure()
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    light_value = light_sensor.read()  # 讀取光敏電阻的值

    home_sensor["temperature"] = temperature
    home_sensor["humidity"] = humidity
    home_sensor["light"] = light_value
    home_sensor_json = json.dumps(home_sensor)
    # 讀取Json資料範例: data = json.loads(home_sensor_json)
    # print("Temperature:", data["temperature"])

    oled.fill(0)  # 清除顯示內容
    oled.text("MQTT LED Control", 0, 0)
    oled.text("Topic: dino", 0, 8)
    oled.text(f"Light: {light_value}, {round(light_value * 100 / 1024)}%", 0, 16)
    oled.text(f"T:{temperature}C", 0, 24)
    oled.text(f"H:{humidity}%", 0, 32)
    display_message(40, "Msg: " + global_msg)
    mqtt_client.check_msg()  # 檢查是否有收到新的 MQTT 訊息
    if global_msg == "ON":
        led.led_open(1023, 1023, 1023)  # 白光
    elif global_msg == "OFF":
        led.led_open(0, 0, 0)  # 關閉
    elif global_msg == "AUTO":
        led.led_open(light_value, light_value, light_value)  # 自動調整亮度
    elif global_msg == "PLAY":
        mp3.start(volume=100, song=1)  # 播放音樂
        time.sleep(5)
        mp3.stop()

    if pub_counter >= 5:
        pub_counter = 0
        mqtt_client.publish("dino_home", home_sensor_json)
    pub_counter += 1
    global_msg = ""
    oled.show()
    time.sleep(1)
