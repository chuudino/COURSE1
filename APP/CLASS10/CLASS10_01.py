from ttkbootstrap import *
import sys
import os

#######################設定工作目錄########################
os.chdir(sys.path[0])  # 設定工作目錄


#######################定義函數########################
def show_result():
    entry_text = entry1.get()
    try:
        result = eval(entry_text)
    except:
        result = "輸入格式錯誤無法計算"
    label1.configure(text=result)


#######################建立視窗########################
window = tk.Tk()
window.title("COURSE 10_01")  # 設定視窗標題

#######################設定字型########################
font_size = 26
window.option_add("*Font", f"TimesNewRoman {font_size}")

#######################設定主題########################
style = Style(theme="simplex")
style.configure("my.TButton", font=(f"TimesNewRoman {font_size}"))
style.configure("my.TLabel", font=(f"TimesNewRoman {font_size}"))

#######################建立輸入########################
# Entry物件
entry1 = Entry(window, width=30)  # 建立Entry物件
entry1.grid(row=1, column=0, padx=10, pady=10, sticky="NEWS")

#######################建立標籤########################
label1 = Label(window, text="計算結果", style="my.TLabel", anchor="center")
label1.grid(row=3, column=0, padx=10, pady=10, sticky="NEWS")
# padx=10 設定與其他格子的左右邊距, pady=10 設定與其他格子的上下邊距, sticky="NEWS" 設定在格子中的顯示方式
# rowspan=2 設定格子的行數, columnspan=2 設定格子的列數

#######################建立按鈕########################
button = Button(window, text="顯示計算結果", style="my.TButton", command=show_result)
button.grid(row=2, column=0, padx=10, pady=10, sticky="NEWS")

######################運行應用程式########################
window.mainloop()  # 進入主迴圈
