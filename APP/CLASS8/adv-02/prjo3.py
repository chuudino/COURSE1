#######################匯入模組#######################
from tkinter import *
import sys
import os

#######################設定工作目錄########################
os.chdir(sys.path[0])


#######################建立視窗########################
windows = Tk()

# 設定視窗標題
windows.title("Exercise 3 2024/09/27")

# 設定視窗大小
windows.geometry("800x600")

#######################設定視窗圖片########################
windows.iconbitmap(crocodile2.gif")

######################載入圖片########################
img = Imageopen("crocodile2.gif")
img = img.resize((300, 300))

######################顥示圖片########################
my_img = canvas.create_image(300, 300, image=img)


#######################運行應用程式########################

windows.mainloop()  # 進入主迴圈
