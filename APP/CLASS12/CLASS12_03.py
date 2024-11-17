import requests
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import datetime

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
xlist = []
ylist = []
if "list" in info:
    for forecast in info["list"]:
        dt_txt = forecast["dt_txt"]
        temp = forecast["main"]["temp"]
        time = datetime.datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").strftime(
            "%m/%d %H"
        )
        xlist.append(time)
        ylist.append(temp)
        weather_description = forecast["weather"][0]["description"]
        print(f" {dt_txt}\n溫度: {temp}℃\n天氣狀況: {weather_description}")
else:
    print("找不到該城市或無法獲取天氣資訊")

############################繪製圖表############################
font = FontProperties(fname="LXGWWenKaiTC-Regular.ttf", size=20)
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(xlist, ylist)
ax.set_xlabel("時間", fontproperties=font)
ax.set_ylabel("溫度", fontproperties=font)
ax.set_title("天氣預報", fontproperties=font)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("forecast.png")
plt.show()
