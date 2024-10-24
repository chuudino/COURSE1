#######################匯入模組#######################
from tkinter import *

#######################全域變數########################
cnt = 0


#######################定義函數########################
def hi_fun():
    display = Label(windows, text="Hi Singular", fg="red", bg="black")
    display.pack()


def clear_text():
    label.config(text="")


#######################建立視窗########################
windows = Tk()

# 設定視窗標題
windows.title("Exercise 01 - 2024/09/27 CLASS 8")

# 設定視窗大小
windows.geometry("800x600")

#######################建立顯示文本的標簽########################
label = Label(windows, text="Hi Singular")


#######################建立按鈕########################
btn1 = Button(windows, text="Show Screen", command=hi_fun)
btn1.pack()

btn2 = Button(windows, text="Clear Screen", command=clear_text)
btn2.pack()


#######################運行應用程式########################

windows.mainloop()  # 進入主迴圈
