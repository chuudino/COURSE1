from ttkbootstrap import *
import sys
import os

#######################全域變數########################
cnt = 0


#######################定義函數########################
def hi_fun():
    global cnt
    cnt += 1
    if cnt % 2 == 1:
        label1.configure(text="Green", background="green")  # 修改標籤文字
    else:
        label1.configure(text="Red", background="red")  # 修改標籤文字


#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄

#######################建立視窗########################
window = tk.Tk()
window.title("COURSE 9 EX_02 - Change Label Content & Color")  # 設定視窗標題

#######################設定字型########################
font_size = 26
window.option_add("*Font", f"TimesNewRoman {font_size}")

#######################設定主題########################
style = Style(theme="simplex")
style.configure("my.TButton", font=(f"TimesNewRoman {font_size}"))
style.configure("my.TLabel", font=(f"TimesNewRoman {font_size}"))

#######################建立標籤########################
label1 = Label(window, text="  ", style="my.TLabel", anchor="center")
label1.grid(row=1, column=0, padx=10, pady=10)
# padx=10 設定與其他格子的左右邊距, pady=10 設定與其他格子的上下邊距, sticky="NEWS" 設定在格子中的顯示方式
# rowspan=2 設定格子的行數, columnspan=2 設定格子的列數

#######################建立按鈕########################
button1 = Button(window, text="Click Me", style="my.TButton", command=hi_fun)
button1.grid(row=0, column=0, padx=10, pady=10, sticky="NSWE")

#######################運行應用程式########################
window.mainloop()  # 進入主迴圈
