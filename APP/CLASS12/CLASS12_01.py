import requests
import os
import sys

############################設定工作目錄############################
os.chdir(sys.path[0])

############################定義常數############################
API_KEY = "892da2f13edf3c7f382637760e72d224"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
ICON_BASE_URL = "https://openweathermap.org/img/wn/"
UNITS = "metric"
LANG = "zh_tw"
############################主程式############################
city_name = "taipei"
send_Url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"
print(send_Url)
response = requests.get(send_Url)
info = response.json()
if "list" in info:
    for forecast in info["list"]:
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        weather_description = forecast["weather"][0]["description"]
        print(f" {dt_txt}\n溫度: {temp}℃\n天氣狀況: {weather_description}")
else:
    print("找不到該城市或無法獲取天氣資訊")
