#######################匯入模組#######################
# 匯入 tkinter 模組
# import tkinter
# import tkinter as tk
from tkinter import *  #
import os
import sys
from PIL import Image, ImageTk

#######################切換到當前目錄#######################
os.chdir(sys.path[0])  # 切換到當前目錄

#######################全域變數########################
cnt = 0


#######################定義函數########################
def hi_fun():
    global cnt
    cnt += 1
    if cnt % 3 == 0:
        # label1.config(text="Hello Singular!") # 修改標籤文字
        label1["text"] = "Hello Singular!"  # 修改標籤文字


#######################建立視窗########################
# 創建主視窗
# windows = tkinter.Tk()
# windows = tk.Tk()
windows = Tk()

# 設定視窗標題
windows.title("My First GUI Program")

# 設定視窗大小
windows.geometry("800x600")

# 設定按鈕與標籤文字大小
windows.option_add("*Button.Font", "TimesNewRoman 24")
windows.option_add("*Label.Font", "TimesNewRoman 24")

#######################建立按鈕########################
# 按鈕要連動function，command=函數名稱
btn1 = Button(windows, text="click me!", command=hi_fun)
btn1.pack()  # 放置按鈕到視窗上

#######################建立標籤########################
label1 = Label(windows, text="Hello World!")
label1.pack()  # 放置標籤到視窗上

#######################建立畫布########################
c_width = 800
c_height = 300
canvas = Canvas(windows, bg="white", width=c_width, height=c_height)
canvas.pack()

#######################載入圖片########################
# 載入圖片，只支援 GIF、PGM、PPM、PNG、BMP 格式
# img = PhotoImage(file="crocodile2.gif")
image = Image.open("crocodile2.gif")
# 使用ImageTk模組的PhotoImage方法建立圖片物件
img = ImageTk.PhotoImage(image)

#######################顯示圖片########################
# 在畫布上顯示圖片放到畫布正中央
my_img = canvas.create_image(c_width // 2, c_height // 2, image=img)

#######################運行應用程式########################

windows.mainloop()  # 進入主迴圈
