import requests
import os
import sys
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import datetime
from ttkbootstrap import *
from PIL import Image, ImageTk


############################設定工作目錄############################
os.chdir(sys.path[0])

############################定義常數############################
API_KEY = "892da2f13edf3c7f382637760e72d224"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
ICON_BASE_URL = "https://openweathermap.org/img/wn/"
UNITS = "metric"
LANG = "zh_tw"


############################主程式############################
def get_weather():
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
            time = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").strftime("%m/%d %H")
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
    fig.savefig("forecast.png")
    image = Image.open("forecast.png")
    image = ImageTk.PhotoImage(image)
    label1["image"] = image
    label1.image = image


#######################建立視窗########################
window = tk.Tk()
window.title("Weather.App")  # 設定視窗標題

#######################設定字型########################
font_size = 26
window.option_add("*Font", f"TimesNewRoman {font_size}")

#######################設定主題########################
style = Style(theme="simplex")
style.configure("my.TCheckbutton", font=(f"TimesNewRoman {font_size}"))
style.configure("my.TLabel", font=(f"TimesNewRoman {font_size}"))
style.configure("my.TEntry", font=(f"TimesNewRoman {font_size}"))
style.configure("my.TButton", font=(f"TimesNewRoman {font_size}"))

check_type = BooleanVar()
check_type.set(True)

#######################建立按鈕########################
# 按鈕要連動function，command=函數名稱
btn1 = Button(window, text="顯示圖表", style="my.TButton", command=get_weather)
btn1.grid(row=1, column=0)

#######################建立標籤########################
label1 = Label(window, text="", style="my.TLabel")
label1.grid(row=0, column=0, sticky="nsew")


######################運行應用程式########################
window.mainloop()  # 進入主迴圈
