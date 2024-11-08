from ttkbootstrap import *
import sys
import os

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄


#######################定義函數########################
def show1_result():
    check1.configure(text=str(check1_type.get()))


def show2_result():
    check2.configure(text=str(check2_type.get()))


#######################建立視窗########################
window = tk.Tk()
window.title("COURSE 10_01_1")  # 設定視窗標題
window.geometry("500x200")

#######################設定字型########################
font_size = 26
window.option_add("*Font", f"TimesNewRoman {font_size}")

#######################設定主題########################
style = Style(theme="simplex")
style.configure("my.TCheckbutton", font=(f"TimesNewRoman {font_size}"))

check1_type = BooleanVar()
check1_type.set(True)

check2_type = BooleanVar()
check2_type.set(True)
######################建立check button########################
check1 = Checkbutton(
    window,
    text=str(check1_type.get()),
    style="my.TCheckbutton",
    variable=check1_type,
    command=show1_result,
    onvalue=True,
    offvalue=False,
)
check1.grid(row=0, column=0, padx=10, pady=10, sticky="NEWS")

check2 = Checkbutton(
    window,
    text=str(check2_type.get()),
    style="my.TCheckbutton",
    variable=check2_type,
    command=show2_result,
    onvalue=True,
    offvalue=False,
)
check2.grid(row=0, column=1, padx=10, pady=10, sticky="NEWS")

######################運行應用程式########################
window.mainloop()  # 進入主迴圈
