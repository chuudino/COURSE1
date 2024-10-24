#######################匯入模組#######################
from tkinter import *

#######################全域變數########################
cnt = 0


#######################定義函數########################
def hi_fun1():
    display = Label(windows, text="Hi Singular", fg="red", bg="black")
    display.pack()
    
def hi_fun2():
    display = Label(windows, hide text/btn1)
    display.pack()


#######################建立視窗########################
windows = Tk()

# 設定視窗標題
windows.title("Exercise 01 - 2024/09/27 CLASS 8")

# 設定視窗大小
windows.geometry("800x600")

#######################建立按鈕########################
btn1 = Button(windows, text="Show Screen", command=hi_fun)
btn1.pack()

btn2 = Button(windows, text="Clear Screen", command=hi_fun)
btn2.pack()

#######################運行應用程式########################

windows.mainloop()  # 進入主迴圈
