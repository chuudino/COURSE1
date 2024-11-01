import requests
import os
import sys

############################設定工作目錄############################
os.chdir(sys.path[0])

############################定義常數############################
API_KEY = "892da2f13edf3c7f382637760e72d224"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
ICON_BASE_URL = "https://openweathermap.org/img/wn/"
UNITS = "metric"
LANG = "zh_tw"
############################主程式############################
city_name = "taipei"
send_Url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"
print(send_Url)
response = requests.get(send_Url)
info = response.json()
if "main" in info:
    city = info["name"]
    temp = info["main"]["temp"]
    description = info["weather"][0]["description"]
    icon_code = info["weather"][0]["icon"]
    print(f"城市: {city}\n溫度: {temp}℃\n說明: {description}")

    icon_url = f"{ICON_BASE_URL}{icon_code}.png"
    print(icon_url)
    icon_response = requests.get(icon_url)
    if icon_response.status_code == 200:
        icon_image = icon_response.content
        with open("weather_icon.png", "wb") as f:
            # with 開啟檔案可以在程式結束後自動關閉檔案，as f 則是將檔案開啟後存到變數中
            # wb 是寫入模式，可以寫入二進位檔案，也可以寫入文字檔案
            f.write(icon_image)  # 寫入檔案
        print("圖片已下載")
    else:
        print("圖片下載失敗")
