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
        print("Hello singular")


#######################建立視窗########################
# 創建主視窗
# windows = tkinter.Tk()
# windows = tk.Tk()
windows = Tk()

# 設定視窗標題
windows.title("My First GUI Program")

# 設定視窗大小
windows.geometry("800x600")

#######################建立按鈕########################
btn1 = Button(windows, text="click me!", command=hi_fun)
btn1.pack()

#######################運行應用程式########################

windows.mainloop()  # 進入主迴圈
