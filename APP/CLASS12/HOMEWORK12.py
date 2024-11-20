from ttkbootstrap import *
import sys
import os
from PIL import Image, ImageTk
import requests
import datetime
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄

############################定義常數############################
API_KEY = "892da2f13edf3c7f382637760e72d224"
BASE_URL = "https://api.openweathermap.org/data/2.5/forecast?"
ICON_BASE_URL = "https://openweathermap.org/img/wn/"
UNITS = "metric"
LANG = "zh_tw"


#######################定義函數########################
def change_temp():
    global UNITS, ylist
    UNITS = "metric" if check_type.get() else "imperial"

    if temp_label["text"] != "溫度:?℃":
        if UNITS == "metric":
            temp = round((ylist[0] - 32) * 5 / 9, 2)
        else:
            temp = round((ylist[0] * 9 / 5) + 32, 2)
        temp_label["text"] = f"溫度: {temp}{'℉' if UNITS == 'imperial' else '℃'}"


def get_weather():
    global xlist, ylist, descriptionlist, iconlist
    city_name = entry1.get()
    send_Url = f"{BASE_URL}appid={API_KEY}&q={city_name}&units={UNITS}&lang={LANG}"
    response = requests.get(send_Url)
    info = response.json()
    xlist = []
    ylist = []
    descriptionlist = []
    iconlist = []
    if "list" in info:
        city = info["city"]["name"]
        print(f"城市: {city}")
        for forecast in info["list"]:
            dt_txt = forecast["dt_txt"]
            temp = forecast["main"]["temp"]
            time = datetime.datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S").strftime(
                "%m/%d %H"
            )
            weather_description = forecast["weather"][0]["description"]
            icon_code = forecast["weather"][0]["icon"]
            xlist.append(time)
            ylist.append(temp)
            descriptionlist.append(weather_description)
            iconlist.append(icon_code)
            print(f"日期與時間:{time}\n溫度: {temp}℃\n天氣狀況: {weather_description}")

        icon_url = f"{ICON_BASE_URL}{iconlist[0]}.png"
        print(icon_url)
        icon_response = requests.get(icon_url)
        if icon_response.status_code == 200:
            icon_image = icon_response.content
            with open("weather_icon.png", "wb") as f:
                # with 開啟檔案可以在程式結束後自動關閉檔案，as f 則是將檔案開啟後存到變數中
                # wb 是寫入模式，可以寫入二進位檔案，也可以寫入文字檔案
                f.write(icon_image)  # 寫入檔案
            print("圖片已下載")
            image = Image.open("weather_icon.png")
            image = ImageTk.PhotoImage(image)
            icon_label["image"] = image  # icon_label.config(image=image)
            icon_label.image = image
        else:
            print("圖片下載失敗")

        temp_label["text"] = f"溫度: {ylist[0]}{'℉' if UNITS == 'imperial' else '℃'}"
        description_label["text"] = f"描述: {descriptionlist[0]}"

    else:
        description_label["text"] = "沒有找到城市"

    ############################繪製圖表############################
    font = FontProperties(fname="LXGWWenKaiTC-Regular.ttf", size=20)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(xlist, ylist)
    ax.set_xlabel("日期與時間", fontproperties=font)
    ax.set_ylabel("溫度℃", fontproperties=font)
    ax.set_title("7天的氣溫預測", fontproperties=font)
    plt.xticks(rotation=45)
    plt.tight_layout()
    fig.savefig("forecast.png")
    image = Image.open("forecast.png")
    image = ImageTk.PhotoImage(image)
    label2["image"] = image
    label2.image = image


#######################建立視窗########################
window = tk.Tk()
window.title("Weather forecast.App")  # 設定視窗標題

#######################設定字型########################
font_size = 20
window.option_add("*Font", f"TimesNewRoman {font_size}")

#######################設定主題########################
style = Style(theme="simplex")
style.configure("my.TCheckbutton", font=(f"TimesNewRoman {font_size}"))
style.configure("my.TLabel", font=(f"TimesNewRoman {font_size}"))
style.configure("my.TEntry", font=(f"TimesNewRoman {font_size}"))
style.configure("my.TButton", font=(f"TimesNewRoman {font_size}"))

check_type = BooleanVar()
check_type.set(True)


######################建立標籤########################
label1 = Label(window, text="請輸入想搜尋的城市:", style="my.TLabel")
label1.grid(row=0, column=0)
icon_label = Label(window, text="天氣圖標", style="my.TLabel")
icon_label.grid(row=1, column=0)
temp_label = Label(window, text="溫度:?℃", style="my.TLabel")
temp_label.grid(row=1, column=1)
description_label = Label(window, text="描述:?", style="my.TLabel")
description_label.grid(row=1, column=2)

label2 = Label(window, text=" ", style="my.TLabel")
label2.grid(row=4, column=0, padx=10, pady=10, columnspan=3)


#######################建立按鈕########################
# 按鈕要連動function，command=函數名稱
btn1 = Button(window, text="獲得天氣資料", style="my.TButton", command=get_weather)
btn1.grid(row=0, column=2)


######################建立輸入框########################
entry1 = Entry(window, width=30, style="my.TEntry")
entry1.grid(row=0, column=1)

######################建立check button########################
check1 = Checkbutton(
    window,
    text="溫度單位℃/℉",
    style="my.TCheckbutton",
    variable=check_type,
    command=change_temp,
    onvalue=True,
    offvalue=False,
)
check1.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

######################運行應用程式########################
window.mainloop()  # 進入主迴圈
