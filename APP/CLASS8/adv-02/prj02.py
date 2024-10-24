#######################匯入模組#######################
from tkinter import *  #

#######################全域變數########################
cnt = 0


#######################定義函數########################
def hi_fun():
    global cnt
    cnt += 1
    if cnt % 2 == 1:
        display = Label(windows, Text="Green", fg="black", bg="green")
    else:
        display = Label(windows, Text="Red", fg="black", bg="red")


#######################建立視窗########################
windows = Tk()

# 設定視窗標題
windows.title("Exercise 2 - 2024/09/27 CLASS 8")

# 設定視窗大小
windows.geometry("800x600")

#######################建立按鈕########################
btn = Button(windows, text="Click Me!", command=hi_fun)
btn.pack()

#######################運行應用程式########################

windows.mainloop()  # 進入主迴圈
