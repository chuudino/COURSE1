from ttkbootstrap import *
import sys
import os

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄


#######################定義函數########################
def show_result():
    check1.configure(text=str(check_type.get()))


#######################建立視窗########################
window = tk.Tk()
window.title("COURSE 10_01")  # 設定視窗標題

#######################設定字型########################
font_size = 26
window.option_add("*Font", f"TimesNewRoman {font_size}")

#######################設定主題########################
style = Style(theme="simplex")
style.configure("my.TCheckbutton", font=(f"TimesNewRoman {font_size}"))

check_type = BooleanVar()
check_type.set(False)

######################建立check button########################
check1 = Checkbutton(
    window,
    text=str(check_type.get()),
    style="my.TCheckbutton",
    variable=check_type,
    command=show_result,
    onvalue=True,
    offvalue=False,
)
check1.grid(row=0, column=0, padx=10, pady=10, sticky="NEWS")

######################運行應用程式########################
window.mainloop()  # 進入主迴圈
