from ttkbootstrap import *
import sys
import os
from tkinter import filedialog
from PIL import ImageTk, Image


#######################定義函數########################
def open_file():
    global file_path
    # 選擇檔案, initialdir為初始目錄,這裡設定為程式所在目錄
    file_path = filedialog.askopenfilename(initialdir=sys.path[0])
    label2.configure(text=file_path)  # 設定檔名


def show_image():  # 顯示圖片
    global file_path
    img = Image.open(file_path)  # 打開圖片檔案
    # 調整圖片大小,讓它適合畫布旳大小
    img = img.resize(
        (canvas.winfo_width(), canvas.winfo_height()), Image.LANCZOS
    )  # 調整圖片大小
    # 轉換成tkinter可以使用的格式
    photo = ImageTk.PhotoImage(img)
    # 在畫布上顯示圖片, 圖片的左上角會對齊畫布的左上角
    canvas.create_image(0, 0, anchor="nw", image=photo)
    canvas.image = photo  # 保留圖片,避免被垃圾回收機制回收


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
#######################建立標籤########################
label = Label(window, text="選擇檔案:")
label.grid(row=0, column=0, padx=10, pady=10, sticky="EW")

label2 = Label(window, text="無")
label2.grid(row=0, column=1, padx=10, pady=10, sticky="EW")
# padx=10 設定與其他格子的左右邊距, pady=10 設定與其他格子的上下邊距, sticky="NEWS" 設定在格子中的顯示方式
# rowspan=2 設定格子的行數, columnspan=2 設定格子的列數

#######################建立按鈕########################
button = Button(
    window, text="瀏覽", style="my.TButton", command=open_file
)  # 設定按鈕樣式
button.grid(row=0, column=2, padx=10, pady=10, sticky="W")

button2 = Button(
    window, text="顯示", style="my.TButton", command=show_image
)  # 設定按鈕樣式
button2.grid(row=1, column=0, padx=10, pady=10, sticky="EW", columnspan=3)

canvas = Canvas(window, width=600, height=600)
canvas.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

#######################運行應用程式########################
window.mainloop()  # 進入主迴圈
