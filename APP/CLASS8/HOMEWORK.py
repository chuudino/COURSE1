#######################匯入模組#######################
# 匯入 tkinter 模組
# import tkinter
# import tkinter as tk
from tkinter import *  #

#######################全域變數########################
cnt = 0


#######################定義函數########################
def hi_fun():
    global cnt
    cnt += 1
    if cnt % 3 == 0:
        # label1.config(text="Hello Singular!") # 修改標籤文字
        label1["text"] = ""  # 修改標籤文字


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

#######################運行應用程式########################

windows.mainloop()  # 進入主迴圈
